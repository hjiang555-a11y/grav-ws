# 当前稿字数与引用审计

仅计数，未改论文。实际源：`/data/AI_Research/projects/grav-ws/manuscript_48h/nature_fig1_20261107T234421Z/manuscript`。

口径：Pandoc AST 排除标题/小标题、所有行内和展示公式、引文编号、表格及 Table 1 整个图表说明块；主文不含摘要、作者、参考文献、Methods/SI、图注。独立 ± 等符号不计词。数字和单位作为正文词；内部小数点、千位逗号及撇号保留。下表左列把连字符/短长破折号连接的词合为一词，右列拆开。第三列为行内数学表达式各计一词的敏感性口径。

| 部分 | 连字符合并 | 拆开 | 行内数学各计一词（合并连字符） |
|---|---:|---:|---:|
| abstract | 189 | 194 | 189 |
| Introduction | 396 | 403 | 403 |
| Results | 974 | 1017 | 993 |
| Discussion | 374 | 395 | 384 |
| Summary_including_final_prior_work_note | 119 | 126 | 119 |
| Summary_without_final_prior_work_note | 78 | 81 | 78 |
| main_Introduction_Results_Discussion_Summary | 1863 | 1941 | 1899 |
| main_plus_abstract | 2052 | 2135 | 2088 |
| Methods_core | 2008 | 2113 | 2048 |
| Methods_auxiliary | 1187 | 1260 | 1235 |
| Methods_combined | 3195 | 3373 | 3283 |
| Supplementary_Methods | 2628 | 2783 | 2741 |

## 主图注

含 Fig. 编号、题名和面板字母；排除公式/引文编号。

| 图 | 合并 | 拆开 |
|---|---:|---:|
| Figure_1 | 165 | 170 |
| Figure_2 | 129 | 139 |
| Figure_3 | 217 | 236 |
| Figure_4 | 142 | 148 |

## 引用与格式

主文不同引用：26 条；引用标记出现 26 次。完整编译稿参考文献 32 条；源文献库 61 条，未引用源编号 [1, 2, 3, 4, 7, 9, 11, 13, 14, 30, 31, 32, 34, 35, 36, 37, 39, 40, 41, 42, 43, 45, 48, 49, 50, 51, 53, 56, 57]。

题名：52 字符（含空格），7 词；Markdown 为 H1，非显式 **加粗** 标记。DOCX 题名样式：{'style': 'Heading 1', 'paragraph_style_bold': True, 'text_run_bold_values': ['None']}。题名无引文：True。

摘要：整段 Markdown 加粗=True；DOCX={'style': 'Body Text', 'paragraph_style_bold': None, 'text_run_bold_values': ['True']}；引用编号=[]。

## 小标题字符数

| 文件:行 | 标题 | 含空格字符 | 不含空格字符 |
|---|---|---:|---:|
| sections/opening.md:5 | Introduction | 12 | 12 |
| sections/results_discussion.md:1 | Results | 7 | 7 |
| sections/results_discussion.md:3 | Measuring a coastal–inland potential difference | 47 | 43 |
| sections/results_discussion.md:11 | Tidal amplitude, phase and observation coverage | 47 | 42 |
| sections/results_discussion.md:19 | Amplitude spectrum and separate semidiurnal detections | 54 | 49 |
| sections/results_discussion.md:25 | Reliability of the separated signals | 36 | 32 |
| sections/results_discussion.md:33 | Ocean loading and diurnal response | 34 | 30 |
| sections/results_discussion.md:37 | Discussion | 10 | 10 |
| sections/results_discussion.md:66 | Summary | 7 | 7 |
| sections/methods.md:1 | Methods | 7 | 7 |
| sections/methods.md:3 | Clocks, frequency transfer and sampling | 39 | 35 |
| sections/methods.md:11 | Data selection | 14 | 13 |
| sections/methods.md:19 | Solid Earth tide and ocean loading | 34 | 29 |
| sections/methods.md:41 | Tidal fits and uncertainty | 26 | 23 |
| sections/methods.md:55 | Daily disturbances and validation | 33 | 30 |
| sections/methods.md:73 | Primary spectral diagnostics | 28 | 26 |
| sections/methods.md:79 | Fibre-link phase locking and monitoring | 39 | 35 |
| sections/methods.md:85 | Environmental analysis | 22 | 21 |
| sections/auxiliary_methods.md:1 | Auxiliary grouped-response and phase estimates | 46 | 42 |
| sections/auxiliary_methods.md:15 | Signal-to-noise ratios for the retained sampling | 48 | 43 |
| sections/auxiliary_methods.md:40 | Local amplitude spectrum in Figure 3 | 36 | 31 |
| sections/auxiliary_methods.md:54 | Auxiliary frequency-domain analysis | 35 | 33 |
| sections/auxiliary_methods.md:62 | Compensation sensitivity and template correlation | 49 | 45 |
| sections/supplementary_methods.md:1 | Supplementary Methods | 21 | 20 |
| sections/supplementary_methods.md:3 | SM1. Physical model implementation and sensitivity | 50 | 45 |
| sections/supplementary_methods.md:15 | SM2. Selection and timing checks | 32 | 28 |
| sections/supplementary_methods.md:21 | SM3. Primary uncertainty calibration and injection validation | 61 | 55 |
| sections/supplementary_methods.md:31 | SM4. Primary prediction, monitoring and environmental checks | 60 | 54 |
| sections/supplementary_methods.md:47 | SM5. Primary spectral displays and alternative processing | 57 | 51 |
| sections/supplementary_methods.md:57 | SM6. Auxiliary response and uncertainty details | 47 | 42 |
| sections/supplementary_methods.md:69 | SM7. Compensation, alias and correlation diagnostics | 52 | 47 |

复现：`python WORD_COUNTS.py --source /path/to/manuscript`。原样保留待计数文字于 WORD_COUNTS_PLAIN_TEXT.json，完整数值、口径、来源 hash 和软件版本于 WORD_COUNTS.json。未用旧稿字数推断当前稿，也未核定期刊限制。
