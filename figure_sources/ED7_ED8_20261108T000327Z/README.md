# Extended Data Fig. 7 和 Fig. 8：图件与绘图源文件

**给同事转发：[下载 ED7_ED8_FIGURES_AND_CODE.zip](ED7_ED8_FIGURES_AND_CODE.zip)。**

这两张图都有真实绘图代码。包中提供当前论文的单独图件、绘图脚本、已经算好的曲线数据，以及可编辑SVG。解压即可使用，不需要访问原服务器的 `/data/AI_Research/...` 路径。

| 图 | 当前稿原图 | 直接绘图脚本 | 可编辑重绘图 |
|---|---|---|---|
| Extended Data Fig. 7 | [PDF](figures/ED_Figure_7.pdf) · [PNG](figures/ED_Figure_7.png) | [plot_ed7.py](scripts/plot_ed7.py) | [SVG](reproduced/ED_Figure_7.svg) |
| Extended Data Fig. 8 | [PDF](figures/ED_Figure_8.pdf) · [PNG](figures/ED_Figure_8.png) | [plot_ed8.py](scripts/plot_ed8.py) | [SVG](reproduced/ED_Figure_8.svg) |

## 运行

在解压后的目录中，安装依赖并运行：

```sh
python -m pip install -r requirements.txt
python scripts/plot_ed7.py
python scripts/plot_ed8.py
```

输出位于 `reproduced/`，提供PDF、PNG、SVG。运行入口从 `data/` 读取保存的曲线、条件扫描和补偿系数扫描结果，不重新拟合钟观测、不重新计算检出结论。可在脚本中调整文字、字体、颜色和面板布局。

## 文件来源

`figures/` 中的两张图与当前论文采用的文件逐字节一致，图注另存为Markdown。`reproduced/` 是同一保存数据通过独立绘图入口生成的版本；图内原有标题和坐标定义保留，SVG将文字保留为可编辑文本。本次交付没有替换论文中的图。

`original_scripts/` 保留原始完整程序的原字节副本，供追溯绘图块来源。它们原本位于更大的分析目录中，完整程序会调用上游计算；本包的直接使用入口是上面的两个 `plot_ed*.py`，而不是这些溯源副本。

`data/` 包含实际绘图所需的已计算CSV/JSON，不是原始一秒钟观测数据。来源清单中的绝对路径仅记录文件从哪里取得，实际输入已包含在包内。数字验证、软件版本和文件哈希随包提供；不需要同事另找服务器上的输入文件。
