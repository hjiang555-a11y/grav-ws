# Task 1 改动与数值去向清单

基线：`7dc014f`。采用academic-humanizer的polish模式；作者最新裁定`AUTHOR_STEERING_20261109.md`高于先前“数字出现次数守恒”约束。没有科学重算。下文“主分析”是既有Auxiliary的编辑名称，“滤波验证”是既有Primary的编辑名称，不声称这些用途/名称在实验前预设。原始处理事实不变。

## 组织及证据表达

| ID | 原位置及原表述要点 | 新位置/处理 | 原因、技能规则 |
|:--|:--|:--|:--|
| E01 | Introduction首段同时列本地红移、网络、测地、暗物质和引力波应用 | 首段先陈述钟—势差—传递网络能力；原毫米原子样品、量级换算、量子网络及Gozzard传递文献均保留。测地互补句移入第二段；暗物质/引力波不在首段重复，但结尾保留原应用及来源38、62 | Rule 8段落单点、Rule 4.4减少重复；无独有内容删除 |
| E02 | Results基线段并列两种筛选/滤波和两种总时长 | 正文保留主分析545.9 h、54段、五campaign、353天及图1→2索引；滤波/样本参数仅由原有Methods/SI集中解释 | Rules 8/11，作者单主结果系列 |
| E03 | 总响应后给第二套lunar/near-12-h响应及Primary自由相位数值 | 仅给主分析0.96±0.11、1.00±0.13及其Fig.3相位证据；五campaign一致性与Fig.2时序明确标注滤波分析 | Rules 5/8/10；删值见D02 |
| E04 | 频谱扫描/联合拟合后用Primary0.90±0.29再次量化检出 | 保留扫描峰、条件谱、联合自由相位幅度；段末以Fig.3a预测相位组响应解释“同一组内固定S₂/K₂相位”与自由相位频谱证据的区别，不另给第二套组响应 | Rules 5/8；标题、摘要、separately detect/identifiable主张不改 |
| E05 | 月潮对daily影响先给Primary再给Auxiliary上界 | 只保留主分析0.023/0.030/0.12，保留10⁻¹⁸及24/12h、全记录共同相位/独立campaign相位条件；Fig.4清楚说明滤波验证，温度/链路/海岸敏感性也明确来源 | Rules 5/10，防止把两类上界或稳健性误用为S₂归因 |
| E06 | Results末节给另一套loading和diurnal响应，再解释与Table1不同 | 改为Table1现有SNR近unity的定性描述；原滤波弱响应与预测相容及Methods/SI索引保留，末句引出precision问题 | Rules 5/8；未把辅助loading响应强行搬入正文 |
| E07 | Discussion一般标度公式后直接提白噪声Table1 | 依次解释模型输入、offset吸收/耦合、一般公式、实际采样+实测幅度+共同噪声的本次实现、相同估计器误差的实际比较 | Rules 5/6/8；We develop及accounts for most保留；无噪声来源新归因 |
| E08 | 对照后观测建议混合时长/连续运行 | 保留两天及相位锁定要求，分别将稳定度、保留曝光、相位覆盖、日历跨度、站点和环境记录联系到已有模型因素；明确时间外推取决于噪声和采样效率 | Rules 6/8/10；不把标度宣称为已由累积观测验证 |
| E09 | 结论重述两谱峰及模型输入/吻合 | 压缩重复；保留测量与分离、模型、sub-centimetre背景及geodesy/dark matter/GW应用；最后回应秒重定义和厘米高程统一及原引用 | Rules 4.4/8 |
| E10 | Methods先大段Primary，Auxiliary及SNR在后 | 先共同钟链/记录，再完整主分析组响应、频谱和SNR配方；随后滤波验证的筛选、模型、拟合和环境检查。文件内外迁移完整公式，重采样/误差条件不改 | Rules 8/11、作者明确方法组织授权 |
| E11 | Methods重复报loading响应；SI SM3/SM6/对照表重复主响应系列 | 删除重复出现，未新建任何补存段落；保留SM3独有校准、SM4环境/耦合、SM5独立处理、SM6协方差/误差传播、Supplementary Table2主估计量 | Rule 4.4及作者明确删重复授权；见D06–D10 |
| E12 | 主图caption只用旧Primary/Auxiliary名称 | Fig.1b标示滤波记录来源，Fig.2/4标示滤波验证，Fig.3标示主分析与Auxiliary别名；原caption参数、图件路径、四图次序和宽度标签不改 | Rules 5/10；没有将图4重标为主估计 |
| E13 | h/H在后出现，文字写defined below | 方法顺序改变后改为defined in the signal-to-noise calculation；公式不动 | Rule 8，交叉指引随位置同步 |
| E14 | SI SM7 serves as an algebraic control | is an algebraic control | Rule 1 copula简化，代数性质不改 |

