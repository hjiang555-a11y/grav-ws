# v3.22 整稿终审

审阅基线 `43f9bf3`，完成稿 `e272360`。本报告依据整分支 review package、实际源文/差异、最新作者裁定、计划 Global Constraints、progress ledger、Task 1/修复轮1及 Task 2 独立审阅，审查全文、Methods、ED/SI、投稿信、暂定元数据和构建交付的一致性。已读工作站规则及 shared 中本轮研究方案；后出的 AUTHOR_STEERING 覆盖初始方案的双处理并列展示要求。

本次没有修改论文源文、重建稿件、重新筛选/分箱/拟合、运行原始科学分析或另行外部文献检索。数值为实际成稿及既有验证记录中的数值，不是本审阅重新计算的结果。未将已有检查再次执行一遍，也不将其伪称为本次独立复现。

## 分项结论

- **Spec verdict：PASS。** 正文采用作者指定的既有 0.96 ± 0.11 / 1.00 ± 0.13 主响应系列；移除另一处理的重复估计而非新搬入 Methods/SI。精确标题、批准摘要及结尾、四主图资产/布局、Table 1、展示公式、35 来源及 develop 模型定位保持。原图和原 ED 验证材料保留其真实处理身份，符合图件冻结及来源披露要求。
- **Scholarly/editorial verdict：PASS FOR AUTHOR REVIEW；重要科学作者事项未关闭。** 未发现本轮必须修改正文的新 Critical、Important 或 Minor 问题。方法前置后，结果—估计器—误差—图件对应清楚；投稿信与最终科学文字相符。此结论认证本轮编辑质量，不能解释为已确认 S₂ 检出强度/天文来源、原始窗口选择依据或全部科学结果。
- **Integration verdict：稿件及现有 PDF/Word 构建证据 PASS；交付准备有一项 Minor 收尾。** F1 只涉及源包所含检查程序与报告承诺，须在打包前处理。源包独立重建、最终清单和私有上传字节核对尚未完成，属于既定后续任务，本终审不提前认证。

## 新增可执行项

### F1 — Minor — 检查程序的源包范围与报告承诺不完全一致

位置：`reports/FORMAT_CHECK_ZH.md:13`；`scripts/prepare_delivery.py:57`。

格式报告写“详细程序与JSON记录随源包保留”，但当前打包清单只纳入 `build_formal.py`、`export_editable.py` 和 `export_letter.py`，没有纳入产生所述检查证据的 `validate_editorial.py`、`inspect_pdf.py`、`check_word.py`。因此接收者可重建排版，却不能从包内检查程序追溯全部 JSON 的检查逻辑。

处理：打包前加入这些检查脚本，并将最终使用的 `check_source_rebuild.py` 一并归档；README 明确哪些检查依赖工作站冻结基线/LibreOffice 预览，不能宣称所有审计在便携源包内独立可运行。也可收窄报告承诺，但保留实际使用程序更符合本项目追溯要求。本项不涉及科学数据、公式或论文排版，修复无需重新编译科学稿件。

## 全文与方法一致性

| 核对项 | 结论及定位 |
|:--|:--|
| 唯一主响应系列 | `sections/results_discussion.md:13` 对应 Fig. 3 和 `sections/methods.md:15` 的 main/auxiliary；没有将旧 primary 值换标签为主值。`agents/task1/CHANGE_MAP.md` 逐项解释删除/移动，最终验证明确 numeric multiset 已改变，未作虚假守恒声明。 |
| 两种处理的身份 | `sections/results_discussion.md:9`、`:15`、`:27` 与 `sections/figures_tables.md:5`、`:9`、`:13`、`:17` 及 Supplementary Table 4 相符。545.9 h 属主分析，544 h 属滤波记录；图2/4是共享观测的滤波验证，未被称为独立测量。Fig. 4 图内旧标签保持，但同页图注已明示其滤波身份。 |
| 主选择/分箱溯源 | `sections/methods.md:17` 所披露 10-Hz gate、每段独立当地600-s网格、至少180名义一秒成员、名义箱中心，对应同一冻结输入及源码哈希的溯源报告。没有把这些解释冒充本轮新处理，也没有宣称原窗口选择理由已知。 |
| R1/R2 修复整合 | `sections/methods.md:23` 已就地列全三组八分量；`sections/auxiliary_methods.md:43` 明确正文日周期界限的主三组设计/权重与 Fig. 4 的滤波等权算子，后续注入/环境/预测检查也标清为滤波。未见回归。 |
| 相位和谱估计对象 | `sections/results_discussion.md:21` 区分自由相位条件谱、联合拟合幅度和固定组内相位的组响应；`sections/methods.md:25`、`:37` 及 Fig. 3 图注保留 covariance contour 与较大 marginal error 的区别；旧 bootstrap 相位仍明确在滤波 SM3。未以扫描幅度替代测量精度。 |
| 模型与外推 | `sections/results_discussion.md:35`、`:43`、`:56` 保留 We develop、实测幅度、同估计器精度比较和未来噪声/采样效率条件；`sections/methods.md:41`、`:56` 定义 H、噪声传播及各列估计器。没有把未来曝光标度说成已由新的观测验证。 |
| 不确定性和弱分量 | 主响应使用较大的 scaled least-squares / UTC-day jackknife error；滤波 resampling、group/segment bootstrap 另有定义。Table 1 保留 measured-amplitude S/R，未将其当作校准检出概率。日周期和加载弱约束仍与近unity S/R相符。 |
| 投稿信与作者事实 | `submission/COVER_LETTER_v3.22.md:9`、`:11` 对应主系列、谱峰幅度、模型及条件性外推；`:15` 披露共享274 h及相关工作。`:17`、`:23` 与 `sections/author_block.md:15`、`sections/author_contributions.md:3` 明示待确认，没有把编辑授权替代作者同意或独占声明。 |

