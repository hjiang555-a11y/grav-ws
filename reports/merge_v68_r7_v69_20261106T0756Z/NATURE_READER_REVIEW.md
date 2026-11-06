# Nature 广泛读者与编辑视角：单轮评审

评审对象：`NATURE_ARTICLE_v68_R7_WORKING.md`（上一轮已交付工作稿）。范围：论文叙事、证据措辞、主文与Methods分工、引用；没有新做拟合。实际使用ECC `article-writing` 与 `scientific-thinking-scholar-evaluation`。主笔负责修改全文，本文件只给出一轮意见。

**结论：物理问题值得讲清楚，但当前稿子像两条分析管线的验收报告。最紧急的新增错误是参考文献被生成程序替换成扩展数据目录。** 去掉标题的Lunar合理；用光钟网络作简短入口也合理。正文应让读者先看到两种半日节律在同一联合模型中得到不同系数，再说明地理与采样为何允许这样做。主估计器未定、v68主链缺项和作者声明是投稿阻碍，不能通过删句假装完成。

## 六项优先修改

1. **[P0，实际生成错误] 修复参考文献解析，而非仅重编号。** 已交付稿References 2–6写成“Campaign time series”“Local-time and blackbody diagnostics”“Campaign amplitudes”“Resampling calibration”“Separate-reduction comparison”。这些不是书目。`assemble_working.py`从整个v68文件匹配数字列表并构建字典，后面的Extended Data目录覆盖了旧编号1–5。修复应只读References和Methods references区段，拒绝重复编号；再按首次引用绑定。验收必须检查实际作者/题名/DOI，不能只检查没有未绑定占位符或编号连续。此错误已经告知主笔，应在本轮闭环报告中如实记录。

2. **[P0，推断边界] 区分“分开估计两组响应”与“分别检测纯太阳和纯月球分潮”。** M2+N2和S2+K2联合拟合是本稿的对象，K2为日月共同作用。现有误差和协方差支持明确报告两组响应；单独M2、N2、S2、K2并未都被自由估计。R7现有条件覆盖表针对A_L，不能自动称为A_S或两组联合检出校准。不要为了去掉Lunar，把标题升级为未经验证的“独立检测太阳与月球”。首选标题为 **Tidal potential measured on a coastal–inland optical-clock baseline**。备选 **Semidiurnal tidal potentials on a coastal–inland optical-clock baseline**。在技术组核查前，用“separately estimate the lunar and neighbouring semidiurnal responses”最稳妥。

3. **[P1，可立即修改] 给读者一个三句以内的钟网络入口。** 第一段目前一开始就是M2/S2，第二段才解释为什么钟能测势，顺序应调整。建议逻辑：不同引力势使钟的速率不同 → 光纤允许远端光钟作这种比较 → 潮汐给出小时尺度变化、相位已知的试验信号。然后引入M2约12.42 h、S2为12 h，日期变化带来的相对相位是分离手段。Stahl摘要有效的顺序正是物理效应、网络、动态势；借鉴这个解释层次即可，无须借用其主张或措辞。

4. **[P1，可立即修改] 把分析协调过程移出主文。** “Support across time and the estimator decision”中61%/50.2%、四个桥接系数、修正表示变化8e−5以及如何选择最终估计器，放入Methods、扩展表和合并记录。主文只留跨时段支持的可读结论及必要的一个子集对照。文中“v68”“R7”“saved tables”“replayed”“common-support audit”等工作流词汇可在Methods统一定义；工作稿状态另放一页作者说明。不能删除实际不确定性，但不必每段都汇报管理状态。未确定唯一主估计器时，这仍是工作稿；不能以排版决定科学主结果。

5. **[P1，可立即修改] 将技术名词换成物理动作，保留定量证据。** 海洋负荷直接解释为“海水重新分布引起的引力变化、地球形变以及钟的垂直位移”；三分之一预测贡献紧接0.89±0.55未分辨结果即可。相位图正文写“data and prediction receive the same background-removal and averaging steps”，将投影矩阵、rank11、每箱31–36日移到Methods/图注。主文优先陈述温度和往返记录实际覆盖的通道，ERA5室外代理与PT100实测只需一句区别。删去“Environmental evidence is strongest when…”等泛泛方法论开场，直接从所测渠道及数值开始。

6. **[P2，图与结尾] 让结果与读者的问题对应。** Fig.2平均相位曲线是最容易理解的观测展示；Fig.3并排的两组半日响应回答“是否分开”；Fig.4说明时段和实测控制。图注共同观测身份说明保留一次，不重复“不独立”“不混合”“不校准”的否定三连。结尾强调沿海–内陆势变化和相位多样性带来的测量能力，Hou重叠观测边界及Stahl互补位置留一段。不要以“尚未选择估计器”的管理任务作为文章结论；该状态仍需保留在作者说明和合并记录中。

## 开头的逻辑样例（供主笔改写，不是完整主文）

> Clocks at different gravitational potentials tick at different rates. Optical fibre links allow those rates to be compared between distant laboratories, making clock networks a way to measure the Earth's gravity potential. Tides provide a changing signal with a known astronomical phase. A coastal–inland comparison is particularly informative because moving ocean water changes both gravitational attraction and the height of the clocks.

接下来再讲M2和S2随日期改变相对相位，沪汉的间断长记录采到这些相位，联合估计M2+N2与S2+K2。引用采用稿内已有Lisdat、Riehle、Voigt及负荷基础文献。以上样例没有添加精度、优先权或新实验结论。

Stahl来源已核对官方摘要：[Optical clock network tracks tidal variations of the gravity potential](https://arxiv.org/abs/2610.39635)。其摘要由相对论速率效应进入静态与动态势，再介绍网络和不同基线。这种叙述顺序可参考；不必在本稿前三句点名欧洲。此处只读到官方摘要，未声称本轮完成该预印本全文复核。

## 评审量表

分数为当前工作稿编辑诊断，不是录用概率。总体约3/5；文字诊断把握高，完整物理/统计可投性取决于专门核查。

| 维度 | 分数 | 依据 |
|---|---:|---|
| 问题与贡献 | 4 | 相位分离与海岸–内陆联合势明确，尚被管线对账遮蔽 |
| 背景 | 3 | 基础文献足够，缺少简短网络发展解释 |
| 方法 | 3 | 两设计透明，但主估计器和共同物理模板尚未闭环 |
| 数据证据 | 3 | R7保存表可复算；v68主链及部分控制仍来源报告 |
| 分析 | 4 | 误差来源、协方差、删除及覆盖诊断清楚，不能跨目标转移校准 |
| 解释 | 3 | 群响应边界正确；纯太阳/纯月球“分别检出”需更精准 |
| 局限 | 5 | 具体且充分，但主文重复太多 |
| 写作结构 | 2 | 前半篇偏技术，主文含太多协调与验收语言 |
| 引文 | 1 | 生成错误造成5条非书目条目，需立即修复后重评 |

## 本轮验收要点

修复后的文献内容正确且首次出现顺序一致；标题无Lunar；前两段非领域读者可理解测量对象；主文不混合两稿权重、点和误差；“太阳/月球”的措辞与拟合群及校准范围一致；未完成的实验认证仍明确留在作者说明。只进行本轮意见对应的一次修改，不以反复改稿代替缺失实验输入。
