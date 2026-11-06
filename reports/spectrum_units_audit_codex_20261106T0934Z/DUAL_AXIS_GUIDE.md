# 双纵轴展示

最终推荐图：`figures/spectrum_dual_axes_per_microhertz.pdf`（另有SVG和PNG）。按作者要求，横轴为µHz，两个纵轴均用“/µHz”，不再用µHz⁻¹。

- 左轴：Nominal potential PSD，单位 `(m²/s²)²/µHz`。
- 右轴：Fractional-frequency PSD，单位 `10⁻³⁵/µHz`。相对频率y本身无量纲，其谱密度仍带倒频率单位。
- 对应关系：`S_W = c⁴ S_y`。右侧刻度1表示 `S_y=10⁻³⁵/µHz`，严格对应左侧 `0.08077608713 (m²/s²)²/µHz`。
- M₂附近峰：左侧0.19044115，右侧2.35764271；S₂附近峰：左侧0.06802246，右侧0.84211134。右侧两数的尺度均为10⁻³⁵/µHz。
- 两侧共用同一组曲线，右轴是固定物理换算，不是独立缩放。蓝线观测、橙线固定理论扣除后的残差，数据、峰位、残差和归一化均未改变。

代码：`scripts/draw_dual_axes.py`；双单位CSV：`data/dual_axis_spectra.csv`；验收：`verification/FINAL_CHECK.json`。完整换算解释与21频点、3序列的独立验算见 `UNITS_AUDIT_REPORT.md`。

保留间断数据的标称600秒LS归一化说明；该图不是对连续全年噪声底的重新标定。