## 科学数字逐项删除/重复次数减少

所有删除都直接删除对应重复出现；没有新建Methods/SI段落保存第二套headline响应。表中“仍保留”指本轮之前已存在的位置，不是本轮迁入。

| ID | 来源 | 删除的出现及条件 | 仍保留/去向 |
|:--|:--|:--|:--|
| D01 | Results基线 | Primary544 h；1,200-s triangular/600-s steps；Auxiliary3,299 non-overlapping600-s means；同54段的第二次出现 | 这些配方、544h保留在Methods/Supp.Table4；主545.9h保留正文；两处理仍共享观测 |
| D02 | Amplitude, phase and coverage | Primary lunar0.97±0.14、near-12-h0.90±0.29；Primary free-phase幅度0.98±0.11及−6°±8°、segment-bootstrap条件 | 不搬移；独有相位验证已在原SM3及原图/表支持材料保留；主Fig.3b相位依据在正文 |
| D03 | Separate semidiurnal detections | Primary predicted-phase(S₂,K₂)0.90±0.29第二次正文出现 | 不搬移；用主Fig.3a的组响应定性解释估计对象；conditional spectra/free-phase幅度不改 |
| D04 | Reliability | Primary10⁻¹⁸/24h或12h、共同相位上界0.020及独立campaign相位0.032/0.12这一套重复条件与上界 | 正文仅保留Auxiliary同样扰动下0.023及0.030/0.12；原Fig.4数据/条件均不变 |
| D05 | Ocean loading and diurnal response | Primary loading0.89±0.55；two-band diurnal0.36±0.50 | 不搬移；原SM4/SM5及EDFig.2b仍有这些独有验证结果；正文Table1定性衔接 |
| D06 | Methods Primary fit | 20°、expectedA=1.32、solid-only1.19±0.20、loading0.89±0.55的重复报告 | 原SM4仍给出拟合参数/不确定度及实际采样预期；正文物理phasor20°不动；Methods改为配方和SM4索引 |
| D07 | Methods SNR | Auxiliary two-template A_solid1.08±0.32和A_loading0.49±0.54 | 删除额外四舍五入复述；主估计及误差定义保留在原Supp.Table2，未把其数字新增到正文 |
| D08 | SI SM3 | Primary full0.90±0.12及semidiurnal0.96±0.12的重复一句 | 不迁移；原EDFig.1等仍在；校准、phase/bootstrap、campaign一致性及条件均保留 |
| D09 | SI SM6 | Auxiliary full0.9551±0.1082、lunar1.0004±0.1320、nearby0.9251±0.3649的一句过细复述 | 原Supp.Table2已有其舍入后的主响应系列；SM6改为索引该表，phase-relaxed系数/独有误差传播不动 |
| D10 | Supp.Table4 | 整行Full template/lunar/near-12-h：Primary0.90±0.12/0.97±0.14/0.90±0.29，Auxiliary0.96±0.11/1.00±0.13/0.93±0.36 | 按作者“相同结果不需在methods/SI体现”的裁定删除比较行，只留真正方法对照 |
| D11 | Discussion结论 | 谱峰4.87/2.87cm重复一次 | 摘要及Results频谱首句保持原值，结论不再抄数 |

