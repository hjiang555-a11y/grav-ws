# 项目结构、材料与环境地图

原项目：`/home/room115/gravitation-whsh`。检查方式：递归元数据枚举和选定材料只读抽查；无原脚本执行、无实际数据分析。统计排除符号链接的目标，大小为逻辑字节数之和。完整索引与检查时间在本文附录。

## 主要目录及用途

| 目录 | 用途与证据 | 内容检查深度 |
| --- | --- | --- |
| clock/ | 冻结PRL基础：数据加载、参数、溯源、分段；data/含两类拍频和MATLAB；segment_analysis/为分析代码 | shared.py等源码静态阅读；原数据只读头部 |
| clock_ratio/ | 比值、系统与统计不确定度、潮汐修正、manifest、报告和测试 | 静态代码/路径/导入检查 |
| data/fes2022/ | 海潮模型图集；load_tide、ocean_tide、ocean_tide_extrapolated、mask、doc、scripts、logs、derived | 文件数/大小、少量签名及清单；不读取下载凭证或日志内容、不解压格网 |
| newdata/ | 2025-09/10与2026-01/04/05新拍频、分组DOCX | DOCX有限正文与TXT格式头部 |
| research/prl-2026/ | 冻结PRL分支说明 | 与结构文档交叉定位 |
| research/tidal-kalman/ | 夏季Kalman、LS、周期图、零模板与敏感性探索 | 结果文档及代码/产物位置 |
| research/tidal-spring/ | 跨季节数据、固体/海洋负荷模型、联合拟合；data/按solid/otl/total/archive分层 | 文档、部分源码、模板表头/存在性 |
| research/tidal-spring/lunar-v7-20261103/ | V7联合估计、三表与数值门禁、诊断记录 | README及报告；不运行门禁 |
| research/V7twin/ | 后续独立选样及候选模型诊断 | ASSESSMENT、VALIDATION、run-manifest；不读大缓存 |
| research/v10-review-20261103/、v13-review-20261103/ | 内部审阅报告及local材料 | V13报告重点阅读；不把内部评估视为编辑决定 |
| paper/nature/lunar-independent-v14-20261103/ | 最新导航所指V14作者审阅版，TeX、PDF、图、source-data、tools | README/验证/Methods/数值JSON、PDF元数据与首页面 |
| paper/nature/其他子目录 | V7写稿、图文预览、旧54段稿、评估和修改方案 | 关键入口；其余元数据索引 |
| paper/prl/、paper/overleaf-prl/ | PRL正文、补充材料及提交包 | PDF元数据/首页面、修正材料 |
| paper/rev2/、paper/overleaf*/、paper/archive/ | 历史稿、数字生成和快照 | 入口与相关修正报告；冻结只读 |
| paper/ref/ | 本地参考材料，45 PDF和1份来源映射README | 目录元数据；未做完整引文核验 |
| docs/ | STRUCTURE、DATA_REGISTRY、METHODOLOGY、NOTATION、WORKFLOW、审计和计划 | 入口/数据登记重点阅读 |
| docs/raw/ | 6份实验处理DOCX与其他上传材料 | DOCX有限正文；不复制 |
| results/ | 专业潮汐模型表、audit-v1结果与历史验证 | 代表性表头和当前冻结清单 |
| archive/ | 历史分析、温度材料、旧图文和diff快照 | 目录/文件元数据为主，不作现行真值 |
| .git/ | 版本对象、索引和引用 | 仅元数据统计；无Git命令、无remote/认证配置读取 |
| .venv/ | 原项目本地虚拟环境 | pyvenv.cfg、dist-info名称；未启动解释器或导入包 |
| .remember/、.pytest_cache/、__pycache__/ | 自动记录、测试和字节码缓存 | 仅元数据，不全文读取 |

E编号见PROJECT_PROFILE；文件用途以E01–E04、E06、E22–E26及静态内容为依据。空目录、隐藏目录和内部缓存也列入元数据枚举；科研文件统计口径见附录。

## 主要科研材料

