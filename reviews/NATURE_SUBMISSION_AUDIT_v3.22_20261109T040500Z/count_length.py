"""Read-only editorial length accounting; SI/contributions deliberately excluded."""
from pathlib import Path
import argparse, hashlib, json, re, subprocess, sys

ap = argparse.ArgumentParser()
ap.add_argument('--source', type=Path, required=True)
ap.add_argument('--build', type=Path, required=True)
ap.add_argument('--out', type=Path, required=True)
args = ap.parse_args()
args.out.mkdir(parents=True, exist_ok=True)
names = ['opening', 'results_discussion', 'methods', 'auxiliary_methods',
         'figures_tables', 'extended_data', 'references', 'author_block',
         'declarations_pre', 'declarations_post']
texts = {n: (args.source / (n + '.md')).read_text() for n in names}

def normalize(s):
    # Display equations are separately counted, not treated as prose words.
    s = re.sub(r'\$\$.*?\$\$', '', s, flags=re.S)
    # One inline mathematical expression is one object/token; no TeX commands count.
    s = re.sub(r'\$([^$\n]+)\$', 'MATH', s)
    s = re.sub(r'\^[\d,–\- ]+\^', '', s)
    s = re.sub(r'\[([\d,–\- ]+)\]', '', s)
    s = re.sub(r'!\[[^\]]*\]\([^)]*\)(?:\{[^}]*\})?', '', s)
    s = re.sub(r'\[([^\]]+)\]\([^)]*\)', r'\1', s)
    s = re.sub(r'(?m)^\s*#{1,6} .*$', '', s)
    s = re.sub(r'(?m)^\s*:::.*$', '', s)
    s = re.sub(r'(?m)^\s*\|[\s:|\-]+\|\s*$', '', s)
    s = s.replace('\\clearpage', '').replace('**', '').replace('*', '')
    s = re.sub(r'(?m)^\d+\.\s+', '', s)  # bibliography list numbers
    s = s.replace('|', ' ')
    return ' '.join(w for w in s.split() if any(ch.isalnum() for ch in w))

records = {}
def add(key, s):
    clean = normalize(s)
    records[key] = {'words': len(clean.split()),
                    'inline_math_objects': len(re.findall(r'(?<!\$)\$(?!\$)[^$\n]+\$(?!\$)', re.sub(r'\$\$.*?\$\$', '', s, flags=re.S))),
                    'display_equations': len(re.findall(r'\$\$.*?\$\$', s, flags=re.S))}
    (args.out / (key + '.counted.txt')).write_text(clean + '\n')
    return records[key]['words']

opening = texts['opening']
abstract = opening.split('## Introduction')[0].split('\n', 1)[1].strip()
intro = opening.split('## Introduction', 1)[1]
body = texts['results_discussion']
table_match = re.search(r'::: display\n.*?\n:::', body, re.S)
assert table_match, 'Table 1 block not found'
table = table_match.group()
body = body[:table_match.start()] + body[table_match.end():]
note = body.split('**Note added.**', 1)[1]
body = body.split('**Note added.**', 1)[0]
results, discussion = body.split('## Discussion', 1)
add('abstract', abstract)
add('introduction', intro)
add('results', results)
add('discussion', discussion)
add('note_added', note)
add('main_body_no_table_no_note', intro + '\n' + results + '\n' + discussion)
add('main_body_with_note_no_table', intro + '\n' + results + '\n' + discussion + '\n' + note)
add('summary_plus_body_with_note', abstract + '\n' + intro + '\n' + results + '\n' + discussion + '\n' + note)
add('table1_all', table)
add('summary_body_note_table1', abstract + '\n' + intro + '\n' + results + '\n' + discussion + '\n' + note + '\n' + table)
add('methods', texts['methods'] + '\n' + texts['auxiliary_methods'])
add('availability', texts['declarations_pre'].split('## Funding')[0])
add('funding_and_other_endnotes', '## Funding' + texts['declarations_pre'].split('## Funding', 1)[1] + '\n' + texts['declarations_post'])
add('author_names_affiliations_correspondence', texts['author_block'])
for i, s in enumerate(re.findall(r'\*\*Fig\. [1-4] \|.*?(?=\n!\[|\Z)', texts['figures_tables'], re.S), 1):
    add(f'figure{i}_legend_with_title_labels', s)
