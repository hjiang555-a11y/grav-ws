# Main（旧Auxiliary）冻结均值：筛选与分箱溯源

2026-11-09。只读manifest、已存证据及源码，计算文件SHA256；未执行原始数据读取/处理、拟合或科学重算。Grok仅作参考，本轮遵循作者指定的单Main处理系列，不在Methods/SI并列重复旧估计值。

**结论：找到与指定 `bins.csv` SHA256 完全相同的生成证据链，足以证明分箱最小支持阈值180、每段600-s墙钟分箱及10-Hz计数跳变筛选。它不是相似long_ratio脚本。实验团队最初为什么选择每段起止窗口，仍不能单靠此源码追溯完全。**

## 1. 相同文件与生成源码的强链

目标SHA256：`860b442aad8b1c39ad750aa27af0d8766cf210ae9b013006169d77fdb9e93d8d`。

1. `/data/AI_Research/projects/grav-ws/manuscript_48h/audit_v3_17_noAC_20261108T084244Z/replay/data_code/results_library/inputs/MANIFEST.json` 指向 `nature_methods_closure_20261107T1343Z/data/amplitude_spectrum/inputs/bins.csv`，记录目标SHA。
2. 同amplitude_spectrum目录 `RESULTS.json` 的input_manifest进一步指向 `/home/room115/gravitation-whsh/final_candidates/A_v81_integration/sources/frozen_v72/bins.csv`，仍是相同SHA；同时记录n_rows=3299、n_segments=54、member_hours=545.9241666666667。
3. 本次对上述frozen_v72/bins.csv实际执行sha256sum，结果与目标完全一致。
4. **同一frozen_v72的 `evidence.json`**：dataset_kind为measured，`table_sha256['bins.csv']`正是目标SHA；`input_sha256`逐项记录生成时 `research/opencode-period-offset-20261105/pipeline/` 的源码哈希。因此链路不是仅靠目录名称或3299/54推断。
5. 本次实际读取并hash的源码与evidence逐项一致：

| 文件（共同前缀 `/home/room115/gravitation-whsh/research/opencode-period-offset-20261105/pipeline/`） | SHA256 |
|---|---|
| bins.py | `bcfbc5c14703b5b8a8666a196d5f9ab1df07f185962caec6affc3d2a4f972eb9` |
| raw.py | `a4714492e6f6a14da7a63765086781d52f33b686d4c49b7ba6683afdc3e3c720` |
| run.py | `c96c640b81599d5dc0bce020164cf69f6708f1e2d6bdb2df0db4870228d8c5d3` |
| rules.py | `61bf355950faf7e19ddde8033e0e6798a468dffb7693d2a778702c50c939cb23` |

frozen_v72 `raw_archive_manifest.json` 再次记录原始执行源码哈希与冻结R7源码匹配、bins目标SHA，以及R7 raw-support audit脚本来源。历史template.py存在已记录的文档哈希变化；本次检查的raw/bins/run均不涉及该差异。

## 2. 可直接进入Methods的事实与源码位置

共同源码前缀同上。

- **预定义分段窗口**：raw.py说明使用sample/segments_54.csv；按窗口含端点切片。raw.py:219为 `inside = (t >= start_s) & (t <= end_s)`。相邻段共享边界秒时归较早段，较后段从start+1s开始（raw.py:228–239）。这并不证明窗口选择本身随机或与结果无关。
- **跳变门限**：raw.py:73设 `JUMP_HZ = 10.0`；raw.py:223–225为 `med = np.nanmedian(bw)`、`keep = np.abs(bw - med) <= jump_hz`。因此在每个分段窗口内，偏离该窗口beat中位数**超过10 Hz**的行剔除；NaN也不通过。不能把此说成完全没有任何筛选，也不能等同旧Primary的transient-screening规则。
- **分箱网格**：bins.py:58–60定义 `BIN_SECONDS = 600`、`MIN_SAMPLES = 180`。bins.py:108 `keys = (secs // BIN_SECONDS) * BIN_SECONDS`：BJT墙钟600-s不重叠网格，左闭右开。
- **最小支持**：bins.py:109–112对网格计数，`keep = counts >= min_n`，均值为 `sums[keep] / counts[keep]`。make_bins逐segment处理，使用上述MIN_SAMPLES。因此是**每箱至少180个保留的名义一秒成员**，不是必须600点满箱，也不是插值补齐。
- **不同段不合并**：bins.py:23–31及make_bins定义：每segment独立分箱，唯一键为(t_utc,seg)；两个段落在同一墙钟箱可分别保留部分均值，成员互不重复。因此“3299个不重叠600-s均值”应解释为成员不重用，不能误称3299个不同中心时刻或3299个完整600秒暴露。
- **时间戳**：bins.py:115–127为网格起点+300s，BJT减8h转UTC；是名义箱中心，不是每箱实际成员时刻平均。
- **调用链**：run.py:194先raw.load_all_segments，:207调用prepare_observed_bins，:209赋sigma，随后写bins.csv并记录table_sha256（:230）。这将raw筛选、bins函数与目标输出接起来。

可用的简明英文表述（整合者按单Main命名调整）：

> Within each predefined observing segment, beat-frequency records differing by more than 10 Hz from the segment median were excluded. Retained records were averaged separately within each segment on a 600-s wall-clock grid, retaining bins with at least 180 nominal one-second members. Bin timestamps denote the grid centres; no missing samples were imputed.

最后一句由分箱实现直接支持，不表示全部原始仪器数据均已核验。若正文声称“without transient screening”，应明确其特指未采用旧Primary的瞬态筛选，而不是隐去本链的10-Hz counter-jump gate。

## 3. 现存审计的交叉支持（本次未重跑）

frozen_v72 `raw_support_summary.json` 已记录：saved_bins3299、segments54、accepted_rows1965327、accepted_hours545.9241666666667、underfilled_bins29、underfilled_rows1581、jump_rejected_rows4；saved_bin_membership_counts_match=true，bin_max_abs_diffs各项0。另有3291个唯一中心、8个额外同中心均值；accepted_bin_n_min181、max602，55箱超过600成员，原因与名义秒标签抖动重复有关（raw.py说明每行是一个名义一秒样本，标签可重复，均保留）。这些数值仅引用既有审计，不是本次计算所得；Methods不必堆入全部审计计数。

## 4. 尚未闭合的边界

- 可以补写确切180-member阈值、600-s网格、均值、边界归属、10-Hz门限，证据链已足够强。
- 不能因此补造最初valid-window选择的实验标准、掉锁/人工剔除原因或完全无选择偏倚。窗口清单与原始成员受控档案可追踪，不等于所有实验筛选理由已完整书面化。
- 不把旧Primary的1200-s三角滤波、transient条件或long_ratio实现迁入Main。不给出新的保留率、拟合结果或合并估计值。
- 本次没有复跑raw_support审计；只核实目标文件身份、历史执行证据与相同哈希源码。所有旧文件保持只读，未改论文。
