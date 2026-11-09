# 正式PDF嵌入图表与图注独立复核

结论：通过。核查文件为 `/data/AI_Research/projects/grav-ws/manuscript_48h/editorial_v322_20261109T014000Z/formal_build_01/NATURE_ARTICLE_v3.22.pdf`（40页），SHA256为 `1fc472e2321a5c64f327b730f056cbe6b6da6e83e9b5417eecd5efd9a95b7bd9`。本轮仅阅读正式PDF，未修改稿件。

共逐页目视14个显示项：主图4张、Extended Data图8张、Extended Data表2张。所有图表及其完整图注均在同一页，未出现跨页截断；图与图注的分图字母、颜色/线型指代和内容对应一致，未发现本轮组合造成的新重叠、缺字或比例异常。

| 显示项 | PDF页 | 结果 |
|---|---:|---|
| Fig. 1 | 10 | 图表及图注完整同页 |
| Fig. 2 | 11 | 图表及图注完整同页 |
| Fig. 3 | 12 | 图表及图注完整同页 |
| Fig. 4 | 13 | 图表及图注完整同页 |
| Extended Data Fig. 1 | 24 | 图表及图注完整同页 |
| Extended Data Fig. 2 | 25 | 图表及图注完整同页 |
| Extended Data Fig. 3 | 26 | 图表及图注完整同页 |
| Extended Data Fig. 4 | 27 | 图表及图注完整同页 |
| Extended Data Fig. 5 | 28 | 图表及图注完整同页 |
| Extended Data Fig. 6 | 29 | 图表及图注完整同页 |
| Extended Data Fig. 7 | 30 | 图表及图注完整同页 |
| Extended Data Fig. 8 | 31 | 图表及图注完整同页 |
| Extended Data Table 1 | 32 | 图表及图注完整同页 |
| Extended Data Table 2 | 33 | 图表及图注完整同页 |

重点核对新ED1（a–d）、ED2（a–c）、ED7（a–f）及两张合并表：源面板完整，字母顺序与图注相符；坐标、图例、上/下标、表头和行列未被裁切。ED Table1的a–c与ED Table2的a–d及各段表注均完整。图1插图的1、2等值线标签另做放大检查，确实存在。

图件按稿件页宽等比例嵌入；嵌入后的可见图内字号范围逐项记录于JSON，最小值约5.07 pt，保持可读。独立投稿图件的原生尺寸与字号由图件审查记录负责；此处不把缩放后分图字母虚称为8 pt。

预览位于 `embedded_review_pages/page_10.png` 等文件。复核引擎PyMuPDF，120 dpi全页；图1插图另以4倍矢量渲染检查。主代理负责整本文档Poppler渲染、编译日志和Word检查。未对科学估计作重新验证，也没有产生新的统计结果。
