# C01–C05实施：独立验收

**源稿验收：PASS。** 当前源稿与执行前备份相比，精确落实五个获准候选；除允许的行尾纯空格修剪，没有附带修改。

基线：`archive/before_condensation_20261109T084928Z/sections/`及本任务`BEFORE_MANIFEST.json`。批准文本：本目录`APPROVED_CANDIDATES.json`。

| 核查项 | 结果 |
|---|---|
| C01、C02 | 备份中的原句均唯一匹配；现稿准确采用批准文本，原句不再出现。 |
| C03 | 准确缩短两路线导航，main/auxiliary与filtered/primary的分工、共享观测和非独立测量限定保留。 |
| C04 | 仅删除批准的一句轮廓复述；Fig.3图注仍明确scaled least-squares covariance和radii one and two。Methods中原误差选择、全系数重拟合说明不动。 |
| C05 | 准确使用“are averaged in 30° M₂-phase bins on identical sampling”，保留数据减偏置/非月潮项、M₂+N₂模型、相同采样与平均定义；day-by-day jackknife仍固定非月潮拟合，3-h显示和6-h间隙门槛保留。 |
| 指定保留句 | 从“This difference may reflect the greater relative impact…”到SM4指引的完整句逐字保留，没有再润色或删限定。 |
| 其他源稿 | 13个章节中仅results_discussion、methods、auxiliary_methods按批准规则改变，其余10个章节字节不变。 |
| 摘要、数学、引用 | opening整文件不变；三个变动文件的数学表达及文献上标序列与备份相同；references、作者信息、声明及图注不变。 |
| 图件 | 与执行前清单核对，119个图件均保持SHA256，无附带改图。 |

独立在内存中从备份应用全部五项替换，并逐行比较当前源文；两者相同，仅允许行尾空格修剪。`APPROVED_CANDIDATES.json`保留原计划快照中的`executed:false`，不据这一历史字段误判执行状态；本报告基于实际源文差异确认五项已执行。

本次仅写入此报告，未改源稿。此阶段结论为源稿验收；正在进行的PDF/Word重建可随后依据最终产物另补验证，不冒充已完成。
