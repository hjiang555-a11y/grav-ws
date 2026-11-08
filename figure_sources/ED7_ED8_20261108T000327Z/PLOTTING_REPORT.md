# ED7 / ED8 绘图入口与实际核验

两份脚本只读取已计算的冻结曲线，未重新拟合、扫频、生成观测或改变统计结果。绘图块取自真实原脚本；内部标题、曲线、标签、单位、范围、配色、尺寸及 PNG DPI 保留。新增 SVG 输出使用 `svg.fonttype='none'`，文字可在矢量编辑软件中编辑。

在包内或任意目录执行：

```sh
python /path/to/package/scripts/plot_ed7.py
python /path/to/package/scripts/plot_ed8.py
```

所有读取/输出路径相对于脚本位置解析，不依赖原科研服务器目录；`data/INPUT_MANIFEST.json` 和 `SOURCE_PROVENANCE.json` 中绝对路径仅为来源记录。安装依赖见 `requirements.txt`。运行会更新 `reproduced/` 内相应派生图和核验记录，不修改 `data/`。

| 核验 | ED7 | ED8 |
|---|---:|---:|
| 冻结输入行数 | 1,286 个谱频点；237 个条件点（M₂ 118、S₂ 119） | 488 行；每种组合 61 个 λ |
| 与源数组严格相等的绘制数据曲线 | 13 | 18 |
| PNG 尺寸 | 1710 × 1292 | 2000 × 1800 |
| 与 reference PNG 最大像素差 | 0 | 0 |
| PNG 是否逐字节 SHA256 相同 | 是 | 是 |
| SVG `<text>` 节点数 | 54 | 75 |

生成文件为 `reproduced/ED_Figure_7.{pdf,png,svg}` 和 `ED_Figure_8.{pdf,png,svg}`。每张图的 `_VALIDATION.json` 保留输入哈希、行数、逐条曲线核对、轴范围/标签、软件版本、脚本哈希及输出哈希；`_plotted_arrays.npz` 保存实际送到绘图对象的数组，包括参考竖线。`PIXEL_COMPARISON.json` 记录与原图的像素及哈希核验。

ED8 沿用原图的相位 unwrap，仅用于显示既有相位数组，不重新估计模型。两张图的密度保持原 nominal 600 s LS density 定义与线性纵轴；没有转换成新统计量。

实际执行环境：Python 3.12.3，NumPy 2.5.4，pandas 3.1.0，matplotlib 3.11.2。绘图无随机过程；无需随机种子。PDF 的生成时间等元数据可能改变文件哈希，因此除原 PNG 精确一致性外，也保留全部绘制数组核对；未要求 PDF 二进制相同。