| 路径/类型 | 实测数量/大小或格式 | 说明 |
| --- | --- | --- |
| clock/data/环外数据（第八列数据）/*.txt | 25文件；单文件大多约17.02 MB | 2026夏季计数器记录 |
| clock/data/光纤环外（第二列数据）/*.txt | 29文件；大多约9.42 MB | 链路环外记录，登记为未接入当前主链 |
| newdata/*.txt | 17文件，另1 DOCX；整个目录282,269,479字节 | 2份2025、4份2026-01、11份2026-04/05 |
| clock/武汉-上海潮汐结果（0620-0910）-30秒间隔数据.xlsx | 22,433,405字节；Sheet1；XML维度A1:J239042 | 声明范围不是有效观测数量；未读全表 |
| docs/raw/*.docx | 6份 | 分段、系统频移修订和潮汐修正记录 |
| paper/*.docx | 2份 | 旧光钟论文草稿、水准测量 |
| newdata/数据分组.docx | 21,915字节 | 包含原始时段、38段、分频和MATLAB R2025a报告 |
| data/fes2022/*.nc.xz（分子目录） | 76文件，13,761,544,464字节 | 34 load、34 ocean、8 extrapolated；本次未重做xz完整性检验 |
| data/fes2022/mask/mask_fes2022B.nc | 1,027,081字节；HDF5签名 | 只读文件头；内部维度/变量未读取 |
| research/沪汉潮汐_Nature稿_v13_20261103.pdf | 720,541字节；11页 | 作者原稿 |
| paper/nature/lunar-independent-v14-20261103/main.pdf | 588,549字节；13页 | 图文作者审阅版 |
| paper/prl/main.pdf、supplementary.pdf | 3,187,292字节/7页；926,341字节/8页 | PRL正文与补充 |
| docs/2610.39635v1.pdf | 4,986,248字节；27页 | 光钟网络潮汐相关文献；本次仅确认首页面身份 |
| paper/ref/ | 46文件；128,201,316字节 | 本地参考文献集合；没有据其存在认证DOI或发表状态 |
| 全部PNG/SVG/PDF | PNG166、SVG19、PDF163 | 含历史重复图、论文和参考文献，非独立研究结果数 |
| PKL/NPZ | 6/42文件 | 派生缓存；未反序列化或做数据计算 |

其他CSV、TXT、PDF、DOCX、LaTeX、BibTeX、JSON、压缩包等的全部数量/大小和相对路径见附录。没有发现科研文件范围内的.R/.Rmd/.Rproj、.ipynb、.xls或TIFF；不据此判断站外没有相关材料。

## 代码入口与引用关系

```text
clock/data/ + clock/params.json + results/comp_shanghai-wuhan-beijintime.csv
  → clock/shared.py、data_provenance.py
  → clock_ratio/（ratio、statistics、uncertainty、tidal、manifest）
  → results/audit-v1/runs/<run>/manifest.json
  → paper/rev2/tools/build_numbers.py → PRL数字/表格（旧管线）

newdata/ + clock/data/ + FES2022/模型表
  → research/tidal-spring/ 和 tidal-kalman/
  → 多版模板、拟合、报告与旧54段稿

V7候选材料 → lunar-v7-20261103/、V7twin/ → 候选诊断
  （不能直接认证V13/V14）

V13作者PDF → V14 source-data/model-and-estimates.json
  → tools/build_numbers.py → numbers.tex → main.tex/main.pdf
  → tools/plot_summary.py → 图1、3、4
V13作者PDF → tools/retain_author_panels.py → 保留面板和溯源记录
```

箭头为静态代码/文档声明，不表示本次已执行或整个链已经闭合。

代码范围实测：Python 186份（clock 13、clock_ratio 52、research 99、paper 17、archive 4、根run_all.py 1），Shell 6份，MATLAB 2份。测试脚本包含在Python计数中，不等于186个独立分析。所有代码位置可查附录扩展名。

重点入口：
- `run_all.py`：既有legacy/audit总入口，可能写staging、结果与verified链接，本阶段禁止执行。
- `clock/shared.py`：REPO_ROOT由源码路径确定，查找上级raw目录；导入时读取params.json。绝对比值使用Decimal 80位。
- `clock_ratio/compute_ratio.py`、`statistical_methods*.py`、`uncertainty_budget.py`、`build_result_manifest.py`：比值/统计/预算/结果清单。
- `research/tidal-spring/check_data.py`、`all_data_fit.py`、`unified_fit.py`、`make_sop_template.py`、`gpu_otl_prem.py`：跨期选样、拟合与模型构建；多版本用途需逐项确认。
- `research/V7twin/raw_audit.py`、`reconstruct.py`、`robustness.py`：诊断重建，会写local缓存及结果，不能在源项目直接运行。
- Shell分布：海潮下载3份，paper/rev2/tools内check/sync_overleaf/publish共3份。只登记位置，不运行。
- MATLAB两份：`clock/data/代码/SrYb_35bin_equal_secondary_full_analysis_20260825.m`、`YbSr_NISTstyle_14bin_full_analysis_20260824.m`。

## 环境识别（未执行原环境）

| 层级 | 所见信息 | 限制 |
| --- | --- | --- |
| pyproject.toml | Python>=3.12,<3.13；NumPy、SciPy、Matplotlib、Pydantic、Typer、openpyxl | 主配置不能覆盖所有后续研究/绘图依赖 |
| 可选配置 | test: pytest>=8.3,<9；weather: meteostat>=1.6,<2 | 不代表已安装 |
| uv.lock | Python==3.12.*；pytest8.4.2、pandas3.0.6、meteostat1.7.6等 | 锁文件本身未执行 |
| .venv/pyvenv.cfg | CPython3.12.3；include-system-site-packages=false | 解释器为符号链接，未跟随执行 |
| .venv dist-info | numpy2.5.3、scipy1.18.1、matplotlib3.11.2、pandas2.3.3、openpyxl3.1.5、pydantic2.13.5、typer0.27.2 | 仅安装元数据，未验证导入可用性 |
| 环境差异 | 本地pandas2.3.3≠锁定3.0.6；meteostat2.1.5≠锁定1.7.6且超出声明<2 | 禁止直接执行uv sync修复；后续另行设计环境 |
| 历史运行记录 | 冻结manifest记录Python3.12.3；V7twin记录pyTMD3.0.9 | 此次.venv元数据未发现pyTMD，可能使用另一环境；实际当前可用性UNKNOWN |
| 扩展imports | pandas、astropy、netCDF4、pysolid、pyTMD、xarray、cupy、cartopy、shapely、fitz、reportlab、bs4等 | 静态AST中出现；包含可选/分支依赖，不认定每个脚本都必须全部安装 |
| 未在.venv dist-info发现 | pytest、pyTMD、xarray、CuPy、Cartopy、Shapely、ReportLab等 | 不等于系统环境没有，也不证明全项目无法运行 |
| R | 未发现R代码或R环境声明；当前PATH无R/Rscript | 原项目R版本UNKNOWN |
| MATLAB | DOCX写明MATLAB R2025a；两份.m脚本 | 本次未执行验证；PATH无matlab/octave |
| TeX工具 | PATH发现pdflatex、bibtex；未发现latexmk | 未编译、未测版本；V14源包不需BibTeX，历史稿可能需要 |
| 其他外部工具 | PATH发现uv、xz、pdftotext、pdfinfo、nvidia-smi；未发现gmt | 仅工具可定位；没有运行GPU任务 |
| GPU依赖 | gpu_otl_prem.py注释要求系统Python/CuPy、CUDA_PATH=/usr/local/cuda-12.8；原记录提及双GPU | 当前设备/驱动/CUDA兼容性未验证 |

核查环境使用的是工作站既有Python标准库，不是原项目解释器；没有安装依赖或修改配置。

## 路径和可迁移性问题

1. `clock/shared.py`按自身位置寻找raw目录，`compute_ratio.py`等OUT_DIR是源码所在目录；从新cwd调用旧脚本仍可能写回原项目。
2. `love_prem.py`和`gpu_otl_prem.py`含原项目绝对路径；模型表具体版本仍应绑定。不要简单替换路径并假定物理口径一致。
3. `research/tidal-spring/unified_fit.py`引用同目录total_tide_sop.csv，该文件位置缺失；历史版存在于data/archive/。其他脚本也可能保留旧默认模板；本次只确认此例，不宣称静态依赖图完整。
4. V14绘图通过NATURE_FIGURE_SCRIPTS或用户目录下nature-figure脚本实现质量检查；这是项目外依赖，本次未进入或执行。source-data/basemap使用相对路径，需相应工作目录。
5. V14的保留面板源是本地V13 PDF及提取文本；可编译源包并不包含全部原始科研输入，也不是完整分析复现包。
6. `paper/prl/REVIEW_RESPONSE.md`被路由文档提及，但本次未发现对应文件；目录说明可能落后于实际文件。
7. 数据目录和results混合存放原始输入、模型输入与派生结果；不得依据“results”目录名判定都可覆盖。
8. 原项目外符号链接一律不跟随；verified内部目标经边界检查后按真实路径读取，其他链接仅元数据登记。

## 盘点覆盖与限制

所有普通文件递归统计包含.git、.venv和隐藏记录；“科研文件”统一排除任意以点开头的路径组件及__pycache__，因此不是只按扩展名筛选，也不等于全部为原始数据。文件数含复制的稿件、图表和历史版本，不按内容去重。

本次没有读取认证文件、私钥、令牌或密码内容，没有输出环境变量全集；隐藏配置只计元数据。没有加载大型数据、反序列化pickle、重建统计、执行原项目代码或Git命令。只读可能触发操作系统访问时间更新，本文不把atime用作完整性证据。

## 递归盘点附录

检查时间：2026-11-03T20:38:52+08:00。

普通文件 30,963 个，合计 18,427,597,316 字节；科研口径 1,551 个，15,770,230,766 字节；符号链接 9 个。

### 顶层统计（包含该目录内隐藏/缓存文件，不包含链接目标）

| 顶层 | 文件数 | 字节数 |
| --- | ---: | ---: |
| `[root]` | 7 | 98,398 |
| `.git` | 6,578 | 1,952,690,298 |
| `.pytest_cache` | 5 | 29,620 |
| `.remember` | 8,673 | 3,555,289 |
| `.venv` | 14,018 | 699,203,699 |
| `__pycache__` | 1 | 15,144 |
| `archive` | 161 | 18,845,621 |
| `clock` | 83 | 743,154,216 |
| `clock_ratio` | 102 | 1,456,839 |
| `data` | 84 | 13,766,498,395 |
| `docs` | 28 | 43,033,180 |
| `newdata` | 18 | 282,269,479 |
| `paper` | 579 | 194,353,655 |
| `research` | 505 | 601,168,715 |
| `results` | 121 | 121,224,768 |

### 科研文件扩展名统计

| 扩展名 | 文件数 | 字节数 |
| --- | ---: | ---: |
| `.aux` | 16 | 149,601 |
| `.bbl` | 12 | 117,160 |
| `.bib` | 15 | 327,313 |
| `.blg` | 12 | 13,844 |
| `.cpg` | 2 | 10 |
| `.csv` | 108 | 295,969,348 |
| `.dbf` | 2 | 139,810 |
| `.docx` | 9 | 15,616,631 |
| `.html` | 11 | 5,941,797 |
| `.json` | 259 | 2,076,074 |
| `.lock` | 1 | 56,855 |
| `.log` | 27 | 513,071 |
| `.m` | 2 | 206,151 |
| `.md` | 167 | 1,350,065 |
| `.nc` | 1 | 1,027,081 |
| `.npz` | 42 | 34,168,084 |
| `.out` | 11 | 1,198 |
| `.patch` | 1 | 93,669 |
| `.pdf` | 163 | 174,779,557 |
| `.pkl` | 6 | 372,759,945 |
| `.png` | 166 | 34,266,646 |
| `.pptx` | 5 | 2,842,560 |
| `.prj` | 2 | 286 |
| `.py` | 186 | 1,357,361 |
| `.sh` | 6 | 10,166 |
| `.sha256` | 1 | 7,694 |
| `.shp` | 2 | 2,097,060 |
| `.shx` | 2 | 22,984 |
| `.svg` | 19 | 676,682 |
| `.tex` | 102 | 993,804 |
| `.toc` | 1 | 990 |
| `.toml` | 1 | 576 |
| `.txt` | 107 | 1,002,342,145 |
| `.xlsx` | 1 | 22,433,405 |
| `.xz` | 76 | 13,761,544,464 |
| `.zip` | 6 | 36,314,736 |
| `[无扩展名]` | 1 | 11,943 |

### 符号链接（只分类，不遍历目标目录）

| 链接位置 | 目标边界 |
| --- | --- |
| `.codegraph` | 项目外，未跟随 |
| `.venv/bin/python` | 项目外，未跟随 |
| `.venv/bin/python3` | 项目内（词法边界；不代表已遍历） |
| `.venv/bin/python3.12` | 项目内（词法边界；不代表已遍历） |
| `.venv/lib64` | 项目内（词法边界；不代表已遍历） |
| `results/audit-v1/verification/20261007T161859Z/verified` | 项目内（词法边界；不代表已遍历） |
| `results/audit-v1/verification/20261007T172640Z/verified` | 项目内（词法边界；不代表已遍历） |
| `results/audit-v1/verification/20261007T173310Z/verified` | 项目内（词法边界；不代表已遍历） |
| `results/audit-v1/verified` | 项目内（词法边界；不代表已遍历） |

### 主要目录完整清单（不展开隐藏/缓存目录）

```text
archive
archive/diffs
archive/legacy-products
archive/legacy-products/clock
archive/legacy-products/clock/segment_analysis
archive/legacy-products/clock_ratio
archive/legacy-products/clock_ratio/paper_figs
archive/legacy-products/clock_ratio/tidal_correction
archive/overleaf-rev2
archive/overleaf-rev2/figs
archive/overleaf-rev2/generated
archive/overleaf-rev2/sections
archive/physics_analysis
archive/rev2-pre-format-guide-2026-10-28
archive/rev2-pre-format-guide-2026-10-28/figs
archive/rev2-pre-format-guide-2026-10-28/generated
archive/rev2-pre-format-guide-2026-10-28/sections
archive/superpowers
archive/superpowers/plans
archive/superpowers/specs
archive/temperature
clock
clock/data
clock/data/代码
clock/data/光纤环外（第二列数据）
clock/data/环外数据（第八列数据）
clock/segment_analysis
clock_ratio
clock_ratio/paper_figs
clock_ratio/tidal_correction
data
data/fes2022
data/fes2022/derived
data/fes2022/doc
data/fes2022/load_tide
data/fes2022/logs
data/fes2022/mask
data/fes2022/ocean_tide
data/fes2022/ocean_tide_extrapolated
data/fes2022/scripts
docs
docs/audit
docs/raw
docs/superpowers
docs/superpowers/plans
docs/superpowers/specs
newdata
paper
paper/archive
paper/archive/prl-submission-2026-11-02-v2-corrected
paper/nature
paper/nature/figs
paper/nature/figs/review-20261103
paper/nature/independent-concurrent-revision-20261103
paper/nature/independent-concurrent-revision-20261103/local
paper/nature/lunar-independent-v14-20261103
paper/nature/lunar-independent-v14-20261103/figures
paper/nature/lunar-independent-v14-20261103/local
paper/nature/lunar-independent-v14-20261103/source-data
paper/nature/lunar-independent-v14-20261103/source-data/basemap
paper/nature/lunar-independent-v14-20261103/tools
paper/nature/lunar-measured-v7-20261103
paper/nature/lunar-measured-v7-20261103/figures
paper/nature/lunar-measured-v7-20261103/source-data
paper/nature/lunar-measured-v7-20261103/tools
paper/nature/lunar-measured-v7-figure-pass-20261103
paper/nature/lunar-measured-v7-figure-pass-20261103/figures
paper/nature/lunar-measured-v7-figure-pass-20261103/source-data
paper/nature/lunar-measured-v7-figure-pass-20261103/tools
paper/nature/preview-4plus2-20261103
paper/nature/preview-4plus2-20261103/tools
paper/nature/review
paper/nature/tables
paper/nature/tools
paper/overleaf
paper/overleaf-prl
paper/overleaf-prl/figs
paper/overleaf-rev2-v2
paper/overleaf-rev2-v2/figs
paper/overleaf-rev2-v2/generated
paper/overleaf/figs
paper/prl
paper/prl/figs
paper/prl/revision
paper/ref
paper/rev2
paper/rev2/figs
paper/rev2/generated
paper/rev2/tools
research
research/V7twin
research/V7twin/local
research/V7twin/prl-check
research/prl-2026
research/tidal-kalman
research/tidal-spring
research/tidal-spring/data
research/tidal-spring/data/archive
research/tidal-spring/data/otl
research/tidal-spring/data/solid
research/tidal-spring/data/total
research/tidal-spring/lunar-v7-20261103
research/tidal-spring/lunar-v7-20261103/fig2-reconstruction
research/tidal-spring/lunar-v7-20261103/may-timing-rebuilt
research/tidal-spring/lunar-v7-20261103/prl-model-check
research/tidal-spring/nature-review-20261103
research/v10-review-20261103
research/v10-review-20261103/local
research/v13-review-20261103
research/v13-review-20261103/local
results
results/audit-v1
results/audit-v1/runs
results/audit-v1/runs/15725f5246e87af5
results/audit-v1/runs/15725f5246e87af5/tide-conversion
results/audit-v1/runs/48a6010196134530
results/audit-v1/runs/48a6010196134530/tide-conversion
results/audit-v1/runs/a0d8a696bba93641
results/audit-v1/runs/a0d8a696bba93641/tide-conversion
results/audit-v1/runs/ac725aaba8ec744b
results/audit-v1/runs/ac725aaba8ec744b/tide-conversion
results/audit-v1/runs/ba3c434326918289
results/audit-v1/runs/ba3c434326918289/tide-conversion
results/audit-v1/verification
results/audit-v1/verification/20261007T161859Z
results/audit-v1/verification/20261007T161859Z/runs
results/audit-v1/verification/20261007T161859Z/runs/cb10d16d8c687a50
results/audit-v1/verification/20261007T161859Z/runs/cb10d16d8c687a50/tide-conversion
results/audit-v1/verification/20261007T172640Z
results/audit-v1/verification/20261007T172640Z/runs
results/audit-v1/verification/20261007T172640Z/runs/03b02b974391582e
results/audit-v1/verification/20261007T172640Z/runs/03b02b974391582e/tide-conversion
results/audit-v1/verification/20261007T173310Z
results/audit-v1/verification/20261007T173310Z/runs
results/audit-v1/verification/20261007T173310Z/runs/327182fd8fec6c16
results/audit-v1/verification/20261007T173310Z/runs/327182fd8fec6c16/tide-conversion
```

### 科研文件逐项索引

以下路径均相对原项目根目录；列出全部科研口径文件的名称、格式后缀及大小。列表不代表已全文阅读或已认证，不包含隐藏环境、Git及缓存内部文件。

<details>
<summary>展开 1,551 个科研/项目文件索引</summary>

| 相对路径 | 格式后缀 | 字节数 |
| --- | --- | ---: |
| `AGENTS.md` | `.md` | 7,987 |
| `LICENSE` | `[无扩展名]` | 11,943 |
| `README.md` | `.md` | 7,132 |
| `archive/ANALYSIS.md` | `.md` | 12,447 |
| `archive/CONCLUSION_17.md` | `.md` | 4,529 |
| `archive/CORRELATION_REPORT.md` | `.md` | 9,288 |
| `archive/FINAL_REPORT.md` | `.md` | 9,331 |
| `archive/INVESTIGATION_NOTES.md` | `.md` | 9,921 |
| `archive/PDF_METHODOLOGY_REVIEW.md` | `.md` | 9,605 |
| `archive/PROJECT_REPORT.md` | `.md` | 27,212 |
| `archive/README.md` | `.md` | 3,000 |
| `archive/SEGMENT_17_SUMMARY.md` | `.md` | 4,675 |
| `archive/VARIANTS_COMPARISON.md` | `.md` | 3,047 |
| `archive/batch_17seg_overview.png` | `.png` | 77,359 |
| `archive/comparison_scatter.png` | `.png` | 84,397 |
| `archive/comparison_spectrum.png` | `.png` | 140,337 |
| `archive/comparison_timeseries.png` | `.png` | 108,418 |
| `archive/diffs/README.md` | `.md` | 1,097 |
| `archive/diffs/main_rev_latest.pdf` | `.pdf` | 1,703,176 |
| `archive/diffs/main_rev_latest.tex` | `.tex` | 58,685 |
| `archive/diffs/main_vs_seg9.pdf` | `.pdf` | 1,720,904 |
| `archive/diffs/main_vs_seg9.tex` | `.tex` | 70,174 |
| `archive/diffs/seg9_rev_latest.pdf` | `.pdf` | 1,702,994 |
| `archive/diffs/seg9_rev_latest.tex` | `.tex` | 59,169 |
| `archive/earthquake_analysis.md` | `.md` | 2,594 |
| `archive/earthquake_analysis.py` | `.py` | 2,799 |
| `archive/legacy-products/clock/atomic-clock-comp.pdf` | `.pdf` | 2,139,762 |
| `archive/legacy-products/clock/clock_tidal_shift.csv` | `.csv` | 1,830 |
| `archive/legacy-products/clock/clock_tidal_shift.png` | `.png` | 128,001 |
| `archive/legacy-products/clock/correlation.png` | `.png` | 88,746 |
| `archive/legacy-products/clock/segment13_correlation.png` | `.png` | 330,283 |
| `archive/legacy-products/clock/segment_analysis/batch_aggregate.csv` | `.csv` | 284 |
| `archive/legacy-products/clock/segment_analysis/batch_forest.png` | `.png` | 43,839 |
| `archive/legacy-products/clock/segment_analysis/batch_shared_axis.png` | `.png` | 1,207,494 |
| `archive/legacy-products/clock/segment_analysis/batch_summary.csv` | `.csv` | 2,056 |
| `archive/legacy-products/clock/segment_analysis/segment13_shared_axis.png` | `.png` | 198,785 |
| `archive/legacy-products/clock/segment_analysis/segment6_shared_axis.png` | `.png` | 156,992 |
| `archive/legacy-products/clock/segment_analysis/variant1_30s_tide_forest.png` | `.png` | 40,168 |
| `archive/legacy-products/clock/segment_analysis/variant1_30s_tide_summary.csv` | `.csv` | 1,583 |
| `archive/legacy-products/clock/segment_analysis/variant30s_forest.png` | `.png` | 43,968 |
| `archive/legacy-products/clock/segment_analysis/variant30s_summary.csv` | `.csv` | 1,583 |
| `archive/legacy-products/clock_ratio/EXPERIMENT_REPORT.md` | `.md` | 19,680 |
| `archive/legacy-products/clock_ratio/concatenated_stability.csv` | `.csv` | 4,584 |
| `archive/legacy-products/clock_ratio/concatenated_stability.md` | `.md` | 3,499 |
| `archive/legacy-products/clock_ratio/concatenated_stability.pdf` | `.pdf` | 22,835 |
| `archive/legacy-products/clock_ratio/concatenated_stability.png` | `.png` | 162,452 |
| `archive/legacy-products/clock_ratio/concatenated_stability_16seg.csv` | `.csv` | 8,587 |
| `archive/legacy-products/clock_ratio/concatenated_stability_16seg.md` | `.md` | 4,859 |
| `archive/legacy-products/clock_ratio/concatenated_stability_16seg.pdf` | `.pdf` | 35,415 |
| `archive/legacy-products/clock_ratio/concatenated_stability_16seg.png` | `.png` | 251,138 |
| `archive/legacy-products/clock_ratio/concatenated_stability_16seg_theory.pdf` | `.pdf` | 31,466 |
| `archive/legacy-products/clock_ratio/concatenated_stability_16seg_theory.png` | `.png` | 212,936 |
| `archive/legacy-products/clock_ratio/concatenated_stability_long.csv` | `.csv` | 5,523 |
| `archive/legacy-products/clock_ratio/concatenated_stability_long.md` | `.md` | 3,887 |
| `archive/legacy-products/clock_ratio/concatenated_stability_long.pdf` | `.pdf` | 27,214 |
| `archive/legacy-products/clock_ratio/concatenated_stability_long.png` | `.png` | 148,975 |
| `archive/legacy-products/clock_ratio/correlation_reanalysis.csv` | `.csv` | 325 |
| `archive/legacy-products/clock_ratio/correlation_reanalysis.png` | `.png` | 92,058 |
| `archive/legacy-products/clock_ratio/correlation_reanalysis_seg9_excluded.csv` | `.csv` | 242 |
| `archive/legacy-products/clock_ratio/correlation_reanalysis_seg9_excluded.png` | `.png` | 86,910 |
| `archive/legacy-products/clock_ratio/correlation_reanalysis_seg9_independent.csv` | `.csv` | 374 |
| `archive/legacy-products/clock_ratio/correlation_reanalysis_seg9_independent.json` | `.json` | 4,355 |
| `archive/legacy-products/clock_ratio/correlation_reanalysis_timeweighted.csv` | `.csv` | 377 |
| `archive/legacy-products/clock_ratio/correlation_reanalysis_timeweighted.png` | `.png` | 107,658 |
| `archive/legacy-products/clock_ratio/paper_figs/fig1_ratio_segments.pdf` | `.pdf` | 12,415 |
| `archive/legacy-products/clock_ratio/paper_figs/fig1_ratio_segments.png` | `.png` | 66,564 |
| `archive/legacy-products/clock_ratio/paper_figs/fig2_tidal_detection.pdf` | `.pdf` | 13,486 |
| `archive/legacy-products/clock_ratio/paper_figs/fig2_tidal_detection.png` | `.png` | 84,586 |
| `archive/legacy-products/clock_ratio/paper_figs/fig3_correction.pdf` | `.pdf` | 12,763 |
| `archive/legacy-products/clock_ratio/paper_figs/fig3_correction.png` | `.png` | 89,329 |
| `archive/legacy-products/clock_ratio/paper_figs/fig4_methods_summary.pdf` | `.pdf` | 12,278 |
| `archive/legacy-products/clock_ratio/paper_figs/fig4_methods_summary.png` | `.png` | 69,399 |
| `archive/legacy-products/clock_ratio/ratio_17seg.csv` | `.csv` | 2,981 |
| `archive/legacy-products/clock_ratio/ratio_17seg_summary.csv` | `.csv` | 477 |
| `archive/legacy-products/clock_ratio/ratio_segments.png` | `.png` | 80,568 |
| `archive/legacy-products/clock_ratio/statistical_methods.csv` | `.csv` | 1,442 |
| `archive/legacy-products/clock_ratio/statistical_methods.json` | `.json` | 895 |
| `archive/legacy-products/clock_ratio/statistical_methods_tidal.json` | `.json` | 16,453 |
| `archive/legacy-products/clock_ratio/statistical_methods_tidal_seg9_excluded.json` | `.json` | 15,967 |
| `archive/legacy-products/clock_ratio/tidal_correction/REPORT.md` | `.md` | 13,184 |
| `archive/legacy-products/clock_ratio/tidal_correction/ratio_scenarios.csv` | `.csv` | 25,837 |
| `archive/legacy-products/clock_ratio/tidal_correction/stability.csv` | `.csv` | 55,819 |
| `archive/legacy-products/clock_ratio/tidal_correction/summary.json` | `.json` | 4,637 |
| `archive/legacy-products/clock_ratio/tidal_new_model_compare.json` | `.json` | 2,483 |
| `archive/legacy-products/clock_ratio/tidal_new_model_compare.md` | `.md` | 5,957 |
| `archive/legacy-products/clock_ratio/tidal_solid_only_compare.json` | `.json` | 8,143 |
| `archive/legacy-products/clock_ratio/tidal_solid_only_compare.md` | `.md` | 4,832 |
| `archive/legacy-products/clock_ratio/tidal_solid_only_scatter.png` | `.png` | 141,822 |
| `archive/legacy-products/clock_ratio/tidal_within_segment_16seg.json` | `.json` | 9,118 |
| `archive/overleaf-rev2-upload.zip` | `.zip` | 71,887 |
| `archive/overleaf-rev2/README.md` | `.md` | 2,817 |
| `archive/overleaf-rev2/figs/fig1_network.pdf` | `.pdf` | 20,046 |
| `archive/overleaf-rev2/figs/fig2_campaign.pdf` | `.pdf` | 19,135 |
| `archive/overleaf-rev2/figs/fig3_compare.pdf` | `.pdf` | 18,840 |
| `archive/overleaf-rev2/generated/numbers.json` | `.json` | 4,580 |
| `archive/overleaf-rev2/generated/numbers.tex` | `.tex` | 4,033 |
| `archive/overleaf-rev2/generated/numbers_manifest.json` | `.json` | 12,210 |
| `archive/overleaf-rev2/generated/segment_table.tex` | `.tex` | 825 |
| `archive/overleaf-rev2/main.tex` | `.tex` | 4,196 |
| `archive/overleaf-rev2/refs.bib` | `.bib` | 32,768 |
| `archive/overleaf-rev2/sections/abstract.tex` | `.tex` | 1,535 |
| `archive/overleaf-rev2/sections/appendix.tex` | `.tex` | 6,025 |
| `archive/overleaf-rev2/sections/discussion.tex` | `.tex` | 5,295 |
| `archive/overleaf-rev2/sections/introduction.tex` | `.tex` | 4,035 |
| `archive/overleaf-rev2/sections/methods.tex` | `.tex` | 5,560 |
| `archive/overleaf-rev2/sections/results.tex` | `.tex` | 4,588 |
| `archive/physics_analysis/ABSTRACT.md` | `.md` | 10,978 |
| `archive/physics_analysis/ABSTRACT_EN_SHORT.md` | `.md` | 2,370 |
| `archive/physics_analysis/ABSTRACT_NATURE.md` | `.md` | 6,103 |
| `archive/physics_analysis/NATURE_FRAMEWORK.md` | `.md` | 16,353 |
| `archive/physics_analysis/README.md` | `.md` | 4,042 |
| `archive/physics_analysis/REPORT.md` | `.md` | 39,143 |
| `archive/physics_analysis/refs.bib` | `.bib` | 22,416 |
| `archive/physics_analysis/sensitivity_estimate.py` | `.py` | 12,383 |
| `archive/physics_analysis/sensitivity_estimates.csv` | `.csv` | 998 |
| `archive/physics_analysis/sensitivity_summary.json` | `.json` | 1,499 |
| `archive/rev2-pre-format-guide-2026-10-28/README.md` | `.md` | 755 |
| `archive/rev2-pre-format-guide-2026-10-28/figs/fig1_network.png` | `.png` | 868,235 |
| `archive/rev2-pre-format-guide-2026-10-28/figs/fig2_ratio.png` | `.png` | 347,177 |
| `archive/rev2-pre-format-guide-2026-10-28/figs/fig3_history.png` | `.png` | 186,156 |
| `archive/rev2-pre-format-guide-2026-10-28/figs/fig5_spliced_stability.pdf` | `.pdf` | 28,720 |
| `archive/rev2-pre-format-guide-2026-10-28/figs/fig5_spliced_stability.png` | `.png` | 208,548 |
| `archive/rev2-pre-format-guide-2026-10-28/figs/figSI_fit_grid.pdf` | `.pdf` | 66,740 |
| `archive/rev2-pre-format-guide-2026-10-28/figs/figSI_fit_grid.png` | `.png` | 435,396 |
| `archive/rev2-pre-format-guide-2026-10-28/figs/fig_method_setup_a3p.pdf` | `.pdf` | 298,249 |
| `archive/rev2-pre-format-guide-2026-10-28/figs/fig_methods_forest.pdf` | `.pdf` | 21,869 |
| `archive/rev2-pre-format-guide-2026-10-28/figs/fig_methods_forest.png` | `.png` | 68,793 |
| `archive/rev2-pre-format-guide-2026-10-28/generated/correlation_table.tex` | `.tex` | 733 |
| `archive/rev2-pre-format-guide-2026-10-28/generated/loo_table.tex` | `.tex` | 785 |
| `archive/rev2-pre-format-guide-2026-10-28/generated/numbers.json` | `.json` | 4,608 |
| `archive/rev2-pre-format-guide-2026-10-28/generated/numbers.tex` | `.tex` | 6,209 |
| `archive/rev2-pre-format-guide-2026-10-28/generated/numbers_manifest.json` | `.json` | 19,447 |
| `archive/rev2-pre-format-guide-2026-10-28/generated/ratio_intermediates.tex` | `.tex` | 1,282 |
| `archive/rev2-pre-format-guide-2026-10-28/generated/sample_ledger_table.tex` | `.tex` | 907 |
| `archive/rev2-pre-format-guide-2026-10-28/generated/segment_table.tex` | `.tex` | 827 |
| `archive/rev2-pre-format-guide-2026-10-28/generated/shift_components_table.tex` | `.tex` | 1,270 |
| `archive/rev2-pre-format-guide-2026-10-28/generated/tidal_synthesis_table.tex` | `.tex` | 336 |
| `archive/rev2-pre-format-guide-2026-10-28/main.pdf` | `.pdf` | 1,851,661 |
| `archive/rev2-pre-format-guide-2026-10-28/main.tex` | `.tex` | 6,514 |
| `archive/rev2-pre-format-guide-2026-10-28/refs.bib` | `.bib` | 33,340 |
| `archive/rev2-pre-format-guide-2026-10-28/sections/abstract.tex` | `.tex` | 1,509 |
| `archive/rev2-pre-format-guide-2026-10-28/sections/conclusion.tex` | `.tex` | 1,227 |
| `archive/rev2-pre-format-guide-2026-10-28/sections/discussion.tex` | `.tex` | 7,459 |
| `archive/rev2-pre-format-guide-2026-10-28/sections/introduction.tex` | `.tex` | 3,541 |
| `archive/rev2-pre-format-guide-2026-10-28/sections/methods.tex` | `.tex` | 11,160 |
| `archive/rev2-pre-format-guide-2026-10-28/sections/results.tex` | `.tex` | 7,474 |
| `archive/rev2-pre-format-guide-2026-10-28/supplementary.pdf` | `.pdf` | 869,006 |
| `archive/rev2-pre-format-guide-2026-10-28/supplementary.tex` | `.tex` | 18,844 |
| `archive/segment17_correlation.md` | `.md` | 3,098 |
| `archive/segment17_correlation.py` | `.py` | 5,621 |
| `archive/session_dff_old_vs_professional.png` | `.png` | 100,922 |
| `archive/superpowers/plans/2026-10-06-clock-analysis-audit.md` | `.md` | 62,349 |
| `archive/superpowers/plans/2026-10-21-methods-si-alignment.md` | `.md` | 9,335 |
| `archive/superpowers/plans/2026-10-21-tidal-defense-relocation.md` | `.md` | 9,744 |
| `archive/superpowers/specs/2026-10-06-clock-comparison-audit-paper-design.md` | `.md` | 19,010 |
| `archive/temperature/ANALYSIS.md` | `.md` | 5,392 |
| `archive/temperature/fetch_temperature.py` | `.py` | 2,074 |
| `archive/temperature/fx_b2_lock_fraction.png` | `.png` | 43,588 |
| `archive/temperature/fx_b4_vs_temperature.png` | `.png` | 76,831 |
| `archive/temperature/temperature_hefei_hourly.csv` | `.csv` | 49,006 |
| `archive/temperature/temperature_merged_hourly.csv` | `.csv` | 65,361 |
| `archive/temperature/temperature_shanghai_hourly.csv` | `.csv` | 49,009 |
| `archive/temperature/temperature_wuhan_hourly.csv` | `.csv` | 49,006 |
| `archive/temperature_diurnal.png` | `.png` | 384,522 |
| `clock/PARAMS.md` | `.md` | 3,715 |
| `clock/PROFESSIONAL_TIDAL_DATA.md` | `.md` | 10,503 |
| `clock/SIGN_COEFFICIENT_ANALYSIS.md` | `.md` | 10,022 |
| `clock/build_parameter_ledger.py` | `.py` | 10,304 |
| `clock/build_sample_ledger.py` | `.py` | 8,019 |
| `clock/clock_tidal_shift.py` | `.py` | 6,123 |
| `clock/correlation_analysis.py` | `.py` | 3,493 |
| `clock/data/代码/SrYb_35bin_equal_secondary_full_analysis_20260825.m` | `.m` | 104,667 |
| `clock/data/代码/YbSr_NISTstyle_14bin_full_analysis_20260824.m` | `.m` | 101,484 |
| `clock/data/光纤环外（第二列数据）/Freq_A_2_260627_1.txt` | `.txt` | 9,418,084 |
| `clock/data/光纤环外（第二列数据）/Freq_A_2_260628_1.txt` | `.txt` | 9,418,084 |
| `clock/data/光纤环外（第二列数据）/Freq_A_2_260629_1.txt` | `.txt` | 9,418,084 |
| `clock/data/光纤环外（第二列数据）/Freq_A_2_260630_1.txt` | `.txt` | 9,418,084 |
| `clock/data/光纤环外（第二列数据）/Freq_A_2_260701_1.txt` | `.txt` | 9,418,084 |
| `clock/data/光纤环外（第二列数据）/Freq_A_2_260702_1.txt` | `.txt` | 9,418,084 |
| `clock/data/光纤环外（第二列数据）/Freq_A_2_260703_1.txt` | `.txt` | 9,418,084 |
| `clock/data/光纤环外（第二列数据）/Freq_A_2_260704_1.txt` | `.txt` | 9,418,084 |
| `clock/data/光纤环外（第二列数据）/Freq_A_2_260705_1.txt` | `.txt` | 9,418,084 |
| `clock/data/光纤环外（第二列数据）/Freq_A_2_260706_1.txt` | `.txt` | 9,418,084 |
| `clock/data/光纤环外（第二列数据）/Freq_A_2_260807_1.txt` | `.txt` | 9,418,084 |
| `clock/data/光纤环外（第二列数据）/Freq_A_2_260808_1.txt` | `.txt` | 9,418,084 |
| `clock/data/光纤环外（第二列数据）/Freq_A_2_260809_1.txt` | `.txt` | 9,418,084 |
| `clock/data/光纤环外（第二列数据）/Freq_A_2_260810_1.txt` | `.txt` | 9,418,084 |
| `clock/data/光纤环外（第二列数据）/Freq_A_2_260811_1.txt` | `.txt` | 9,418,084 |
| `clock/data/光纤环外（第二列数据）/Freq_A_2_260812_1.txt` | `.txt` | 9,418,084 |
| `clock/data/光纤环外（第二列数据）/Freq_A_2_260813_1.txt` | `.txt` | 9,418,084 |
| `clock/data/光纤环外（第二列数据）/Freq_A_2_260814_1.txt` | `.txt` | 9,418,084 |
| `clock/data/光纤环外（第二列数据）/Freq_A_2_260815_1.txt` | `.txt` | 9,418,084 |
| `clock/data/光纤环外（第二列数据）/Freq_A_2_260816_1.txt` | `.txt` | 9,418,084 |
| `clock/data/光纤环外（第二列数据）/Freq_A_2_260817_1.txt` | `.txt` | 9,418,084 |
| `clock/data/光纤环外（第二列数据）/Freq_A_2_260818_1.txt` | `.txt` | 9,418,084 |
| `clock/data/光纤环外（第二列数据）/Freq_A_2_260819_1.txt` | `.txt` | 5,984,366 |
| `clock/data/光纤环外（第二列数据）/Freq_A_2_260820_1.txt` | `.txt` | 9,418,084 |
| `clock/data/光纤环外（第二列数据）/Freq_A_2_260821_1.txt` | `.txt` | 9,418,084 |
| `clock/data/光纤环外（第二列数据）/Freq_A_2_260822_1.txt` | `.txt` | 9,418,084 |
| `clock/data/光纤环外（第二列数据）/Freq_A_2_260823_1.txt` | `.txt` | 9,418,084 |
| `clock/data/光纤环外（第二列数据）/Freq_A_2_260824_1.txt` | `.txt` | 9,418,084 |
| `clock/data/光纤环外（第二列数据）/Freq_A_2_260825_1.txt` | `.txt` | 9,418,084 |
| `clock/data/环外数据（第八列数据）/Freq_B_2_260627_1.txt` | `.txt` | 17,021,422 |
| `clock/data/环外数据（第八列数据）/Freq_B_2_260628_1.txt` | `.txt` | 17,021,422 |
| `clock/data/环外数据（第八列数据）/Freq_B_2_260629_1.txt` | `.txt` | 17,021,422 |
| `clock/data/环外数据（第八列数据）/Freq_B_2_260630_1.txt` | `.txt` | 17,021,422 |
| `clock/data/环外数据（第八列数据）/Freq_B_2_260701_1.txt` | `.txt` | 17,021,422 |
| `clock/data/环外数据（第八列数据）/Freq_B_2_260702_1.txt` | `.txt` | 17,020,800 |
| `clock/data/环外数据（第八列数据）/Freq_B_2_260703_1.txt` | `.txt` | 17,021,422 |
| `clock/data/环外数据（第八列数据）/Freq_B_2_260704_1.txt` | `.txt` | 17,021,422 |
| `clock/data/环外数据（第八列数据）/Freq_B_2_260705_1.txt` | `.txt` | 17,021,422 |
| `clock/data/环外数据（第八列数据）/Freq_B_2_260706_1.txt` | `.txt` | 17,021,422 |
| `clock/data/环外数据（第八列数据）/Freq_B_2_260707_1.txt` | `.txt` | 17,021,422 |
| `clock/data/环外数据（第八列数据）/Freq_B_2_260806_1.txt` | `.txt` | 17,021,422 |
| `clock/data/环外数据（第八列数据）/Freq_B_2_260807_1.txt` | `.txt` | 17,021,422 |
| `clock/data/环外数据（第八列数据）/Freq_B_2_260808_1.txt` | `.txt` | 17,021,422 |
| `clock/data/环外数据（第八列数据）/Freq_B_2_260809_1.txt` | `.txt` | 17,021,422 |
| `clock/data/环外数据（第八列数据）/Freq_B_2_260810_1.txt` | `.txt` | 17,021,422 |
| `clock/data/环外数据（第八列数据）/Freq_B_2_260811_1.txt` | `.txt` | 17,021,422 |
| `clock/data/环外数据（第八列数据）/Freq_B_2_260812_1.txt` | `.txt` | 51,749,764 |
| `clock/data/环外数据（第八列数据）/Freq_B_2_260820_1.txt` | `.txt` | 6,088,321 |
| `clock/data/环外数据（第八列数据）/Freq_B_2_260821_1.txt` | `.txt` | 17,021,422 |
| `clock/data/环外数据（第八列数据）/Freq_B_2_260822_1.txt` | `.txt` | 17,021,422 |
| `clock/data/环外数据（第八列数据）/Freq_B_2_260823_1.txt` | `.txt` | 17,021,422 |
| `clock/data/环外数据（第八列数据）/Freq_B_2_260824_1.txt` | `.txt` | 17,021,422 |
| `clock/data/环外数据（第八列数据）/Freq_B_2_260825_1.txt` | `.txt` | 17,021,422 |
| `clock/data/环外数据（第八列数据）/Freq_B_2_260826_1.txt` | `.txt` | 17,021,422 |
| `clock/data_provenance.py` | `.py` | 4,752 |
| `clock/params.json` | `.json` | 4,715 |
| `clock/sample_selection.py` | `.py` | 6,226 |
| `clock/segment13_correlation.py` | `.py` | 10,154 |
| `clock/segment_analysis/batch_analysis.py` | `.py` | 16,090 |
| `clock/segment_analysis/segment13_triangular.py` | `.py` | 6,536 |
| `clock/segment_analysis/segment6_triangular.py` | `.py` | 5,905 |
| `clock/segment_analysis/variant1_30s_tide.py` | `.py` | 7,661 |
| `clock/segment_analysis/variant30s_analysis.py` | `.py` | 7,720 |
| `clock/shared.py` | `.py` | 8,872 |
| `clock/武汉-上海潮汐结果（0620-0910）-30秒间隔数据.xlsx` | `.xlsx` | 22,433,405 |
| `clock/潮汐修正后的比值计算.pdf` | `.pdf` | 1,270,325 |
| `clock_ratio/audit_report.py` | `.py` | 18,249 |
| `clock_ratio/build_result_manifest.py` | `.py` | 21,646 |
| `clock_ratio/compute_ratio.py` | `.py` | 4,750 |
| `clock_ratio/concatenated_stability.py` | `.py` | 12,873 |
| `clock_ratio/concatenated_stability_16seg.py` | `.py` | 16,720 |
| `clock_ratio/concatenated_stability_long.py` | `.py` | 10,493 |
| `clock_ratio/correlation_reanalysis.py` | `.py` | 5,413 |
| `clock_ratio/correlation_reanalysis_seg9_excluded.py` | `.py` | 4,884 |
| `clock_ratio/correlation_reanalysis_seg9_independent.py` | `.py` | 6,443 |
| `clock_ratio/correlation_reanalysis_timeweighted.py` | `.py` | 6,950 |
| `clock_ratio/evidence.py` | `.py` | 386 |
| `clock_ratio/make_paper_figures.py` | `.py` | 9,713 |
| `clock_ratio/make_report.py` | `.py` | 31,595 |
| `clock_ratio/make_report_figures.py` | `.py` | 3,218 |
| `clock_ratio/make_tidal_report.py` | `.py` | 12,142 |
| `clock_ratio/nature_figstyle.py` | `.py` | 1,489 |
| `clock_ratio/ratio_model.py` | `.py` | 1,275 |
| `clock_ratio/result_manifest.py` | `.py` | 16,255 |
| `clock_ratio/segment_uncertainty.py` | `.py` | 4,545 |
| `clock_ratio/statistical_combination.py` | `.py` | 1,963 |
| `clock_ratio/statistical_methods.py` | `.py` | 11,872 |
| `clock_ratio/statistical_methods_tidal.py` | `.py` | 7,201 |
| `clock_ratio/statistical_methods_tidal_seg9.py` | `.py` | 8,844 |
| `clock_ratio/statistical_models.py` | `.py` | 8,574 |
| `clock_ratio/statistical_scenarios.py` | `.py` | 13,459 |
| `clock_ratio/test_audit_report.py` | `.py` | 3,873 |
| `clock_ratio/test_concatenated_stability.py` | `.py` | 452 |
| `clock_ratio/test_data_provenance.py` | `.py` | 8,154 |
| `clock_ratio/test_paper_figures.py` | `.py` | 536 |
| `clock_ratio/test_result_manifest.py` | `.py` | 18,946 |
| `clock_ratio/test_sample_selection.py` | `.py` | 10,822 |
| `clock_ratio/test_segment_uncertainty.py` | `.py` | 9,674 |
| `clock_ratio/test_statistical_combination.py` | `.py` | 7,268 |
| `clock_ratio/test_statistical_scenarios.py` | `.py` | 9,645 |
| `clock_ratio/test_tidal_analysis.py` | `.py` | 10,621 |
| `clock_ratio/test_tidal_inference.py` | `.py` | 6,385 |
| `clock_ratio/test_tidal_outputs.py` | `.py` | 11,764 |
| `clock_ratio/test_tidal_report.py` | `.py` | 20,343 |
| `clock_ratio/test_tide_conversion.py` | `.py` | 12,776 |
| `clock_ratio/test_uncertainty_budget.py` | `.py` | 10,151 |
| `clock_ratio/test_windowing.py` | `.py` | 3,904 |
| `clock_ratio/tidal_analysis.py` | `.py` | 5,888 |
| `clock_ratio/tidal_correction.py` | `.py` | 11,566 |
| `clock_ratio/tidal_new_model_compare.py` | `.py` | 7,828 |
| `clock_ratio/tidal_report_data.py` | `.py` | 8,185 |
| `clock_ratio/tidal_solid_only_compare.py` | `.py` | 8,250 |
| `clock_ratio/tidal_stability.py` | `.py` | 4,410 |
| `clock_ratio/tidal_within_segment_16seg.py` | `.py` | 17,119 |
| `clock_ratio/tide_conversion.py` | `.py` | 19,840 |
| `clock_ratio/uncertainty_budget.py` | `.py` | 7,658 |
| `clock_ratio/verify_result_manifest.py` | `.py` | 1,455 |
| `clock_ratio/windowing.py` | `.py` | 8,683 |
| `data/fes2022/MANIFEST.md` | `.md` | 3,290 |
| `data/fes2022/README.md` | `.md` | 2,996 |
| `data/fes2022/doc/hdbk_FES2022.pdf` | `.pdf` | 3,856,163 |
| `data/fes2022/load_tide/2n2_fes2022.nc.xz` | `.xz` | 208,734,696 |
| `data/fes2022/load_tide/eps2_fes2022.nc.xz` | `.xz` | 211,027,428 |
| `data/fes2022/load_tide/j1_fes2022.nc.xz` | `.xz` | 192,572,412 |
| `data/fes2022/load_tide/k1_fes2022.nc.xz` | `.xz` | 192,956,944 |
| `data/fes2022/load_tide/k2_fes2022.nc.xz` | `.xz` | 213,360,640 |
| `data/fes2022/load_tide/l2_fes2022.nc.xz` | `.xz` | 214,774,764 |
| `data/fes2022/load_tide/lambda2_fes2022.nc.xz` | `.xz` | 214,487,360 |
| `data/fes2022/load_tide/m2_fes2022.nc.xz` | `.xz` | 211,923,200 |
| `data/fes2022/load_tide/m3_fes2022.nc.xz` | `.xz` | 228,569,028 |
| `data/fes2022/load_tide/m4_fes2022.nc.xz` | `.xz` | 233,979,040 |
| `data/fes2022/load_tide/m6_fes2022.nc.xz` | `.xz` | 242,665,104 |
| `data/fes2022/load_tide/m8_fes2022.nc.xz` | `.xz` | 250,252,052 |
| `data/fes2022/load_tide/mf_fes2022.nc.xz` | `.xz` | 184,649,216 |
| `data/fes2022/load_tide/mks2_fes2022.nc.xz` | `.xz` | 218,527,748 |
| `data/fes2022/load_tide/mm_fes2022.nc.xz` | `.xz` | 183,049,928 |
| `data/fes2022/load_tide/mn4_fes2022.nc.xz` | `.xz` | 233,127,268 |
| `data/fes2022/load_tide/ms4_fes2022.nc.xz` | `.xz` | 236,629,472 |
| `data/fes2022/load_tide/msf_fes2022.nc.xz` | `.xz` | 201,445,240 |
| `data/fes2022/load_tide/msqm_fes2022.nc.xz` | `.xz` | 197,896,240 |
| `data/fes2022/load_tide/mtm_fes2022.nc.xz` | `.xz` | 188,241,164 |
| `data/fes2022/load_tide/mu2_fes2022.nc.xz` | `.xz` | 211,867,040 |
| `data/fes2022/load_tide/n2_fes2022.nc.xz` | `.xz` | 210,772,464 |
| `data/fes2022/load_tide/n4_fes2022.nc.xz` | `.xz` | 232,462,704 |
| `data/fes2022/load_tide/nu2_fes2022.nc.xz` | `.xz` | 210,502,568 |
| `data/fes2022/load_tide/o1_fes2022.nc.xz` | `.xz` | 193,223,096 |
| `data/fes2022/load_tide/p1_fes2022.nc.xz` | `.xz` | 193,047,256 |
| `data/fes2022/load_tide/q1_fes2022.nc.xz` | `.xz` | 192,953,644 |
| `data/fes2022/load_tide/r2_fes2022.nc.xz` | `.xz` | 213,464,488 |
| `data/fes2022/load_tide/s1_fes2022.nc.xz` | `.xz` | 189,686,560 |
| `data/fes2022/load_tide/s2_fes2022.nc.xz` | `.xz` | 213,082,836 |
| `data/fes2022/load_tide/s4_fes2022.nc.xz` | `.xz` | 235,605,800 |
| `data/fes2022/load_tide/sa_fes2022.nc.xz` | `.xz` | 215,600,084 |
| `data/fes2022/load_tide/ssa_fes2022.nc.xz` | `.xz` | 180,652,964 |
| `data/fes2022/load_tide/t2_fes2022.nc.xz` | `.xz` | 212,955,620 |
| `data/fes2022/logs/download.log` | `.log` | 57,982 |
| `data/fes2022/mask/mask_fes2022B.nc` | `.nc` | 1,027,081 |
| `data/fes2022/ocean_tide/2n2_fes2022.nc.xz` | `.xz` | 153,913,728 |
| `data/fes2022/ocean_tide/eps2_fes2022.nc.xz` | `.xz` | 154,235,296 |
| `data/fes2022/ocean_tide/j1_fes2022.nc.xz` | `.xz` | 149,140,040 |
| `data/fes2022/ocean_tide/k1_fes2022.nc.xz` | `.xz` | 149,274,848 |
| `data/fes2022/ocean_tide/k2_fes2022.nc.xz` | `.xz` | 154,120,000 |
| `data/fes2022/ocean_tide/l2_fes2022.nc.xz` | `.xz` | 154,144,176 |
| `data/fes2022/ocean_tide/lambda2_fes2022.nc.xz` | `.xz` | 154,114,444 |
| `data/fes2022/ocean_tide/m2_fes2022.nc.xz` | `.xz` | 153,574,660 |
| `data/fes2022/ocean_tide/m3_fes2022.nc.xz` | `.xz` | 164,958,088 |
| `data/fes2022/ocean_tide/m4_fes2022.nc.xz` | `.xz` | 171,504,148 |
| `data/fes2022/ocean_tide/m6_fes2022.nc.xz` | `.xz` | 172,524,544 |
| `data/fes2022/ocean_tide/m8_fes2022.nc.xz` | `.xz` | 176,698,832 |
| `data/fes2022/ocean_tide/mf_fes2022.nc.xz` | `.xz` | 149,292,668 |
| `data/fes2022/ocean_tide/mks2_fes2022.nc.xz` | `.xz` | 160,088,540 |
| `data/fes2022/ocean_tide/mm_fes2022.nc.xz` | `.xz` | 144,267,812 |
| `data/fes2022/ocean_tide/mn4_fes2022.nc.xz` | `.xz` | 165,834,416 |
| `data/fes2022/ocean_tide/ms4_fes2022.nc.xz` | `.xz` | 167,438,396 |
| `data/fes2022/ocean_tide/msf_fes2022.nc.xz` | `.xz` | 162,224,464 |
| `data/fes2022/ocean_tide/msqm_fes2022.nc.xz` | `.xz` | 160,644,728 |
| `data/fes2022/ocean_tide/mtm_fes2022.nc.xz` | `.xz` | 154,114,180 |
| `data/fes2022/ocean_tide/mu2_fes2022.nc.xz` | `.xz` | 154,701,956 |
| `data/fes2022/ocean_tide/n2_fes2022.nc.xz` | `.xz` | 153,692,392 |
| `data/fes2022/ocean_tide/n4_fes2022.nc.xz` | `.xz` | 167,765,504 |
| `data/fes2022/ocean_tide/nu2_fes2022.nc.xz` | `.xz` | 153,546,672 |
| `data/fes2022/ocean_tide/o1_fes2022.nc.xz` | `.xz` | 148,581,892 |
| `data/fes2022/ocean_tide/p1_fes2022.nc.xz` | `.xz` | 149,063,700 |
| `data/fes2022/ocean_tide/q1_fes2022.nc.xz` | `.xz` | 148,064,072 |
| `data/fes2022/ocean_tide/r2_fes2022.nc.xz` | `.xz` | 156,272,332 |
| `data/fes2022/ocean_tide/s1_fes2022.nc.xz` | `.xz` | 167,580,520 |
| `data/fes2022/ocean_tide/s2_fes2022.nc.xz` | `.xz` | 154,460,344 |
| `data/fes2022/ocean_tide/s4_fes2022.nc.xz` | `.xz` | 168,541,860 |
| `data/fes2022/ocean_tide/sa_fes2022.nc.xz` | `.xz` | 128,812,488 |
| `data/fes2022/ocean_tide/ssa_fes2022.nc.xz` | `.xz` | 128,927,840 |
| `data/fes2022/ocean_tide/t2_fes2022.nc.xz` | `.xz` | 155,992,460 |
| `data/fes2022/ocean_tide_extrapolated/k1_fes2022.nc.xz` | `.xz` | 158,865,904 |
| `data/fes2022/ocean_tide_extrapolated/k2_fes2022.nc.xz` | `.xz` | 164,005,756 |
| `data/fes2022/ocean_tide_extrapolated/m2_fes2022.nc.xz` | `.xz` | 163,489,712 |
| `data/fes2022/ocean_tide_extrapolated/n2_fes2022.nc.xz` | `.xz` | 163,540,508 |
| `data/fes2022/ocean_tide_extrapolated/o1_fes2022.nc.xz` | `.xz` | 158,175,680 |
| `data/fes2022/ocean_tide_extrapolated/p1_fes2022.nc.xz` | `.xz` | 158,605,048 |
| `data/fes2022/ocean_tide_extrapolated/q1_fes2022.nc.xz` | `.xz` | 157,598,960 |
| `data/fes2022/ocean_tide_extrapolated/s2_fes2022.nc.xz` | `.xz` | 164,404,788 |
| `data/fes2022/scripts/download_fes2022.sh` | `.sh` | 1,834 |
| `data/fes2022/scripts/download_fes2022_extras.sh` | `.sh` | 1,618 |
| `data/fes2022/scripts/download_fes2022_extras_parallel.sh` | `.sh` | 2,967 |
| `docs/2610.39635v1.pdf` | `.pdf` | 4,986,248 |
| `docs/DATA_REGISTRY.md` | `.md` | 7,596 |
| `docs/ERROR_CHECKLIST.md` | `.md` | 10,730 |
| `docs/METHODOLOGY.md` | `.md` | 33,349 |
| `docs/NOTATION.md` | `.md` | 14,833 |
| `docs/STRUCTURE.md` | `.md` | 7,622 |
| `docs/WORKFLOW.md` | `.md` | 15,033 |
| `docs/audit/PHASE1_SUMMARY.md` | `.md` | 10,485 |
| `docs/audit/README.md` | `.md` | 2,626 |
| `docs/audit/task-07-batch-head-vs-current.txt` | `.txt` | 4,981 |
| `docs/audit/task-07-batch-tracked-vs-rerun.txt` | `.txt` | 4,974 |
| `docs/audit/task-07-window-baseline-vs-current.txt` | `.txt` | 422 |
| `docs/audit/task-09-stats-old-vs-new.txt` | `.txt` | 4,329 |
| `docs/audit/task-10-scenarios-old-vs-new.txt` | `.txt` | 2,538 |
| `docs/audit/task-12-covariance-old-vs-new.txt` | `.txt` | 2,368 |
| `docs/raw/6.24-7.7光钟比对结果处理.docx` | `.docx` | 1,233,472 |
| `docs/raw/6.24-7.7光钟比对结果更新.docx` | `.docx` | 263,722 |
| `docs/raw/8月光钟比对数据处理.docx` | `.docx` | 920,467 |
| `docs/raw/上研院至武汉精测院光纤链路参数及设备安装情况(1).pptx` | `.pptx` | 65,456 |
| `docs/raw/光钟比对数据处理.docx` | `.docx` | 2,944,257 |
| `docs/raw/国内外水准测量标准.zip` | `.zip` | 28,741,848 |
| `docs/raw/比对数据汇总Yb.docx` | `.docx` | 22,243 |
| `docs/raw/潮汐修正后的比值计算.docx` | `.docx` | 2,038,918 |
| `docs/superpowers/plans/2026-10-31-tidal-kalman-probes.md` | `.md` | 13,490 |
| `docs/superpowers/specs/2026-10-30-repo-layering-design.md` | `.md` | 4,835 |
| `docs/实验情况介绍.pptx` | `.pptx` | 1,616,598 |
| `docs/无潮汐修正统计结果.pptx` | `.pptx` | 30,080 |
| `docs/计算参数三组对照.pptx` | `.pptx` | 29,660 |
| `newdata/20250908WH.txt` | `.txt` | 22,298,152 |
| `newdata/251008_1WH.txt` | `.txt` | 21,658,702 |
| `newdata/Freq_B_1_260107_1.txt` | `.txt` | 17,021,422 |
| `newdata/Freq_B_1_260108_1.txt` | `.txt` | 17,021,422 |
| `newdata/Freq_B_1_260109_1.txt` | `.txt` | 17,021,422 |
| `newdata/Freq_B_1_260110_1.txt` | `.txt` | 17,021,422 |
| `newdata/Freq_B_2_260415_1.txt` | `.txt` | 17,021,422 |
| `newdata/Freq_B_2_260416_1.txt` | `.txt` | 17,021,422 |
| `newdata/Freq_B_2_260417_1.txt` | `.txt` | 17,021,422 |
| `newdata/Freq_B_2_260418_1.txt` | `.txt` | 17,021,422 |
| `newdata/Freq_B_2_260419_1.txt` | `.txt` | 17,021,422 |
| `newdata/Freq_B_2_260515_1.txt` | `.txt` | 17,021,422 |
| `newdata/Freq_B_2_260516_1.txt` | `.txt` | 17,021,422 |
| `newdata/Freq_B_2_260517_1.txt` | `.txt` | 17,021,422 |
| `newdata/Freq_B_2_260518_1.txt` | `.txt` | 9,802,948 |
| `newdata/Freq_B_2_260518_3.txt` | `.txt` | 7,209,276 |
| `newdata/Freq_B_2_260519_1.txt` | `.txt` | 17,021,422 |
| `newdata/数据分组.docx` | `.docx` | 21,915 |
| `paper/NATURE_FRAMEWORK.md` | `.md` | 12,732 |
| `paper/README.md` | `.md` | 7,021 |
| `paper/archive/prl-submission-2026-11-02-v2-corrected/CORRECTION_REPORT.md` | `.md` | 6,346 |
| `paper/archive/prl-submission-2026-11-02-v2-corrected/CORRECTION_REPORT.pdf` | `.pdf` | 213,284 |
| `paper/archive/prl-submission-2026-11-02-v2-corrected/STABILITY_IMPROVEMENT.md` | `.md` | 2,708 |
| `paper/archive/prl-submission-2026-11-02-v2-corrected/correction_comparison.pdf` | `.pdf` | 28,903 |
| `paper/archive/prl-submission-2026-11-02-v2-corrected/correction_comparison.png` | `.png` | 139,945 |
| `paper/archive/prl-submission-2026-11-02-v2-corrected/correlation_table.tex` | `.tex` | 733 |
| `paper/archive/prl-submission-2026-11-02-v2-corrected/loo_table.tex` | `.tex` | 871 |
| `paper/archive/prl-submission-2026-11-02-v2-corrected/main.pdf` | `.pdf` | 3,187,292 |
| `paper/archive/prl-submission-2026-11-02-v2-corrected/main.tex` | `.tex` | 25,103 |
| `paper/archive/prl-submission-2026-11-02-v2-corrected/merged_segment_table.tex` | `.tex` | 1,265 |
| `paper/archive/prl-submission-2026-11-02-v2-corrected/numbers.tex` | `.tex` | 5,716 |
| `paper/archive/prl-submission-2026-11-02-v2-corrected/refs.bib` | `.bib` | 34,498 |
| `paper/archive/prl-submission-2026-11-02-v2-corrected/shift_components_table.tex` | `.tex` | 2,165 |
| `paper/archive/prl-submission-2026-11-02-v2-corrected/supplementary.pdf` | `.pdf` | 926,341 |
| `paper/archive/prl-submission-2026-11-02-v2-corrected/supplementary.tex` | `.tex` | 26,441 |
| `paper/main.tex` | `.tex` | 55,019 |
| `paper/main_seg9_excluded.tex` | `.tex` | 55,651 |
| `paper/nature/INDEPENDENT_REVIEW_2026-11-03.md` | `.md` | 14,687 |
| `paper/nature/LOGIC_RESTRUCTURE.md` | `.md` | 8,021 |
| `paper/nature/NATURE_CLAIM.md` | `.md` | 7,247 |
| `paper/nature/PRL_UPDATE_NATURE_PLAN.pptx` | `.pptx` | 1,100,766 |
| `paper/nature/README.md` | `.md` | 8,075 |
| `paper/nature/RESEARCH_SYNTHESIS.md` | `.md` | 21,612 |
| `paper/nature/RESTRUCTURE_CLAIM.md` | `.md` | 5,879 |
| `paper/nature/TOPIC_AND_TITLE.md` | `.md` | 5,562 |
| `paper/nature/europe_twin.aux` | `.aux` | 6,408 |
| `paper/nature/europe_twin.bbl` | `.bbl` | 3,462 |
| `paper/nature/europe_twin.blg` | `.blg` | 1,090 |
| `paper/nature/europe_twin.log` | `.log` | 11,883 |
| `paper/nature/europe_twin.pdf` | `.pdf` | 383,006 |
| `paper/nature/europe_twin.tex` | `.tex` | 22,065 |
| `paper/nature/europe_twin_fig1_per_segment.pdf` | `.pdf` | 31,063 |
| `paper/nature/europe_twin_fig1_per_segment.png` | `.png` | 90,036 |
| `paper/nature/europe_twin_fig2_kalman.pdf` | `.pdf` | 20,596 |
| `paper/nature/europe_twin_fig2_kalman.png` | `.png` | 77,947 |
| `paper/nature/europe_twin_fig3_timedomain.pdf` | `.pdf` | 110,829 |
| `paper/nature/europe_twin_fig3_timedomain.png` | `.png` | 109,695 |
| `paper/nature/europe_twin_fig_processing.pdf` | `.pdf` | 19,309 |
| `paper/nature/europe_twin_fig_processing.png` | `.png` | 68,267 |
| `paper/nature/fig1_abc.pdf` | `.pdf` | 134,633 |
| `paper/nature/fig1_abc.png` | `.png` | 554,304 |
| `paper/nature/fig1_bc_tide.pdf` | `.pdf` | 63,774 |
| `paper/nature/fig1_bc_tide.png` | `.png` | 568,907 |
| `paper/nature/fig1_network.png` | `.png` | 868,235 |
| `paper/nature/fig1a_v7.png` | `.png` | 63,675 |
| `paper/nature/fig2_abc.pdf` | `.pdf` | 35,645 |
| `paper/nature/fig2_abc.png` | `.png` | 241,094 |
| `paper/nature/fig_A_comparison.pdf` | `.pdf` | 19,540 |
| `paper/nature/fig_A_comparison.png` | `.png` | 84,292 |
| `paper/nature/fig_band_admittance.pdf` | `.pdf` | 18,396 |
| `paper/nature/fig_band_admittance.png` | `.png` | 58,750 |
| `paper/nature/fig_cumulative_band_A.pdf` | `.pdf` | 23,870 |
| `paper/nature/fig_cumulative_band_A.png` | `.png` | 136,967 |
| `paper/nature/fig_europe_followup.pdf` | `.pdf` | 28,449 |
| `paper/nature/fig_europe_followup.png` | `.png` | 102,811 |
| `paper/nature/fig_europe_summary.pdf` | `.pdf` | 20,109 |
| `paper/nature/fig_europe_summary.png` | `.png` | 74,071 |
| `paper/nature/fig_method_model.pdf` | `.pdf` | 37,019 |
| `paper/nature/fig_method_model.png` | `.png` | 150,941 |
| `paper/nature/fig_per_campaign_A.pdf` | `.pdf` | 33,820 |
| `paper/nature/fig_per_campaign_A.png` | `.png` | 152,346 |
| `paper/nature/fig_per_campaign_band_A.pdf` | `.pdf` | 21,098 |
| `paper/nature/fig_per_campaign_band_A.png` | `.png` | 144,902 |
| `paper/nature/fig_ratio.pdf` | `.pdf` | 25,329 |
| `paper/nature/fig_ratio.png` | `.png` | 119,672 |
| `paper/nature/fig_ratio_history.pdf` | `.pdf` | 22,570 |
| `paper/nature/fig_ratio_history.png` | `.png` | 91,432 |
| `paper/nature/fig_seasonal_correction.pdf` | `.pdf` | 26,742 |
| `paper/nature/fig_seasonal_correction.png` | `.png` | 173,550 |
| `paper/nature/fig_three_way_A.pdf` | `.pdf` | 18,547 |
| `paper/nature/fig_three_way_A.png` | `.png` | 83,125 |
| `paper/nature/fig_time_domain.pdf` | `.pdf` | 268,328 |
| `paper/nature/fig_time_domain.png` | `.png` | 226,085 |
| `paper/nature/fig_v7_agreement.pdf` | `.pdf` | 23,179 |
| `paper/nature/fig_v7_agreement.png` | `.png` | 137,328 |
| `paper/nature/figs/review-20261103/band_response.pdf` | `.pdf` | 19,073 |
| `paper/nature/figs/review-20261103/baseline_model.pdf` | `.pdf` | 58,895 |
| `paper/nature/figs/review-20261103/response_coverage.pdf` | `.pdf` | 22,906 |
| `paper/nature/figs/review-20261103/spectrum_correction.pdf` | `.pdf` | 61,896 |
| `paper/nature/independent-concurrent-revision-20261103/README.md` | `.md` | 805 |
| `paper/nature/independent-concurrent-revision-20261103/REVISION_PLAN.md` | `.md` | 18,461 |
| `paper/nature/independent-concurrent-revision-20261103/REVISION_PLAN.pdf` | `.pdf` | 117,334 |
| `paper/nature/independent-concurrent-revision-20261103/build_document.py` | `.py` | 1,274 |
| `paper/nature/independent-concurrent-revision-20261103/local/page-1.png` | `.png` | 131,586 |
| `paper/nature/independent-concurrent-revision-20261103/local/page-2.png` | `.png` | 94,260 |
| `paper/nature/independent-concurrent-revision-20261103/local/page-6.png` | `.png` | 103,497 |
| `paper/nature/independent-concurrent-revision-20261103/manifest.json` | `.json` | 843 |
| `paper/nature/lomb_scargle_prem.pdf` | `.pdf` | 58,011 |
| `paper/nature/lomb_scargle_prem.png` | `.png` | 199,131 |
| `paper/nature/lunar-independent-v14-20261103/BRIEF.md` | `.md` | 2,440 |
| `paper/nature/lunar-independent-v14-20261103/CHECKSUMS.sha256` | `.sha256` | 7,694 |
| `paper/nature/lunar-independent-v14-20261103/README.md` | `.md` | 4,159 |
| `paper/nature/lunar-independent-v14-20261103/VALIDATION.md` | `.md` | 5,892 |
| `paper/nature/lunar-independent-v14-20261103/abstract.tex` | `.tex` | 1,371 |
| `paper/nature/lunar-independent-v14-20261103/body.tex` | `.tex` | 12,193 |
| `paper/nature/lunar-independent-v14-20261103/captions-summary.md` | `.md` | 4,323 |
| `paper/nature/lunar-independent-v14-20261103/captions.tex` | `.tex` | 3,381 |
| `paper/nature/lunar-independent-v14-20261103/extended.tex` | `.tex` | 4,733 |
| `paper/nature/lunar-independent-v14-20261103/figure-qc.md` | `.md` | 10,964 |
| `paper/nature/lunar-independent-v14-20261103/figures/ed1.collision-audit.json` | `.json` | 557 |
| `paper/nature/lunar-independent-v14-20261103/figures/ed1.pdf` | `.pdf` | 39,256 |
| `paper/nature/lunar-independent-v14-20261103/figures/ed1.png` | `.png` | 52,648 |
| `paper/nature/lunar-independent-v14-20261103/figures/ed1.svg` | `.svg` | 62,749 |
| `paper/nature/lunar-independent-v14-20261103/figures/ed1.visible-text-audit.json` | `.json` | 416 |
| `paper/nature/lunar-independent-v14-20261103/figures/ed2.collision-audit.json` | `.json` | 557 |
| `paper/nature/lunar-independent-v14-20261103/figures/ed2.pdf` | `.pdf` | 38,336 |
| `paper/nature/lunar-independent-v14-20261103/figures/ed2.png` | `.png` | 37,690 |
| `paper/nature/lunar-independent-v14-20261103/figures/ed2.svg` | `.svg` | 67,798 |
| `paper/nature/lunar-independent-v14-20261103/figures/ed2.visible-text-audit.json` | `.json` | 418 |
| `paper/nature/lunar-independent-v14-20261103/figures/ed3.collision-audit.json` | `.json` | 557 |
| `paper/nature/lunar-independent-v14-20261103/figures/ed3.pdf` | `.pdf` | 38,901 |
| `paper/nature/lunar-independent-v14-20261103/figures/ed3.png` | `.png` | 93,777 |
| `paper/nature/lunar-independent-v14-20261103/figures/ed3.svg` | `.svg` | 73,821 |
| `paper/nature/lunar-independent-v14-20261103/figures/ed3.visible-text-audit.json` | `.json` | 419 |
| `paper/nature/lunar-independent-v14-20261103/figures/ed4.collision-audit.json` | `.json` | 1,159 |
| `paper/nature/lunar-independent-v14-20261103/figures/ed4.pdf` | `.pdf` | 47,290 |
| `paper/nature/lunar-independent-v14-20261103/figures/ed4.png` | `.png` | 148,032 |
| `paper/nature/lunar-independent-v14-20261103/figures/ed4.svg` | `.svg` | 178,135 |
| `paper/nature/lunar-independent-v14-20261103/figures/ed4.visible-text-audit.json` | `.json` | 523 |
| `paper/nature/lunar-independent-v14-20261103/figures/fig1.alignment.json` | `.json` | 1,334 |
| `paper/nature/lunar-independent-v14-20261103/figures/fig1.alignment.svg` | `.svg` | 731 |
| `paper/nature/lunar-independent-v14-20261103/figures/fig1.bundle-qc.json` | `.json` | 2,258 |
| `paper/nature/lunar-independent-v14-20261103/figures/fig1.collision-audit.json` | `.json` | 558 |
| `paper/nature/lunar-independent-v14-20261103/figures/fig1.pdf` | `.pdf` | 23,683 |
| `paper/nature/lunar-independent-v14-20261103/figures/fig1.png` | `.png` | 320,404 |
| `paper/nature/lunar-independent-v14-20261103/figures/fig1.source-audit.json` | `.json` | 3,860 |
| `paper/nature/lunar-independent-v14-20261103/figures/fig1.svg` | `.svg` | 25,271 |
| `paper/nature/lunar-independent-v14-20261103/figures/fig1.text-audit.json` | `.json` | 278 |
| `paper/nature/lunar-independent-v14-20261103/figures/fig1.visible-text-audit.json` | `.json` | 389 |
| `paper/nature/lunar-independent-v14-20261103/figures/fig2.collision-audit.json` | `.json` | 558 |
| `paper/nature/lunar-independent-v14-20261103/figures/fig2.pdf` | `.pdf` | 66,290 |
| `paper/nature/lunar-independent-v14-20261103/figures/fig2.png` | `.png` | 123,839 |
| `paper/nature/lunar-independent-v14-20261103/figures/fig2.svg` | `.svg` | 85,788 |
| `paper/nature/lunar-independent-v14-20261103/figures/fig2.visible-text-audit.json` | `.json` | 419 |
| `paper/nature/lunar-independent-v14-20261103/figures/fig3.alignment.json` | `.json` | 809 |
| `paper/nature/lunar-independent-v14-20261103/figures/fig3.alignment.svg` | `.svg` | 534 |
| `paper/nature/lunar-independent-v14-20261103/figures/fig3.collision-audit.json` | `.json` | 558 |
| `paper/nature/lunar-independent-v14-20261103/figures/fig3.pdf` | `.pdf` | 24,539 |
| `paper/nature/lunar-independent-v14-20261103/figures/fig3.png` | `.png` | 262,298 |
| `paper/nature/lunar-independent-v14-20261103/figures/fig3.svg` | `.svg` | 15,773 |
| `paper/nature/lunar-independent-v14-20261103/figures/fig3.text-audit.json` | `.json` | 278 |
| `paper/nature/lunar-independent-v14-20261103/figures/fig3.visible-text-audit.json` | `.json` | 387 |
| `paper/nature/lunar-independent-v14-20261103/figures/fig4.alignment.json` | `.json` | 809 |
| `paper/nature/lunar-independent-v14-20261103/figures/fig4.alignment.svg` | `.svg` | 534 |
| `paper/nature/lunar-independent-v14-20261103/figures/fig4.collision-audit.json` | `.json` | 558 |
| `paper/nature/lunar-independent-v14-20261103/figures/fig4.pdf` | `.pdf` | 27,957 |
| `paper/nature/lunar-independent-v14-20261103/figures/fig4.png` | `.png` | 234,537 |
| `paper/nature/lunar-independent-v14-20261103/figures/fig4.svg` | `.svg` | 13,175 |
| `paper/nature/lunar-independent-v14-20261103/figures/fig4.text-audit.json` | `.json` | 278 |
| `paper/nature/lunar-independent-v14-20261103/figures/fig4.visible-text-audit.json` | `.json` | 388 |
| `paper/nature/lunar-independent-v14-20261103/local/build-0.log` | `.log` | 8,035 |
| `paper/nature/lunar-independent-v14-20261103/local/build-1.log` | `.log` | 7,418 |
| `paper/nature/lunar-independent-v14-20261103/local/build-2.log` | `.log` | 7,418 |
| `paper/nature/lunar-independent-v14-20261103/local/build-first.log` | `.log` | 12,054 |
| `paper/nature/lunar-independent-v14-20261103/local/clean-bundle-build-0.log` | `.log` | 12,158 |
| `paper/nature/lunar-independent-v14-20261103/local/clean-bundle-build-1.log` | `.log` | 7,418 |
| `paper/nature/lunar-independent-v14-20261103/local/contact-1.png` | `.png` | 425,497 |
| `paper/nature/lunar-independent-v14-20261103/local/contact-2.png` | `.png` | 525,475 |
| `paper/nature/lunar-independent-v14-20261103/local/contact-3.png` | `.png` | 50,526 |
| `paper/nature/lunar-independent-v14-20261103/local/delivery-build-0.log` | `.log` | 7,418 |
| `paper/nature/lunar-independent-v14-20261103/local/delivery-build-1.log` | `.log` | 7,418 |
| `paper/nature/lunar-independent-v14-20261103/local/ed1.collision.json` | `.json` | 482 |
| `paper/nature/lunar-independent-v14-20261103/local/ed2.collision.json` | `.json` | 482 |
| `paper/nature/lunar-independent-v14-20261103/local/ed3-final.png` | `.png` | 59,400 |
| `paper/nature/lunar-independent-v14-20261103/local/ed3.collision.json` | `.json` | 482 |
| `paper/nature/lunar-independent-v14-20261103/local/ed4.collision.json` | `.json` | 1,081 |
| `paper/nature/lunar-independent-v14-20261103/local/ed4.collision.pdf` | `.pdf` | 47,587 |
| `paper/nature/lunar-independent-v14-20261103/local/fig2.collision.json` | `.json` | 483 |
| `paper/nature/lunar-independent-v14-20261103/local/final-build-0.log` | `.log` | 7,418 |
| `paper/nature/lunar-independent-v14-20261103/local/final-build-1.log` | `.log` | 7,418 |
| `paper/nature/lunar-independent-v14-20261103/local/final-page-1.png` | `.png` | 226,359 |
| `paper/nature/lunar-independent-v14-20261103/local/final-page-10.png` | `.png` | 178,783 |
| `paper/nature/lunar-independent-v14-20261103/local/final-page-11.png` | `.png` | 91,744 |
| `paper/nature/lunar-independent-v14-20261103/local/final-page-12.png` | `.png` | 110,696 |
| `paper/nature/lunar-independent-v14-20261103/local/final-page-13.png` | `.png` | 94,098 |
| `paper/nature/lunar-independent-v14-20261103/local/final-page-4.png` | `.png` | 121,106 |
| `paper/nature/lunar-independent-v14-20261103/local/final-page-7.png` | `.png` | 224,264 |
| `paper/nature/lunar-independent-v14-20261103/local/intermediate-retained-panel-qa.json` | `.json` | 4,078 |
| `paper/nature/lunar-independent-v14-20261103/local/ne_50m_coastline.zip` | `.zip` | 455,936 |
| `paper/nature/lunar-independent-v14-20261103/local/ne_50m_land.zip` | `.zip` | 457,183 |
| `paper/nature/lunar-independent-v14-20261103/local/superseded-ed1.collision.json` | `.json` | 1,093 |
| `paper/nature/lunar-independent-v14-20261103/local/superseded-ed1.text-audit.json` | `.json` | 245 |
| `paper/nature/lunar-independent-v14-20261103/local/superseded-ed2.collision.json` | `.json` | 526 |
| `paper/nature/lunar-independent-v14-20261103/local/superseded-ed2.text-audit.json` | `.json` | 1,417 |
| `paper/nature/lunar-independent-v14-20261103/local/superseded-ed3.collision.json` | `.json` | 1,110 |
| `paper/nature/lunar-independent-v14-20261103/local/superseded-ed3.text-audit.json` | `.json` | 320 |
| `paper/nature/lunar-independent-v14-20261103/local/superseded-ed4.collision.json` | `.json` | 1,125 |
| `paper/nature/lunar-independent-v14-20261103/local/superseded-ed4.text-audit.json` | `.json` | 1,499 |
| `paper/nature/lunar-independent-v14-20261103/local/superseded-fig1.collision-audit.pdf` | `.pdf` | 24,219 |
| `paper/nature/lunar-independent-v14-20261103/local/superseded-fig2.collision.json` | `.json` | 527 |
| `paper/nature/lunar-independent-v14-20261103/local/superseded-fig2.text-audit.json` | `.json` | 321 |
| `paper/nature/lunar-independent-v14-20261103/main.aux` | `.aux` | 18,766 |
| `paper/nature/lunar-independent-v14-20261103/main.log` | `.log` | 27,107 |
| `paper/nature/lunar-independent-v14-20261103/main.out` | `.out` | 0 |
| `paper/nature/lunar-independent-v14-20261103/main.pdf` | `.pdf` | 588,549 |
| `paper/nature/lunar-independent-v14-20261103/main.tex` | `.tex` | 2,027 |
| `paper/nature/lunar-independent-v14-20261103/manuscript-source.zip` | `.zip` | 2,998,642 |
| `paper/nature/lunar-independent-v14-20261103/method-notes.md` | `.md` | 14,354 |
| `paper/nature/lunar-independent-v14-20261103/methods.tex` | `.tex` | 14,934 |
| `paper/nature/lunar-independent-v14-20261103/numbers.tex` | `.tex` | 487 |
| `paper/nature/lunar-independent-v14-20261103/prose-notes.md` | `.md` | 10,761 |
| `paper/nature/lunar-independent-v14-20261103/references.tex` | `.tex` | 3,735 |
| `paper/nature/lunar-independent-v14-20261103/source-data/basemap/ne_50m_coastline.cpg` | `.cpg` | 5 |
| `paper/nature/lunar-independent-v14-20261103/source-data/basemap/ne_50m_coastline.dbf` | `.dbf` | 70,101 |
| `paper/nature/lunar-independent-v14-20261103/source-data/basemap/ne_50m_coastline.prj` | `.prj` | 143 |
| `paper/nature/lunar-independent-v14-20261103/source-data/basemap/ne_50m_coastline.shp` | `.shp` | 1,046,728 |
| `paper/nature/lunar-independent-v14-20261103/source-data/basemap/ne_50m_coastline.shx` | `.shx` | 11,524 |
| `paper/nature/lunar-independent-v14-20261103/source-data/basemap/ne_50m_land.cpg` | `.cpg` | 5 |
| `paper/nature/lunar-independent-v14-20261103/source-data/basemap/ne_50m_land.dbf` | `.dbf` | 69,709 |
| `paper/nature/lunar-independent-v14-20261103/source-data/basemap/ne_50m_land.prj` | `.prj` | 143 |
| `paper/nature/lunar-independent-v14-20261103/source-data/basemap/ne_50m_land.shp` | `.shp` | 1,050,332 |
| `paper/nature/lunar-independent-v14-20261103/source-data/basemap/ne_50m_land.shx` | `.shx` | 11,460 |
| `paper/nature/lunar-independent-v14-20261103/source-data/edition-qc.json` | `.json` | 4,632 |
| `paper/nature/lunar-independent-v14-20261103/source-data/model-and-estimates.json` | `.json` | 9,653 |
| `paper/nature/lunar-independent-v14-20261103/source-data/retained-panel-provenance.json` | `.json` | 3,170 |
| `paper/nature/lunar-independent-v14-20261103/tools/build_numbers.py` | `.py` | 916 |
| `paper/nature/lunar-independent-v14-20261103/tools/check_edition.py` | `.py` | 4,017 |
| `paper/nature/lunar-independent-v14-20261103/tools/package_source.py` | `.py` | 875 |
| `paper/nature/lunar-independent-v14-20261103/tools/plot_summary.py` | `.py` | 14,739 |
| `paper/nature/lunar-independent-v14-20261103/tools/retain_author_panels.py` | `.py` | 4,997 |
| `paper/nature/lunar-measured-v7-20261103/AUTHOR_DECISION.md` | `.md` | 13,449 |
| `paper/nature/lunar-measured-v7-20261103/HANDOFF.md` | `.md` | 7,867 |
| `paper/nature/lunar-measured-v7-20261103/README.md` | `.md` | 4,820 |
| `paper/nature/lunar-measured-v7-20261103/VALIDATION.md` | `.md` | 5,296 |
| `paper/nature/lunar-measured-v7-20261103/body.tex` | `.tex` | 12,132 |
| `paper/nature/lunar-measured-v7-20261103/captions.tex` | `.tex` | 3,407 |
| `paper/nature/lunar-measured-v7-20261103/document-validation.json` | `.json` | 732 |
| `paper/nature/lunar-measured-v7-20261103/evidence.json` | `.json` | 3,438 |
| `paper/nature/lunar-measured-v7-20261103/extended.tex` | `.tex` | 3,108 |
| `paper/nature/lunar-measured-v7-20261103/figures/Fig1.alignment.json` | `.json` | 2,345 |
| `paper/nature/lunar-measured-v7-20261103/figures/Fig1.collision.json` | `.json` | 1,096 |
| `paper/nature/lunar-measured-v7-20261103/figures/Fig1.pdf` | `.pdf` | 36,974 |
| `paper/nature/lunar-measured-v7-20261103/figures/Fig1.png` | `.png` | 166,043 |
| `paper/nature/lunar-measured-v7-20261103/figures/Fig2.alignment.json` | `.json` | 1,605 |
| `paper/nature/lunar-measured-v7-20261103/figures/Fig2.collision.json` | `.json` | 519 |
| `paper/nature/lunar-measured-v7-20261103/figures/Fig2.pdf` | `.pdf` | 18,655 |
| `paper/nature/lunar-measured-v7-20261103/figures/Fig2.png` | `.png` | 63,057 |
| `paper/nature/lunar-measured-v7-20261103/figures/Fig3.alignment.json` | `.json` | 1,610 |
| `paper/nature/lunar-measured-v7-20261103/figures/Fig3.collision.json` | `.json` | 523 |
| `paper/nature/lunar-measured-v7-20261103/figures/Fig3.pdf` | `.pdf` | 19,224 |
| `paper/nature/lunar-measured-v7-20261103/figures/Fig3.png` | `.png` | 77,353 |
| `paper/nature/lunar-measured-v7-20261103/figures/Fig4.alignment.json` | `.json` | 1,072 |
| `paper/nature/lunar-measured-v7-20261103/figures/Fig4.collision.json` | `.json` | 519 |
| `paper/nature/lunar-measured-v7-20261103/figures/Fig4.pdf` | `.pdf` | 18,415 |
| `paper/nature/lunar-measured-v7-20261103/figures/Fig4.png` | `.png` | 48,098 |
| `paper/nature/lunar-measured-v7-20261103/main.aux` | `.aux` | 8,400 |
| `paper/nature/lunar-measured-v7-20261103/main.bbl` | `.bbl` | 3,030 |
| `paper/nature/lunar-measured-v7-20261103/main.blg` | `.blg` | 893 |
| `paper/nature/lunar-measured-v7-20261103/main.log` | `.log` | 27,000 |
| `paper/nature/lunar-measured-v7-20261103/main.out` | `.out` | 0 |
| `paper/nature/lunar-measured-v7-20261103/main.pdf` | `.pdf` | 432,860 |
| `paper/nature/lunar-measured-v7-20261103/main.tex` | `.tex` | 3,746 |
| `paper/nature/lunar-measured-v7-20261103/methods.tex` | `.tex` | 14,958 |
| `paper/nature/lunar-measured-v7-20261103/numbers.tex` | `.tex` | 2,025 |
| `paper/nature/lunar-measured-v7-20261103/refs.bib` | `.bib` | 2,992 |
| `paper/nature/lunar-measured-v7-20261103/source-data/Fig1.csv` | `.csv` | 552 |
| `paper/nature/lunar-measured-v7-20261103/source-data/Fig2.csv` | `.csv` | 171 |
| `paper/nature/lunar-measured-v7-20261103/source-data/Fig3.csv` | `.csv` | 884 |
| `paper/nature/lunar-measured-v7-20261103/source-data/Fig4.csv` | `.csv` | 330 |
| `paper/nature/lunar-measured-v7-20261103/source-data/v7-qc-status.json` | `.json` | 177 |
| `paper/nature/lunar-measured-v7-20261103/status.tex` | `.tex` | 4,080 |
| `paper/nature/lunar-measured-v7-20261103/tools/build_draft.py` | `.py` | 12,823 |
| `paper/nature/lunar-measured-v7-20261103/tools/check_document.py` | `.py` | 3,277 |
| `paper/nature/lunar-measured-v7-figure-pass-20261103/README.md` | `.md` | 4,888 |
| `paper/nature/lunar-measured-v7-figure-pass-20261103/body.tex` | `.tex` | 12,249 |
| `paper/nature/lunar-measured-v7-figure-pass-20261103/captions.tex` | `.tex` | 3,531 |
| `paper/nature/lunar-measured-v7-figure-pass-20261103/document-validation.json` | `.json` | 954 |
| `paper/nature/lunar-measured-v7-figure-pass-20261103/evidence.json` | `.json` | 3,438 |
| `paper/nature/lunar-measured-v7-figure-pass-20261103/extended.tex` | `.tex` | 3,242 |
| `paper/nature/lunar-measured-v7-figure-pass-20261103/figures/ExtendedDataFig1.collision.json` | `.json` | 547 |
| `paper/nature/lunar-measured-v7-figure-pass-20261103/figures/ExtendedDataFig1.pdf` | `.pdf` | 13,657 |
| `paper/nature/lunar-measured-v7-figure-pass-20261103/figures/ExtendedDataFig1.png` | `.png` | 52,401 |
| `paper/nature/lunar-measured-v7-figure-pass-20261103/figures/ExtendedDataFig1.svg` | `.svg` | 8,663 |
| `paper/nature/lunar-measured-v7-figure-pass-20261103/figures/ExtendedDataFig2.alignment.json` | `.json` | 1,606 |
| `paper/nature/lunar-measured-v7-figure-pass-20261103/figures/ExtendedDataFig2.collision.json` | `.json` | 547 |
| `paper/nature/lunar-measured-v7-figure-pass-20261103/figures/ExtendedDataFig2.pdf` | `.pdf` | 19,473 |
| `paper/nature/lunar-measured-v7-figure-pass-20261103/figures/ExtendedDataFig2.png` | `.png` | 85,635 |
| `paper/nature/lunar-measured-v7-figure-pass-20261103/figures/ExtendedDataFig2.svg` | `.svg` | 19,520 |
| `paper/nature/lunar-measured-v7-figure-pass-20261103/figures/Fig1.alignment.json` | `.json` | 2,345 |
| `paper/nature/lunar-measured-v7-figure-pass-20261103/figures/Fig1.collision.json` | `.json` | 536 |
| `paper/nature/lunar-measured-v7-figure-pass-20261103/figures/Fig1.pdf` | `.pdf` | 41,645 |
| `paper/nature/lunar-measured-v7-figure-pass-20261103/figures/Fig1.png` | `.png` | 198,882 |
| `paper/nature/lunar-measured-v7-figure-pass-20261103/figures/Fig1.svg` | `.svg` | 53,321 |
| `paper/nature/lunar-measured-v7-figure-pass-20261103/figures/Fig2.alignment.json` | `.json` | 1,605 |
| `paper/nature/lunar-measured-v7-figure-pass-20261103/figures/Fig2.collision.json` | `.json` | 532 |
| `paper/nature/lunar-measured-v7-figure-pass-20261103/figures/Fig2.pdf` | `.pdf` | 22,367 |
| `paper/nature/lunar-measured-v7-figure-pass-20261103/figures/Fig2.png` | `.png` | 62,479 |
| `paper/nature/lunar-measured-v7-figure-pass-20261103/figures/Fig2.svg` | `.svg` | 2,767 |
| `paper/nature/lunar-measured-v7-figure-pass-20261103/figures/Fig3.alignment.json` | `.json` | 1,610 |
| `paper/nature/lunar-measured-v7-figure-pass-20261103/figures/Fig3.collision.json` | `.json` | 535 |
| `paper/nature/lunar-measured-v7-figure-pass-20261103/figures/Fig3.pdf` | `.pdf` | 19,224 |
| `paper/nature/lunar-measured-v7-figure-pass-20261103/figures/Fig3.png` | `.png` | 77,353 |
| `paper/nature/lunar-measured-v7-figure-pass-20261103/figures/Fig3.svg` | `.svg` | 22,321 |
| `paper/nature/lunar-measured-v7-figure-pass-20261103/figures/Fig4.alignment.json` | `.json` | 940 |
| `paper/nature/lunar-measured-v7-figure-pass-20261103/figures/Fig4.collision.json` | `.json` | 535 |
| `paper/nature/lunar-measured-v7-figure-pass-20261103/figures/Fig4.pdf` | `.pdf` | 16,618 |
| `paper/nature/lunar-measured-v7-figure-pass-20261103/figures/Fig4.png` | `.png` | 48,036 |
| `paper/nature/lunar-measured-v7-figure-pass-20261103/figures/Fig4.svg` | `.svg` | 11,607 |
| `paper/nature/lunar-measured-v7-figure-pass-20261103/main-data-review-20261103.aux` | `.aux` | 10,844 |
| `paper/nature/lunar-measured-v7-figure-pass-20261103/main-data-review-20261103.bbl` | `.bbl` | 4,244 |
| `paper/nature/lunar-measured-v7-figure-pass-20261103/main-data-review-20261103.blg` | `.blg` | 923 |
| `paper/nature/lunar-measured-v7-figure-pass-20261103/main-data-review-20261103.log` | `.log` | 30,145 |
| `paper/nature/lunar-measured-v7-figure-pass-20261103/main-data-review-20261103.out` | `.out` | 0 |
| `paper/nature/lunar-measured-v7-figure-pass-20261103/main-data-review-20261103.pdf` | `.pdf` | 494,289 |
| `paper/nature/lunar-measured-v7-figure-pass-20261103/main-four-figures-20261103.aux` | `.aux` | 9,133 |
| `paper/nature/lunar-measured-v7-figure-pass-20261103/main-four-figures-20261103.bbl` | `.bbl` | 4,244 |
| `paper/nature/lunar-measured-v7-figure-pass-20261103/main-four-figures-20261103.blg` | `.blg` | 924 |
| `paper/nature/lunar-measured-v7-figure-pass-20261103/main-four-figures-20261103.log` | `.log` | 28,402 |
| `paper/nature/lunar-measured-v7-figure-pass-20261103/main-four-figures-20261103.out` | `.out` | 0 |
| `paper/nature/lunar-measured-v7-figure-pass-20261103/main-four-figures-20261103.pdf` | `.pdf` | 464,562 |
| `paper/nature/lunar-measured-v7-figure-pass-20261103/main-lunar-measured-20261103.aux` | `.aux` | 10,885 |
| `paper/nature/lunar-measured-v7-figure-pass-20261103/main-lunar-measured-20261103.bbl` | `.bbl` | 4,244 |
| `paper/nature/lunar-measured-v7-figure-pass-20261103/main-lunar-measured-20261103.blg` | `.blg` | 926 |
| `paper/nature/lunar-measured-v7-figure-pass-20261103/main-lunar-measured-20261103.log` | `.log` | 30,801 |
| `paper/nature/lunar-measured-v7-figure-pass-20261103/main-lunar-measured-20261103.out` | `.out` | 0 |
| `paper/nature/lunar-measured-v7-figure-pass-20261103/main-lunar-measured-20261103.pdf` | `.pdf` | 514,988 |
| `paper/nature/lunar-measured-v7-figure-pass-20261103/main-reconstructed-20261103.aux` | `.aux` | 10,885 |
| `paper/nature/lunar-measured-v7-figure-pass-20261103/main-reconstructed-20261103.bbl` | `.bbl` | 4,244 |
| `paper/nature/lunar-measured-v7-figure-pass-20261103/main-reconstructed-20261103.blg` | `.blg` | 925 |
| `paper/nature/lunar-measured-v7-figure-pass-20261103/main-reconstructed-20261103.log` | `.log` | 30,792 |
| `paper/nature/lunar-measured-v7-figure-pass-20261103/main-reconstructed-20261103.out` | `.out` | 0 |
| `paper/nature/lunar-measured-v7-figure-pass-20261103/main-reconstructed-20261103.pdf` | `.pdf` | 513,642 |
| `paper/nature/lunar-measured-v7-figure-pass-20261103/main.aux` | `.aux` | 10,844 |
| `paper/nature/lunar-measured-v7-figure-pass-20261103/main.bbl` | `.bbl` | 4,244 |
| `paper/nature/lunar-measured-v7-figure-pass-20261103/main.blg` | `.blg` | 902 |
| `paper/nature/lunar-measured-v7-figure-pass-20261103/main.log` | `.log` | 29,955 |
| `paper/nature/lunar-measured-v7-figure-pass-20261103/main.out` | `.out` | 0 |
| `paper/nature/lunar-measured-v7-figure-pass-20261103/main.pdf` | `.pdf` | 494,284 |
| `paper/nature/lunar-measured-v7-figure-pass-20261103/main.tex` | `.tex` | 3,715 |
| `paper/nature/lunar-measured-v7-figure-pass-20261103/methods.tex` | `.tex` | 16,129 |
| `paper/nature/lunar-measured-v7-figure-pass-20261103/numbers.tex` | `.tex` | 2,025 |
| `paper/nature/lunar-measured-v7-figure-pass-20261103/refs.bib` | `.bib` | 4,313 |
| `paper/nature/lunar-measured-v7-figure-pass-20261103/source-data/ExtendedDataFig1.csv` | `.csv` | 217 |
| `paper/nature/lunar-measured-v7-figure-pass-20261103/source-data/ExtendedDataFig2.csv` | `.csv` | 1,286 |
| `paper/nature/lunar-measured-v7-figure-pass-20261103/source-data/Fig1.csv` | `.csv` | 1,041 |
| `paper/nature/lunar-measured-v7-figure-pass-20261103/source-data/Fig2.csv` | `.csv` | 171 |
| `paper/nature/lunar-measured-v7-figure-pass-20261103/source-data/Fig3.csv` | `.csv` | 884 |
| `paper/nature/lunar-measured-v7-figure-pass-20261103/source-data/Fig4.csv` | `.csv` | 368 |
| `paper/nature/lunar-measured-v7-figure-pass-20261103/source-data/v7-qc-status.json` | `.json` | 177 |
| `paper/nature/lunar-measured-v7-figure-pass-20261103/status.tex` | `.tex` | 4,830 |
| `paper/nature/lunar-measured-v7-figure-pass-20261103/tools/build_draft.py` | `.py` | 21,144 |
| `paper/nature/lunar-measured-v7-figure-pass-20261103/tools/check_document.py` | `.py` | 3,889 |
| `paper/nature/lunar-measured-v7-figure-pass-20261103/tools/test_build_draft.py` | `.py` | 2,472 |
| `paper/nature/main.aux` | `.aux` | 7,408 |
| `paper/nature/main.bbl` | `.bbl` | 6,019 |
| `paper/nature/main.blg` | `.blg` | 1,393 |
| `paper/nature/main.log` | `.log` | 12,569 |
| `paper/nature/main.pdf` | `.pdf` | 1,391,735 |
| `paper/nature/main.tex` | `.tex` | 19,629 |
| `paper/nature/numbers_review.tex` | `.tex` | 1,421 |
| `paper/nature/preview-4plus2-20261103/DESIGN.md` | `.md` | 5,119 |
| `paper/nature/preview-4plus2-20261103/PLAN.md` | `.md` | 3,770 |
| `paper/nature/preview-4plus2-20261103/tools/build_preview.py` | `.py` | 23,590 |
| `paper/nature/preview-4plus2-20261103/tools/test_build_preview.py` | `.py` | 2,094 |
| `paper/nature/refs.bib` | `.bib` | 10,342 |
| `paper/nature/review/POLICY_AND_SCOPE.md` | `.md` | 3,438 |
| `paper/nature/review/ROUND1_RESPONSE.md` | `.md` | 4,639 |
| `paper/nature/review/ROUND1_REVIEW.md` | `.md` | 8,755 |
| `paper/nature/review/ROUND2_RESPONSE.md` | `.md` | 4,413 |
| `paper/nature/review/ROUND2_REVIEW.md` | `.md` | 3,691 |
| `paper/nature/review/VALIDATION.md` | `.md` | 5,259 |
| `paper/nature/review/figure_build_manifest.json` | `.json` | 1,671 |
| `paper/nature/review/final_snapshot.json` | `.json` | 2,153 |
| `paper/nature/review/round1_snapshot.json` | `.json` | 1,497 |
| `paper/nature/supplementary.aux` | `.aux` | 2,264 |
| `paper/nature/supplementary.log` | `.log` | 9,918 |
| `paper/nature/supplementary.pdf` | `.pdf` | 160,701 |
| `paper/nature/supplementary.tex` | `.tex` | 7,949 |
| `paper/nature/supplementary.toc` | `.toc` | 990 |
| `paper/nature/supplementary_twin.aux` | `.aux` | 3,083 |
| `paper/nature/supplementary_twin.log` | `.log` | 10,918 |
| `paper/nature/supplementary_twin.pdf` | `.pdf` | 208,445 |
| `paper/nature/supplementary_twin.tex` | `.tex` | 16,041 |
| `paper/nature/tables/review_month_table.tex` | `.tex` | 351 |
| `paper/nature/tables/review_segment_table.tex` | `.tex` | 3,451 |
| `paper/nature/tools/build_review.py` | `.py` | 12,991 |
| `paper/overleaf-prl.zip` | `.zip` | 3,589,240 |
| `paper/overleaf-prl/correlation_table.tex` | `.tex` | 733 |
| `paper/overleaf-prl/figs/fig1_network.png` | `.png` | 2,326,084 |
| `paper/overleaf-prl/figs/fig2_ratio.png` | `.png` | 333,820 |
| `paper/overleaf-prl/figs/fig3_history.png` | `.png` | 186,156 |
| `paper/overleaf-prl/figs/fig5_spliced_stability.png` | `.png` | 156,915 |
| `paper/overleaf-prl/figs/figSI_fit_grid.png` | `.png` | 435,396 |
| `paper/overleaf-prl/figs/fig_method_setup_a3p.pdf` | `.pdf` | 300,709 |
| `paper/overleaf-prl/figs/fig_methods_forest.png` | `.png` | 79,591 |
| `paper/overleaf-prl/loo_table.tex` | `.tex` | 871 |
| `paper/overleaf-prl/main.tex` | `.tex` | 24,995 |
| `paper/overleaf-prl/merged_segment_table.tex` | `.tex` | 1,265 |
| `paper/overleaf-prl/numbers.tex` | `.tex` | 5,715 |
| `paper/overleaf-prl/refs.bib` | `.bib` | 34,498 |
| `paper/overleaf-prl/shift_components_table.tex` | `.tex` | 2,165 |
| `paper/overleaf-prl/supplementary.tex` | `.tex` | 26,343 |
| `paper/overleaf-rev2-v2/figs/fig1_network.png` | `.png` | 868,235 |
| `paper/overleaf-rev2-v2/figs/fig2_ratio.png` | `.png` | 347,177 |
| `paper/overleaf-rev2-v2/figs/fig3_history.png` | `.png` | 186,156 |
| `paper/overleaf-rev2-v2/figs/fig5_spliced_stability.pdf` | `.pdf` | 28,720 |
| `paper/overleaf-rev2-v2/figs/fig5_spliced_stability.png` | `.png` | 208,548 |
| `paper/overleaf-rev2-v2/figs/fig_method_setup_a3p.pdf` | `.pdf` | 298,249 |
| `paper/overleaf-rev2-v2/figs/fig_methods_forest.pdf` | `.pdf` | 21,869 |
| `paper/overleaf-rev2-v2/figs/fig_methods_forest.png` | `.png` | 68,793 |
| `paper/overleaf-rev2-v2/generated/concat_stability_table.tex` | `.tex` | 638 |
| `paper/overleaf-rev2-v2/generated/correlation_table.tex` | `.tex` | 733 |
| `paper/overleaf-rev2-v2/generated/loo_table.tex` | `.tex` | 785 |
| `paper/overleaf-rev2-v2/generated/numbers.json` | `.json` | 4,608 |
| `paper/overleaf-rev2-v2/generated/numbers.tex` | `.tex` | 5,661 |
| `paper/overleaf-rev2-v2/generated/numbers_manifest.json` | `.json` | 18,047 |
| `paper/overleaf-rev2-v2/generated/ratio_intermediates.tex` | `.tex` | 1,282 |
| `paper/overleaf-rev2-v2/generated/sample_ledger_table.tex` | `.tex` | 907 |
| `paper/overleaf-rev2-v2/generated/segment_table.tex` | `.tex` | 827 |
| `paper/overleaf-rev2-v2/generated/shift_components_table.tex` | `.tex` | 1,270 |
| `paper/overleaf-rev2-v2/generated/tidal_synthesis_table.tex` | `.tex` | 336 |
| `paper/overleaf-rev2-v2/main.tex` | `.tex` | 44,339 |
| `paper/overleaf-rev2-v2/refs.bib` | `.bib` | 33,922 |
| `paper/overleaf-rev2-v2/supplementary.tex` | `.tex` | 15,690 |
| `paper/overleaf/README.md` | `.md` | 1,849 |
| `paper/overleaf/figs/1.png` | `.png` | 184,175 |
| `paper/overleaf/figs/2.png` | `.png` | 514,717 |
| `paper/overleaf/figs/3.png` | `.png` | 399,608 |
| `paper/overleaf/figs/4.png` | `.png` | 87,314 |
| `paper/overleaf/figs/figS2_correlation.png` | `.png` | 79,541 |
| `paper/overleaf/figs/figS3_stability_long.png` | `.png` | 130,136 |
| `paper/overleaf/main.tex` | `.tex` | 55,019 |
| `paper/overleaf/refs.bib` | `.bib` | 24,902 |
| `paper/prl/COVER_LETTER.txt` | `.txt` | 5,800 |
| `paper/prl/JUSTIFICATION.txt` | `.txt` | 675 |
| `paper/prl/README_SM.txt` | `.txt` | 1,094 |
| `paper/prl/REVISION_NOTES_PREM.md` | `.md` | 5,548 |
| `paper/prl/correlation_table.tex` | `.tex` | 733 |
| `paper/prl/figs/fig1_network.png` | `.png` | 2,326,084 |
| `paper/prl/figs/fig2_ratio.png` | `.png` | 333,820 |
| `paper/prl/figs/fig3_history.png` | `.png` | 186,156 |
| `paper/prl/figs/fig5_spliced_prem.pdf` | `.pdf` | 25,124 |
| `paper/prl/figs/fig5_spliced_prem.png` | `.png` | 100,964 |
| `paper/prl/figs/fig5_spliced_stability.png` | `.png` | 156,915 |
| `paper/prl/figs/figSI_fit_grid.png` | `.png` | 435,396 |
| `paper/prl/figs/fig_method_setup_a3p.pdf` | `.pdf` | 300,709 |
| `paper/prl/figs/fig_methods_forest.png` | `.png` | 79,591 |
| `paper/prl/loo_table.tex` | `.tex` | 871 |
| `paper/prl/main.aux` | `.aux` | 11,649 |
| `paper/prl/main.bbl` | `.bbl` | 57,118 |
| `paper/prl/main.blg` | `.blg` | 1,968 |
| `paper/prl/main.log` | `.log` | 20,704 |
| `paper/prl/main.pdf` | `.pdf` | 3,187,292 |
| `paper/prl/main.tex` | `.tex` | 25,103 |
| `paper/prl/mainNotes.bib` | `.bib` | 0 |
| `paper/prl/make_fig3_prl.py` | `.py` | 2,483 |
| `paper/prl/merged_segment_table.tex` | `.tex` | 1,265 |
| `paper/prl/numbers.tex` | `.tex` | 5,716 |
| `paper/prl/refs.bib` | `.bib` | 34,498 |
| `paper/prl/revision/PARAMETER_PROVENANCE.md` | `.md` | 7,138 |
| `paper/prl/revision/README.md` | `.md` | 1,336 |
| `paper/prl/revision/REVISION_NOTES_PREM.md` | `.md` | 5,548 |
| `paper/prl/revision/STATUS_PREM_ALIGNMENT.md` | `.md` | 2,724 |
| `paper/prl/revision/admittance_bands.json` | `.json` | 1,360 |
| `paper/prl/revision/all_data_fit_prem.json` | `.json` | 335 |
| `paper/prl/revision/correction_effect_prem.json` | `.json` | 729 |
| `paper/prl/revision/fig5_spliced_prem.pdf` | `.pdf` | 25,124 |
| `paper/prl/revision/fig5_spliced_prem.png` | `.png` | 100,964 |
| `paper/prl/revision/gpu_otl_prem.json` | `.json` | 3,655 |
| `paper/prl/revision/prl_summer_prem.json` | `.json` | 1,202 |
| `paper/prl/shift_components_table.tex` | `.tex` | 2,165 |
| `paper/prl/supplementary.aux` | `.aux` | 7,161 |
| `paper/prl/supplementary.bbl` | `.bbl` | 4,613 |
| `paper/prl/supplementary.blg` | `.blg` | 1,949 |
| `paper/prl/supplementary.log` | `.log` | 22,994 |
| `paper/prl/supplementary.pdf` | `.pdf` | 926,341 |
| `paper/prl/supplementary.tex` | `.tex` | 26,441 |
| `paper/prl/supplementaryNotes.bib` | `.bib` | 0 |
| `paper/ref/2026-arxiv-Ytterbium lattice clock with systematic uncertaintyof 1.3×10^-18 and instability at the 10^-19 level.pdf` | `.pdf` | 3,785,811 |
| `paper/ref/3104.pdf` | `.pdf` | 7,862,746 |
| `paper/ref/Dimarcq_2024_Metrologia_61_012001.pdf` | `.pdf` | 1,592,280 |
| `paper/ref/Jia_2026_Metrologia_63_025002.pdf` | `.pdf` | 3,613,713 |
| `paper/ref/Pizzocaro 等 - 2021 - Intercontinental comparison of optical atomic clocks through very long baseline interferometry.pdf` | `.pdf` | 3,588,023 |
| `paper/ref/README_original_sources.md` | `.md` | 3,389 |
| `paper/ref/Vishwakarma 等 - 2026 - Interspecies clock comparison below $5 times 10^{-18}$ uncertainty with a transportable clock(1).pdf` | `.pdf` | 703,302 |
| `paper/ref/advfapn2022_FA-PN.pdf` | `.pdf` | 7,186,897 |
| `paper/ref/aeppli2024sr_arXiv2403.10664.pdf` | `.pdf` | 11,101,549 |
| `paper/ref/akamatsu2014ybsr_arXiv1403.5836.pdf` | `.pdf` | 360,310 |
| `paper/ref/birge1932errors_PhysRev.pdf` | `.pdf` | 1,151,109 |
| `paper/ref/caldwell2023geo_arXiv2212.12541.pdf` | `.pdf` | 3,090,003 |
| `paper/ref/cctf2025strategy_CCTF-Strategy.pdf` | `.pdf` | 1,068,354 |
| `paper/ref/cctf2025taskforce_TF-Progress.pdf` | `.pdf` | 1,184,728 |
| `paper/ref/cuzk2015_Navod.pdf` | `.pdf` | 4,023,248 |
| `paper/ref/dawel2026ptbalplus_arXiv2606.23151.pdf` | `.pdf` | 4,065,395 |
| `paper/ref/denker2018geodetic_JGeod.pdf` | `.pdf` | 2,497,605 |
| `paper/ref/derevianko2014topological_arXiv1311.1244.pdf` | `.pdf` | 2,297,236 |
| `paper/ref/fgcc1984_FGCC.pdf` | `.pdf` | 2,869,471 |
| `paper/ref/filzinger2026multiion_arXiv2603.23446.pdf` | `.pdf` | 6,683,129 |
| `paper/ref/fortier2026review_Optica.pdf` | `.pdf` | 4,091,628 |
| `paper/ref/g865-9mk1 (1).pdf` | `.pdf` | 852,589 |
| `paper/ref/gb12897_GBT12897-2006.pdf` | `.pdf` | 3,577,487 |
| `paper/ref/grotti2018geodesy_arXiv1705.04089.pdf` | `.pdf` | 857,235 |
| `paper/ref/heavner2014nistf2_Metrologia.pdf` | `.pdf` | 854,824 |
| `paper/ref/iers2010conventions_TN36.pdf` | `.pdf` | 2,983,786 |
| `paper/ref/l4bh-ryxs.pdf` | `.pdf` | 1,590,636 |
| `paper/ref/lindvall2025coordinated_arXiv2505.06763.pdf` | `.pdf` | 1,541,944 |
| `paper/ref/lu2025ntsc_Metrologia.pdf` | `.pdf` | 1,486,404 |
| `paper/ref/mandel1970interlaboratory_AnalChem.pdf` | `.pdf` | 379,416 |
| `paper/ref/marshall2025alplus_arXiv2504.13071.pdf` | `.pdf` | 1,571,762 |
| `paper/ref/mcgrew2018geodesy_arXiv1807.11282.pdf` | `.pdf` | 1,602,258 |
| `paper/ref/ncomms12443.pdf` | `.pdf` | 925,029 |
| `paper/ref/nemitz2016ybsr_arXiv1601.04582.pdf` | `.pdf` | 1,637,694 |
| `paper/ref/nphys3000 A quantum network of clocks.pdf` | `.pdf` | 806,123 |
| `paper/ref/riehle2017networks_NatPhoton.pdf` | `.pdf` | 1,350,610 |
| `paper/ref/s41377-026-02299-1 (1).pdf` | `.pdf` | 1,758,052 |
| `paper/ref/s41586-022-05228-5.pdf` | `.pdf` | 2,975,916 |
| `paper/ref/s41586-026-11072-8.pdf` | `.pdf` | 5,433,859 |
| `paper/ref/shen2021satellite_Optica.pdf` | `.pdf` | 8,501,205 |
| `paper/ref/takamoto2020redshift_NatPhoton.pdf` | `.pdf` | 2,216,195 |
| `paper/ref/vngc-c1xv (1).pdf` | `.pdf` | 1,181,037 |
| `paper/ref/voigt2016timevariable_Metrologia.pdf` | `.pdf` | 3,789,345 |
| `paper/ref/wcislo2018global_arXiv1806.04762.pdf` | `.pdf` | 5,158,418 |
| `paper/ref/weyers2018ptbcsf_arXiv1809.03362.pdf` | `.pdf` | 727,785 |
| `paper/ref/zhang2026etideload_ETideLoad4.5-GeophysicalModels.pdf` | `.pdf` | 1,621,781 |
| `paper/refs.bib` | `.bib` | 24,902 |
| `paper/rev2/COVER_LETTER.pdf` | `.pdf` | 24,801 |
| `paper/rev2/COVER_LETTER.txt` | `.txt` | 5,588 |
| `paper/rev2/REVIEW_ADVERSARIAL.md` | `.md` | 4,124 |
| `paper/rev2/REVIEW_NOTES.md` | `.md` | 81,755 |
| `paper/rev2/combined_submission.pdf` | `.pdf` | 2,797,247 |
| `paper/rev2/extended_data.out` | `.out` | 111 |
| `paper/rev2/figs/fig1_network.png` | `.png` | 868,235 |
| `paper/rev2/figs/fig2_ratio.png` | `.png` | 347,177 |
| `paper/rev2/figs/fig3_history.png` | `.png` | 186,156 |
| `paper/rev2/figs/fig5_spliced_stability.pdf` | `.pdf` | 28,720 |
| `paper/rev2/figs/fig5_spliced_stability.png` | `.png` | 208,548 |
| `paper/rev2/figs/fig_method_setup_a3p.pdf` | `.pdf` | 298,249 |
| `paper/rev2/figs/fig_methods_forest.pdf` | `.pdf` | 21,869 |
| `paper/rev2/figs/fig_methods_forest.png` | `.png` | 68,793 |
| `paper/rev2/generated/correlation_table.tex` | `.tex` | 733 |
| `paper/rev2/generated/loo_table.tex` | `.tex` | 785 |
| `paper/rev2/generated/numbers.json` | `.json` | 4,608 |
| `paper/rev2/generated/numbers.tex` | `.tex` | 5,661 |
| `paper/rev2/generated/numbers_manifest.json` | `.json` | 18,047 |
| `paper/rev2/generated/ratio_intermediates.tex` | `.tex` | 1,282 |
| `paper/rev2/generated/sample_ledger_table.tex` | `.tex` | 907 |
| `paper/rev2/generated/segment_table.tex` | `.tex` | 827 |
| `paper/rev2/generated/shift_components_table.tex` | `.tex` | 1,270 |
| `paper/rev2/generated/tidal_synthesis_table.tex` | `.tex` | 336 |
| `paper/rev2/main.aux` | `.aux` | 16,996 |
| `paper/rev2/main.bbl` | `.bbl` | 21,698 |
| `paper/rev2/main.blg` | `.blg` | 914 |
| `paper/rev2/main.log` | `.log` | 25,212 |
| `paper/rev2/main.out` | `.out` | 0 |
| `paper/rev2/main.pdf` | `.pdf` | 2,161,019 |
| `paper/rev2/main.tex` | `.tex` | 44,339 |
| `paper/rev2/refs.bib` | `.bib` | 33,922 |
| `paper/rev2/supplementary.aux` | `.aux` | 6,815 |
| `paper/rev2/supplementary.bbl` | `.bbl` | 0 |
| `paper/rev2/supplementary.blg` | `.blg` | 1,037 |
| `paper/rev2/supplementary.log` | `.log` | 21,497 |
| `paper/rev2/supplementary.out` | `.out` | 1,087 |
| `paper/rev2/supplementary.pdf` | `.pdf` | 250,439 |
| `paper/rev2/supplementary.tex` | `.tex` | 15,690 |
| `paper/rev2/test_flatten.aux` | `.aux` | 8,060 |
| `paper/rev2/test_flatten.log` | `.log` | 31,019 |
| `paper/rev2/test_flatten.out` | `.out` | 0 |
| `paper/rev2/tools/build_numbers.py` | `.py` | 43,123 |
| `paper/rev2/tools/check.sh` | `.sh` | 1,071 |
| `paper/rev2/tools/make_figures.py` | `.py` | 2,365 |
| `paper/rev2/tools/publish.sh` | `.sh` | 721 |
| `paper/rev2/tools/sync_overleaf.sh` | `.sh` | 1,955 |
| `paper/光钟比对论文 hj.docx` | `.docx` | 2,583,627 |
| `paper/武汉-上海水准测量0930R1.docx` | `.docx` | 5,588,010 |
| `pyproject.toml` | `.toml` | 576 |
| `research/PREM_load_love_numbers_HanWahr_n0-696.txt` | `.txt` | 49,421 |
| `research/V7twin/ASSESSMENT.md` | `.md` | 6,366 |
| `research/V7twin/BRANCH.md` | `.md` | 1,169 |
| `research/V7twin/README.md` | `.md` | 4,274 |
| `research/V7twin/VALIDATION.md` | `.md` | 1,384 |
| `research/V7twin/assess.py` | `.py` | 10,093 |
| `research/V7twin/check_love.py` | `.py` | 1,100 |
| `research/V7twin/check_prl.py` | `.py` | 486 |
| `research/V7twin/claims.csv` | `.csv` | 2,658 |
| `research/V7twin/fit-diagnostics.json` | `.json` | 42,654 |
| `research/V7twin/input-manifest.json` | `.json` | 1,150 |
| `research/V7twin/inventory.py` | `.py` | 2,750 |
| `research/V7twin/local/00966a4fca7b423ec1bfe617f6d83753a9665c78eb23079f71ed14e016ad87e0.npz` | `.npz` | 783,869 |
| `research/V7twin/local/00d37c725f62645ad475a23c5b38b7a489a9c85fbe3a3e3cda8cc19b8afb0782.npz` | `.npz` | 785,575 |
| `research/V7twin/local/0253558513175ea05b7a515992ad93891fc086b65ac59ab6e86e9edb832cd177.npz` | `.npz` | 798,320 |
| `research/V7twin/local/040178413975add6ca963060e8bd0550be59defd34c1d674b3de027bc7078c97.npz` | `.npz` | 787,789 |
| `research/V7twin/local/151899e5eb416ff3fd171f3e1621323541fc37de91863fd80b80b3ac92a4086c.npz` | `.npz` | 808,661 |
| `research/V7twin/local/184bb9fdd5044b2c5395d4ed248f00533b61beb4a22a38dd9c18d387efeb2738.npz` | `.npz` | 1,097,661 |
| `research/V7twin/local/1b44d3e5f62eb075ffeaec1e9397bafc498218f1bbd6ad351059167e7a939fa7.npz` | `.npz` | 779,786 |
| `research/V7twin/local/1b7409d1f0772df5c4a85e5a83a4a579f8e94e45ee44b9e3ce3395f235913655.npz` | `.npz` | 790,123 |
| `research/V7twin/local/1c704e83f8a3dc905501b95cda0978ddaf8dafecd494da50bb4d54221666af1d.npz` | `.npz` | 780,611 |
| `research/V7twin/local/27e6704a29fbfc957e11b9a2cdc835ae841fb3f8a81878a3f1b715f9829dac0e.npz` | `.npz` | 779,142 |
| `research/V7twin/local/372ac52315bb7018a0e1f7f2915171a255aec79f02f83e992ba2f328d96e1a73.npz` | `.npz` | 867,935 |
| `research/V7twin/local/4f71b44d5ce973fd224d49349d57dc8a5479c61bd96ce65cd806ade013ef6acd.npz` | `.npz` | 782,781 |
| `research/V7twin/local/53e2619d5eb8ee18db62acc9c85a4375e024f4beeb624a625ffad11bd701874f.npz` | `.npz` | 796,227 |
| `research/V7twin/local/5c2cbb0911bcf6ab7b52936273564f7ce94eb992fb2a2e63b9262f5970ed13e8.npz` | `.npz` | 783,316 |
| `research/V7twin/local/648e39b7ae0219ac538643b2d506079bc9a24c7b418f5f127e3b786f6dbf4030.npz` | `.npz` | 782,660 |
| `research/V7twin/local/656cc828870d6708bd95dba1c018fc680139fbe65651db4d7b78430957b2d22a.npz` | `.npz` | 780,729 |
| `research/V7twin/local/742ba484024f5b4b67644a4eb79052a62d2107800b608b74cefc17757832fc7e.npz` | `.npz` | 781,688 |
| `research/V7twin/local/8a9cff27081bd39ea4600b558521de78a0ae511c034019d5e4330439beda794c.npz` | `.npz` | 778,439 |
| `research/V7twin/local/9f796c4abdf716a8f759ce7d603f8d7e33e8648d34b41ecad4109b812db6405b.npz` | `.npz` | 835,507 |
| `research/V7twin/local/a5c804e1019d5804c34a583ba5925a6cb881e425020b42e5a50faf0b7958905f.npz` | `.npz` | 789,987 |
| `research/V7twin/local/adea83a264561072dd9b4f7f0d48f89f188bb06f603a21796453faef93480fb1.npz` | `.npz` | 780,822 |
| `research/V7twin/local/ba5debbb9e044a0ca9c671a0d9223200d4450b41542785efd50482b4a9c2a4c6.npz` | `.npz` | 784,631 |
| `research/V7twin/local/be9b930fd7c7456a3236e417a36a4d28270c0231ac899bb07aa56a8aaf49f0e2.npz` | `.npz` | 785,493 |
| `research/V7twin/local/bins-synthetic.pkl` | `.pkl` | 288,605 |
| `research/V7twin/local/bins-t.pkl` | `.pkl` | 288,605 |
| `research/V7twin/local/c0cbfe98f87bb03d52e73c9b81794c23560e32fab7e42652339b9d5b52123459.npz` | `.npz` | 332,930 |
| `research/V7twin/local/c41c450d3d419030cd7f8a5e64fd02ed9aeef04530fceae70a240bc31bea115c.npz` | `.npz` | 803,220 |
| `research/V7twin/local/c79015acbda42bc518526b0f4c305e30f09ed9d2ddb35110c6fa1c5090484a1e.npz` | `.npz` | 814,386 |
| `research/V7twin/local/c8db7509261bcdb8b352ed491526cfb9933294b014b1b0120c6c1f7605184f52.npz` | `.npz` | 281,119 |
| `research/V7twin/local/candidate-selection.pkl` | `.pkl` | 182,969,174 |
| `research/V7twin/local/d51352e1402037da529fe0c6eadd3786c2e6f589aa9e96322bd1a4a103f32a2b.npz` | `.npz` | 778,348 |
| `research/V7twin/local/d811384b1c34b0793dfee057c438a50052c256e6f7f83c76a71ad15f8d489016.npz` | `.npz` | 794,716 |
| `research/V7twin/local/d8c3dca345653c2341405065034c938bb80d397669581d8dc41346198d035c3a.npz` | `.npz` | 2,375,917 |
| `research/V7twin/local/d8cb9fb2337983e112a672142d80566d7000251aafd06c85f38dca6b14eb83bb.npz` | `.npz` | 781,660 |
| `research/V7twin/local/d9be95f3a665501129a6e6fc68bc0a653545ca81444be84bcfbbb70aec181442.npz` | `.npz` | 783,069 |
| `research/V7twin/local/dd79d8de913b1240c3b01c0fef4eda95627b98f99421e7e7bf327efd25afc228.npz` | `.npz` | 780,902 |
| `research/V7twin/local/dd9261023c835c9d3fa17830016585af7b0f434fc7ca74668c1b07cf6e54e27e.npz` | `.npz` | 794,061 |
| `research/V7twin/local/e8af4c9347e95e807404e9db252245c5dac368d12e33563b1977b8a9ff7fd444.npz` | `.npz` | 1,122,383 |
| `research/V7twin/local/eb242e0a0190c0efdad226df54ed970b1f0bb7a20eb388505279619bdce1f6fd.npz` | `.npz` | 781,771 |
| `research/V7twin/local/eec743c95bd1feace3f7d2ff54da099c666e657c4a1a5db4ff45292eda369dad.npz` | `.npz` | 779,571 |
| `research/V7twin/local/f203034e4ce3dbdc942e168233339fc396022cf723cd31948f915d59d89bf797.npz` | `.npz` | 452,359 |
| `research/V7twin/local/f21488bc4b6612d218f0b9444683ba42a2e12c85ce76a90e0e0c5fb6567cc967.npz` | `.npz` | 828,068 |
| `research/V7twin/local/f5781a875d69639526eb69321aae9b0aa49ec08af787b0b2d3a1912c72194efd.npz` | `.npz` | 786,483 |
| `research/V7twin/local/f78e68d6f459fbde694eb8be831ef9c9bce8f49757a0ba9871199960052f0a83.npz` | `.npz` | 788,985 |
| `research/V7twin/local/fb4f53fba88fce62d4e27e23781cff980a61bf76f9ab0de7a2ed8af5eb02112e.npz` | `.npz` | 786,384 |
| `research/V7twin/local/may-kalman-100.0.csv` | `.csv` | 31,777 |
| `research/V7twin/local/may-kalman-1000.0.csv` | `.csv` | 31,762 |
| `research/V7twin/local/may-kalman-10000.0.csv` | `.csv` | 31,783 |
| `research/V7twin/local/raw-rows.pkl` | `.pkl` | 157,153,381 |
| `research/V7twin/love-number-check.json` | `.json` | 1,062 |
| `research/V7twin/noise-synthetic.csv` | `.csv` | 2,720 |
| `research/V7twin/noise-t.csv` | `.csv` | 2,720 |
| `research/V7twin/plot_audit.py` | `.py` | 3,079 |
| `research/V7twin/prl-check/per-group.csv` | `.csv` | 7,024 |
| `research/V7twin/prl-check/results.json` | `.json` | 31,348 |
| `research/V7twin/raw-audit.json` | `.json` | 1,047 |
| `research/V7twin/raw-files.csv` | `.csv` | 9,909 |
| `research/V7twin/raw_audit.py` | `.py` | 7,848 |
| `research/V7twin/reconstruct.py` | `.py` | 7,608 |
| `research/V7twin/robustness.json` | `.json` | 5,690 |
| `research/V7twin/robustness.py` | `.py` | 6,134 |
| `research/V7twin/run-manifest.json` | `.json` | 1,948 |
| `research/V7twin/semidiurnal-audit.alignment.json` | `.json` | 924 |
| `research/V7twin/semidiurnal-audit.collision.json` | `.json` | 504 |
| `research/V7twin/semidiurnal-audit.pdf` | `.pdf` | 18,519 |
| `research/V7twin/semidiurnal-audit.png` | `.png` | 96,884 |
| `research/V7twin/semidiurnal-audit.svg` | `.svg` | 18,567 |
| `research/V7twin/summer-noise-audit.alignment.json` | `.json` | 915 |
| `research/V7twin/summer-noise-audit.collision.json` | `.json` | 505 |
| `research/V7twin/summer-noise-audit.pdf` | `.pdf` | 18,849 |
| `research/V7twin/summer-noise-audit.png` | `.png` | 139,879 |
| `research/V7twin/summer-noise-audit.svg` | `.svg` | 15,607 |
| `research/V7twin/test_raw_audit.py` | `.py` | 600 |
| `research/V7twin/test_reconstruct.py` | `.py` | 518 |
| `research/V7twin/test_robustness.py` | `.py` | 521 |
| `research/V7twin/window-audit.csv` | `.csv` | 12,775 |
| `research/prl-2026/BRANCH.md` | `.md` | 1,864 |
| `research/tidal-kalman/ANALYSIS.md` | `.md` | 6,586 |
| `research/tidal-kalman/A_PARAMETER_EVIDENCE.md` | `.md` | 8,004 |
| `research/tidal-kalman/BRANCH.md` | `.md` | 2,201 |
| `research/tidal-kalman/DISCUSSION_REPORT.md` | `.md` | 11,677 |
| `research/tidal-kalman/DISCUSSION_REPORT.pdf` | `.pdf` | 256,382 |
| `research/tidal-kalman/GRAVIMETER_METHOD_REFERENCE.md` | `.md` | 5,711 |
| `research/tidal-kalman/KALMAN_BENEFITS_AUDIT.md` | `.md` | 5,073 |
| `research/tidal-kalman/KALMAN_VALIDATION.md` | `.md` | 5,878 |
| `research/tidal-kalman/METHODOLOGY.md` | `.md` | 8,929 |
| `research/tidal-kalman/METHOD_VALIDITY.md` | `.md` | 9,635 |
| `research/tidal-kalman/OTL_OVERESTIMATION_LITERATURE.md` | `.md` | 4,841 |
| `research/tidal-kalman/OTL_PARAMETERIZATION.md` | `.md` | 5,085 |
| `research/tidal-kalman/OTL_UNDERESTIMATION_TEST.md` | `.md` | 4,510 |
| `research/tidal-kalman/POTENTIAL_HYPOTHESIS_VERIFICATION.md` | `.md` | 2,849 |
| `research/tidal-kalman/POTENTIAL_VS_CONVERSION_MODEL.md` | `.md` | 4,520 |
| `research/tidal-kalman/REPORT.md` | `.md` | 15,541 |
| `research/tidal-kalman/RESULTS.md` | `.md` | 5,554 |
| `research/tidal-kalman/SIGNIFICANCE_ANALYSIS.md` | `.md` | 3,126 |
| `research/tidal-kalman/SIGNIFICANCE_DECOMPOSITION.md` | `.md` | 5,281 |
| `research/tidal-kalman/SOLID_OTL_SEPARATION.md` | `.md` | 7,356 |
| `research/tidal-kalman/TIDAL_PARAMETER_FIT_PLAN.md` | `.md` | 6,234 |
| `research/tidal-kalman/algorithm_comparison.json` | `.json` | 588 |
| `research/tidal-kalman/algorithm_comparison.py` | `.py` | 5,262 |
| `research/tidal-kalman/kalman_diagnostics.json` | `.json` | 816 |
| `research/tidal-kalman/kalman_diagnostics.py` | `.py` | 5,697 |
| `research/tidal-kalman/kalman_tide.json` | `.json` | 3,041 |
| `research/tidal-kalman/kalman_tide.png` | `.png` | 70,605 |
| `research/tidal-kalman/kalman_tide.py` | `.py` | 8,081 |
| `research/tidal-kalman/kalman_tide_prem.json` | `.json` | 2,492 |
| `research/tidal-kalman/kalman_tide_prem.png` | `.png` | 78,195 |
| `research/tidal-kalman/kalman_tide_prem.py` | `.py` | 6,522 |
| `research/tidal-kalman/kalman_tide_prem_54seg.json` | `.json` | 4,201 |
| `research/tidal-kalman/lomb_scargle_prem.json` | `.json` | 159,767 |
| `research/tidal-kalman/lomb_scargle_prem.pdf` | `.pdf` | 58,011 |
| `research/tidal-kalman/lomb_scargle_prem.png` | `.png` | 199,131 |
| `research/tidal-kalman/lomb_scargle_prem.py` | `.py` | 7,849 |
| `research/tidal-kalman/ls_bootstrap.json` | `.json` | 392 |
| `research/tidal-kalman/ls_bootstrap.py` | `.py` | 5,176 |
| `research/tidal-kalman/model_comparison.json` | `.json` | 722 |
| `research/tidal-kalman/model_comparison.py` | `.py` | 4,447 |
| `research/tidal-kalman/probes.json` | `.json` | 51,546 |
| `research/tidal-kalman/probes.png` | `.png` | 104,471 |
| `research/tidal-kalman/probes.py` | `.py` | 9,579 |
| `research/tidal-kalman/residual_drift.json` | `.json` | 177 |
| `research/tidal-kalman/residual_drift.py` | `.py` | 3,585 |
| `research/tidal-kalman/segment_comparison.json` | `.json` | 3,767 |
| `research/tidal-kalman/segment_comparison.png` | `.png` | 50,592 |
| `research/tidal-kalman/segment_comparison.py` | `.py` | 5,200 |
| `research/tidal-kalman/sensitivity.json` | `.json` | 637 |
| `research/tidal-kalman/sensitivity.png` | `.png` | 52,135 |
| `research/tidal-kalman/sensitivity.py` | `.py` | 4,090 |
| `research/tidal-kalman/smooth_fit.json` | `.json` | 275 |
| `research/tidal-kalman/smooth_fit.py` | `.py` | 4,238 |
| `research/tidal-kalman/test_kalman_diagnostics.py` | `.py` | 3,736 |
| `research/tidal-kalman/test_kalman_tide.py` | `.py` | 1,966 |
| `research/tidal-kalman/test_ls_bootstrap.py` | `.py` | 2,226 |
| `research/tidal-kalman/test_model_comparison.py` | `.py` | 3,588 |
| `research/tidal-kalman/test_residual_drift.py` | `.py` | 1,293 |
| `research/tidal-kalman/test_segment_comparison.py` | `.py` | 875 |
| `research/tidal-kalman/test_sensitivity.py` | `.py` | 1,675 |
| `research/tidal-kalman/test_smooth_fit.py` | `.py` | 2,272 |
| `research/tidal-kalman/test_time_domain.py` | `.py` | 1,758 |
| `research/tidal-kalman/time_domain.json` | `.json` | 284 |
| `research/tidal-kalman/time_domain.png` | `.png` | 132,846 |
| `research/tidal-kalman/time_domain.py` | `.py` | 4,327 |
| `research/tidal-spring/BRANCH.md` | `.md` | 11,478 |
| `research/tidal-spring/CROSS_CHECK_EU_V5.md` | `.md` | 7,949 |
| `research/tidal-spring/EU2610_CLOSE_READING.md` | `.md` | 5,487 |
| `research/tidal-spring/FUTURE_NETWORK_REQUIREMENTS.md` | `.md` | 6,021 |
| `research/tidal-spring/GRID_CONVENTION_DECISION.md` | `.md` | 1,830 |
| `research/tidal-spring/NATURE_PAPER_CONCEPT.md` | `.md` | 6,941 |
| `research/tidal-spring/OTL_DIFFERENCE_DIAGNOSIS.md` | `.md` | 2,700 |
| `research/tidal-spring/PAPER_IDEAS.md` | `.md` | 9,168 |
| `research/tidal-spring/PAPER_STRUCTURE.md` | `.md` | 4,028 |
| `research/tidal-spring/PARAMETER_PROVENANCE.md` | `.md` | 7,138 |
| `research/tidal-spring/PHASE_FIX_REPORT.md` | `.md` | 10,001 |
| `research/tidal-spring/PHASE_FIX_REPORT.pdf` | `.pdf` | 141,671 |
| `research/tidal-spring/REPLY_TO_COLLEAGUE.md` | `.md` | 2,598 |
| `research/tidal-spring/REPLY_TO_COLLEAGUE_LOVE_TABLE.md` | `.md` | 2,484 |
| `research/tidal-spring/REPLY_TO_COLLEAGUE_NODAL_FACTOR.md` | `.md` | 1,739 |
| `research/tidal-spring/REPLY_TO_COLLEAGUE_Q1Q2.md` | `.md` | 3,793 |
| `research/tidal-spring/SOP.md` | `.md` | 4,648 |
| `research/tidal-spring/STATUS_PREM_ALIGNMENT.md` | `.md` | 3,532 |
| `research/tidal-spring/SUMMARY.md` | `.md` | 11,178 |
| `research/tidal-spring/TEMPLATE_CONVENTION_SUMMARY.md` | `.md` | 3,664 |
| `research/tidal-spring/TIDAL_CORRECTION_0.7_VERIFICATION.md` | `.md` | 2,281 |
| `research/tidal-spring/V7_COMPARISON_REPORT.md` | `.md` | 5,744 |
| `research/tidal-spring/V7_COMPARISON_REPORT.pdf` | `.pdf` | 103,210 |
| `research/tidal-spring/V7_DIFFERENCES.md` | `.md` | 5,049 |
| `research/tidal-spring/V7_DIFFERENCES_FOR_CHECK.md` | `.md` | 5,107 |
| `research/tidal-spring/admittance_bands.json` | `.json` | 1,360 |
| `research/tidal-spring/admittance_bands.py` | `.py` | 8,252 |
| `research/tidal-spring/admittance_bands_extrapolated.json` | `.json` | 588 |
| `research/tidal-spring/admittance_bands_prem.json` | `.json` | 597 |
| `research/tidal-spring/admittance_fit.json` | `.json` | 5,038 |
| `research/tidal-spring/admittance_fit.py` | `.py` | 8,549 |
| `research/tidal-spring/all_data_fit.json` | `.json` | 656 |
| `research/tidal-spring/all_data_fit.py` | `.py` | 9,933 |
| `research/tidal-spring/all_data_fit_extrapolated.json` | `.json` | 315 |
| `research/tidal-spring/all_data_fit_gpu.json` | `.json` | 676 |
| `research/tidal-spring/all_data_fit_gpu.py` | `.py` | 4,352 |
| `research/tidal-spring/all_data_fit_prem.json` | `.json` | 335 |
| `research/tidal-spring/all_data_fit_prem_extrapolated.json` | `.json` | 347 |
| `research/tidal-spring/check_data.py` | `.py` | 8,949 |
| `research/tidal-spring/clock_state.json` | `.json` | 20,462 |
| `research/tidal-spring/clock_state.py` | `.py` | 10,280 |
| `research/tidal-spring/component_compare.json` | `.json` | 4,035 |
| `research/tidal-spring/component_compare.py` | `.py` | 5,525 |
| `research/tidal-spring/correction_effect_by_season.json` | `.json` | 5,793 |
| `research/tidal-spring/correction_effect_by_season.py` | `.py` | 5,455 |
| `research/tidal-spring/correction_effect_extrapolated.json` | `.json` | 726 |
| `research/tidal-spring/correction_effect_prem.json` | `.json` | 729 |
| `research/tidal-spring/cross_year_comparison.json` | `.json` | 1,879 |
| `research/tidal-spring/cross_year_comparison.py` | `.py` | 3,636 |
| `research/tidal-spring/data/README.md` | `.md` | 3,772 |
| `research/tidal-spring/data/archive/otl_extrapolated_series.csv` | `.csv` | 14,589,332 |
| `research/tidal-spring/data/archive/otl_potential_series.csv` | `.csv` | 14,565,808 |
| `research/tidal-spring/data/archive/otl_potential_series_gpu.csv` | `.csv` | 14,592,294 |
| `research/tidal-spring/data/archive/solid_tide_template.csv` | `.csv` | 14,593,303 |
| `research/tidal-spring/data/archive/total_tide_extrapolated.csv` | `.csv` | 14,577,119 |
| `research/tidal-spring/data/archive/total_tide_gpu.csv` | `.csv` | 14,580,801 |
| `research/tidal-spring/data/archive/total_tide_sop.csv` | `.csv` | 14,585,294 |
| `research/tidal-spring/data/otl/otl_prem_extrapolated_series.csv` | `.csv` | 14,587,474 |
| `research/tidal-spring/data/otl/otl_prem_series.csv` | `.csv` | 14,587,712 |
| `research/tidal-spring/data/solid/solid_tide_sop.csv` | `.csv` | 14,590,668 |
| `research/tidal-spring/data/total/total_tide_prem.csv` | `.csv` | 14,588,285 |
| `research/tidal-spring/data/total/total_tide_prem_extrapolated.csv` | `.csv` | 14,591,215 |
| `research/tidal-spring/data_quality.json` | `.json` | 21,798 |
| `research/tidal-spring/diurnal_anomaly.py` | `.py` | 9,464 |
| `research/tidal-spring/diurnal_anomaly_2025.json` | `.json` | 4,572 |
| `research/tidal-spring/double_check_frozen.json` | `.json` | 24,456 |
| `research/tidal-spring/double_check_frozen.py` | `.py` | 16,685 |
| `research/tidal-spring/fetch_pressure.py` | `.py` | 4,016 |
| `research/tidal-spring/final_consistency_check.json` | `.json` | 4,911 |
| `research/tidal-spring/final_consistency_check.py` | `.py` | 6,557 |
| `research/tidal-spring/gpu_otl_extrapolated.json` | `.json` | 1,739 |
| `research/tidal-spring/gpu_otl_extrapolated.py` | `.py` | 5,872 |
| `research/tidal-spring/gpu_otl_potential.json` | `.json` | 3,649 |
| `research/tidal-spring/gpu_otl_potential.py` | `.py` | 5,608 |
| `research/tidal-spring/gpu_otl_potential_exact.json` | `.json` | 3,758 |
| `research/tidal-spring/gpu_otl_potential_exact.py` | `.py` | 6,447 |
| `research/tidal-spring/gpu_otl_prem.json` | `.json` | 3,655 |
| `research/tidal-spring/gpu_otl_prem.py` | `.py` | 5,888 |
| `research/tidal-spring/gpu_otl_prem_extrapolated.json` | `.json` | 3,849 |
| `research/tidal-spring/gpu_otl_prem_extrapolated.py` | `.py` | 6,234 |
| `research/tidal-spring/hybrid_eu_prl.json` | `.json` | 1,601 |
| `research/tidal-spring/hybrid_eu_prl.py` | `.py` | 10,086 |
| `research/tidal-spring/hybrid_filter_compare.json` | `.json` | 606 |
| `research/tidal-spring/hybrid_filter_compare.py` | `.py` | 8,700 |
| `research/tidal-spring/long_runs.json` | `.json` | 2,811 |
| `research/tidal-spring/long_runs.py` | `.py` | 8,683 |
| `research/tidal-spring/love_prem.py` | `.py` | 4,401 |
| `research/tidal-spring/lunar-v7-20261103/README.md` | `.md` | 3,330 |
| `research/tidal-spring/lunar-v7-20261103/audit_may_offsets.py` | `.py` | 4,397 |
| `research/tidal-spring/lunar-v7-20261103/check_prl_models.py` | `.py` | 6,445 |
| `research/tidal-spring/lunar-v7-20261103/check_v7.py` | `.py` | 5,808 |
| `research/tidal-spring/lunar-v7-20261103/estimator.py` | `.py` | 10,549 |
| `research/tidal-spring/lunar-v7-20261103/fig2-reconstruction/README.md` | `.md` | 1,468 |
| `research/tidal-spring/lunar-v7-20261103/fig2-reconstruction/SUPERPOWERS_PLAN.md` | `.md` | 3,422 |
| `research/tidal-spring/lunar-v7-20261103/fig2-reconstruction/endpoint-qc.json` | `.json` | 711 |
| `research/tidal-spring/lunar-v7-20261103/fig2-reconstruction/offset-audit.json` | `.json` | 910 |
| `research/tidal-spring/lunar-v7-20261103/local_model_probe.json` | `.json` | 2,814 |
| `research/tidal-spring/lunar-v7-20261103/may-timing-rebuilt/coverage.csv` | `.csv` | 12,919 |
| `research/tidal-spring/lunar-v7-20261103/may-timing-rebuilt/may-coverage.pdf` | `.pdf` | 19,672 |
| `research/tidal-spring/lunar-v7-20261103/may-timing-rebuilt/may-coverage.png` | `.png` | 52,130 |
| `research/tidal-spring/lunar-v7-20261103/may-timing-rebuilt/report.json` | `.json` | 954 |
| `research/tidal-spring/lunar-v7-20261103/prl-model-check/REPORT.md` | `.md` | 5,546 |
| `research/tidal-spring/lunar-v7-20261103/prl-model-check/per-group.csv` | `.csv` | 7,024 |
| `research/tidal-spring/lunar-v7-20261103/prl-model-check/results.json` | `.json` | 31,348 |
| `research/tidal-spring/lunar-v7-20261103/probe_local.py` | `.py` | 3,712 |
| `research/tidal-spring/lunar-v7-20261103/probe_raw.py` | `.py` | 4,689 |
| `research/tidal-spring/lunar-v7-20261103/raw_exposure_probe.json` | `.json` | 3,356 |
| `research/tidal-spring/lunar-v7-20261103/rebuild_fig2.py` | `.py` | 2,516 |
| `research/tidal-spring/lunar-v7-20261103/rebuild_may_timing.py` | `.py` | 3,642 |
| `research/tidal-spring/lunar-v7-20261103/test_estimator.py` | `.py` | 3,064 |
| `research/tidal-spring/lunar_group_prem.json` | `.json` | 126 |
| `research/tidal-spring/make_otl_potential.py` | `.py` | 15,010 |
| `research/tidal-spring/make_sop_template.py` | `.py` | 2,743 |
| `research/tidal-spring/make_tide_template.py` | `.py` | 7,420 |
| `research/tidal-spring/nature-review-20261103/README.md` | `.md` | 2,743 |
| `research/tidal-spring/nature-review-20261103/evidence.json` | `.json` | 208,786 |
| `research/tidal-spring/nature_review_evidence.py` | `.py` | 14,810 |
| `research/tidal-spring/otl_extrapolation_scan.json` | `.json` | 24,369 |
| `research/tidal-spring/otl_extrapolation_scan.py` | `.py` | 5,753 |
| `research/tidal-spring/otl_potential_validation.json` | `.json` | 4,047 |
| `research/tidal-spring/per_campaign_band_A.json` | `.json` | 2,067 |
| `research/tidal-spring/per_segment_A.json` | `.json` | 10,310 |
| `research/tidal-spring/per_segment_band_A.json` | `.json` | 16,432 |
| `research/tidal-spring/per_segment_band_fit.py` | `.py` | 6,287 |
| `research/tidal-spring/pipeline_crosscheck.py` | `.py` | 5,667 |
| `research/tidal-spring/pipeline_crosscheck_summer.json` | `.json` | 4,719 |
| `research/tidal-spring/polarity_check.json` | `.json` | 3,294 |
| `research/tidal-spring/polarity_check.py` | `.py` | 10,191 |
| `research/tidal-spring/pole_atl.py` | `.py` | 5,625 |
| `research/tidal-spring/pole_atl_check.json` | `.json` | 1,350 |
| `research/tidal-spring/pressure_admittance.json` | `.json` | 541 |
| `research/tidal-spring/pressure_admittance.py` | `.py` | 6,444 |
| `research/tidal-spring/pressure_fetch.json` | `.json` | 551 |
| `research/tidal-spring/pressure_series.csv` | `.csv` | 264,480 |
| `research/tidal-spring/prl_fig3_redraw.json` | `.json` | 2,450 |
| `research/tidal-spring/prl_fig3_redraw.pdf` | `.pdf` | 24,812 |
| `research/tidal-spring/prl_fig3_redraw.png` | `.png` | 204,159 |
| `research/tidal-spring/prl_fig3_redraw.py` | `.py` | 8,585 |
| `research/tidal-spring/prl_fig3_redraw_full.json` | `.json` | 5,790 |
| `research/tidal-spring/prl_fig3_redraw_full.pdf` | `.pdf` | 29,990 |
| `research/tidal-spring/prl_fig3_redraw_full.png` | `.png` | 277,665 |
| `research/tidal-spring/prl_fig3_redraw_full.py` | `.py` | 8,831 |
| `research/tidal-spring/prl_summer_prem.json` | `.json` | 909 |
| `research/tidal-spring/pysolid_validate.py` | `.py` | 4,192 |
| `research/tidal-spring/pysolid_validation.json` | `.json` | 555 |
| `research/tidal-spring/q2_green_diagnosis.json` | `.json` | 3,147 |
| `research/tidal-spring/q2_green_diagnosis.py` | `.py` | 5,950 |
| `research/tidal-spring/qc_report.json` | `.json` | 3,782 |
| `research/tidal-spring/qc_report.py` | `.py` | 9,541 |
| `research/tidal-spring/replicate_all_v5.py` | `.py` | 12,826 |
| `research/tidal-spring/replicate_v5.json` | `.json` | 1,203 |
| `research/tidal-spring/replicate_v5.py` | `.py` | 9,058 |
| `research/tidal-spring/schureman_phase.py` | `.py` | 5,711 |
| `research/tidal-spring/schureman_phase_check.json` | `.json` | 422 |
| `research/tidal-spring/schureman_vu.json` | `.json` | 379 |
| `research/tidal-spring/schureman_vu.py` | `.py` | 6,398 |
| `research/tidal-spring/seasonal_modulation.json` | `.json` | 912 |
| `research/tidal-spring/seasonal_modulation.py` | `.py` | 4,652 |
| `research/tidal-spring/solid_decompose.py` | `.py` | 3,401 |
| `research/tidal-spring/solid_per_constituent.json` | `.json` | 3,401 |
| `research/tidal-spring/spectrum_analysis.json` | `.json` | 4,790 |
| `research/tidal-spring/spectrum_analysis.png` | `.png` | 357,589 |
| `research/tidal-spring/spectrum_analysis.py` | `.py` | 10,747 |
| `research/tidal-spring/spliced_instability_prem.json` | `.json` | 5,045 |
| `research/tidal-spring/spring_tide_fit.json` | `.json` | 15,054 |
| `research/tidal-spring/spring_tide_fit.py` | `.py` | 13,787 |
| `research/tidal-spring/synthesize_otl_gpu.py` | `.py` | 2,872 |
| `research/tidal-spring/template_sensitivity.json` | `.json` | 771 |
| `research/tidal-spring/template_validation.json` | `.json` | 489 |
| `research/tidal-spring/test_nature_review_evidence.py` | `.py` | 2,094 |
| `research/tidal-spring/test_tidal_spring.py` | `.py` | 5,667 |
| `research/tidal-spring/unified_fit.json` | `.json` | 5,283 |
| `research/tidal-spring/unified_fit.py` | `.py` | 12,907 |
| `research/tidal-spring/v5_replication_report.json` | `.json` | 5,860 |
| `research/tidal-spring/v5_replication_report.md` | `.md` | 3,692 |
| `research/tidal-spring/v5_replication_report.pdf` | `.pdf` | 74,798 |
| `research/tidal-spring/v7_new_analyses.json` | `.json` | 773 |
| `research/tidal-spring/v7_new_analyses.py` | `.py` | 9,334 |
| `research/v10-review-20261103/BRANCH.md` | `.md` | 1,113 |
| `research/v10-review-20261103/PACKET.md` | `.md` | 3,543 |
| `research/v10-review-20261103/READING_NOTES.md` | `.md` | 5,992 |
| `research/v10-review-20261103/README.md` | `.md` | 2,372 |
| `research/v10-review-20261103/REPORT.md` | `.md` | 23,838 |
| `research/v10-review-20261103/REPORT.pdf` | `.pdf` | 225,890 |
| `research/v10-review-20261103/build_report.py` | `.py` | 4,200 |
| `research/v10-review-20261103/check_estimation.py` | `.py` | 4,913 |
| `research/v10-review-20261103/check_stability.py` | `.py` | 1,565 |
| `research/v10-review-20261103/data-validation.json` | `.json` | 595 |
| `research/v10-review-20261103/estimator-validation.json` | `.json` | 11,894 |
| `research/v10-review-20261103/fetch_readings.py` | `.py` | 2,138 |
| `research/v10-review-20261103/local/europe.txt` | `.txt` | 83,009 |
| `research/v10-review-20261103/local/final-1.png` | `.png` | 136,655 |
| `research/v10-review-20261103/local/final-11.png` | `.png` | 133,072 |
| `research/v10-review-20261103/local/final-24.png` | `.png` | 78,444 |
| `research/v10-review-20261103/local/final-4.png` | `.png` | 134,174 |
| `research/v10-review-20261103/local/final-8.png` | `.png` | 111,940 |
| `research/v10-review-20261103/local/manuscript.txt` | `.txt` | 50,953 |
| `research/v10-review-20261103/local/page-1.png` | `.png` | 201,647 |
| `research/v10-review-20261103/local/page-1.txt` | `.txt` | 4,028 |
| `research/v10-review-20261103/local/page-2.png` | `.png` | 266,781 |
| `research/v10-review-20261103/local/page-2.txt` | `.txt` | 5,399 |
| `research/v10-review-20261103/local/page-3.png` | `.png` | 247,059 |
| `research/v10-review-20261103/local/page-3.txt` | `.txt` | 4,985 |
| `research/v10-review-20261103/local/page-4.png` | `.png` | 283,483 |
| `research/v10-review-20261103/local/page-4.txt` | `.txt` | 5,826 |
| `research/v10-review-20261103/local/page-5.png` | `.png` | 147,664 |
| `research/v10-review-20261103/local/page-5.txt` | `.txt` | 2,484 |
| `research/v10-review-20261103/local/page-6.png` | `.png` | 73,737 |
| `research/v10-review-20261103/local/page-6.txt` | `.txt` | 1,385 |
| `research/v10-review-20261103/local/page-7.png` | `.png` | 209,062 |
| `research/v10-review-20261103/local/page-7.txt` | `.txt` | 2,233 |
| `research/v10-review-20261103/local/page-8.png` | `.png` | 147,890 |
| `research/v10-review-20261103/local/page-8.txt` | `.txt` | 2,529 |
| `research/v10-review-20261103/local/page-9.png` | `.png` | 174,172 |
| `research/v10-review-20261103/local/page-9.txt` | `.txt` | 1,948 |
| `research/v10-review-20261103/local/policy-editorial-criteria-and-processes.txt` | `.txt` | 23,277 |
| `research/v10-review-20261103/local/policy-formatting-guide.txt` | `.txt` | 33,079 |
| `research/v10-review-20261103/local/policy-initial-submission.txt` | `.txt` | 19,275 |
| `research/v10-review-20261103/local/probe.html` | `.html` | 551,749 |
| `research/v10-review-20261103/local/report-1.png` | `.png` | 136,656 |
| `research/v10-review-20261103/local/report-11.png` | `.png` | 133,082 |
| `research/v10-review-20261103/local/report-13.png` | `.png` | 94,673 |
| `research/v10-review-20261103/local/report-24.png` | `.png` | 78,448 |
| `research/v10-review-20261103/local/report-26.png` | `.png` | 79,911 |
| `research/v10-review-20261103/local/report-3.png` | `.png` | 133,346 |
| `research/v10-review-20261103/local/report-5.png` | `.png` | 124,068 |
| `research/v10-review-20261103/local/report-7.png` | `.png` | 134,465 |
| `research/v10-review-20261103/local/report-9.png` | `.png` | 106,451 |
| `research/v10-review-20261103/local/s41586-026-10517-4.html` | `.html` | 476,785 |
| `research/v10-review-20261103/local/s41586-026-10517-4.txt` | `.txt` | 51,345 |
| `research/v10-review-20261103/local/s41586-026-10521-8.html` | `.html` | 503,646 |
| `research/v10-review-20261103/local/s41586-026-10521-8.txt` | `.txt` | 63,083 |
| `research/v10-review-20261103/local/s41586-026-10617-1.html` | `.html` | 739,595 |
| `research/v10-review-20261103/local/s41586-026-10617-1.txt` | `.txt` | 89,023 |
| `research/v10-review-20261103/local/s41586-026-10681-7.html` | `.html` | 522,549 |
| `research/v10-review-20261103/local/s41586-026-10681-7.txt` | `.txt` | 90,508 |
| `research/v10-review-20261103/local/s41586-026-10754-7.html` | `.html` | 458,651 |
| `research/v10-review-20261103/local/s41586-026-10754-7.txt` | `.txt` | 56,763 |
| `research/v10-review-20261103/local/s41586-026-10999-2.html` | `.html` | 509,201 |
| `research/v10-review-20261103/local/s41586-026-10999-2.txt` | `.txt` | 68,517 |
| `research/v10-review-20261103/local/s41586-026-11011-7.html` | `.html` | 490,811 |
| `research/v10-review-20261103/local/s41586-026-11011-7.txt` | `.txt` | 57,937 |
| `research/v10-review-20261103/local/s41586-026-11072-8.html` | `.html` | 551,751 |
| `research/v10-review-20261103/local/s41586-026-11072-8.txt` | `.txt` | 82,472 |
| `research/v10-review-20261103/local/s41586-026-11084-4.html` | `.html` | 577,187 |
| `research/v10-review-20261103/local/s41586-026-11084-4.txt` | `.txt` | 68,221 |
| `research/v10-review-20261103/local/s41586-026-11122-1.html` | `.html` | 559,872 |
| `research/v10-review-20261103/local/s41586-026-11122-1.txt` | `.txt` | 62,864 |
| `research/v10-review-20261103/local/selected.pkl` | `.pkl` | 31,812,912 |
| `research/v10-review-20261103/local/triangular.pkl` | `.pkl` | 247,268 |
| `research/v10-review-20261103/packet-manifest.json` | `.json` | 188 |
| `research/v10-review-20261103/reading-manifest.json` | `.json` | 22,289 |
| `research/v10-review-20261103/release-manifest.json` | `.json` | 2,531 |
| `research/v10-review-20261103/review-freeze.json` | `.json` | 341 |
| `research/v10-review-20261103/reviewer-1.md` | `.md` | 13,445 |
| `research/v10-review-20261103/reviewer-2.md` | `.md` | 15,439 |
| `research/v10-review-20261103/reviewer-3.md` | `.md` | 15,720 |
| `research/v10-review-20261103/stability-validation.json` | `.json` | 9,873 |
| `research/v10-review-20261103/test_audit.py` | `.py` | 720 |
| `research/v10-review-20261103/v10-selection.csv` | `.csv` | 5,575 |
| `research/v10-review-20261103/validate_data.py` | `.py` | 3,150 |
| `research/v13-review-20261103/PACKET.md` | `.md` | 1,331 |
| `research/v13-review-20261103/README.md` | `.md` | 1,283 |
| `research/v13-review-20261103/REPORT.md` | `.md` | 14,866 |
| `research/v13-review-20261103/REPORT.pdf` | `.pdf` | 133,431 |
| `research/v13-review-20261103/arithmetic-checks.json` | `.json` | 600 |
| `research/v13-review-20261103/build_report.py` | `.py` | 944 |
| `research/v13-review-20261103/input-manifest.json` | `.json` | 264 |
| `research/v13-review-20261103/local/manuscript.txt` | `.txt` | 60,361 |
| `research/v13-review-20261103/local/page-10.png` | `.png` | 119,006 |
| `research/v13-review-20261103/local/page-11.png` | `.png` | 65,307 |
| `research/v13-review-20261103/local/page-8.png` | `.png` | 145,589 |
| `research/v13-review-20261103/local/page-9.png` | `.png` | 103,960 |
| `research/v13-review-20261103/local/report-1.png` | `.png` | 118,405 |
| `research/v13-review-20261103/local/report-3.png` | `.png` | 154,760 |
| `research/v13-review-20261103/local/report-8.png` | `.png` | 114,586 |
| `research/v13-review-20261103/local/text-diff.patch` | `.patch` | 93,669 |
| `research/v13-review-20261103/release-manifest.json` | `.json` | 1,469 |
| `research/v13-review-20261103/review-freeze.json` | `.json` | 347 |
| `research/v13-review-20261103/reviewer-1.md` | `.md` | 3,012 |
| `research/v13-review-20261103/reviewer-2.md` | `.md` | 2,865 |
| `research/v13-review-20261103/reviewer-3.md` | `.md` | 2,918 |
| `research/沪汉潮汐_Nature稿_v10_20261103.pdf` | `.pdf` | 687,868 |
| `research/沪汉潮汐_Nature稿_v13_20261103.pdf` | `.pdf` | 720,541 |
| `research/沪汉潮汐_初稿_v5_20261101.pdf` | `.pdf` | 336,372 |
| `research/沪汉潮汐_初稿_v7_20261101.pdf` | `.pdf` | 345,272 |
| `results/audit-v1/README.md` | `.md` | 3,306 |
| `results/audit-v1/runs/15725f5246e87af5/ANALYSIS_AUDIT.md` | `.md` | 15,267 |
| `results/audit-v1/runs/15725f5246e87af5/manifest.json` | `.json` | 30,820 |
| `results/audit-v1/runs/15725f5246e87af5/manifest.json.run.json` | `.json` | 57 |
| `results/audit-v1/runs/15725f5246e87af5/parameter_conflicts.json` | `.json` | 7,710 |
| `results/audit-v1/runs/15725f5246e87af5/parameter_ledger.csv` | `.csv` | 15,062 |
| `results/audit-v1/runs/15725f5246e87af5/ratio_17seg.csv` | `.csv` | 2,981 |
| `results/audit-v1/runs/15725f5246e87af5/ratio_17seg_summary.csv` | `.csv` | 477 |
| `results/audit-v1/runs/15725f5246e87af5/sample_ledger.csv` | `.csv` | 1,690 |
| `results/audit-v1/runs/15725f5246e87af5/statistical_methods.csv` | `.csv` | 1,441 |
| `results/audit-v1/runs/15725f5246e87af5/statistical_methods.json` | `.json` | 894 |
| `results/audit-v1/runs/15725f5246e87af5/statistical_methods_tidal.json` | `.json` | 22,396 |
| `results/audit-v1/runs/15725f5246e87af5/statistical_methods_tidal_seg9_excluded.json` | `.json` | 42,453 |
| `results/audit-v1/runs/15725f5246e87af5/tide-conversion/professional_tidal_delta_30s.csv` | `.csv` | 10,962,045 |
| `results/audit-v1/runs/15725f5246e87af5/tide-conversion/professional_tidal_delta_30s.diff.json` | `.json` | 1,370 |
| `results/audit-v1/runs/15725f5246e87af5/time_quality.json` | `.json` | 16,263 |
| `results/audit-v1/runs/48a6010196134530/manifest.json` | `.json` | 29,403 |
| `results/audit-v1/runs/48a6010196134530/manifest.json.run.json` | `.json` | 57 |
| `results/audit-v1/runs/48a6010196134530/parameter_conflicts.json` | `.json` | 7,719 |
| `results/audit-v1/runs/48a6010196134530/parameter_ledger.csv` | `.csv` | 15,071 |
| `results/audit-v1/runs/48a6010196134530/ratio_17seg.csv` | `.csv` | 2,981 |
| `results/audit-v1/runs/48a6010196134530/ratio_17seg_summary.csv` | `.csv` | 477 |
| `results/audit-v1/runs/48a6010196134530/sample_ledger.csv` | `.csv` | 1,690 |
| `results/audit-v1/runs/48a6010196134530/statistical_methods.csv` | `.csv` | 1,424 |
| `results/audit-v1/runs/48a6010196134530/statistical_methods.json` | `.json` | 877 |
| `results/audit-v1/runs/48a6010196134530/statistical_methods_tidal.json` | `.json` | 22,388 |
| `results/audit-v1/runs/48a6010196134530/statistical_methods_tidal_seg9_excluded.json` | `.json` | 42,386 |
| `results/audit-v1/runs/48a6010196134530/tide-conversion/professional_tidal_delta_30s.csv` | `.csv` | 10,962,045 |
| `results/audit-v1/runs/48a6010196134530/tide-conversion/professional_tidal_delta_30s.diff.json` | `.json` | 1,331 |
| `results/audit-v1/runs/48a6010196134530/time_quality.json` | `.json` | 16,263 |
| `results/audit-v1/runs/a0d8a696bba93641/manifest.json` | `.json` | 30,586 |
| `results/audit-v1/runs/a0d8a696bba93641/manifest.json.run.json` | `.json` | 57 |
| `results/audit-v1/runs/a0d8a696bba93641/parameter_conflicts.json` | `.json` | 7,719 |
| `results/audit-v1/runs/a0d8a696bba93641/parameter_ledger.csv` | `.csv` | 15,071 |
| `results/audit-v1/runs/a0d8a696bba93641/ratio_17seg.csv` | `.csv` | 2,981 |
| `results/audit-v1/runs/a0d8a696bba93641/ratio_17seg_summary.csv` | `.csv` | 477 |
| `results/audit-v1/runs/a0d8a696bba93641/sample_ledger.csv` | `.csv` | 1,690 |
| `results/audit-v1/runs/a0d8a696bba93641/statistical_methods.csv` | `.csv` | 1,424 |
| `results/audit-v1/runs/a0d8a696bba93641/statistical_methods.json` | `.json` | 877 |
| `results/audit-v1/runs/a0d8a696bba93641/statistical_methods_tidal.json` | `.json` | 22,312 |
| `results/audit-v1/runs/a0d8a696bba93641/statistical_methods_tidal_seg9_excluded.json` | `.json` | 42,358 |
| `results/audit-v1/runs/a0d8a696bba93641/tide-conversion/professional_tidal_delta_30s.csv` | `.csv` | 10,962,045 |
| `results/audit-v1/runs/a0d8a696bba93641/tide-conversion/professional_tidal_delta_30s.diff.json` | `.json` | 1,331 |
| `results/audit-v1/runs/a0d8a696bba93641/time_quality.json` | `.json` | 16,263 |
| `results/audit-v1/runs/ac725aaba8ec744b/ANALYSIS_AUDIT.md` | `.md` | 15,020 |
| `results/audit-v1/runs/ac725aaba8ec744b/manifest.json` | `.json` | 30,586 |
| `results/audit-v1/runs/ac725aaba8ec744b/manifest.json.run.json` | `.json` | 57 |
| `results/audit-v1/runs/ac725aaba8ec744b/parameter_conflicts.json` | `.json` | 7,719 |
| `results/audit-v1/runs/ac725aaba8ec744b/parameter_ledger.csv` | `.csv` | 15,071 |
| `results/audit-v1/runs/ac725aaba8ec744b/ratio_17seg.csv` | `.csv` | 2,981 |
| `results/audit-v1/runs/ac725aaba8ec744b/ratio_17seg_summary.csv` | `.csv` | 477 |
| `results/audit-v1/runs/ac725aaba8ec744b/sample_ledger.csv` | `.csv` | 1,690 |
| `results/audit-v1/runs/ac725aaba8ec744b/statistical_methods.csv` | `.csv` | 1,424 |
| `results/audit-v1/runs/ac725aaba8ec744b/statistical_methods.json` | `.json` | 877 |
| `results/audit-v1/runs/ac725aaba8ec744b/statistical_methods_tidal.json` | `.json` | 22,317 |
| `results/audit-v1/runs/ac725aaba8ec744b/statistical_methods_tidal_seg9_excluded.json` | `.json` | 42,366 |
| `results/audit-v1/runs/ac725aaba8ec744b/tide-conversion/professional_tidal_delta_30s.csv` | `.csv` | 10,962,045 |
| `results/audit-v1/runs/ac725aaba8ec744b/tide-conversion/professional_tidal_delta_30s.diff.json` | `.json` | 1,331 |
| `results/audit-v1/runs/ac725aaba8ec744b/time_quality.json` | `.json` | 16,263 |
| `results/audit-v1/runs/ba3c434326918289/manifest.json` | `.json` | 29,244 |
| `results/audit-v1/runs/ba3c434326918289/manifest.json.run.json` | `.json` | 57 |
| `results/audit-v1/runs/ba3c434326918289/parameter_conflicts.json` | `.json` | 7,719 |
| `results/audit-v1/runs/ba3c434326918289/parameter_ledger.csv` | `.csv` | 15,071 |
| `results/audit-v1/runs/ba3c434326918289/ratio_17seg.csv` | `.csv` | 2,981 |
| `results/audit-v1/runs/ba3c434326918289/ratio_17seg_summary.csv` | `.csv` | 477 |
| `results/audit-v1/runs/ba3c434326918289/sample_ledger.csv` | `.csv` | 1,690 |
| `results/audit-v1/runs/ba3c434326918289/statistical_methods.csv` | `.csv` | 1,424 |
| `results/audit-v1/runs/ba3c434326918289/statistical_methods.json` | `.json` | 877 |
| `results/audit-v1/runs/ba3c434326918289/statistical_methods_tidal.json` | `.json` | 22,388 |
| `results/audit-v1/runs/ba3c434326918289/statistical_methods_tidal_seg9_excluded.json` | `.json` | 42,386 |
| `results/audit-v1/runs/ba3c434326918289/tide-conversion/professional_tidal_delta_30s.csv` | `.csv` | 10,962,045 |
| `results/audit-v1/runs/ba3c434326918289/tide-conversion/professional_tidal_delta_30s.diff.json` | `.json` | 1,331 |
| `results/audit-v1/runs/ba3c434326918289/time_quality.json` | `.json` | 16,263 |
| `results/audit-v1/verification/20261007T161859Z/runs/cb10d16d8c687a50/ANALYSIS_AUDIT.md` | `.md` | 14,781 |
| `results/audit-v1/verification/20261007T161859Z/runs/cb10d16d8c687a50/manifest.json` | `.json` | 29,883 |
| `results/audit-v1/verification/20261007T161859Z/runs/cb10d16d8c687a50/manifest.json.run.json` | `.json` | 57 |
| `results/audit-v1/verification/20261007T161859Z/runs/cb10d16d8c687a50/parameter_conflicts.json` | `.json` | 7,710 |
| `results/audit-v1/verification/20261007T161859Z/runs/cb10d16d8c687a50/parameter_ledger.csv` | `.csv` | 15,062 |
| `results/audit-v1/verification/20261007T161859Z/runs/cb10d16d8c687a50/ratio_17seg.csv` | `.csv` | 2,981 |
| `results/audit-v1/verification/20261007T161859Z/runs/cb10d16d8c687a50/ratio_17seg_summary.csv` | `.csv` | 477 |
| `results/audit-v1/verification/20261007T161859Z/runs/cb10d16d8c687a50/sample_ledger.csv` | `.csv` | 1,690 |
| `results/audit-v1/verification/20261007T161859Z/runs/cb10d16d8c687a50/statistical_methods.csv` | `.csv` | 1,441 |
| `results/audit-v1/verification/20261007T161859Z/runs/cb10d16d8c687a50/statistical_methods.json` | `.json` | 894 |
| `results/audit-v1/verification/20261007T161859Z/runs/cb10d16d8c687a50/statistical_methods_tidal.json` | `.json` | 18,010 |
| `results/audit-v1/verification/20261007T161859Z/runs/cb10d16d8c687a50/statistical_methods_tidal_seg9_excluded.json` | `.json` | 38,348 |
| `results/audit-v1/verification/20261007T161859Z/runs/cb10d16d8c687a50/tide-conversion/professional_tidal_delta_30s.csv` | `.csv` | 10,962,045 |
| `results/audit-v1/verification/20261007T161859Z/runs/cb10d16d8c687a50/tide-conversion/professional_tidal_delta_30s.diff.json` | `.json` | 1,370 |
| `results/audit-v1/verification/20261007T161859Z/runs/cb10d16d8c687a50/time_quality.json` | `.json` | 16,263 |
| `results/audit-v1/verification/20261007T172640Z/runs/03b02b974391582e/ANALYSIS_AUDIT.md` | `.md` | 15,267 |
| `results/audit-v1/verification/20261007T172640Z/runs/03b02b974391582e/manifest.json` | `.json` | 30,819 |
| `results/audit-v1/verification/20261007T172640Z/runs/03b02b974391582e/manifest.json.run.json` | `.json` | 57 |
| `results/audit-v1/verification/20261007T172640Z/runs/03b02b974391582e/parameter_conflicts.json` | `.json` | 7,710 |
| `results/audit-v1/verification/20261007T172640Z/runs/03b02b974391582e/parameter_ledger.csv` | `.csv` | 15,062 |
| `results/audit-v1/verification/20261007T172640Z/runs/03b02b974391582e/ratio_17seg.csv` | `.csv` | 2,981 |
| `results/audit-v1/verification/20261007T172640Z/runs/03b02b974391582e/ratio_17seg_summary.csv` | `.csv` | 477 |
| `results/audit-v1/verification/20261007T172640Z/runs/03b02b974391582e/sample_ledger.csv` | `.csv` | 1,690 |
| `results/audit-v1/verification/20261007T172640Z/runs/03b02b974391582e/statistical_methods.csv` | `.csv` | 1,441 |
| `results/audit-v1/verification/20261007T172640Z/runs/03b02b974391582e/statistical_methods.json` | `.json` | 894 |
| `results/audit-v1/verification/20261007T172640Z/runs/03b02b974391582e/statistical_methods_tidal.json` | `.json` | 22,396 |
| `results/audit-v1/verification/20261007T172640Z/runs/03b02b974391582e/statistical_methods_tidal_seg9_excluded.json` | `.json` | 42,453 |
| `results/audit-v1/verification/20261007T172640Z/runs/03b02b974391582e/tide-conversion/professional_tidal_delta_30s.csv` | `.csv` | 10,962,045 |
| `results/audit-v1/verification/20261007T172640Z/runs/03b02b974391582e/tide-conversion/professional_tidal_delta_30s.diff.json` | `.json` | 1,370 |
| `results/audit-v1/verification/20261007T172640Z/runs/03b02b974391582e/time_quality.json` | `.json` | 16,263 |
| `results/audit-v1/verification/20261007T173310Z/runs/327182fd8fec6c16/ANALYSIS_AUDIT.md` | `.md` | 15,267 |
| `results/audit-v1/verification/20261007T173310Z/runs/327182fd8fec6c16/manifest.json` | `.json` | 30,820 |
| `results/audit-v1/verification/20261007T173310Z/runs/327182fd8fec6c16/manifest.json.run.json` | `.json` | 57 |
| `results/audit-v1/verification/20261007T173310Z/runs/327182fd8fec6c16/parameter_conflicts.json` | `.json` | 7,710 |
| `results/audit-v1/verification/20261007T173310Z/runs/327182fd8fec6c16/parameter_ledger.csv` | `.csv` | 15,062 |
| `results/audit-v1/verification/20261007T173310Z/runs/327182fd8fec6c16/ratio_17seg.csv` | `.csv` | 2,981 |
| `results/audit-v1/verification/20261007T173310Z/runs/327182fd8fec6c16/ratio_17seg_summary.csv` | `.csv` | 477 |
| `results/audit-v1/verification/20261007T173310Z/runs/327182fd8fec6c16/sample_ledger.csv` | `.csv` | 1,690 |
| `results/audit-v1/verification/20261007T173310Z/runs/327182fd8fec6c16/statistical_methods.csv` | `.csv` | 1,441 |
| `results/audit-v1/verification/20261007T173310Z/runs/327182fd8fec6c16/statistical_methods.json` | `.json` | 894 |
| `results/audit-v1/verification/20261007T173310Z/runs/327182fd8fec6c16/statistical_methods_tidal.json` | `.json` | 22,396 |
| `results/audit-v1/verification/20261007T173310Z/runs/327182fd8fec6c16/statistical_methods_tidal_seg9_excluded.json` | `.json` | 42,453 |
| `results/audit-v1/verification/20261007T173310Z/runs/327182fd8fec6c16/tide-conversion/professional_tidal_delta_30s.csv` | `.csv` | 10,962,045 |
| `results/audit-v1/verification/20261007T173310Z/runs/327182fd8fec6c16/tide-conversion/professional_tidal_delta_30s.diff.json` | `.json` | 1,370 |
| `results/audit-v1/verification/20261007T173310Z/runs/327182fd8fec6c16/time_quality.json` | `.json` | 16,263 |
| `results/comp_shanghai-wuhan-beijintime.csv` | `.csv` | 15,442,754 |
| `results/professional_tidal_delta_30s.csv` | `.csv` | 8,243,522 |
| `results/solid_tide_old_30s_utc.csv` | `.csv` | 8,627,917 |
| `run_all.py` | `.py` | 11,706 |
| `uv.lock` | `.lock` | 56,855 |

</details>

### 原项目保护核对

初始与建档前对全部普通文件的相对路径、大小、mtime_ns排序计算SHA-256摘要一致：

`889e80c24f8f36a713e4d841753379ff4a204e681850f5d1bc6046c6f41eb2c2`。

建档后再次检查该摘要，须一致才完成交付。此检查覆盖.git普通文件的相同元数据，不执行Git命令；未对18.43 GB内容做全量哈希，不声称检测得到所有可能的同大小/同mtime内容变化。