上表涉及的科学数学片段净删23个（只是出现次数，不是23项科学量）；显示公式全部字节守恒。对应净减少：`0.96±0.11`×1、`1.00±0.13`×1、`0.97±0.14`×2、`0.90±0.29`×3、`0.98±0.11`×1、`−6°±8°`×1、`0.89±0.55`×2、`0.36±0.50`×1、`A=1.32`×1、`1.19±0.20`×1、`A_solid=1.08±0.32`×1、`A_loading=0.49±0.54`×1、`0.90±0.12`×2、`0.96±0.12`×1、`0.9551±0.1082`×1、`1.0004±0.1320`×1、`0.9251±0.3649`×1、`0.93±0.36`×1。

技能脚本在数学外同时计参考编号/交叉索引。其净减少token为0.020×1、0.032×1、0.12×1、1×1、1,200×1、12×3、2.87×1、20×1、3,299×1、38,62×1、4.87×1、54×1、544×1、600×2；新增token为2×1、3×1、4×3，均属新增/调整的现有图表索引。不是新观测/新参数。整个原子样品、1cm/1mm/0.1mm句原样保留；脚本的“1”变化来自删改交叉索引，而不是删除换算值。

## 参数、公式、引用迁移

- 原auxiliary_methods的Grouped estimates、Spectra and constituent separation、Signal-to-noise ratios整体移到methods：包含NB=3299、600s、353.39d、54段、h₂=.6078、k₂=.3010、g=9.794、18constituents、所有权重/噪声系数、54offset及43UTC日协方差、353.3889d/0.03275μHz/0.002729μHz、条件扫描±.16μHz、共同α=5.4×10⁻¹⁶√s、式(2)/(3)及所有设计矩阵/误差传播公式。没有改值。
- 原methods的Data selection、Tidal model、Primary fit、Daily disturbances等整体移到auxiliary_methods，编译合并顺序仍为methods后接auxiliary_methods。其中只删除D06所列复述；其余筛选阈值、物理模型/格网、分量、重采样单位/次数、注入条件、温度和链路诊断完整保留。
- 移到auxiliary_methods的历史方括号引用转换为同ID的`^ID^`，因为构建脚本仅自动转换methods.md的方括号，不转换auxiliary_methods。不是新增或删除来源。
- 引言的8、54随测地句移至第二段；38、62在第一段的重复引用删去，结尾仍完整保留其应用及引用。Gozzard65与44/59保留首段。无来源丢失：整稿实际来源ID集合35项完全相同。编号重排由构建程序按首次出现执行。
- Table1容器、所有单元格和表注逐字不变；紧随表格的`As shown in Table 1`构建边界不变。所有显示公式内容多重集合完全相同；无数学公式重新解释或删除。

## 技能与意义核查

Rule8组织/衔接11组（E01–E10、E13）；Rule5/6/10证据与适用条件9组（E03–E08、E10–E12）；Rule4.4重复4组（E01/E09/E11/E06）；Rule11把运行细节集中到方法2组（E02/E10）；Rule1明确copula1组（E14）。同一组可对应多条规则，不把机械跨文件迁移计成新的科学改写。

`compare`实际退出1：数学外数字652→640，数学片段263→240，为上面逐项授权删除，不伪称“全数字不变”。真实限定词12→12，无LOST项。`citations unchanged(1)`是脚本面向LaTeX的识别口径，不能代替Markdown来源验证；另用支持caret/旧方括号的检查逐条得到35来源集合守恒。审核保留phase-locked loop、toolkit、robustness/effective等技术用语；残差resampling不是运行日志。仍有长技术句和caption条件，保留其必要内容；无证据占位、无新来源、无未授权S₂来源排除。

## 独立审阅修复轮1（基线d0abd39）

本轮只处理R1/R2及R3已获强溯源支持的部分，不改Results/Discussion、标题、摘要、图件或caption。

