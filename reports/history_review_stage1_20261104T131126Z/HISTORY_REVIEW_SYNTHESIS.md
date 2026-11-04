# 历史 REVIEW 汇总：第一阶段

生成：2026-11-04T13:28:25.588430+00:00。**25项SUMMARY_ONLY已逐项读取并汇总，25/25文件SHA256与接管记录一致，文本与SQLite结果一致；任务仍为REVIEW，没有自动批准。** 本轮形成统一证据目录及12项差异登记，未启动正式拟合、模拟或新的科研任务。

入口：[统一科研证据目录](EVIDENCE_CATALOG.md) · [25项任务ID、Agent、完整路径与SHA256](TASK_REVIEW_SYNTHESIS.csv) · [严格差异登记](DISCREPANCY_REGISTER.md) · [下一步及保留任务清单](NEXT_ACTIONS.md)。

VERIFIED：本轮已直接核查所注明的文件身份、记录内容或摘要算术；必须带范围，不代表硬件认证、完整独立复现或任务批准。AUTHOR-REPORTED：作者、PI或专家已有报告的陈述，本轮未独立重演其观测/测试/计算。PENDING：尚缺同版本定义、实验记录或独立核对。BLOCKED：缺口已阻止所列更强主张或验收，仍保留已有证据。一个结果文件可身份VERIFIED而其科学主张仍PENDING/BLOCKED。

研究问题是：现有成果在何种证据范围内能支持Nature第二阶段叙述，哪些差异仍需核对。本轮是既有材料汇总，不是新的观察性分析。原研究涉及54段、5个campaign及声明的29个操作组；一秒记录、重叠滤波点和重复段成员有相关性，均不视作独立重复。没有生物学/技术重复的对应概念，也未引入随机化、盲法或新增实验单位。重复结论按20个C编号归并，保留各专家任务ID，不能把重复报告当成独立重复研究。

