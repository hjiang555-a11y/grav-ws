# Nature 主刊政策及审稿事实核查

核查日期：2026-11-09（Asia/Shanghai）。对象：Nature 主刊 Article；v3.21 已交付源文及本轮 v3.22 开始时的副本。工作范围为政策检索、文本计数、已报告数值及估计量溯源；未重算科学结果、未改论文、未上传数据。本轮已读取工作站与项目 AGENTS.md，以及 `shared/research_plans/grav_ws_editorial_v322_20261109T014000Z.md`。

**结论：审稿提出的“Nature Article 摘要约150词且无引用”和“初投必须有 Zenodo DOI”均不能作为主刊硬性要求。作者贡献与通讯信息确需补齐；本轮允许暂写但未知事实仍须占位。现有摘要按既有口径188词，有引用。夏季0.67与0.87属于不同估计量；辅助模型实际 k₂=0.3010。**

## 1. 来源、访问状态和适用阶段

官方HTML直接打开受到 `idp.nature.com/authorize` 重定向限制；以下HTML信息来自本次检索返回的**官方原页面索引正文**（检索标示当前/近日抓取），不声称直读成功或通读实时原站。官方四页PDF通过浏览工具直接读取全部135行。网页索引不等于编辑部对具体稿件的决定。未用子刊规则替代主刊规则。

