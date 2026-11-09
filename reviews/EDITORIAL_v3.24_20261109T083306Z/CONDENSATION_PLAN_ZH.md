# v3.24全文检查与可选精简计划

> **状态更新：C01–C05已于2026年11月9日获准并全部执行。** 下文保留执行前的计划原文，词数及“未执行”表述指当时状态。当前结果见[精简执行与验收](CONDENSATION_EXECUTION_ZH.md)。

2026年11月9日｜已落实获准修改；以下额外精简尚未执行

**结论：不需要再做整体压缩或结构调整。可选择5处局部优化，合计减少约64个英文词元，主要去掉重复说明并缩短图示导航。** 不调整刚批准的aliasing与SNR解释，不再展开新一轮科学主张修改。

## 本轮已经完成的内容

v3.24已逐字落实上一份第二版计划的A、B及T1–T3：两处句子替换、三处sampling aliases术语统一。该版保留v3.23的Table 1 model estimated标签和已修复的LLM披露标题。旧v3.23独立保留。除此之外，稿件未实施下文的精简候选。

五处修改带来的新增数字标记仅为已讨论的24 h、12 h及ED Fig.1d指引；没有新增测量结果，数学表达式和文献编号顺序不变。修改后完整阅读PDF40页，主稿PDF25页，SI单独7页；这些是当前审阅版页数。

## 当前篇幅与是否需要压缩

| 口径 | 当前词数 |
|---|---:|
| 摘要 | 188 |
| 正文含Note added，不含摘要及Table 1 | 1675 |
| 摘要＋正文＋Note added | 1863 |
| 上项另含Table 1及表注的保守口径 | 1958 |
| Methods，含LLM披露，不含数据/代码声明 | 2311 |
| Methods另含数据/代码声明 | 2359 |

SI不计入上述正文或Methods数字。图注、参考文献、作者信息分开统计，不能把整个PDF的文字量当成正文篇幅。

