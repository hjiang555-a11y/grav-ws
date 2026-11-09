# 频谱与Discussion局部修改计划（第二版）

2026年11月9日｜基于当前v3.23｜讨论计划，尚未修改论文

**按作者最新意见：保留两处主要句子替换，并统一三处相关术语。** 本版取代[上一版计划](SPECTRUM_AND_SNR_REVISION_PLAN_ZH.md)的候选措辞；不扩写章节、不改变模型或科学结果。

## A．频谱相关段落：只用sampling aliasing，说明相关性

**替换位置：** Results → Reliability of the separated signals，第一段第一句；`sections/results_discussion.md:25`。

**原句：**

> Reciprocal subtraction tests the coupling introduced by the sampling (Extended Data Fig. 4).

**替换为一句：**

> Sampling aliasing in the finite, interrupted record introduces correlations between frequency components, which we test by reciprocal subtraction (Extended Data Fig. 4).

中文意思：有限、间断记录中的采样混叠引入频率分量之间的相关性，我们通过双向扣除检验这种作用。

**与上一版的差别：** 去掉候选句中的“spectral leakage and sampling aliases”并列，统一用 **sampling aliasing**。保留频率分量相关性与双向扣除的衔接。原句后面的扣除数值、0.290相关性及图件指引全部保留。

本稿讨论的是实际观测窗口造成的频率响应和分量耦合，统一采用该术语即可；不另加“所有谱泄漏与混叠在一般定义下完全等同”的论断。

## B．Discussion：间接解释强、弱分量的符合程度差异

**替换位置：** Discussion中Table 1之后第一段的第一句；`sections/results_discussion.md:56`。用下面两句替换该首句，不另起段。

**原句：**

> As shown in Table 1, the lunar precision agrees well with the white-noise expectation, whereas the solar-frequency, diurnal and loading estimates have larger empirical uncertainties.

**替换为两句：**

> The model-estimated signal-to-noise ratio closely matches the measured value for the lunar component, whereas agreement is poorer for the weaker components (Table 1). This difference may reflect the greater relative impact of residual contamination through sampling aliases on weak signals, together with non-white laboratory variations at 24 h and 12 h that could increase the uncertainties of the diurnal and solar-frequency components (Methods; Extended Data Fig. 1d; Supplementary Methods SM4).

**中文意思：** 模型估计的信噪比与月球分量的实测值非常接近，而较弱分量的符合程度较差。这一差异可能与弱信号对采样混叠所传递的残余污染更敏感有关，也可能受到24 h和12 h非白噪声实验室变化的影响，后者可能增大日潮和太阳频率分量的不确定度。

**具体差别：**

- 第一处把“月潮精度符合白噪声预期”明确写成“模型SNR与实测SNR比较”，对应Table 1的model estimated/measured标签。
- 第二处加入两类可能原因：弱信号受到残余混叠污染的相对影响，以及24 h/12 h实验室变化的非白噪声性质。采用 **may reflect / could** 间接表述，不将可能机制写成已经完成的因果归因。
- “较弱分量不准”写为 **agreement is poorer**，即模型与实测的一致性较差，不把经验估计本身判作错误。
- 使用 **residual contamination**：现有模型已包含采样窗口和分量耦合，这里指未被充分描述或去除的残余影响，不将已计入的耦合再算一遍。

**紧接其后的原句及该段其余内容不动：**

> Short segments constrain diurnal cycles weakly after offset removal, and the smaller loading signal overlaps the solid-Earth waveform.

这句继续解释日潮的短段/偏置限制和海洋负荷的波形重叠；环境日周期的候选解释不泛化到所有弱分量。

## C．其他位置：仅做术语统一

当前已编译稿中没有“spectral leakage”字样；它出现在上一版候选A句。此次从候选中去掉，并将当前稿涉及同一采样旁峰的三处表述统一为sampling aliases：

| 编号 | 精确位置 | 原短语 | 拟替换短语 | 其余内容 |
|---|---|---|---|---|
| T1 | Introduction第二段末句；`opening.md:9` | their sampling sidelobes | their sampling aliases | 不动 |
| T2 | Reliability首段末句；`results_discussion.md:25` | the strongest sampling sidelobes | the strongest sampling aliases | 相关性数值、扣除结论和ED Fig.6指引不动 |
| T3 | Discussion观测建议段；`results_discussion.md:58` | while gaps create sidelobes (Extended Data Fig. 6) | while gaps create sampling aliases (Extended Data Fig. 6) | 只替换这一短语，不扩写建议 |

ED Fig.6标题已用“Sampling aliases”；SM7标题及正文已用“alias diagnostics”，无需再次改动。以上都是用词统一，不增加新的论证段落。

## D．环境解释的现有指引

B句末的三个指引分别对应：

- **Methods：** Daily terms, environment and prediction，`auxiliary_methods.md:35–51`，包含24 h/12 h拟合项、气温替代模型与室温回归。
- **Extended Data Fig.1d：** 按当地时间折叠的残差及温度重叠记录，图注说明黑体辐射变化已做实时校正。
- **Supplementary Methods SM4：** `supplementary_methods.md:35,39,41`，包含温度回归、24 h/12 h项及日项模型检查。

只指引过去，不把这些结果再抄入Discussion。现有检查主要提供日周期/环境敏感性证据，并未独立量化它们对S₂信噪比差额的贡献，因此保留间接表述。两钟已实施黑体辐射实时校正，不能把未经校正的变化当作当前残余噪声。

## E．执行边界与验收

- A：一句替换一句；B：一句替换两句；T1–T3：三个短语替换。
- 原句/短语均需在当前源稿中唯一匹配；其余句子不动。
- 摘要、We develop模型定位、公式、已有结果数值、主图及Table 1数据不变。
- 不进行新拟合、模拟、误差预算或归因计算。
- 实施后核对术语与指引、篇幅及排版。当前仅发布计划，不执行候选替换。

## 版本记录

当前源稿：`/data/AI_Research/projects/grav-ws/manuscript_48h/editorial_v323_20261109T073128Z/`。

行号为Markdown源文件行号。所有原句均从实际源文件核对；候选替换的JSON及差异预览另存本任务目录。**差异预览只在内存中生成，没有改写稿件。**