| 官方来源 | 本次可核实内容及阶段 | 短引文（每源累计不超过25词） |
|---|---|---|
| [Nature — Initial submission](https://www.nature.com/nature/for-authors/initial-submission) | 初投形式灵活，鼓励PDF/Word图文同文件，PDF需行号、图注同页；可编辑LaTeX到接收阶段提供。初投页已要求各作者贡献、通讯负责者和利益冲突声明。cover letter 可选。所列约200词摘要及典型2500词/四个图表属于篇幅指导。 | “The Nature journals are flexible with regard to the format of initial submissions.” |
| [Nature — Formatting guide](https://www.nature.com/nature/for-authors/formatting-guide) | Article 摘要是带引用的summary paragraph，理想不超200词；面向跨学科读者。数字/缩写尽量少，但必要时允许。 | “Articles start with a fully referenced summary paragraph, ideally of no more than 200 words” |
| [Nature — Formatting Rules and Manuscript Essentials: Guidance for Primary Research Articles](https://www.nature.com/documents/nature-manuscript-checklist-research.pdf) | 已直接读取。p1–2摘要≤230词、至少一处引用；Methods在主文件；贡献、通讯等声明；ED图表合计≤10；主图和ED分别上传、源数据文件、可编辑生产文件等。该表含最终制作要求，不能据此否定初投页面明确允许的合并PDF。ORCID节点明确为formal acceptance前。 | “Abstract ≤230 words. Must include at least 1 reference.” |
| [Nature — Final submission](https://www.nature.com/nature/for-authors/final-submission) | 明确仅适用于accepted in principle且编辑要求production-quality材料之时。最终文字文件排除图件，图、ED和SI另传。 | “The instructions apply only if your manuscript has been accepted in principle for publication” |
| [Nature — Reporting standards and availability of data, materials, code and protocols](https://www.nature.com/nature/editorial-policies/reporting-standards) | 必须清楚说明复现所需最小数据集的访问条件；限制在提交时披露；审稿要求时提供数据和核心自定义代码。公开仓库为首选，某些数据类型强制入库。代码发表时推荐DOI仓库，如Zenodo或Code Ocean；不是指定Zenodo一家，也不是声明所有初稿已经公开。 | “Code should be deposited in a DOI-minting repository such as Zenodo or Code Ocean” |
| [Nature — Forms and declarations](https://www.nature.com/nature/for-authors/forms-and-declarations) | 页面定位为发表前填写的表格；重申发表时数据和材料公开。不能由此推导本轮已获公开上传授权。 | “Nature authors must make data and materials publicly available upon publication.” |

200词理想值与检查表230词上限并存，应分别记录，不能只取一条而删除另一条。对于本稿，现有188词已经兼容两条，不需为满足150词而删结果或引用。图注等生产规则不同页面亦有差异，应在最终阶段遵循编辑部具体要求。

## 2. 审稿意见判定及本轮可执行事项

| 审稿命题 | 判定 | 本轮处理边界 |
|---|---|---|
| Nature Article 摘要约150词、不得有引用 | **不准确**。主刊明示带引用，理想≤200词；官方检查表≤230且至少一引用。 | 保留已批准摘要及引文；不要套用Nature Communications或其他子刊摘要规则。 |
| 当前摘要约206词 | **按实际源文不可复现**。详见下节；188词口径成立。 | 明示计数方法，避免把数学运算符作为英文词，也不擅改摘要。 |
| 单写upon reasonable request即可宣布data/code政策闭合 | **不能支持此结论**。现有声明无具体访问条件、限制理由或联系人，不能称完整可访问性已认证。 | 记录作者待确认真实分享路径、复现文件和限制；可在审阅清单建议存档。不得编造URL/DOI或承诺尚未确认公开。 |
| 所有稿件初投前必须公开至Zenodo取得DOI | **过度推断**。官方要求可用性与透明度；公开仓库优先，核心代码推荐DOI仓库，但Zenodo非唯一选择，发表节点和初投节点不同。 | DOI存档是值得作者后续落实的准备事项；本轮无新增公开上传授权，不上传，不将未存档说成已存档。 |
| 应有author contributions及correspondence | **支持**。初投页即有明确要求，不只是接收后制作格式。 | 本轮用户已允许暂写，取代旧版“完全不纳入”的选择。PJW策划、指挥、论文写作可沿用已确认事实；其余职责、具体通讯姓名/邮箱未知者标为待确认，不能凭排序推断。作者审阅稿可以含清晰占位，正式提交前需人工闭合。 |

Reporting Summary应按研究类型适用。主刊政策列life sciences、behavioural/social sciences、ecology/evolution/environmental sciences，以及特定physical sciences的solar cells和claims of lasing。本光钟潮汐研究没有因“物理研究”这一标签而自动落入后两类；不能补造伦理审批或宣称编辑系统不会追加要求。

## 3. 实际摘要计数与引用

输入：v3.21与v3.22 `sections/opening.md` 的首个粗体段落；本次读取时二者摘要一致。先去除形如 `^16,19^` 的参考标记，再以空白切分：**190 tokens；去除两个独立的±运算符后188 words**。与v3.21 `formal_build_01/BUILD_CHECKS.json` 的 `abstract_whitespace_tokens=190`、`abstract_words_excluding_operators=188` 一致。不同软件对连字符词/数字的词定义可能略异；不把206当作已核实数字。

摘要有7处引文标记、9个不同来源：源编号16,19；5；6,29；21；22；63；64。v3.21 `formal_build_01/CITATION_ORDER.json` 对应成稿编号1–9：IERS Conventions；Farrell加载；Chou相对论光钟；Lisdat网络；McGrew厘米下测地；Jia Sr钟；Zhu Yb钟；Dimarcq秒重新定义；Wu高程统一。此次只核对本地引用身份及编号映射，没有重新验证每篇论文的全部内容。成稿引用总数35来自实际映射，不等于references.md保留的全部历史条目数。

复核口径：Python 3.12.3，解释器 `/data/AI_Research/environments/python/sci/bin/python`；标准库pathlib/re，不涉及分析包或随机过程。表达式为 `re.sub(r'\^[\d,–\- ]+\^', '', abstract).split()`，然后仅排除等于 `±` 的token。

## 4. 本地科学事实与估计量：只核对，未重算

以下路径均相对于 `editorial_v321_20261109T010919Z/`。这些是既有作者报告的数值及定义，并不代表本次独立重算已验证。

| 项目 | 可读依据 | 核查结果及边界 |
|---|---|---|
| 辅助Love数 | `sections/auxiliary_methods.md` 第9行附近 | **k₂=0.3010**，h₂=0.6078，g=9.794 m/s²；primary写k₂₂=0.29801。审稿0.30190不符当前源文。原文已报告相关组合差0.4%，本次未重新计算。不得为修正审稿笔误改成0.30190。 |
| Fig.1b campaign hours | `figures/figure1_v319.pdf` 提取文字；`sections/figures_tables.md`；`sections/methods.md` | 图上为**60、68、73、70、274 h**，对应五campaign。图中整数逐项之和545，与Methods primary总544 h并不相同；可能涉及逐项取整，但当前未找到精确逐campaign时长以确认该解释。不可把545当作未取整总值或偷偷改小时数。primary为544 h、54段；auxiliary为545.9 h、3299均值，两类时长也不可互换。caption可标整数为rounded（须先确认来源取整），或作为待作者核实项。 |
| 夏季0.67±0.18 | `sections/extended_data.md` ED Table1 Jun–Aug行及表注 | **primary full-template A**，不含empirical daily terms，residual-calibrated uncertainty；不是lunar，也不是auxiliary full-template。 |
| 夏季0.87±0.18 | 同表最后一列；`sections/supplementary_methods.md` SM4/SM6 | **primary lunar-group**，夏季单独估计；SM4同时给 earlier campaigns together 1.05±0.31，夏季信息份额61%。不能用0.67替换或宣称与Hou一致即估计量相同。 |
| Hou 0.87(15) | ED Table2、SM6 | Hou模型及分段相关估计、夏季16段，reported weighted statistical error；同批观测，不独立合并。 |
| Hou-style 0.78±0.19 | ED Table2说明、SM6 | 同夏季记录，采用本稿physical model、Hou分段估计量、非重叠1200-s窗口、逆方差合并；与Hou原0.87(15)及本稿joint lunar0.87±0.18要区分。 |
| 全记录primary | ED Table2 | lunar0.97±0.14；full-template0.90±0.12；均为residual-resampling calibrated。不是auxiliary摘要full0.96±0.11、lunar1.00±0.13。 |
| held-out结果 | `sections/methods.md` Data selection/Robustness；SM4 | **八个observation periods**为留出单位（不是五campaign/54segment/29operating groups）。每次训练幅度，留出段只重新拟合offset。whole-template七/八改善、pooled RSS降低4.9%；lunar六/八改善、pooled1.7%。这是现有结果，允许准确引用或移入Discussion；不能改写为严格前瞻预测或完全未知数据。 |
| 独立2026处理held-out | SM6 | 非重叠600-s means、系统修正、固定十日baseline；whole0.88±0.10，含daily terms时lunar0.89±0.28；whole在**六个2026留出period全部改善**。不得与上行八期或pooled4.9%合并成一个指标。 |

未找到当前包中逐period预测评分CSV/JSON以重新逐项验算；上述留出计数和百分比已在本地稿件及SI中直接报告，既有compiled/rebuilt文档也保留同文。此处认证的是“现有稿件含这些结果及其定义”，不是重新运行预测或评估数据泄漏。新增RMSE、误差条、显著性、每期评分、采样效率校正或统一Primary/Auxiliary结果均需要新的科学计算，超出本轮范围。

## 5. 交给整合者的具体结论

1. 保持摘要及引用；报告188词计数口径，拒绝150词无引用的错误硬性要求。
2. 暂定贡献与通讯可纳入，但明确未知事实；正式提交手续仍待作者确认。
3. 不捏造Zenodo DOI，不把存档推荐写成已经完成；将数据/代码声明实质闭合列待作者落实事项。
4. k₂使用当前实际0.3010；夏季full/lunar/Hou三种估计量逐项区分。
5. Fig.1时长存在整数和与primary总值差1 h的可见口径问题，须保留记录，不擅自重算或改图。
6. 原有held-out数字可准确引用；新增预测图或指标需要新计算，不在本次编辑授权内。

本报告未认证作者贡献的完整真实性、全作者同意、无一稿多投、所有数值已独立重算，亦未代为投稿或公开发布。
