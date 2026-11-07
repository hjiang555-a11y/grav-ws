# v85 完整稿：作者审阅说明

本版按已确认主线完成英文 Article。使用 ECC article-writing、verification-loop，并结合 nature-writing 与 academic-humanizer。论文正文为 Introduction、Results、Discussion；摘要及既定段落保持原文。本文是供作者审阅的完整稿，尚非已获得作者批准的投稿稿。

## 本轮实际修改

- 第一层结论是两台相距 692 km 的光钟检出潮汐位差变化；第二层是同一记录中相邻半日潮组的响应估计。先写测量现象，再解释模型和成分。
- 冻结标题、作者定稿 Abstract、确认版 Introduction、最新 Results 1 及图 1 图注。它们在正文中逐字保留；建议另见 `FROZEN_TEXT_SUGGESTIONS_ZH.md`。
- 补全后续 Results 和 Discussion，沿用已报告的全模板 0.96±0.11、月潮组 1.00±0.13、邻近组 0.93±0.36，不平均不同估计器。
- 图 2 保留全记录相位图及真实 UTC 时序；时序按保留有效观测时长最多选取，主估计仍使用全部 3,299 个均值。
- 图 3c 仅改为对数纵轴。左轴 cm²/µHz，右轴分数频率谱密度；谱曲线来自已有绘图结果，未重算频谱。16.7/9.3 dB 在 Methods 明确定义为减去固定单位预测前后的同频功率比。
- 图 4 只展示八期各自的两个半日潮组系数。零点方案、删期结果和光纤回归放入 Extended Data。
- 按最新指示，把同数据八期／54 段零点的系数和差值放入 Methods。Discussion 解释短段去均值的信息损失，以及采样和投影对谱旁峰的影响；不声称两种现象已被证明具有同一来源。
- 保留双钟加链路的比较稳定度 5.4×10⁻¹⁶/√(τ/s)，up to a few days，明确主要来自双钟。保留已发表 Sr、Yb 评估及 Light 链路文献。
- 无 Hou 文献。Stahl 只在 Discussion 末句提到，作为独立同期 arXiv 工作。

## 篇幅与版式

摘要 195 词；正文约 2,330 词（含小标题）；Methods 约 2,950 词。4 幅主图、4 幅扩展图、5 张扩展表，共 28 条文献。Nature 当前指南以约 2,500 词正文和四幅适中图表作为典型六页 Article 的参考；Methods 中的图表另置 Extended Data。本版采用行号、双倍行距和矢量 PDF 图，便于作者审阅。

官方依据：[Article formatting guide](https://www.nature.com/nature/for-authors/formatting-guide)、[initial submission](https://www.nature.com/nature/for-authors/initial-submission)。篇幅不是投稿适格或编辑接收的保证。

## 证据使用范围

本轮仅读取已有稿件、既有结果表及绘图输出。没有运行实验数据清洗、筛选、拟合、仿真或正确性核查；Methods 中的计算和模拟描述均继承已有分析，不代表本轮重新完成。表中的历史 replay 状态亦不是本轮验证结论。

主估计沿用既有 segment-based reduction：54 段独立零点、原 Allan 权重、600 s 均值和原误差规则。固体项仍是既有位移到有效势的近似；未将 v68 的直接势实现混入这套结果。另行解释或升级模型需要独立授权。

## 作者仍需确认

1. 署名、单位对应、通讯作者、贡献、基金、利益冲突及实际 AI 使用范围。
2. 审稿人可用的数据和代码访问地址、许可证，以及原始记录的访问条件。
3. 对已定稿摘要的措辞建议是否采用，尤其是“joint measurement”“consistency”和谱功率比的命名。
4. 双钟比较多日稳定度的引用依据及适用记录。正文按作者指定指标保留；Methods 继续说明其不用于主拟合权重，也不由拟合接续的稳定度构建权重。
5. 与既有频率比稿的观测重叠及相关稿件状态，在投稿信中如实向编辑披露。本版遵照指示不在正文引用该稿。

所有结果仍需作者承担最终科学核验与投稿决定；本轮不代为投稿。
