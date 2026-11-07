# Nature 论文收尾交付

论文：**Tidal potential measured with distant optical clocks**。科学内容采用作者选定的 `nature_focused_humanized_20261107T145113Z`。本次提供两种阅读形式，保留相同的文字、数值和图表。

## 论文

| 形式 | 文件 | 内容 |
|---|---|---|
| 合并阅读版 | [NATURE_ARTICLE_COMBINED.pdf](combined/NATURE_ARTICLE_COMBINED.pdf) | 46 页，逐字节保留已选定版本；正文、Methods、图表、Extended Data 和补充方法在同一个文件中 |
| 分开版主稿 | [NATURE_ARTICLE_MAIN.pdf](separate/NATURE_ARTICLE_MAIN.pdf) | 原稿第 1–39 页，包含正文、Methods、参考文献及主图表、Extended Data |
| 分开版补充信息 | [SUPPLEMENTARY_INFORMATION.pdf](separate/SUPPLEMENTARY_INFORMATION.pdf) | 7 页，包含 SM1–SM7；独立标题与页码，引用沿用主稿编号 |

**两种形式择一阅读即可。** 分开版主稿与补充信息需要配套阅读；拆分没有更换分析路线、数值或图件。文中 SM1–SM7 是补充方法章节编号。

## 可编辑文件和数据

- [合并版可编辑源文件包](EDITABLE_MANUSCRIPT_SOURCE.zip)：Word、LaTeX、Markdown、分节源文件、图件及构建脚本。
- [分开版可编辑源文件包](SEPARATE_EDITABLE_SOURCE.zip)：主稿和补充信息的 Word、LaTeX、Markdown，以及图件和使用说明。
- [主稿 Word](separate/NATURE_ARTICLE_MAIN.docx)；[补充信息 Word](separate/SUPPLEMENTARY_INFORMATION.docx)。
- [数据与代码包](DATA_CODE_PACKAGE.zip)：冻结处理数据、模板、脚本、结果库和实际复现核验记录。
- [数据包说明](data_code/README.md)：数据类型、各拟合与误差定义、运行方法、验证范围。
- [结果库 JSON](data_code/RESULTS_LIBRARY.json)；[结果库 SQLite](data_code/RESULTS_LIBRARY.sqlite)。
- [补充信息文件说明 SIGuide.doc](separate/SIGuide.doc)；[Word 新格式](separate/SIGuide.docx)。

数据包从附带的非重叠均值与冻结模型输入重跑振幅扫描、结果库、主要信噪比计算及表格。它的范围是可核验的辅助分析，不代表已重新获取或复现全部原始一秒记录和 v29 主分析。

## Cover letter 与作者审核材料

- [Cover letter PDF](editorial/COVER_LETTER_DRAFT.pdf)；[Word](editorial/COVER_LETTER_DRAFT.docx)；[Markdown](editorial/COVER_LETTER_DRAFT.md)。
- [实际红字作者核对清单](editorial/AUTHOR_CHECKLIST_ZH.pdf)：统一列出投稿前需处理的实际事项。
- [声明草案](editorial/DECLARATIONS_DRAFT.md)；[文件使用说明](editorial/SUBMISSION_FILES_ZH.md)。

这是作者审核与保存用的收尾包，尚未代为投稿或发送 cover letter。文件拆分不等于已满足全部投稿要求；具体剩余事项以红字清单为准。

## 下载与核验

本目录提供各项文件的独立查看与下载链接。论文源文件和数据代码各有完整 ZIP，便于分别保存。

[SHA-256 清单](MANIFEST_SHA256.json) 记录单项交付文件；[文件一致性核验](checks/DELIVERY_VALIDATION.json) 记录合并版原样保留及拆分内容一致性。数据包内另有运行日志、软件版本和数值比对结果。

Nature 官方依据：[初投指南](https://www.nature.com/nature/for-authors/initial-submission)、[补充材料指南](https://www.nature.com/nature/for-authors/supp-info)、[Extended Data 指南](https://research-figure-guide.nature.com/figures/extended-data-formatting-guidelines/)。本目录上传至作者已授权的私有 GitHub 仓库，保留旧版文件。
