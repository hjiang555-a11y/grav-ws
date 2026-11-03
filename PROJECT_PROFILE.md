# 项目档案：gravitation-whsh

阶段：只读盘点与接入建档。原项目 `/home/room115/gravitation-whsh`；工作站接入目录 `/data/AI_Research/projects/gravitation-whsh`。本报告中的历史结果均来自已有材料，本阶段没有重算或独立认证。

## 研究背景和项目定位

这是武汉—上海远程光钟比对及潮汐引力红移研究。材料描述武汉 Yb 光晶格钟与上海 Sr 光晶格钟经 1,350 km 相位稳定光纤、1550 nm 传递光与光梳相连，通过钟频率比变化研究重力位差。[E02、E08、E27]

项目有两条需保持区分的科学产出：
1. PRL/计量线：重建 Yb/Sr 绝对频率比、系统频移和静态引力红移修正，评估统计及总不确定度。
2. 当前 Nature/月潮线：在太阳日周期干扰存在时，从时间变化的钟比中测量可辨识的月球半日潮势响应；探索固体潮及海洋负荷势模型的适用范围。[E03、E05–E09]

海岸—内陆基线是本项目的几何条件。V14 报告站点直线距离约 692 km，不能与 1,350 km 光纤长度混用。旧文档约 687 km 属历史口径，精确测地定义最终仍需同版确认。[E08、E09、E26]

## 科学问题与假设

| 问题 | 材料中的假设/估计量 | 本次能够确认的边界 |
| --- | --- | --- |
| 钟比能否跟随预测潮汐势变化？ | 分数钟比变化 y 对指定差分潮汐模板 s(t) 的振幅 A；A=1 为单位模型预测 | 是稿件明确目标；模型和误差尚待独立认证 |
| 月潮与太阳日干扰能否区分？ | 联合拟合月潮 M2、N2，并给每次 campaign 自由 24 h/12 h 项 | 当前主估计量；太阳项的具体物理来源 UNKNOWN |
| 是否跨实验期重复？ | 五次 campaign 的条件拟合及删实验敏感性 | 五次 campaign 不是五次独立保守月潮检出 |
| 是否独立测出海洋负荷？ | 完整负荷势纳入预测，另有固体/负荷分量研究 | V14 明确未独立分辨负荷，不可声称已独立检出 |
| 绝对钟比达到怎样的不确定度？ | PRL 16 段主组合与 17 段/leave-one-out 敏感性 | 冻结清单和后续 PDF 数字不完全一致，须先版本对账 |

来源：E08–E09、E11、E14–E16。以上是材料中的研究框架，不构成新的假设检验。

## 实验设计与观测单位

- 物理计量观测，无生物学样本。“生物学/技术重复”不直接适用；需区分 1 s 读数、连续运行、分段、29 个操作组及 5 次 campaign，并处理时间相关，不能把所有点或 54 段当作独立实验。
- V13/V14 报告 2025 年 9–10 月及 2026 年 1、4、5、6–8 月共 5 次 campaign，54 段、546 h，分为前期 38 段/272 h 与夏季 16 段/274 h。[E08、E09]
- 这些时长尚非已核准事实：已有复核记录为 552.132 h，另一个采用不同选样的 V7twin 候选重建记录为 552.356944 h。不得相互替代；详见 RESEARCH_STATUS。[E07、E11、E12]
- 夏季最初 17 段中第 9 段在 PRL 主组合中隔离，冻结清单保留 16 段、986,416 个接受样本。这是清单记载值，本阶段未计数原始数据行。[E14]
- 原始 DOCX 记录了锁定、重启、断纤、断电等事件，分段有运行状态依据；新数据 DOCX 先列 13 个原始组，再列 38 个处理段。V14 的 29 操作组与所有原始行的最终映射仍为 UNKNOWN。[E17、E18、E08]

## 数据来源、变量与指标