Nature官方指南对典型6页Article给出约2500词、4个展示项，对典型8页Article给出约4300词、5–6个展示项；Methods通常不超过3000词，但强调保留解释和复现所需内容。这些是版面指导值，不是要求把审阅PDF压成6或8页。现稿4图＋1表、正文及Methods均无迫切字数压缩需要。[Nature初投指南](https://www.nature.com/nature/for-authors/initial-submission)；[Nature格式指南](https://www.nature.com/nature/for-authors/formatting-guide)。本判断只涉及篇幅，不替代全部投稿信息的验收。

## 全文检查覆盖与处理建议

| 部分 | 检查结论 |
|---|---|
| 摘要 | 已定188词；保留，不另行压缩 |
| 引言 | 三段职责清楚；新术语已统一，不扩写也不删背景引用 |
| Results | 论证顺序完整；可选压缩图示导航和弱分量过渡句（C01、C02） |
| Discussion | 新批准的两类可能解释已落实，保留may/could与residual限定；不立即再改新句，也不删模型实现边界 |
| Methods | 核心方法已较紧；可选缩短两路线导航、删除重复轮廓句及压缩显示方法（C03–C05） |
| 主图图注 | 功能、误差定义和处理归属需可独立阅读；不为少几个词进一步压缩 |
| Extended Data与SI | 承载独有验证和复现细节，当前不建议搬表、撤图、重排SM或强行删减 |
| 文献、声明、作者信息 | 保留；不以精简为理由删引用、恢复作者贡献或代填通讯作者事实 |

## 可选清单：原句、替换范围与候选

以下五项都是备选，尚未执行。每项以当前v3.24源文件中的唯一原句或句组为目标；无需整段重写。词数为逐项编辑词元统计，含图号等文本、连字符词按一词处理，与上面的期刊篇幅统计口径分开。

### C01｜Results：缩短时序与图示导航

位置：`sections/results_discussion.md:15`。将下列原句/句组整体替换；其余句子不动。

**原文：**

> As shown in Fig. 2, the summer time series and its dependence on lunar phase, after removal of the fitted offsets and non-lunar groups, agree well with the predicted lunar variation. Gaps are compressed on the time axis; Extended Data Fig. 2a shows the records of all campaigns, and Extended Data Fig. 2b,c shows the April campaign in calendar time.

**候选：**

> After removal of fitted offsets and non-lunar groups, the summer time series and its dependence on lunar phase agree well with the predicted variation (Fig. 2). The time axis compresses gaps; Extended Data Fig. 2a shows all campaigns, and panels b,c show April in calendar time.

**理由：** 把处理条件前置，避免主语与谓语之间插入长限定；压缩连续两次完整ED图号的导航文字。保留时序与相位两类支持证据。

**保留：** fitted offsets与non-lunar groups已被移除；summer time series和dependence on lunar phase；agree well的符合程度；Fig. 2、Extended Data Fig. 2a及同一图的b,c；压缩时间轴与April保留calendar time的区别；无结果数字或文献上标删改

**词元变化：** 60 → 46，减少14。

### C02｜Results：去掉过渡句的重复比较语

位置：`sections/results_discussion.md:31`。将下列原句/句组整体替换；其余句子不动。

**原文：**

> These weaker constraints, compared with the lunar response, motivate a quantitative account of component precision.

**候选：**

> These weaker constraints motivate a quantitative account of component precision.

**理由：** 去掉在前文月球主响应及本段less precisely/near unity对照后已清楚的插入比较语，保留弱分量引出精度解释的桥梁。

**保留：** These weaker constraints仍指本段ocean-loading与diurnal responses；quantitative account of component precision过渡功能不变；本段Table 1、ED Fig. 1b、SM4/SM5及ref15全部不动；无数字、误差定义、模型结论或因果限定删改

**词元变化：** 15 → 10，减少5。

### C03｜Methods：简洁交代两路线名称和职责

位置：`sections/methods.md:15`。将下列原句/句组整体替换；其余句子不动。

**原文：**

> The main analysis (labelled the auxiliary reduction in the supplementary material) provides the summary responses, spectra and signal-to-noise ratios. The filtered validation analysis (labelled the primary reduction in the figure and supplementary labels) provides the time-domain displays and robustness checks. These analyses share observations and are not independent measurements (Extended Data Table 1a).

**候选：**

> The main analysis (auxiliary reduction) provides summary responses, spectra and signal-to-noise ratios; the filtered validation analysis (primary reduction) provides time-domain displays and robustness checks. Their observations are shared, so they are not independent measurements (Extended Data Table 1a).

**理由：** 去掉标签所在文件的重复说明，直接一一映射两套名称；保留分析分工，不能删掉整个导航段。

**保留：** 保留两种分析名称/别名、全部用途、共享观测非独立、ED Table1a入口；SI第3行仍交代各SM归属。

**词元变化：** 53 → 38，减少15。

### C04｜Methods：删除与Fig.3图注重复的一句

位置：`sections/methods.md:25`。将下列原句/句组整体替换；其余句子不动。

**原文：**

> The contours in Fig. 3b show the scaled least-squares covariance at radii one and two.

**拟处理：** 仅删除上述一句，不插入新句；同一轮廓定义完整保留在Fig.3图注。

**理由：** 纯重复：Fig. 3b图注已完整给出同一轮廓定义，Methods前一句保留实测误差规则。仅删除这一句，不动整段。

**保留：** figures_tables.md:13保留scaled least-squares covariance及radii one and two；methods.md:25仍保留取较大误差和逐日全参数重拟合。

**词元变化：** 15 → 0，减少15。

### C05｜Methods：压缩Fig.2显示方法的复述

位置：`sections/auxiliary_methods.md:29`。将下列原句/句组整体替换；其余句子不动。

**原文：**

> The phase-folded summer display (Fig. 2b) subtracts the fitted offsets and non-lunar groups and averages in 30° M₂-phase bins; the M₂+N₂ model is folded with the same sampling, and the day-by-day jackknife error bars hold the fitted non-lunar terms fixed. The time-series display uses 3-h averages, with gaps longer than 6 h removed from the horizontal axis and marked.

**候选：**

> For Fig. 2b, data minus fitted offsets and non-lunar groups, and the M₂+N₂ model, are averaged in 30° M₂-phase bins on identical sampling. Day-by-day jackknife errors hold non-lunar fits fixed. Time-series displays use 3-h averages with marked compression of gaps longer than 6 h.

**理由：** 缩短显示方法的复述；图2图注仍完整独立，不把方法只留一个笼统图号。

**保留：** 保留减去偏置/非月潮项、M₂+N₂、相同采样和30°分箱、误差条件、3-h与6-h。

**词元变化：** 59 → 44，减少15。

## 建议怎样选择

如果只做最少的清理，可优先选 **C03＋C04**，合计减少30个词元；两项都处理Methods已有的重复说明。若同时改善Results和显示方法的阅读，可再选C01、C02、C05，五项合计64个词元。

**保持当前v3.24不再精简，也是合理选择。** 本轮检查未发现需要为字数限额而删除结论、挪走主表或大规模迁移Methods的理由。图3图注内部再合并误差定义、BBR回归句再缩短等低收益候选未纳入推荐清单。

## 实施和验收边界

1. 只按作者选中的C编号实施，当前均未执行；不修改刚获准的A/B解释、摘要或模型定位。
2. C04删除的轮廓半径说明仍须完整保留在Fig.3图注；其他候选保留条件、误差定义、处理归属和图号指向。
3. 不删数据筛选、权重、模板参数、采样效率定义、近岸掩膜敏感性、链路检验及注入结果等复现依据。
4. 不新增分析、数据、模型假设或引用。若执行，提供精确差异，再核对图表指引、引用顺序及PDF/Word排版。

## 检查记录

本轮采用ECC分工：正文审查、Methods/图注/SI审查、独立验证；并用academic-humanizer规则核对冗余与限定条件。脚本识别出的长句或括号密度仅作为检查线索，没有机械改写。新获准的B句保留其完整限定，未因超过某一词数再擅自压缩。

已核对父版本163个稿件文件未变；v3.24的13个章节中，仅opening和results_discussion包含获准五项替换，其余11个章节和119个图件保持字节一致。摘要、35篇已用文献及顺序、数学公式、作者贡献删除状态、LLM披露标题均核对。编辑检查器提示的数字标记增加已逐项核实为获准的24 h、12 h和ED Fig.1d，不是新测量数据。

为适应已批准首句替换，构建脚本将Table 1定位由依赖旧的“As shown in Table 1”文字改为按表格标记边界提取；这是必要的构建维护，不是额外稿件改动。

本文为写作与篇幅检查，不进行科学重算；所述研究仍为同一光钟比较时间序列，5个campaign、54个segment，未新增实验样本。各候选减少的词数来自文本计数，不是科学结果。输入与版本、脚本输出、独立验收和具体候选另见同目录记录。

当前稿件：`editorial_v324_20261109T083306Z/`；统计入口：`scripts/count_length.py --source sections --build formal_build_01 --out reports/length`，Python 3.12.3。选中候选的JSON为`reports/CONDENSATION_CANDIDATES.json`。此MD中所有候选仍处于未执行状态。