Introduction 三段、Results 五节以及 Discussion 的组织保持。正文从观测/分离过渡到分量精度和未来观测建议，处理细节集中到方法，减少了同一结果的重复。既有 SI 的独有校准、替代处理和敏感性结果可继续承担复核作用；它们不是本轮把被删除的 headline 数字换位置隐藏起来。

## 引用、排版及交付证据

`formal_build_01/CITATION_ORDER.json` 给出29篇正文来源、6篇后续方法来源和完整35来源映射；Gozzard 对应 source 65 / compiled 14。构建脚本排除作者机构上标后按首次引用编号，且迁入 auxiliary_methods 的方括号引用已转为同ID caret 标记。已读编译文本与验证结果，没有发现新漏引、悬空引用或由重排引入的错误身份。外部来源是否最新/是否逐条支持所有旧句子，不属于此次重新认证范围。

采用已有 `FINAL_VALIDATION.json`、`PDF_CHECKS.json`、`WORD_CHECKS_FINAL.json` 及 `FORMAT_CHECK_ZH.md` 的实际检查证据：112个旧版冻结文件、66个图目录文件保持；合并稿47页、文字稿24页、SI14页、信1页；无记录中的严重编译警告和越页文字；Word伴随稿149个数学对象及一个可编辑表格，实际预览28页，信预览1页。没有把Word与PDF分页相同作为通过条件。

整合者已查看所有联系表及第一页、四主图、表格、贡献段清晰页。本终审另直接查看 `visual_check_01/contact_01.jpg`、`detail_06.png`、`detail_13.png`，核对摘要所在首页、Table 1/条件性解释及 Fig. 4 来源图注；所查页面没有发现文字截断或图注分离。完整版面通过依据是整合者全稿目视检查与机器证据，本次抽查不冒称独立看完47页高清图。

源包重建和私有交付应继续按既定计划完成，保留实际重建结果及最终文件哈希；成功重建只能说明排版可重复，不能说明原始科研流程已复现。最终报告必须以实际结果更新，不能把预期执行写成已完成。

## 作者控制的未关闭事项

| 等级/来源 | 位置 | 作者行动及结论边界 |
|:--|:--|:--|
| **Important，R3剩余** | `sections/methods.md:11`、`:17`；`agents/policy/MAIN_SELECTION_PROVENANCE.md` | 补齐54段最初起止窗口选择的已有实验依据。已查清窗口后的筛选/分箱，不等于窗口选择依据与选择偏倚已经闭合。不得临时编造无关结果的选择标准。 |
| **Important，R4** | `sections/opening.md:11`；`sections/results_discussion.md:19`、`:21`、`:25`、`:51`；`sections/supplementary_methods.md:90` | 由作者评估原有 separately detect / detections 对 S₂ 的证据强度及天文来源边界。自由相位条件峰、固定组内相位响应和Table 1幅度S/R是不同证据，峰仍可识别本身不等于校准的独立检出显著性；月潮抗日周期扰动不排除S₂自身同频实验室成分。当前稿保留作者既定主张，这一问题尚未解决。若调整，应由作者决定是否强调频率成分分离/估计，不能在本轮静默更改冻结摘要或主要主张。 |
| **Minor，R5** | `sections/figures_tables.md:5`；`sections/methods.md:11`；`figures/figure1_v319.pdf` | 核对图中60、68、73、70、274 h与滤波总544 h的汇总口径。不得将未经查证的逐项取整解释当作事实，也不应自行改冻结图。 |
| **Important，正式提交事实** | `submission/AUTHOR_CONFIRMATIONS_ZH.md:7`；`submission/COVER_LETTER_v3.22.md:17`、`:23`；`sections/author_contributions.md:3` | 作者确认通讯身份/邮箱、逐人贡献、最终版本同意、出版/独占状态、相关稿件及编辑沟通，再据真实信息替换占位。旧作者责任/利益声明也仍是作者声明，编辑验证不能替作者证明。 |
| **Important，数据/代码访问落实** | `sections/declarations_pre.md:3`、`:7` | 将实际可提供的数据、代码和访问条件落实。沿用 upon reasonable request 不等于已完成全部数据代码政策或原始科研复现。 |

上述事项已在 `reports/REVISION_REPORT_ZH.md` 与 controller 决策中披露。不得因本轮编辑/排版通过而从交付说明删去，也不要求为了关闭它们擅自重算、重画或改写科学结论。本终审允许继续完成 F1、源包重建和已授权的私有审阅交付；不构成投稿、预印本或公开发布授权。