| 材料 | 变量/用途 | 注意事项 |
| --- | --- | --- |
| clock/data/环外数据（第八列数据）/ | 25 份夏季拍频 TXT；日期、时间、状态与计数器通道；FXE_B8 为所需拍频通道 | “第八列”是通道名称，不能机械当作完整文本第 8 个字段 |
| newdata/ | 17 份拍频 TXT + 数据分组.docx；2025–2026 前四期 | 2025 最后通道约 66 MHz，为 2 分频；2026 约 33.6 MHz、无分频；分频极性最终证据 UNKNOWN |
| clock/data/光纤环外（第二列数据）/ | 29 份链路环外 TXT | 登记为保留、未接入当前主管线 |
| clock/params.json | 段窗口、排除范围、频率链和系统频移参数 | 冻结输入；比值常数以字符串保精度 |
| results/comp_shanghai-wuhan-beijintime.csv | jd、timestamp_bjt、offset、solid、otl、tide_tot、offset_tot、noise_sim、noise_unknown、signal_sim | 90 s 北京时模型表；含模拟/未知噪声列，不可整体当成实测钟数据 |
| 旧潮汐 Excel/30 s CSV | 历史潮汐输入、单位转换参考 | 已由登记表列为历史，不用于替代当前数字来源 |
| data/fes2022/ | 34 ocean + 34 load + 8 extrapolated 压缩 NetCDF 图集、掩码及手册 | 海潮模型数据，不是光钟观测 |
| 水准测量 DOCX | 约 1113 km 水准路线；报告 ΔW=280.042±0.085 m²/s² | 静态位差来源；永久潮口径仍需核对 |
| V14 methods.tex 的温度说明 | Sr 20 个 PT100、20 s 间隔、2026-06-28 至 07-07、覆盖约 99 h | 本次未定位并认证对应原始 20 通道温度记录；八月及 Yb 温度可用性不足 |

来源：E04、E08、E17–E19、E22；文件数量、CSV 表头来自本次只读元数据检查。更多大小和格式见 PROJECT_MAP。

## 方法体系（按版本，不合并）

**PRL 冻结链**：原始拍频 → 分段/去跳点与样本账本 → 系统频移和重力位修正 → 高精度比值 → WLS/Birge/随机效应/Bayesian 等组合及不确定度预算 → manifest → 论文数字宏。源码 clock/shared.py 使用 80 位 Decimal，直接把约 1.2 的绝对比值转 float64 会破坏 10^-18 差异；分数偏移与绝对比值须分别管理。[E14、E20、E22]

**V13/V14 所述方法**：首时标+样本序号重建时间，段中位数 ±10 Hz 筛选、最长连续运行及端点裁剪；数据与模板同用 1200 s 三角窗、600 s 步长。联合拟合段偏移、潮汐频带及每 campaign 24 h/12 h 正余弦项。主月潮误差取缩放最小二乘与按日删除 jackknife 的较大者；条件估计使用另一套 200 次循环残差校准；300 次注入与 1000 次 bootstrap 是不同检查。[E08]

V14 物理模型描述包括 IERS 固体潮势、位移项，FES2022 潮高与含 (1+k′−h′) 的负荷势卷积、PREM/Han–Wahr Love 数及节点改正。径向位移验证不能自动认证完整势。重叠窗口相关、S2 与 12 h 干扰项不可辨识等限制均须保留。[E08]

**V7/V7twin** 的 10 min 箱联合估计和三表契约属于另一条实现，不得直接冒充 V14 的三角滤波链。[E12、E25]

## UNKNOWN 和范围

最终同版样本/操作组表、作者实际完整模板与拟合脚本、时钟同步精度、实时 BBR 补偿状态、完整温度原始记录、GOT 模型精确版本、最终数据代码许可和投稿状态均未完成确认。作者/单位/贡献声明也未定稿。[E07、E08、E11]

本次不查外部论文优先权或期刊状态，不认证参考文献元数据。项目内文献与稿件中的论断均作为待验证材料，不据文件存在认定已发表。

## 证据索引（全套档案共用）

所有 E 编号均指原项目现存文件；目录和计数另由本次递归元数据盘点取得。文本部分按需阅读；DOCX 为正文有限抽取，PDF 为元数据及选定首页抽取，非全库全文精读或版面审核。

