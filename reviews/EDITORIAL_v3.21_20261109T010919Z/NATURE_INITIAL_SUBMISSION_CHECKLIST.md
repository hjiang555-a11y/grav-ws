# Nature 初投稿格式检查｜v3.21 组稿支线

核查日期：2026-11-09（Asia/Shanghai）。核查对象：v3.21 的 BRANCH、生成脚本与 section 源文；数值性排版检查参考未改动的 v3.20/formal_build_02。此报告不等于新 PDF 已通过最终检查，也不认证科学分析或作者声明真实性。

**结论：四张主图、现有摘要和图文合并的双倍行距阅读版适合继续作为 Nature 初投审阅材料。当前没有必须为初投而重画图、移动条件谱、缩减至四个 display items 或排成六页的理由。通讯信息与作者贡献仍属于作者主动保留的待确认元数据；不能宣称全部投稿手续已齐备。**

## 1. 政策来源与适用阶段

1. [Nature — Initial submission](https://www.nature.com/nature/for-authors/initial-submission)：初投格式有弹性，PDF 应有行号，优先图文同文件；LaTeX 初投提供 PDF。文中 2,500 words/4 items 与 4,300 words/5–6 items 是典型篇幅参考，并非所有初稿均只能放四图表。查阅：2026-11-09。
2. [Nature — Formatting guide](https://www.nature.com/nature/for-authors/formatting-guide)：英文、双倍行距、摘要约200词、章节与引用排列、图注和作者栏规范。初投图片以审稿可判断质量为准。查阅：2026-11-09。
3. [Nature — Formatting Rules and Manuscript Essentials, Guidance for Primary Research Articles](https://www.nature.com/documents/nature-manuscript-checklist-research.pdf)：四页官方检查表。包括可编辑源文件、拆图、图件格式、ED数量、作者声明、源数据及接收前ORCID要求。其拆图及生产质量要求不能覆盖初投页面明确允许的图文合并形式；涉及阶段时按更具体的初投规定执行。官方PDF中摘要阈值230词，与网页理想200词不同；本稿保持188词，兼容两者。查阅：2026-11-09。
4. [Nature — Final submission](https://www.nature.com/nature/for-authors/final-submission)：用于识别接收后制作要求，不能把正式制作源文件要求误判为本轮初投障碍。查阅：2026-11-09。
5. [Nature — AI policy](https://www.nature.com/nature-portfolio/editorial-policies/ai) 与 [Nature Portfolio — Authorship](https://www.nature.com/nature-portfolio/editorial-policies/authorship)：作者责任、贡献与AI使用披露的政策背景。已有稿件包含LLM披露；本轮不新造作者事实。

访问说明：网页直接打开受到 Nature 登录跳转限制；初投及格式网页以当日检索返回的官方页面正文核对；官方四页检查表通过浏览工具直接读取。未采用 Nature 子刊、第三方转载或旧版2017说明替代 Nature 本刊指南。

## 2. 本轮检查表

“符合”指源文或基线构建证据；新版编译后的视觉检查由整合代理完成。

| 项目 | 初投要求/性质 | 当前状态及本轮处理 |
|---|---|---|
| 文件形式 | PDF可初投，图文合并优先；可编辑文件保留 | 生成脚本有合并阅读稿、MAIN拆图稿和独立SI。优先使用合并阅读稿+SI进行初投审阅；MAIN保留备用。无需把合并稿拆到生产版形式。来源1。 |
| 标题 | 简洁；75字符为指南参考 | 当前标题52字符，无需更改。来源1、3。 |
| 摘要 | 单段、充分引用、约200词 | 188英文词（190空格token含两个±）；有引用，开发模型和最后一句应用保留。摘要含本研究必要物理数值，不因“尽量少数字”的写作偏好删除已批准结果。来源1、2。 |
| 正文长度及主图数量 | 典型印刷篇幅建议，初投不机械卡页 | 源文粗计正文约1,800词，不含摘要、Methods、图注、引用；Methods约2,300空格token。四图+一表保留。双倍行距审阅PDF页数不能等同印刷页数。来源1、2。 |
| 字体、行距与行号 | 英文双倍行距；PDF逐行编号 | 构建为12pt Liberation Serif、双倍行距；已有v3.20图注逐行编号修正保留。新版逐页抽查，确认正文、Methods、图注可定位。来源1、2。 |
| 主图及图注 | 审稿清晰；图注同页；说明面板与误差 | 基线图注粗计230、126、175、124词，均低于300。保持四图图件与布局。新版检查图注是否留在对应图页，字体是否清晰。科学误差含义由证据代理复核。来源1、3。 |
| 参考文献 | 有题名、按首次出现连续编号 | 脚本动态重编号，main与Methods列表分开连续编号；基线35篇首次出现1–35。文字移动后必须重建并复核，不能只复制旧编号。来源1、3。 |
| Methods | 与正文同文件，足以理解/复现 | primary与auxiliary两组方法均保留；稿件组稿，不删科学细节、不新增未实施方法。来源1。 |
| ED | 10个图表合计为正式格式上限 | 现有7幅ED图+3张ED表共10项；条件谱保留ED。初投可嵌入，不必生产式拆图。来源1、3。 |
| SI | 文字SI为独立单PDF，有标题页 | 当前脚本生成独立SI，表号与主文/ED区分。新版核对主文引用及SI标题，不新增附件。来源3。 |
| Data/code availability | 声明需真实、明确 | 已有两个独立段落，均为reasonable request。保留原声明，不凭本轮工作推断可公开数据或伪造链接；正式提交前由作者确认实际提供途径及限制。 |
| Funding / interests | 投稿声明必须准确 | 有funding和无利益冲突声明；只保持，不把格式审阅表述成全体作者已再次确认。 |
| LLM使用 | 依实际用途披露 | auxiliary_methods末尾已有Use of large language models；脚本合入Methods，未遗漏。其“authors independently verified all numerical results”是已有作者声明，本轮paperwork不构成重新验证。 |
| Reporting Summary / ethics | 按研究类型适用 | 光钟/潮汐研究不是初投页明列必须Reporting Summary的life sciences及behavioural/social sciences。现有材料未显示人/动物实验，无依据添加审批号；投稿系统另有要求时再核实。来源1。 |
| ORCID /生产图件 /源数据包 | 接收流程或最终制作事项 | 官方表ORCID要求为formal acceptance前，不能因本轮没有ORCID而判定排版失败；保留图源，后续按编辑要求准备生产文件、权利表及源数据。此轮不计算或补造源数据。来源3、4。 |

## 3. 作者元数据：保留用户决定，明确未闭合项

现有 `sections/author_block.md` 列36位作者、6个单位；没有通讯星号或邮箱。`sections/author_contributions.md` 有旧贡献段，但 `scripts/build_formal.py` 只有显式指定 `--include-author-contributions` 才收录，v3.20构建确认值为false。

历史明确指示证据：

`/data/AI_Research/projects/grav-ws/manuscript_48h/nature_author_remerge_20261107T094831Z/author_metadata/USER_LATEST_DECISIONS.md`

该文件明确记录：“不标注通讯作者”，PJW贡献为策划、指挥、论文撰写，“不自动增加共同贡献标记”。本轮接受的 `shared/handoff/grav_ws_editorial_plan_v320_20261109T005115Z/EDITORIAL_REVISION_PLAN_ZH.md` 第9节又明确，贡献与通讯信息沿用待确认记录，不代填。

因此：

- **不自行加通讯作者或邮箱。** 正式初投页要求识别对应作者，投稿系统也需负责沟通者；当前保存作者讨论稿的既定状态，正式递交前由作者决定姓名、邮箱和是否允许文稿标记。不能从账号、末位作者、PI身份推断。
- **不自动恢复旧贡献段。** Nature的完整稿件要求贡献声明；旧段落存在不等于当前全部作者职责已批准。不将缺失视为纯排版问题。
- 以上不妨碍完成本轮文字修订、PDF排版与内部交付，也不需要为同一已明确决定反复询问。本稿应称“按Nature初投版式准备的作者审阅稿”，避免称“全部投稿元数据已完成”。

## 4. 整合后最低验收

1. 摘要文本与批准稿精确相同；四张主图文件不变。
2. 引用首次出现连续；正文、图注、Methods与SI交叉引用有效。
3. 新PDF无缺字/数学符号、重叠/截断和重大编译错误；主要图注有行号且与图同页。
4. 检查合并PDF与SI的文件大小、页数、可读性；如使用官方建议的30MB合并稿限额，按实际输出记录，不臆测。
5. 记录本轮未解决的作者元数据和重大科学措辞候选；不将其隐藏在“全部通过”结论中。

本检查未修改论文、图件或作者元数据，未进行科学计算；仅读取源文、构建脚本、历史授权及官方指南，并作文字长度粗计。
