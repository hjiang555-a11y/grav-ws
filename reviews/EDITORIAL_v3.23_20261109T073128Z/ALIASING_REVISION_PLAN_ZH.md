# 采样混叠的物理解释：文中原句与修改计划

2026年11月9日｜基于当前v3.23｜作者讨论稿

**状态：仅整理讨论方案，尚未修改论文。** 本文件摘录当前稿件中的相关语句，说明拟修改的位置、目的和边界，不提供已实施的替换稿。此次发布仅涉及本计划文件。

## 一、希望讲清楚的物理联系

**有限、间断的观测 → 谱泄漏与采样混叠 → 强潮汐在其他频率产生响应 → 影响弱信号识别及估计精度。**

术语使用需要区分：有限观测时长使谱线展宽，并产生窗口相关的谱泄漏（spectral leakage）；离散采样，特别是带有间断和周期结构的采样窗口，还可能产生混叠峰（sampling aliases）。不把“有限长度必然产生aliasing”作为严格表述。

本文更直接的证据是：选定旁峰的响应与实际采样下的预测一致，并随拟合月潮波形的扣除按预测减弱。谱上出现峰本身不足以确定其来源。

弱信号的影响分两层讨论：强背景建模不充分可能使其估计产生偏差；即使联合拟合模型正确，分量耦合仍可能增大不确定度。不把这种作用一概称为新增随机噪声，也不把采样效率因子η描述为能够自动消除模型遗漏或系统偏差。

## 二、Introduction：提出采样带来的物理问题

位置：`sections/opening.md`，第9行，第二段末尾。

### 文中原句

> Lunar and solar contributions must be distinguished from each other and from laboratory variations that follow the solar day, while observational gaps spread spectral power into neighbouring frequencies. Subtracting the tidal background therefore requires separating the tidal components and their sampling sidelobes and quantifying the precision of each component.

### 修改计划 P01

- 补清楚有限观测长度与间断采样的作用，引入 **spectral leakage and sampling aliases**。
- 说明强潮汐的频谱响应会延伸到其他频率，从而影响弱信号识别。
- 保留月球、太阳频率贡献及实验室太阳日变化需要区分的研究问题。
- 引言只交代问题，不展开数学推导或扣除检验细节。

## 三、Results—Reliability：用已有证据解释采样混叠

位置：`sections/results_discussion.md`，第25行，Reliability of the separated signals首段。

### 文中原句：段首

> Reciprocal subtraction tests the coupling introduced by the sampling (Extended Data Fig. 4).

### 文中原句：段末

> The maximum canonical correlation between the projected sine–cosine pairs is 0.290 (Extended Data Fig. 5), and the strongest sampling sidelobes respond to lunar-waveform subtraction as predicted (Extended Data Fig. 6).

两句之间现有的双向扣除结果及数值仍保留。本计划不是删去该段中间内容。

### 修改计划 P02

这是本轮主要修改位置。

- 段首先解释：实际采样使不同频率分量不能完全分开，强分量会贡献于其他频率的估计。
- 中间保留现有双向扣除结果和数值，让物理解释与检验相连接。
- 段末明确：部分旁峰随月潮波形扣除而按预测减弱，支持其为 **sampling aliases** 的解释。
- 强调证据来自“采样响应预测＋扣除后的变化”，而不只是“谱上出现峰”。

现有SM7记录两个选定旁瓣下降约94%和92%，可作为上述解释的支持依据；**暂不计划往正文再增加一组数字**。不把所有次峰统称为混叠，不声称已经排除所有独立弱信号。

## 四、Discussion开头：连接采样效应与弱信号精度

位置：`sections/results_discussion.md`，第35行，Discussion开头。

### 文中原句

> We develop a signal-to-noise model that relates component precision to signal strength, noise and phase coverage. The observation schedule enters through the sampling window and coupling between fitted components; within short segments, a slowly varying tide is partly absorbed by the fitted offset.

### 修改计划 P03

