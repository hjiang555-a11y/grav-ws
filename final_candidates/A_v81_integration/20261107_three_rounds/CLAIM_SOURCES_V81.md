# v81关键结果与来源

冻结主底稿：A_v80_periods。整合版PDF固定在Git提交df4211fe619f8d611dc8b9c8a5fc86aa50f9e15e；完整哈希见 INTEGRATION_PROVENANCE.json。

| 论文量 | 数值 | 源文件/估计器 | 本轮核验范围 |
|---|---:|---|---|
| 全潮波形 | 0.9551118452 ± 0.1081821399 | segment_reduction/FULL_TIDE.json；整个模板含余项一同缩放 | 独立重算全样本及43次删日，并用显式QR核对 |
| 月球组 | 1.0004025677 ± 0.1319555554 | data/RESULTS.json / segment_reduction/RESULTS.json；固定余项后三组联合 | 冻结v80结果和图件；源代码及派生输入保留 |
| 邻近组 | 0.9251204377 ± 0.3649291060 | 同上，S₂+K₂，非纯太阳组 | 同上 |
| 月潮相位 | 同相1.00±0.13，正交−0.10±0.20 | data/RESULTS.json，phase fit；图3b | 冻结结果核对，不是两组幅度椭圆 |
| 共有24h，全模板 | 1.0316131352 ± 0.1027549212 | full_sensitivity/table.csv第2行；新EDT5 | 整合版EDT4第2行，独立重算 |
| 逐期12h，全模板 | 0.7221949515 ± 0.2212229754 | full_sensitivity/table.csv第3行；新EDT5 | 整合版EDT4第3行，独立重算 |
| 逐期12h，分组 | 0.75±0.24；−5.10±15.01 | review_diagnostics/twelve_hour_sensitivity.csv；原EDT4 | 冻结结果核对，与全模板是不同拟合 |
| 期级符号翻转 | 全模板2/256；新增邻近组16/256 | FULL_TIDE.json；review_diagnostics/REVIEW_RESULTS.json | 历史计算结果核对；不转高斯σ |
| 光纤配对 | 246.634 h；ΔL=0.0061±0.0063；ΔS=0.00594±0.01453 | data/RESULTS.json；EDFig3来源表 | 仅夏季重叠被监测路径，不外推全年 |
| 全样本 | 3299均值、54段、8期、43 UTC日、545.924成员小时 | data/primary_rows.csv、period_ledger.csv | 哈希锁定；没有新增筛选、插值或改原始计数 |

统计误差沿用max(缩放LS, UTC删日jackknife)；真实噪声普适校准、原始计数器逐条重建不在本轮完成范围。新加入的敏感性表明确标为派生数据独立复算，而非原始实验重做。两份稿件同源，不能平均或合并显著性。
