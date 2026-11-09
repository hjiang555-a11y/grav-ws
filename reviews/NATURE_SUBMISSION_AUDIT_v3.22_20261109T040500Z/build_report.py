from pathlib import Path
import subprocess
base=Path(__file__).resolve().parent
text=(base/'NATURE_SUBMISSION_AUDIT_ZH.md').read_text()
text=text.replace('**问题清单——仅供选择执行，本轮一项也未改**',r'\newpage'+'\n\n'+'**问题清单——仅供选择执行，本轮一项也未改**')
subprocess.run(['pandoc','--standalone','--pdf-engine=xelatex','-V','documentclass=article','-V','mainfont=Liberation Serif','-V','CJKmainfont=Noto Serif CJK SC','-V','geometry:margin=18mm','-V','papersize=a4','-V','fontsize=10pt','-V','colorlinks=true','-o',str(base/'NATURE_SUBMISSION_AUDIT_ZH.pdf')],input=text,text=True,cwd=base,check=True)