| finding | 准确修复及来源 | 技能规则与数值出现变化 |
|:--|:--|:--|
| R1 | 通用H投影公式之后明确：正文主上界使用主three-group设计、主采样、lunar/near12/diurnal模板、segment offsets及period-noise weights；Fig.4使用等权filtered-validation H；其后injection/environment/held-out均为filtered记录 | Rules5/8/10；没有恢复旧Primary上界、没有新增计算或结果数值 |
| R2 | 主方法首处列出lunar(M₂,N₂)、near-12-h(S₂,K₂)、diurnal(K₁,O₁,P₁,Q₁)，不再前指未定义的eight named constituents | Rules8/10；只在原组定义补列已有成员，不改模板或公式 |
| R3部分 | 主方法替换含糊own valid-interval selection：每预定义segment内beat偏离该segment中位数>10Hz者排除；每segment分别在BJT(UTC+8)600s墙钟网格求均值；每bin至少180名义1s成员；时间戳为名义grid centre。明确未应用的是filtered路线的additional running-median transient screen/triangular filter；Supp.Table4选择行同步 | Rules5/8/11；10Hz/600s/UTC+8来自已核实代码，180为已有实现阈值首次写入本稿，不是新选择或重算值；未添加既有审计的大量计数、未声称原window选择理由已知 |

### R1已有计算记录（只读，未重跑）

实际阅读`/data/AI_Research/projects/grav-ws/manuscript_48h/audit_v3_17_noAC_20261108T084244Z/checks/independent_checks.py`第6–14行及其已有`INDEPENDENT_CHECKS.json`：读取冻结`primary_rows.csv`（历史文件名，不等于本稿滤波Primary），`X=[lunar,near12,diurnal,segment-indicators]`，`sw=1/sigma`，QR作用于`X*sw`，`H=solve(U,Q.T)*sw`，取`H[0]`对24/12h正余弦投影，并按五campaign求独立相位norm之和。已有记录的24/12h common值分别0.02335443195184823/0.0024971519001481114，independent值0.030293427933105077/0.12372775120052779，对应正文原0.023/0.030/0.12舍入值。本轮只核对记录，不运行该脚本。滤波等权设计和Fig4对应来自既有Primary fit/Supp.Table4 equal weights及原Fig4说明，未换估计器。

### R3冻结输入与真实源码链（只计算文件hash）

已实际阅读`frozen_v72/evidence.json`的dataset_kind、table_sha256、input_sha256；amplitude_spectrum/RESULTS.json的input_manifest中frozen_v72/bins.csv哈希；raw.py:73/204–225、bins.py:58–60/97–127/159起、run.py:194–230。bins实际SHA256与两个metadata相同：`860b442aad8b1c39ad750aa27af0d8766cf210ae9b013006169d77fdb9e93d8d`。

源码公共前缀`/home/room115/gravitation-whsh/research/opencode-period-offset-20261105/pipeline/`。以下实际文件SHA256均与frozen evidence相同：raw.py=`a4714492e6f6a14da7a63765086781d52f33b686d4c49b7ba6683afdc3e3c720`；bins.py=`bcfbc5c14703b5b8a8666a196d5f9ab1df07f185962caec6affc3d2a4f972eb9`；run.py=`c96c640b81599d5dc0bce020164cf69f6708f1e2d6bdb2df0db4870228d8c5d3`；rules.py=`61bf355950faf7e19ddde8033e0e6798a468dffb7693d2a778702c50c939cb23`。原metadata还链接raw输入哈希；本轮没有读取或重跑raw观测处理。

### 本修复轮机器核对

`academic-humanizer compare --changes`：数字640→646，仅新增10×1、12×1、180×1、4×1、600×1、8×1。10/600/180/8分别为已核实筛选、网格、最小支持及时区；12为已定义near-12-h组在H指引中的重复，4为Fig4指引。没有数值删除；数学240→240完全一致；限定词12→12无LOST；无证据占位。原标题、摘要188词、正文全部文字（因本轮未修改Results）、Table1及其正则边界、66个图件、所有caption和Markdown布局均精确相同。R3窗口原始选择理由仍未闭合；R4检出证据强度/太阳同频来源边界及R5时长整数和问题仍由作者控制，不因本轮文本澄清而宣称关闭。
