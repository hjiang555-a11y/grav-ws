# ED7、ED8 只读视觉检查

结论：通过。对 `reproduced/ED_Figure_7.pdf` 与 `reproduced/ED_Figure_8.pdf` 以 130 dpi 实际渲染并逐图查看，未发现页面边界裁切、坐标轴标题截断、面板字母遗漏或新增文字遮挡。未重新拟合或更改任何数据、图件与代码。

| 图 | PDF | SVG text 节点 | PDF SHA-256 |
|---|---|---:|---|
| ED7 | 1 页 | 54 | `9f4a8aaa7338b5c1ed49f214296110d4fd05cc545986f25cc03494d953d401b3` |
| ED8 | 1 页 | 75 | `56fcaca9b4b9803c8313c9381511aded93472fad8ae1dac48298bcbe6731fd22` |

- ED7 的 a–d 四个面板、总标题、左右图例、频率坐标与两处纵轴单位均完整；保留了现有 “Existing spectral route, reproduced” 标题，本次只检查重生成排版，不擅自编辑原措辞。
- ED8 的 a–f 六个面板、两列扣除方向、幅度/相位/谱密度单位、底部补偿系数坐标及图例均完整。b 面板曲线靠近上边界，但未见页面裁掉线条或文字的新问题。
- 两份 SVG 均包含真实 `<text>` 节点，可编辑文字；不是把整图栅格图片包入 SVG。这里确认 SVG 结构，不将其表述为重新验证科学计算。
- 视觉证据位于 `review_render/ED_Figure_7.png`、`review_render/ED_Figure_8.png`。像素一致性由既有 `reproduced/PIXEL_COMPARISON.json` 另行记录；本报告不将该比较冒充重新拟合验证。
