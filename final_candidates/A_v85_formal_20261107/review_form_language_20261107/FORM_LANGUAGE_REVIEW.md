# v85 形式与语言评审

**结论：保留现有结构，做一轮定向语言校订；不需要再整体重写。** 标题、篇幅、四幅主图和正文顺序已适合作为 Nature Article 的作者审阅稿。尚未解决的主要问题是摘要与正文的术语口径、少数统计句子的准确表达，以及技术说明对 Results 阅读节奏的干扰。

评审对象：`NATURE_ARTICLE_A_v85.md` 及其 35 页 PDF。范围为形式、语言、段落功能和稿内定义一致性。没有重算数据、检查实验结果正确性或更换估计器；本报告不是科学有效性认证。原稿及 PDF 均未修改。

## 1. Nature 形式检查

按当前官方说明，初投格式具有弹性；以下将排版建议与真正待补材料分开，不把小幅格式差异当成拒稿依据。[Nature 初投说明](https://www.nature.com/nature/for-authors/initial-submission)

| 项目 | 本稿情况 | 判断 |
|---|---|---|
| 标题 | 67 个字符，排成两行 | 保留已定标题。 |
| 摘要 | 195 词 | 长度合适；尚无摘要内引文。 |
| 正文 | 去掉小标题约 2,300 词 | 摘要与正文合计约 2,495 词。 |
| 四幅主图图注 | 141、162、208、136 词 | 均低于初投说明的 250 词参考长度，且与图同页。 |
| Extended Data | 4 图、5 表，共 9 项 | 在通常 10 项范围内。 |
| Methods | 约 2,950 词 | 接近约 3,000 词指引；无需为凑数删复现信息。 |
| 主文小标题 | 第一节 55 字符，其余 35、32、36 | 第一节超过 40 字符指引，建议缩短，未改冻结文字。 |
| 引文顺序 | 主文 1–24；Methods 25–28 | 首次引用与列表次序一致。这里只核对形式，不重新核验引文内容。 |
| 作者与声明 | 仍有明确占位 | 真实提交前必须由作者完成。 |

**更正上一轮篇幅解释：约 2,500 词的典型六页 Article 指引包含摘要，不只是正文。** 本稿按一致的空白分词法仍约为 2,495 词；公式、连字符及版面会影响最终计数。标题、小标题、摘要引用和 Methods 的安排依据 [Nature formatting guide](https://www.nature.com/nature/for-authors/formatting-guide)，不应把这些指引理解为编辑接收保证。

摘要按指南应有必要的背景引用。既然该段已冻结，建议把“补入已有参考文献”的位置另交作者确认，不自行插入或重排。作者、通讯、贡献、基金、利益声明及可供审稿人使用的数据／代码访问仍需补齐。初投并不意味着所有数据必须已有公开 DOI；应提供与实际访问条件一致的说明。

## 2. 三处优先统一的表述

以下属于稿内定义一致性，不要求新增分析。

### L1：0.96±0.11 的名称与测量对象

位置：摘要，第 1 页；源稿第 19 行。

现文：*the joint measurement of solid-Earth and ocean loading ... with a consistency of 0.96 ± 0.11*。

问题有两层：“consistency”不是正文所定义的估计量名称；“joint measurement of ...”可能被读成两种贡献已经分别测出。正文实际报告一个尺度乘完整合成预测。

建议局部替换为：

> The measured response to the combined solid-Earth and ocean-loading prediction is 0.96 ± 0.11.

这保留检测结论与数值，仅让测量对象、模型和统计量的名称一致。属于冻结摘要，未执行。

### L2：“信噪比”与前后谱功率比并非同一项定义

位置：摘要；Results 第三节；Methods 的谱密度小节。

摘要写 *signal-to-noise ratios*，而 Methods 定义的是固定单位预测扣除前后、同一窗口下的谱功率比。正文还明确后者不是独立测得的仪器噪声底。两种名称不能靠 Methods 的限定语自行消除差异。

建议保留 16.7 和 9.3 dB，统一描述为：

> At the two peaks, the ratios of observed power to residual power after subtracting the unit prediction are 16.7 and 9.3 dB, respectively.

Results 的 *power divided by ... gives ... dB* 还省略了对数换算这一步。可写 *The power ratios, expressed in decibels, are ...*，具体公式继续留在 Methods。这里评审的是命名及句法，没有重新计算比值。

### L3：谱峰与分组尺度应使用不同动词

位置：摘要与 Introduction 末段、Results 第三节。

摘要说分开了 M₂ 和 S₂，Introduction 说联合估计 M₂+N₂ 与 S₂+K₂，正文又把 22.361 和 23.147 µHz 定义为扫描中的局部峰位。这些结果可以共存，但不能让读者把“谱峰位置”“固定组内关系的尺度”和“四个单分潮的独立测量”理解为同一件事。

建议沿用明确的搭配：*spectral peaks near M₂ and S₂*；*jointly estimated responses of M₂+N₂ and S₂+K₂*。例如：

> Spectral analysis resolves local peaks near the principal M₂ and S₂ frequencies, at 22.361 and 23.147 µHz, respectively.

不需要因此削弱全文的潮汐检测主线，也不需要重新讨论日潮组。摘要的调整仍须作者确认。

## 3. 各部分的阅读评价

### Abstract：信息齐全，但最需要局部语言校订

前三句已经给出物理背景。第三句 *precise probes for probing spacetime* 有明显重复，可简化为 *precise probes of spacetime*。结果部分并列多个数字，末句 *laying a foundation for related applications* 又转为空泛评价。建议优先解决 L1–L3，再由作者决定是否将结尾收束到本次动态位差测量能力。

*In this work, we use* 与 *we separated* 时态切换不算语法错误，但同一摘要中用现在时陈述本文结果会更整齐。不得因此改变数值或证据力度。

### Introduction：保留三段，不建议扩写

现有“重力测量需求—光钟与链路能力—本文工作”的顺序清楚。第一段的大气潮句略像插入的知识点，但不影响理解，不值得为此大改。第二段内容较密，已有充足引文，无需继续加技术发展支线。

主要衔接缺口在最后一段：它直接进入分组估计，没有点出 Results 首先报告的全模板响应。可在分组句前加一句：

> We first estimate the response to the complete tidal prediction.

无需在引言重复 0.96±0.11。冻结引言仅列建议。国际最佳钟能力与本实验双钟比较性能目前位于不同章节，这种区分应保留。

### Results：四节顺序成立，局部应从计算语言改为测量语言

- 第一节很好地交代装置与预报量级。保留双钟加链路、主要由双钟贡献的稳定度指标。为避免与“本年度记录连续达到数天”的说法混淆，可考虑给这一句加 *reported comparison instability*，与 Methods 的性能参考口径对应；本轮不判断该性能指标是否正确。
- 第二节先写全记录响应，再写相位与实际时间，顺序正确。但 *project ... against*、*fixed minor-constituent remainder*、*support count* 连续出现，容易让非专业读者暂时失去测量画面。正文可解释为去除段内常数和其他模型潮组；投影定义及误差传播保留在 Methods 和图注。
- 第三节定义了两组的物理组成，值得保留。*We keep these estimates separate* 是作者操作说明，前面的模型区别已足够，可以删去。0.78 与 0.786 µHz 不矛盾，但精确差值不必与天文间距在正文同时强调；峰位和 Methods 的扫描定义仍保留。
- 第四节应继续显示全部八期，不截短宽误差棒。段落不要将宽区间重叠描述成八次精确确认。当前正文已有解释，可保留；标题可选 *Responses across observing periods*，这是可选精简，并非必须改名。

一处直接的语法／统计搭配问题：*the larger of residual-scaled least squares and deletion of individual UTC observing days* 比较的是两种方法，而不是两个误差。建议：

> The reported uncertainty is the larger of the residual-scaled least-squares and UTC-day-deletion jackknife standard errors.

### Discussion：新增分段讨论有价值，语气应再论文化

将另一种分段的具体系数放入 Methods 是正确安排。Discussion 保留短段去均值的信息损失及与谱旁峰的联系，但不要把“观测点删去”“参考水平划分”和“谱泄漏”混作一个操作。

*Consider stability, continuous run length and astronomical phase coverage separately* 像面向作者的工作指令。建议改成条件陈述：

> Neglecting their couplings, stability, continuous run length and astronomical phase coverage impose different requirements on the measurement.

保留“噪声相当、参考水平稳定”以及“不能从现有时段单独隔离段长效应”的条件。不要为了语言有力，把它改写成已证明“单段越长结果必然越好”。

开头的测量总结与第二段的相位解释略有重复，可适度压缩。最后一段的海洋负荷与未来基线联系具体，应保留。欧洲工作仍按作者要求只在 Discussion 末句出现；不据此重写引言或重新定位本文。

### Methods：主体可用，清理工作记录式文字

保留两条估计式、权重定义、各类误差、条件模拟、谱归一化以及分段比较。以下是语言与呈现建议，不是删掉方法条件：

- *frozen primary design*、*previously replayed designs*、表内 *Replayed* 是内部版本状态，宜移到交付记录；论文使用分析设计的实际名称。
- *none is asserted here*、*No scenario is selected because ...* 等编辑过程口吻可用直接的方法说明取代；每项必要限定保留一次。
- 种子、模拟次数和模型参数属于复现信息，不能因为自动语言扫描把它们标成“worklog”就机械删除。
- “the package contains ...”应指向实际分析包，不能让读者误把仅含文稿和图件的编辑源包当作完整数值复现包。作者须补明访问位置与包名。

## 4. 图表及统一用语

| 项目 | 建议 |
|---|---|
| 第一节小标题 | 可改为 *A coastal–inland clock baseline*，满足短标题要求；原题不变。 |
| 图 2 选段规则 | 统一称“有效观测时长最多的段”；图注仍保留 accepted sample count 这一客观依据。不要暗示按吻合程度选择。 |
| 图 2c 图注 | *No ... fit-dependent offset is removed* 与前面的去均值容易误读。建议明确“没有根据潮汐拟合调整段间电平”，不否认已经进行了显示去均值。 |
| 图 3c | 对数轴和单位完整。旁峰在 log 轴下更明显是显示效果，不应在文字中说成新出现的观测结构。保留对数版，不因视觉效果重新选窗。 |
| 图 3b | scaled-LS 协方差轮廓与正文采用的较大标准误不是同一误差对象。图注已有区分，但应让“covariance contours”紧邻图内标签，避免读者按 68%/95% 联合置信区间阅读。无需改数值。 |
| 图 4 | 八期全显示及完整误差范围应保留。每期样本量可留图注，不必在正文逐个复述。 |
| 英文拼写 | 正文混用 fiber/fibre，另有 leveling 与 centred。选择一套正文拼写；参考文献原题及单位的正式名称不随之改写。 |
| 层级术语 | period＝8 个观测期；segment＝54 段；operating group＝29 组；bin＝600 s 均值；member＝一秒成员。正文尽量使用 observations / ten-minute means，把 member 留在 Methods。 |
| 误差名称 | 首次定义 statistical standard error；Methods 说明取最大规则。避免把 working error、nominal interval 与已校准置信域当作同义词。 |

## 5. 下一轮最小修改范围

1. 作者确认后统一摘要的三个术语问题，并补必要引用；不动标题和数值。
2. 引言只补全模板到分组的过渡，不重新扩写。
3. 修正 Results 的误差搭配，压缩投影术语和重复说明。
4. Discussion 保留分段／旁峰联系与长连续段的条件性意义，改掉指令式句子。
5. 缩短第一节标题，统一正文拼写，清理 Methods 的版本状态用语，并由作者完成声明和访问安排。

**推荐结论：形式基本合格，语言需定向修改；无需新分析，也无需再重构文章。** 本轮只有评审意见，没有生成 v86 或更改冻结文字。

## 评审依据与可追溯性

依据 Nature 官方指南、nature-writing / nature-polishing 的结构与一致性规则，以及 academic-humanizer 的人工语言检查。程序仅统计文稿、检查术语和记录文件哈希。

自动扫描中的参考文献作者缩写、文章原题以及 Markdown 表格会产生误报，未据此建议删改真实文献或统计参数。扫描清单不是 AI 文本鉴定，也不等于逐条必须修改。

报告来源文件的 SHA256、统计输出和原始语言扫描一并保存在本评审目录。原稿不变。
