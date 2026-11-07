# Editorial 交付核验

本轮仅在 `editorial/` 新建材料。未改科学稿件、图或其他代理文件；未投稿、未发信、未上传。

## Cover letter

以 `nature_methods_closure_20261107T1343Z/COVER_LETTER_DRAFT.md` 为原稿，按 academic-humanizer 的有限 polish 模式检查。只将原来概括全部信号/旁瓣可追踪的句子改为 reciprocal subtraction 与 sampling-response calculations 追踪 selected lunar sidelobes，随后一句保留跨领域意义。对应规则5（主张范围）及8（拆句衔接）。原段落结构、14个数字、引用链接和限定均保持；工具 compare 全部通过，audit 无候选套话、未定义标签或待补占位符。未新增“首次”、独家投稿或作者已核验全部结果的承诺。

信中0.96±0.11、4.87/2.87 cm、545.9 h/353 d、692 km/1350 km及共享274 h均与当前稿一致。署名 The authors；这是待通讯作者定稿的内容草稿，不是已经发出的信件。

## 作者事实及规则

旧PRL source中的联系人、资助、data-on-request与AI文字已保存来源摘录及SHA256。它们仅作为本稿联系人/资助适用性核对的候选材料。当前作者名单和顺序沿用已确认稿，不重复设置批准流程。没有据缺失资料代填“无利益冲突”或公开存档DOI。

Nature官方初投指南和Extended Data指南已核：初投组织形式有弹性；Extended Data图表合计上限为10项。当前11图+6表=17项，清单明确后续合并，本轮保留全部显示项。数据/代码声明只描述私有研究档案及当前辅助分析代码，不承诺完整重现V29或全图重绘。

## 文件及导出

- `COVER_LETTER_DRAFT.md/.pdf/.docx`
- `AUTHOR_CHECKLIST_ZH.md/.html/.pdf/.docx`：7条编号及全文均为 #C00000。
- `SUBMISSION_FILES_ZH.md/.pdf/.docx`：一页说明，包含完整版、分开版、可编辑稿包及根目录 `DATA_CODE_PACKAGE.zip` 的路径。
- `DECLARATIONS_DRAFT.md/.pdf/.docx`：包含需补定事实，全部相关段落整段标红，不自动写入论文。
- `AUTHOR_FACTS_AND_SOURCES.md`、`sources/`：核查范围、候选事实和来源快照。

四份PDF均为一页。已渲染检查字形、边界、表格和段落，没有发现截断、重叠或缺字。DOCX已按XML核验7条清单和10个声明段落文字的颜色均为C00000。清单HTML为UTF-8并对整条段落应用同一颜色。核验记录为 `EXPORT_CHECKS.json`；cover语言检查为 `COVER_AUDIT.txt` 和 `COVER_COMPARE.txt`。

可用 `scripts/prepare_editorial.py` 与 `scripts/build_editorial.py` 依次生成本目录材料。生成依赖为现有scientific Python、python-docx、pandoc和XeLaTeX；本轮未安装软件。