add('main_figure_legends', texts['figures_tables'])
ed = texts['extended_data']
ed_rows = '\n'.join(line for line in ed.splitlines() if line.startswith('|'))
ed_legends = '\n'.join(line for line in ed.splitlines() if not line.startswith('|'))
add('extended_data_legends', ed_legends)
add('extended_data_table_cells', ed_rows)
add('extended_data_all', ed)

mapping = json.loads((args.build / 'CITATION_ORDER.json').read_text())
refs = {int(m[1]): m[2] for m in re.finditer(r'(?m)^(\d+)\. (.+)$', texts['references'])}
used = [int(k) for k in mapping['source_to_compiled']]
mainrefs = [k for k in used if mapping['origins'][str(k)] == 'main']
methodrefs = [k for k in used if k not in mainrefs]
add('references_main', '\n'.join(refs[k] for k in mainrefs))
add('references_methods', '\n'.join(refs[k] for k in methodrefs))

pdfs = {}
for name in ['NATURE_ARTICLE_v3.22', 'NATURE_ARTICLE_MAIN_v3.22', 'SUPPLEMENTARY_INFORMATION_v3.22']:
    p = args.build / (name + '.pdf')
    info = subprocess.check_output(['pdfinfo', str(p)], text=True)
    page_text = subprocess.check_output(['pdftotext', str(p), '-'], text=True).split('\f')
    if not page_text[-1].strip(): page_text.pop()
    pages = int(re.search(r'^Pages:\s+(\d+)', info, re.M)[1])
    assert pages == len(page_text)
    markers = [i + 1 for i, s in enumerate(page_text) if re.search(r'(?m)^Supplementary Information\s*$', s)]
    pdfs[name] = {'pages': pages, 'si_title_pages': markers,
                 'sha256': hashlib.sha256(p.read_bytes()).hexdigest(),
                 'author_contribution_heading_present': any('Provisional contribution statement' in s or re.search(r'(?m)^Author contributions\s*$', s) for s in page_text)}
    if name == 'NATURE_ARTICLE_v3.22':
        assert len(markers) == 1
        pdfs[name]['pages_excluding_SI'] = markers[0] - 1
        pdfs[name]['SI_pages_in_combined'] = pages - markers[0] + 1

totals = {'main_display_items': len(re.findall(r'^!\[Figure', texts['figures_tables'], re.M)) + len(re.findall(r'^\*\*Table \d+ \|', texts['results_discussion'], re.M)), 'main_figures': len(re.findall(r'^!\[Figure', texts['figures_tables'], re.M)), 'main_tables': len(re.findall(r'^\*\*Table \d+ \|', texts['results_discussion'], re.M)),
          'extended_data_figures': len(re.findall(r'^!\[Extended Data Figure', ed, re.M)),
          'extended_data_tables': len(re.findall(r'^\*\*Extended Data Table', ed, re.M)),
          'main_references': len(mainrefs), 'methods_references': len(methodrefs),
          'source_reference_entries': len(refs), 'used_references': len(used)}
totals['all_nonSI_counted_words_excluding_author_metadata'] = sum(records[k]['words'] for k in ['summary_plus_body_with_note', 'table1_all', 'methods', 'availability', 'funding_and_other_endnotes', 'main_figure_legends', 'extended_data_all', 'references_main', 'references_methods'])
totals['all_nonSI_counted_words_including_author_metadata'] = totals['all_nonSI_counted_words_excluding_author_metadata'] + records['author_names_affiliations_correspondence']['words']
out = {'scope': 'Length accounting only; SI and author contributions excluded; no scientific computation',
       'python': sys.version, 'records': records, 'totals': totals, 'pdfs': pdfs,
       'source_hashes': {n + '.md': hashlib.sha256((args.source / (n + '.md')).read_bytes()).hexdigest() for n in names},
       'build_checks': json.loads((args.build / 'BUILD_CHECKS.json').read_text()),
       'citation_order': mapping}
(args.out / 'LENGTH_COUNTS.json').write_text(json.dumps(out, ensure_ascii=False, indent=2))
print(json.dumps({'records': records, 'totals': totals, 'pdfs': pdfs}, ensure_ascii=False, indent=2))