保留 **We develop** 及团队发展的模型定位，把第二句所概括的作用解释得更有物理直观：

- 强背景建模不充分，可能使弱信号估计产生偏差。
- 即使采用正确的联合拟合，分量耦合仍可能增大不确定度。
- 短记录中的慢变化分量还会与段偏置混淆。

随后自然引入η对采样、偏置及分量耦合造成的精度影响的描述。模型中的η解释的是相应估计器的测量效率；**不把它写成能够自动消除模型遗漏或系统偏差的因子**。

保留一般标度关系与本次白噪声实现的区别，不宣称本文已实测验证任意时间范围的积累指数。

## 五、Discussion观测建议：将建议与物理机制对应

位置：`sections/results_discussion.md`，第58行，后续观测方向段。

### 文中原句

> Continuous runs of at least two days with maintained phase lock cover successive diurnal cycles; a longer calendar span separates neighbouring frequencies, while gaps create sidelobes (Extended Data Fig. 6).

### 修改计划 P04

- 连续运行改善周期覆盖，减弱慢变化分量与段偏置的混淆。
- 更长的日历跨度有助于提高邻频分辨能力。
- 减少有结构的观测间断有助于抑制采样混叠；具体效果仍取决于实际观测窗口。
- 区分连续运行长度、日历跨度与总有效观测时间，避免暗示仅增加总有效时间即可解决所有分量耦合问题。

原段对钟稳定度、额外站点及环境记录的讨论继续保留。此次不新增所需观测小时数、混叠抑制比例或其他尚未计算的设计指标。

## 六、现有支持材料及其职责

### Extended Data Fig. 6

现有标题：

> Sampling aliases and amplitude response to compensation.

位置：`sections/extended_data.md`，第25行。

该图已承担实际采样下的混叠峰与补偿响应展示，正文应明确调用这一证据。本计划不新增主图，不调整主图布局，不重新制图。

### Supplementary Methods SM7

现有标题：

> SM7. Compensation, alias and correlation diagnostics

现有定量说明：

> At 22.1016 and 22.6283 μHz, subtraction of the jointly fitted lunar waveform reduces the amplitudes from 3.149 to 0.204 cm and from 3.307 to 0.266 cm, reductions of 93.51% and 91.97%, with minima at compensation factors 0.9974 and 1.0490 (Extended Data Fig. 6).

位置：`sections/supplementary_methods.md`，第59、71行。

这些是稿件已有结果，不是此次重算。数值继续保留在SM7，正文侧重解释机制与证据关系。

## 七、范围与验收计划

拟修改范围集中在P01–P04四处。摘要、主图布局、科学数值、公式及已确定的模型贡献保持原方案；不借此次讨论改变S₂检出或来源归因的主张强度，也不将月潮稳健性自动推广为S₂来源已被排除。

后续实际改稿的验收要求：

1. 原句与修改句逐项对应，正文物理因果关系更清楚，避免在四处反复重复同一解释。
2. spectral leakage、sampling aliases、分量耦合和随机噪声不混为一谈。
3. 旁峰解释限于已有采样预测与扣除试验支持的对象。
4. 对弱信号的可能偏差和不确定度增大分别说明；不声称η自动修正模型误差。
5. 数值、公式、摘要及图件不变，ED Fig.6与SM7的引用保持正确。
6. 不进行新计算；如后续需要新增量化结论，另列任务，不编造补齐。
7. 改稿完成后再检查篇幅、引用和PDF排版；本讨论文件的发布不表示这些改稿已执行。

## 八、版本与检查记录

来源为当前本地v3.23（已覆盖修复LLM披露标题）：

`/data/AI_Research/projects/grav-ws/manuscript_48h/editorial_v323_20261109T073128Z/`

行号指Markdown源文件，不是PDF行号。原句来自实际读取的当前稿件；此次仅整理计划，未更改论文、图件或数据。原句匹配检查、稿件文件前后SHA256及GitHub发布记录保存在对应计划工作目录。