**主值与不确定度。** [X01](SOURCE_LOCATIONS.md#x01)、[X25](SOURCE_LOCATIONS.md#x25)支持本地保存的
$A=0.857260242008892\pm0.1775932570274874$，两位小数确为0.86±0.18（C01 VERIFIED〔保存值与算术〕）。这是M2+N2共同尺度、含campaign太阳项的估计，误差为max(scaled LS, day jackknife)的一标准差口径；不是95%置信区间。LS为0.1276029903928968，JK为0.1775932570274874；77×77保存协方差对应LS。A/u=4.827099只是一项比值，不能转换为已校准实验显著性。作者同版源行、分组、模板和全部结果认证仍PENDING，不能因为主值舍入一致就宣布整篇通过。

P6保存124/200=.62，作者为.69；P8瞬态处理后p=.0601816487，作者为.21；P9保存(3.9167139±1.2801292)×10⁻¹⁸，作者为(2.8±1.3)×10⁻¹⁸。P9还存在三组潮汐联合/全潮联合、LS/max/JK的目标与误差差别，尚不能归因于单一算法。各项进入D03—D05严格核查，均保持PENDING；没有重新选择参数、权重、掩膜或模型来迎合作者数字。P6保存Wilson 95%区间[.551067,.684410]包含名义.6827，现有200次不足以断言普遍低覆盖。

当前主结果表的瞬态前成员1,966,077，对应546.1325名义小时；瞬态后1,957,294，对应543.6927778小时；3186个滤波输出按600秒折算531小时。这些与旧表1,987,674/1,977,991成员、3221输出分别保留。当前后处理四舍五入与作者544h相容，但不能由此认证逐行支持相同。夏季1391.39h是日历跨度，不是累计观测小时。[S01](SOURCE_LOCATIONS.md#s01)、[S09](SOURCE_LOCATIONS.md#s09)、[X03](SOURCE_LOCATIONS.md#x03)、[X04](SOURCE_LOCATIONS.md#x04)、[X06](SOURCE_LOCATIONS.md#x06)。54段、3186点均非独立样本量；本轮没有新增检验或多重比较，因此不产生新的P值/置信区间。

**2025/2026频率配置。** 2025关系已由PI提供（C05 AUTHOR-REPORTED），[X11](SOURCE_LOCATIONS.md#x11)保留原文：上海N1397=858456、N1550=773598及10.93629485系数；武汉N1156=1295739、N1550_WH=966996；传输到武汉比上海发出光高f10M_SH；武汉CEO=26 f10M_WH，计数值
$f_{beat}=[f_{1550WH}-(26f_{10M\_WH}+N_{1550\_WH}f_{repWH})]/2$。约66 MHz是二分频后的记录值，不能对已乘2恢复的接口再乘2。2026稿件描述约33.6 MHz拍频，已有接口因子1；两个年度的梳齿/参考、方向与时间范围需分别绑定，名义10M不能替成精确常数。逐文件、通道、配置切换和在线校正仍PENDING（D07），本轮没有反演或应用转换。2025关系也不自动补齐BBR、同步或Freq_A链路通道传递系数。[S01](SOURCE_LOCATIONS.md#s01)、[S10](SOURCE_LOCATIONS.md#s10)、[X05](SOURCE_LOCATIONS.md#x05)、[X26](SOURCE_LOCATIONS.md#x26)。

**长链与实验室支路。** PI及PRL描述1350 km长链的round-trip环外监测；无单程测试点。另有几百米实验室周边传递支路无监控（C07 AUTHOR-REPORTED）。Freq_A候选通道与Freq_B钟比值通道分开；不凭相关性选通道、符号、时移，不自动除2，不以10/35 MHz RF中心替代光载频归一化。PRL的DDS参考量化预算不构成全部时变传递噪声上界。长链阴性结果也不能排除未监控支路、非互易项或缺测的7月7日事件，所以“全部光纤影响已排除”仍BLOCKED（C08/D10）。[X12](SOURCE_LOCATIONS.md#x12)、[X13](SOURCE_LOCATIONS.md#x13)、[X45](SOURCE_LOCATIONS.md#x45)、[X46](SOURCE_LOCATIONS.md#x46)。

**M2+N2模板与同步。** 同源复模板相加后取C/S，共同尺度保留M2/N2相对结构；固定相位有符号系数与自由a,b不同。b=0包含反相，联合区域近原点时不能报告确定相位；共同旋转也不等于各分潮按频率产生的时间延迟。模板中的固体潮与负荷是模型组成，不是分别实测的检出。文档定义已核读（C09 VERIFIED〔定义〕），完整模板及频率/势符号实验闭合仍待核。[S02](SOURCE_LOCATIONS.md#s02)、[X19](SOURCE_LOCATIONS.md#x19)、[X25](SOURCE_LOCATIONS.md#x25)、[X27](SOURCE_LOCATIONS.md#x27)、[X28](SOURCE_LOCATIONS.md#x28)。

国内原始记录时区已由PI明确为BJT，后续说明覆盖旧审计“时区未知”，不再要求重复确认，已转UTC数据不再减8小时。但PC标签精度、两计数器对时、门起/中/终点、重叠/死时间和重启记录仍PENDING；作者±10 min敏感性不是实际同步范围。时间未知不能通过A接近1或相位接近0来选择偏移；没有独立校准范围，不能给设备相位或总95%不确定度认证。[S01](SOURCE_LOCATIONS.md#s01)、[S02](SOURCE_LOCATIONS.md#s02)、[X12](SOURCE_LOCATIONS.md#x12)、[X20](SOURCE_LOCATIONS.md#x20)、[X27](SOURCE_LOCATIONS.md#x27)。

**噪声与内部预测。** 主LS/JK误差、循环移位SD及固定估计V的GLS分别列出。已有经验GLS为0.8691648589±0.1411959312，ADEV GLS为0.9106417421±0.1715021747；它们是不同噪声假设下保存的条件结果，不按误差较小选主结果，未覆盖噪声超参数、跨运行相关和未知共同校正的完整不确定度。固定mask循环移位不是重跑选择流程，Kalman无太阳项全潮对照也不是主月潮或绝对水平认证。[S08](SOURCE_LOCATIONS.md#s08)、[X01](SOURCE_LOCATIONS.md#x01)、[X02](SOURCE_LOCATIONS.md#x02)。

E1保存表348行（29折×12候选）的只读重汇总支持S19更正：campaign_FIX0平均loss243.6298，较其NULL251.4750改善7.8452；linear_P45较其NULL改善567.3292，但绝对loss66681.9296，不能称绝对预测更好。原interpretation_stopped=true保留；内部固定模型改善不解除特异性筛查，也不构成外部验证。作者0/20000尾概率仍AUTHOR-REPORTED；E5条件代码及有限模拟不能代替完整全54段尾部或硬件认证。本轮未处理等待人工的E5结果。[S19](SOURCE_LOCATIONS.md#s19)、[S23](SOURCE_LOCATIONS.md#s23)、[S25](SOURCE_LOCATIONS.md#s25)、[X16](SOURCE_LOCATIONS.md#x16)、[X18](SOURCE_LOCATIONS.md#x18)、[X28](SOURCE_LOCATIONS.md#x28)。

**绝对分支与版本更新。** S21既有E2/E4算术审计保留；E2夏季TS-ABS .9183671414±.1880553077仅作条件结果引用。四五月校正后来被标为存疑，E4 .5232850436±.1635741715只能是该校正情景下的历史结果。旧“月内适用有效”陈述保留时间背景，当前解释以X09/X10为准，不能推断五月真实异常、设备故障或长周期检出。夏季39—54主线是后续校正状态，不追改历史54段主值。[S21](SOURCE_LOCATIONS.md#s21)、[S25](SOURCE_LOCATIONS.md#s25)、[X09](SOURCE_LOCATIONS.md#x09)、[X10](SOURCE_LOCATIONS.md#x10)、[X15](SOURCE_LOCATIONS.md#x15)。

**欧洲参考与新颖性。** 仅比较用户所供本地版本《Optical clock network tracks tidal variations of the gravity potential》，不进行新文献搜索或推断最新发表状态。该文已有动态潮汐、含海洋负荷模型、异种钟、随机游走基线与固定A的Kalman、同址零对照；其1.42(35)、1.12(24)、合并1.00(12)是全潮目标，不能与沪汉M2+N2主值直接排名。欧洲10 min不重叠均值/30%覆盖门槛与沪汉1200s三角窗/600s步长也应分列。[X31](SOURCE_LOCATIONS.md#x31)、[X32](SOURCE_LOCATIONS.md#x32)、[X33](SOURCE_LOCATIONS.md#x33)、[X34](SOURCE_LOCATIONS.md#x34)、[X35](SOURCE_LOCATIONS.md#x35)、[X36](SOURCE_LOCATIONS.md#x36)、[X37](SOURCE_LOCATIONS.md#x37)。

可继续论证的候选差异是：在沪汉海岸—内陆记录中，将M2+N2与显式campaign 24/12h项分离，并说明稀疏采样和夏季相位覆盖提供的辨识范围。它仍是PENDING的新颖性主张，不是已证实方法优势；不能声称欧洲有未证实污染，不能以地点、A接近1或地理差别证明创新。沪汉自身PRL夏季16段复用须披露，也不能再次宣称首次动态潮汐或独立海洋负荷检出。[S08](SOURCE_LOCATIONS.md#s08)、[S11](SOURCE_LOCATIONS.md#s11)、[S13](SOURCE_LOCATIONS.md#s13)、[X25](SOURCE_LOCATIONS.md#x25)。

不同意见均保留：S08/S09文档指纹/阈值/路径问题由X07记录修订，六项当前文档与旧备份哈希均相符；S17对E2 v1的缺陷和S19对v2的技术关闭同时归档；S24“10项通过”与S25“online_chain_corrections缺口”同时成立，v2另待技术复审。没有用后续结论抹去原报告或将技术READY变成科研批准。

方法与复现：输入为25个既有结果文件及46个限定补充来源，使用SHA256、逐字节文本比较、只读SQLite事务、JSON字段回读、Decimal摘要求和/舍入及保存协方差首元素开方。未读取原始观测数组、导入科研脚本、重新筛选、拟合、模拟或绘图；不涉及新增随机种子。Python 3.12.3、SQLite 3.45.1，仅标准库。P6的seed=20261103/stream=400是保存结果的历史参数。脚本、实际执行时间与全部输出见[运行记录](evidence/run_metadata.json)和[摘要算术](evidence/saved_result_arithmetic.json)。重放只读核查时输出目录必须不存在：

```bash
/data/AI_Research/environments/python/sci/bin/python -B /data/AI_Research/projects/gravitation-whsh/manuscript_48h/history_review_stage1_20261104T131126Z/scripts/audit_saved_evidence.py --out /data/AI_Research/projects/gravitation-whsh/manuscript_48h/history_review_stage1_20261104T131126Z/evidence/audit_replay_02
```

本轮新表为TASK_REVIEW_SYNTHESIS.csv、HOLD_REGISTER.csv及CLAIMS/DISCREPANCY_REGISTER.json；未生成新科研图片，原图路径由S20/S22原报告保留。报告不能代替作者同版数值复现、实验装置认证、全文新颖性评审或正式拟合许可。

保留核验：SQLite 11表的有序行内容指纹与本轮前快照完全一致，43项任务仍为37 REVIEW、3 FAILED、1 CANCELLED、2 PENDING；47项历史审批仍为45 CONSUMED、2 APPROVED，后两项是历史记录，本轮新增批准为0。25项SUMMARY_ONLY仅在新目录中完成汇总，未改状态；10项HUMAN_REVIEW_REQUIRED、2项TECHNICAL_REVIEW_PENDING、3项FAILED、2项历史PENDING及1项CANCELLED原样保留。没有专家RPC、服务重启/中断、任务重派、原始数据/旧报告修改或GitHub上传。

本阶段交付后等待人工下一步指示。NEXT_ACTIONS仅为待决定目录，不是执行队列。
