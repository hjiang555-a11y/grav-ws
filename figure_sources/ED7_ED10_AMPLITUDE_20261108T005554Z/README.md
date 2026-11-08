# ED7–ED10：振幅谱修正与完整绘图包

本包修正之前遗漏的ED谱图，采用与正文Fig. 3c一致的**等效高程正弦峰值振幅（cm）**。旧包的主图已修改，但ED7、ED8、ED10仍保留旧的“Nominal 600 s LS density”；此前通用源文件包也没有完整提供ED9、ED10的独立绘图入口。本包补齐。

**供外部同事使用：[完整下载包](ED7_ED10_AMPLITUDE_FIGURES_AND_CODE.zip)。**

## 直接找到图和代码

| 图 | 修正后的PDF | 可编辑SVG | 直接绘图脚本 |
|---|---|---|---|
| ED7 | [ED7](figures/ED_Figure_7.pdf) | [SVG](figures/ED_Figure_7.svg) | [plot_ed7.py](scripts/plot_ed7.py) |
| ED8 | [ED8](figures/ED_Figure_8.pdf) | [SVG](figures/ED_Figure_8.svg) | [plot_ed8.py](scripts/plot_ed8.py) |
| ED9 | [ED9](figures/ED_Figure_9.pdf) | [SVG](figures/ED_Figure_9.svg) | [plot_ed9.py](scripts/plot_ed9.py) |
| ED10 | [ED10](figures/ED_Figure_10.pdf) | [SVG](figures/ED_Figure_10.svg) | [plot_ed10.py](scripts/plot_ed10.py) |

**所有共用纵轴标签在 [plot_config.py](scripts/plot_config.py)。** 改文字后运行绘图入口即可，不需要搜索历史大脚本。ED9的纵轴和色标是无量纲相关性，保持其物理含义。

## 运行

解压后，在该目录运行：

```sh
python -m pip install -r requirements.txt
python scripts/run_all.py
```

上面的命令只使用包内已计算的系数与振幅表绘图，生成PDF、PNG和保留文字的SVG。若要从随包的冻结600秒均值和时间戳重新计算扫描系数，再执行：

```sh
python scripts/run_all.py --recompute
```

无需访问原服务器。`INPUT_MANIFEST.json`中的原始绝对路径仅用于来源追溯；运行脚本使用包内相对路径。这里包含的是派生均值及冻结分析结果，不是原始一秒钟观测。

## 修正内容

- ED7：按各面板原来的频率、权重和干扰项设置，提取扫描正余弦系数，并换算为cm。面板a与正文Fig. 3c相同；b–d继续控制N₂/K₂；条件谱另控制竞争主分量。
- ED8：保存的系数换算为cm，保留幅度、相位两排。删除旧密度底排，因此改为2×2面板，图注也同步提供。
- ED9：维持原相关性分析和无量纲量值，提供完整四面板绘图入口与数据。
- ED10：扫描及补偿曲线换算为cm。保留原来从功率诊断选定的候选频率，不重新挑选峰；补偿后的振幅是系数向量的模，不再称为二次功率曲线。

没有对旧密度简单开方或只改轴标签。采用与正文相同的标准重力值9.80665 m/s²和光速299792458 m/s，将相对频率振幅换算为等效高程。

### 已控制频率处的数学可辨识性

扫描频率精确等于已自由控制的N₂或K₂时，目标正余弦列已被干扰项投影消去，不能唯一估计另一个同频振幅。新数组保留这些频率行，并将无唯一解的振幅记为NaN及明确状态；没有删除观测。只看两列之间的条件数不能发现两列同时趋零的问题，因此另检查投影后的列尺度。

接近这些频率但仍可估计的系数全部保留。其大振幅可能来自弱可辨识性和噪声放大，不能直接当作额外物理分量。完整纵轴与明确标注的0–6 cm放大视图一并展示；主半日潮结果与这些同频控制位置分开解释。

## 文稿接入

[REPLACEMENT_TEXT.md](REPLACEMENT_TEXT.md) 提供ED7–ED10图注及Methods替换段落，供正在改稿的同事接入。此次未覆盖主稿。旧图与旧脚本保存在 `originals/`，旧密度数组保存在 `data/frozen_*`，用于核验和追溯；新图在 `figures/`，新振幅数组在 `data/amplitude/`。

旧标签可在 `originals/v86_coupling/finalize_figures.py` 和 `originals/v86_auxiliary/run.py` 搜到。原ED9四面板代码为 `originals/v86_coupling/joint_correlation_figure.py`，原ED10代码在 `originals/v86_coupling/finalize_figures.py` 的第二幅图绘图块。

原99.56%和99.39%是功率下降比例，不能改称振幅下降比例。换用振幅后的显示、极小值和比例均以新计算及其定义为准；相关性、联合系数和原统计误差不因单位换算而改变。
