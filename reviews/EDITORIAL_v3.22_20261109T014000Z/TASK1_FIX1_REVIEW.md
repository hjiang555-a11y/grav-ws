# Task 1 修复轮1独立复核

范围：`d0abd39..f6c6b7c` 实际改动及 fix1 package；读取新增筛选溯源报告、CHANGE_MAP 和任务报告，并只读核对所引用 `independent_checks.py`、`raw.py`、`bins.py` 的相关实现。没有执行科学计算，也未重复跑完整不变项检查。

**Spec verdict: PASS。Scholarly/editorial quality verdict: PASS FOR THIS FIX ROUND，保留既有作者事项。** 未发现本轮新增 Critical、Important 或 Minor 问题；可以进入下一任务。

| 项目 | 复核结论 | 证据及边界 |
|:--|:--|:--|
| R1：日周期上界的 H 对应 | **关闭** | `sections/auxiliary_methods.md:43` 明确正文主上界采用主采样、三组模板、segment offsets 和 period-noise weights；Fig. 4 对应等权滤波算子。随后检查的滤波来源也明确。已读独立检查原码，其 X、sigma 权重及 campaign 范数相加与新增表述一致，没有恢复另一套正文上界。 |
| R2：八分量前向定义 | **关闭** | `sections/methods.md:23` 就地列出 lunar、near-12-h、diurnal 各成员，解决先前未定义的 “eight named constituents”；未改组模型或公式。 |
| R3：筛选/分箱规则 | **可证明部分关闭；窗口选择理由保留** | `sections/methods.md:17` 和 `sections/supplementary_methods.md:112` 与同一冻结 bins 的来源报告和所引原码相符：分段中位数 10-Hz gate、每段独立 BJT 600-s 网格、至少 180 名义一秒成员、名义箱中心。正文准确区分未采用额外 running-median screening 与没有任何筛选，没有宣称最初分段窗口选择标准已查清。 |

新出现的 180 等数字是既有生成规则的首次书面披露，有明确来源；不是新观测值、拟合结果或事后改动阈值。本次实际 diff 仅更改三个方法源文件及两份审计说明，Results/Discussion、opening、图件和 caption 均未修改，未改变单主数值系列、公式、检出措辞或主要主张。

R3 剩余的窗口选择理由，以及前次 R4 的 S₂ 检出证据/归因边界、R5 的 Fig. 1 小时数口径仍应随作者交接保留。本结论不将这些事项视为科学上已关闭，不要求静默改动冻结摘要或既定主张，也不代表完整原始数据复现与投稿批准。