| 编号 | 原始材料 | 用途 |
| --- | --- | --- |
| E01 | [AGENTS.md](/home/room115/gravitation-whsh/AGENTS.md) | 原项目任务路由（部分入口仍为 V7） |
| E02 | [README.md](/home/room115/gravitation-whsh/README.md) | 项目背景与历史口径 |
| E03 | [docs/STRUCTURE.md](/home/room115/gravitation-whsh/docs/STRUCTURE.md) | 三层架构和冻结范围 |
| E04 | [docs/DATA_REGISTRY.md](/home/room115/gravitation-whsh/docs/DATA_REGISTRY.md) | 数据登记（含未同步旧状态） |
| E05 | [paper/nature/README.md](/home/room115/gravitation-whsh/paper/nature/README.md) | 最新 V14 导航及历史版本说明 |
| E06 | [paper/nature/lunar-independent-v14-20261103/README.md](/home/room115/gravitation-whsh/paper/nature/lunar-independent-v14-20261103/README.md) | V14 交付说明 |
| E07 | [paper/nature/lunar-independent-v14-20261103/VALIDATION.md](/home/room115/gravitation-whsh/paper/nature/lunar-independent-v14-20261103/VALIDATION.md) | 数值认证边界与欠项 |
| E08 | [paper/nature/lunar-independent-v14-20261103/methods.tex](/home/room115/gravitation-whsh/paper/nature/lunar-independent-v14-20261103/methods.tex) | 当前作者稿方法（非运行认证） |
| E09 | [paper/nature/lunar-independent-v14-20261103/source-data/model-and-estimates.json](/home/room115/gravitation-whsh/paper/nature/lunar-independent-v14-20261103/source-data/model-and-estimates.json) | V13 来源、主结果、误差定义 |
| E10 | [paper/nature/lunar-independent-v14-20261103/source-data/edition-qc.json](/home/room115/gravitation-whsh/paper/nature/lunar-independent-v14-20261103/source-data/edition-qc.json) | 已有图文构建记录 |
| E11 | [research/v13-review-20261103/REPORT.md](/home/room115/gravitation-whsh/research/v13-review-20261103/REPORT.md) | 内部 V13 评估与时长差异 |
| E12 | [research/V7twin/ASSESSMENT.md](/home/room115/gravitation-whsh/research/V7twin/ASSESSMENT.md) | 候选模型重建及其限制 |
| E13 | [research/V7twin/run-manifest.json](/home/room115/gravitation-whsh/research/V7twin/run-manifest.json) | 该轮 Python/依赖版本记录 |
| E14 | [results/audit-v1/runs/ba3c434326918289/manifest.json](/home/room115/gravitation-whsh/results/audit-v1/runs/ba3c434326918289/manifest.json) | 冻结审计清单 schema 1.2 |
| E15 | [paper/prl/main.pdf](/home/room115/gravitation-whsh/paper/prl/main.pdf) | 现有 PRL PDF（首页文本检查） |
| E16 | [paper/archive/prl-submission-2026-11-02-v2-corrected/CORRECTION_REPORT.md](/home/room115/gravitation-whsh/paper/archive/prl-submission-2026-11-02-v2-corrected/CORRECTION_REPORT.md) | 后续修正说明，不自动等于新审计认证 |
| E17 | [newdata/数据分组.docx](/home/room115/gravitation-whsh/newdata/数据分组.docx) | 实验分组、分频和 MATLAB 记录 |
| E18 | [docs/raw/比对数据汇总Yb.docx](/home/room115/gravitation-whsh/docs/raw/比对数据汇总Yb.docx) | 夏季分段、重锁事件和系统频移 |
| E19 | [paper/武汉-上海水准测量0930R1.docx](/home/room115/gravitation-whsh/paper/武汉-上海水准测量0930R1.docx) | 水准与重力位差来源 |
| E20 | [pyproject.toml](/home/room115/gravitation-whsh/pyproject.toml) | 主环境声明 |
| E21 | [uv.lock](/home/room115/gravitation-whsh/uv.lock) | 锁定依赖 |
| E22 | [clock/shared.py](/home/room115/gravitation-whsh/clock/shared.py) | 路径、精度、常数和旧链入口 |
| E23 | [data/fes2022/MANIFEST.md](/home/room115/gravitation-whsh/data/fes2022/MANIFEST.md) | 海潮图集清单及状态演进 |
| E24 | [research/tidal-spring/data/README.md](/home/room115/gravitation-whsh/research/tidal-spring/data/README.md) | 历史模板分类及再生说明 |
| E25 | [research/tidal-spring/lunar-v7-20261103/README.md](/home/room115/gravitation-whsh/research/tidal-spring/lunar-v7-20261103/README.md) | V7 三表契约和未闭合项 |
| E26 | [research/tidal-kalman/RESULTS.md](/home/room115/gravitation-whsh/research/tidal-kalman/RESULTS.md) | 历史 Kalman 探索记录 |
| E27 | [paper/nature/lunar-independent-v14-20261103/main.pdf](/home/room115/gravitation-whsh/paper/nature/lunar-independent-v14-20261103/main.pdf) | V14 PDF（13 页，首页文本检查） |
| E28 | [research/沪汉潮汐_Nature稿_v13_20261103.pdf](/home/room115/gravitation-whsh/research/沪汉潮汐_Nature稿_v13_20261103.pdf) | V13 上传作者稿（11 页，首页文本检查） |
