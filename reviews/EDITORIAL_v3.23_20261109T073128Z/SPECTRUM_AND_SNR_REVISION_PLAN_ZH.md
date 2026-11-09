# 频谱与Discussion：两处局部语句修改计划

2026年11月9日｜当前v3.23｜仅供讨论，尚未修改稿件

**按作者最新要求，范围限定为两处原句替换：A一处频谱相关说明；B一处Discussion说明。** 不扩写引言，不改章节、模型、公式、摘要、图表或科学数字。本文给出原句、候选替换句和具体差别；发布计划不等于执行改稿。

本计划更新并收窄此前[采样混叠讨论计划](ALIASING_REVISION_PLAN_ZH.md)：旧计划涉及引言、模型开头和观测建议的扩展不再作为当前拟执行范围。这里的“aliasing只放频谱部分”指修改位置的限制，不是声称采样作用在物理上只存在于画谱时。

## A．频谱相关说明：替换一句，点明aliasing与相关性

**位置：** `sections/results_discussion.md`第25行，Results → Reliability of the separated signals，首句。该段紧接半日潮频谱分离结果，已有双向扣除、相关性及旁瓣证据。

### 原句

> Reciprocal subtraction tests the coupling introduced by the sampling (Extended Data Fig. 4).

### 候选替换句

> Finite, interrupted sampling produces spectral leakage and sampling aliases, introducing correlations between frequency components that we test by reciprocal subtraction (Extended Data Fig. 4).

### 改了什么

原句直接说“采样引入耦合”，没有说明其频谱表现。候选句只在这里补出：**有限、间断采样产生谱泄漏和采样混叠，并引入频率分量间的相关性。** 后半句仍用现有双向扣除检验承接，不增加新的检验或结果。

紧随其后的幅度变化、0.290相关性，以及ED Figs.5、6指引全部保留。该段末尾已有“sampling sidelobes”的描述，继续作为具体旁瓣表现，不需要再另加一段aliasing解释。

**范围：只替换这一句。** 不将aliasing扩写进Introduction、Discussion模型开头或观测建议。

## B．Discussion：替换首句为两句，说明估计符合程度与可能的环境影响

**位置：** `sections/results_discussion.md`第56行，Discussion中Table 1之后的首句。

### 原句

> As shown in Table 1, the lunar precision agrees well with the white-noise expectation, whereas the solar-frequency, diurnal and loading estimates have larger empirical uncertainties.

### 候选替换句

> The model-estimated signal-to-noise ratio closely matches the measured value for the lunar component, whereas the weaker components have larger empirical uncertainties than predicted by the white-noise implementation (Table 1). Residual laboratory variations at 24 h or 12 h could further reduce the precision of weak diurnal and solar-frequency components (Methods; Extended Data Fig. 1d; Supplementary Methods SM4).

### 改了什么

1. **第一句更明确地对应Table 1。** 从“月潮精度符合白噪声预期”改成“模型估计的SNR与实测月潮SNR接近，而弱分量经验不确定度更大”。与已确定的 **model estimated / measured** 标签一致，同时说明本次模型实现采用白噪声假设。
2. **第二句补一个可能的物理原因，并直接指引现有材料。** 校正后仍可能存在的24 h或12 h实验室变化，可能进一步降低弱日潮和太阳频率半日潮分量的测量精度。采用 **could**，不写成已经证实的因果解释。
3. **不把“降低精度”写成“必然压低物理振幅”。** 本处讨论的是SNR和经验误差；日周期扰动对具体幅度的影响还取决于相位和投影。

该段第二句及以后保持原文，包括：

> Short segments constrain diurnal cycles weakly after offset removal, and the smaller loading signal overlaps the solid-Earth waveform.

这句已经解释短段/偏置对日潮及波形重叠对负荷的限制，不再重写。候选句也不把环境日周期用于一概解释海洋负荷列。

**范围：将原有首句替换为上述两句，其余段落不动。** 不新增SNR数字、不改变模型定位，不把aliasing扩展成Discussion中的另一段解释。

## 现有环境材料，指引到哪里

| 指引位置 | 已有内容 | 本次如何使用 |
|---|---|---|
| Methods → Daily terms, environment and prediction；`auxiliary_methods.md:35` | filtered验证中的24 h、12 h日项，以及使用气温相位或异常值的替代模型 | 说明日周期扰动已被考虑，不追加新分析 |
| Extended Data Fig.1d；`extended_data.md:5` | 按当地时间折叠的残差、夏季温度重叠记录及BBR比较 | 提供环境日周期的现有图示入口；图注已说明BBR实时校正 |
| Supplementary Methods SM4；`supplementary_methods.md:35,39,41` | 温度回归、24 h/12 h拟合项及不同日项模型下的验证结果 | 提供现成细节，不将表内数字重新搬入Discussion |
| Fig.4及Results第27行 | 月潮估计对日项和环境处理的稳健性 | 保持原位；这些主要检验月潮，不能当作已经量化S₂误差来源的证明 |

本次引用的是**已有检验及可能影响机制**。两钟已实施黑体辐射实时校正，因此候选句用“Residual laboratory variations”；不能把未校正的BBR变化直接写成当前实测残差。

## 为什么这样限定解释

作者希望讲清“月潮这一较强分量估计接近，其他弱分量偏差较大”。现有Table 1支持这一观测事实，但不能仅凭幅度强弱就认定原因：同一列的模型与实测SNR使用同一幅度，差别来自不确定度估计。候选句因此把“符合程度”与“可能的环境影响”分开陈述，避免写成所有强信号都必然估计准确、所有弱信号都不准确。

Methods已通过实际采样、拟合算子和η包含采样窗口、偏置及分量耦合。故不把已有aliasing/耦合另算成模型遗漏的误差。A只补频谱物理说明；B只以可能的残余日周期影响解释白噪声实现的适用局限，并指引已有检验。**这些说明仅用于解释候选措辞的取舍，不准备额外加入正文。**

## 后续实施与验收

- 仅对上述两个唯一匹配的原句执行替换；A一变一，B一变二。
- 不触碰其余句子、摘要、数值、公式和图件。
- 保留model estimated标签和We develop模型定位。
- 指引与现有Methods、ED Fig.1d、SM4一致；明确日周期环境是可能解释，不冒充已完成的误差分解。
- 不扩大aliasing修改范围，不增加计算、表格或数据要求。
- 如后续获准实施，再核对文字差异、引用顺序、篇幅及PDF排版；本阶段只形成并发布MD计划。

## 原句与版本记录

原句从当前v3.23实际源文读取，行号为Markdown源文件行号，不是PDF行号。输入路径：

`/data/AI_Research/projects/grav-ws/manuscript_48h/editorial_v323_20261109T073128Z/`

本轮未运行新的拟合或误差计算，未修改稿件。原句匹配和稿件前后哈希检查另存于本任务记录。
