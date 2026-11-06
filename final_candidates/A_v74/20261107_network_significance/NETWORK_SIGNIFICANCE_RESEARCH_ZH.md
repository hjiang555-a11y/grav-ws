# 光钟网络的技术意义：核验结果与入稿依据

检索日期：2026-11-06；范围：原始研究、计量机构文件及原始数据产品说明，重点补查 2024–2026 年进展。正文以 A_v72 主分析为基础，本轮未新增拟合。

**最适合本稿的意义是：面向共同守时而连接起来的光钟，也能成为观测地球时变位势的基础设施；本实验验证了其中一项具体能力，即在中断和未知段零点下，辨别相邻半日潮响应。** 这是从本实验和下列文献形成的综合判断，不是声称本稿已经实现网络守时或水文监测。

## 证据与引用

| 主题 | 已核实证据 | 对本稿的作用 |
|---|---|---|
| 跨国光钟网络已在运行 | Lindvall 等的协调实验连接六国十台光钟，用光纤与卫星链路比较频率比。正式版为 *Optica* 12, 843–852 (2025)。 | 支持“网络化已有实验基础”，不是把未来说成必然。新增正文引用。 [论文](https://doi.org/10.1364/OPTICA.561754) |
| 联合守时能够容纳间断光钟 | Yao 等以连续微波钟组为飞轮，由间断工作的 Yb 光钟校准时间尺度。 | “间断”是实际网络会面对的条件；该工作不是潮汐测量，本稿也不是新的时间尺度。新增引用。 [论文及原文](https://doi.org/10.1103/PhysRevApplied.12.044069) |
| 守时必须掌握位势 | Dimarcq 等秒重定义路线图将远程比较、对时间尺度的贡献和地球位势知识列为相关挑战；BIPM 2026 战略继续部署光钟与光学链路进入时间尺度。 | 可以连接本研究与红移修正需求，而不宣称本稿已完成绝对零点标定。新增路线图引用。 [路线图](https://doi.org/10.1088/1681-7575/ad17d2)、[BIPM 战略](https://www.bipm.org/documents/d/guest/bipm-strategic-plan-2026-201025v1-1) |
| 地球监测具有明确物理目标 | Schröder 等模拟了大气、水文和冰质量变化对钟比较的影响，强调与 GNSS 高程观测结合；Vincent 与 Müller 对不同区域质量变化和形变作了模拟案例。 | 支持未来方向，不能称为已实测的水文信号。保留原引用并增加 2024 年研究。 [2021 论文](https://doi.org/10.1093/gji/ggab132)、[2024 论文](https://doi.org/10.1016/j.asr.2023.07.058) |
| 与水准测量互补 | Denker 等说明水准与重力资料可以给出位势差；短距离精密水准很强，长距离误差传播及基准联系较复杂。 | 本稿强调建成链路后可重复比较两端，不写“水准只测几何，不能测位势”或“光钟所有精度都更高”。 [原文](https://doi.org/10.1007/s00190-017-1075-1) |
| 与卫星重力互补 | GRACE Tellus 的标准陆地质量产品为月产品，并施加大气等背景修正和空间滤波。 | 可以比较观测时间尺度与量的不同；不能据此称所有卫星观测对日/半日变化无能为力。 [JPL 数据说明](https://grace.jpl.nasa.gov/data/get-data/monthly-mass-grids-land/) |

补查的较新原始材料：Lee 等 2026 年预印本比较了持续超过 20 天的三套全光学时间尺度；Tofful 等 2026 年预印本的长距离钟比较指出红移修正是其不确定度的重要来源。这些材料加强研究背景，但本稿无需堆积所有新文献，未加入正文引用。[Lee 等](https://arxiv.org/abs/2608.00910)、[Tofful 等](https://arxiv.org/abs/2610.29980)

## 落入本稿的三层意义

1. **本次已展示：** 在 692 km 站间距离、真实中断采样与 54 个独立段零点下，联合估计两组半日响应，并解释实测谱的双峰及窗口旁瓣。0.78 µHz 是目标主频间距；这项辨别利用了长期日历覆盖，不能改写为一次数小时观测就达到同等频率分辨率。
2. **网络的共同需求：** 守时把位势引起的频移作为需掌握的修正，地球监测把位势变化作为待测信号。两者都需要区分地球信号与钟、光梳、链路变化。本文的分组模板、相位参考及实测对照回应这一共同需求。
3. **下一步能力：** 连续钟运行、持续链路比对及独立质量判据有助于增强日周期约束。向慢变水文、大气质量等拓展，还需要跨段参考水平的标定与站点高程监测；不能把当前自由段常数模型直接当成季节水文测量方案。

稿件只增加引言的两句背景和讨论的一段意义，四幅主图与数值保持不变。未采用“首次验证”“将全面超过传统测量”等尚无足够检索或实验支撑的说法。

## 入稿英文段落

Clock networks connect this geophysical capability to the realization of time itself. International comparisons already link optical standards across countries, and intermittently operated optical clocks have steered continuous time scales. A common time scale requires clock frequencies to be referred to a consistent gravitational potential; Earth monitoring treats changes in that potential as the signal. Once a frequency-transfer link is established, it can repeatedly compare distant endpoints during operation without resurveying the intervening terrain. Such observations complement levelling surveys and the standard monthly gravity products from satellites. The temporal resolution attainable for a particular signal depends on clock stability and simultaneous operation. With improved continuity, calibrated reference levels and colocated height measurements, future networks could extend these differential observations to atmospheric and hydrological mass changes. Resolving known tidal components across interruptions tests the signal discrimination that those applications require.

精确引用已插入主稿，并按首次出现重新编号。新增四条文献的完整元数据和 BibTeX 位于 `editorial/network_research/`。Crossref 对 Lindvall 只提供首页，对 Yao 漏掉文章号；已分别依据正式论文补为 843–852 和 044069，改动逐项留档。NIST 路线图网页的作者排列与论文首页不一致，正式引用采用原文与 Crossref 一致的 **Dimarcq et al.**。

## 工具记录

检索组合为网页检索、arXiv 原始稿、期刊/机构原文、OpenAlex 和 Crossref；搜索结果相关性不能替代正文证据。`citation-management` 用于元数据提取与校验，`academic-humanizer` 用于英文表达。按所用技能的溯源要求，在本研究记录的软件部分引用：Kassis, T., Agarwal, V., He, Y., Patel, D. & Brueckner, A. M. *Scientific Agent Skills: A Library of Procedural Knowledge for Research Agents*. arXiv:2609.00065 (2026). [来源](https://doi.org/10.48550/arXiv.2609.00065)。它仅是工具出处，不是潮汐物理证据，也未加入论文参考文献。
