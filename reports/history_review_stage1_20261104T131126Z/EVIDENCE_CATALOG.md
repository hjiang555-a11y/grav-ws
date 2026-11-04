# 统一科研证据目录

生成：2026-11-04T13:28:25.588430+00:00。范围为25项SUMMARY_ONLY；46份补充来源仅用于核对这25项引用的数值、定义及后续更正，不新增任务验收。

VERIFIED：本轮已直接核查所注明的文件身份、记录内容或摘要算术；必须带范围，不代表硬件认证、完整独立复现或任务批准。AUTHOR-REPORTED：作者、PI或专家已有报告的陈述，本轮未独立重演其观测/测试/计算。PENDING：尚缺同版本定义、实验记录或独立核对。BLOCKED：缺口已阻止所列更强主张或验收，仍保留已有证据。一个结果文件可身份VERIFIED而其科学主张仍PENDING/BLOCKED。

机器清单：[逐任务CSV](TASK_REVIEW_SYNTHESIS.csv)；[统一主张JSON](CLAIMS.json)；[补充来源清单](supplemental_sources.json)；[实际只读核查输出](evidence/run_metadata.json)。

25项均保留SQLite REVIEW。S01/S02为接管阶段从旧SQLite结果原文导出的文件，本轮再次逐字节核对与SQLite一致；其余直接读取既有专家结果文件。

| 来源 | 任务ID / Agent | 结果文件 | SHA256 | 归并主张 / 结论状态 | 逐项处理记录 |
|---|---|---|---|---|---|
| S01 | `3b82c96328ae4aa5a0f8e5aed4ac41d9`<br>data_agent | [旧样本账本与时间基准审查](SOURCE_LOCATIONS.md#s01) | `738893702f92a168bd5c3e43ebf1a373b3cbaf813b99c17d6dc6ab19432b05ab` | C03 C04 C10<br>PENDING | 旧样本/时间审计仅验证文档相容；保留成员数与唯一行差别。旧“时区未知”被X12覆盖；同步/门时刻仍待证据。 |
| S02 | `a441fcfb26cc4cba8c52b143f7e3b19e`<br>physics_agent | [旧v1相位与频率符号规范审查](SOURCE_LOCATIONS.md#s02) | `912b0888e2a828d5efef9589c057f6b8517501c1cfe18851defdfbc7f48e707f` | C05 C06 C09 C10<br>PENDING | 旧v1共同相位代数成立；旧极性缺项须结合新PI频率关系。v1与当前模板方向不得混用，自由相位不代替对时。 |
| S03 | `c6f4abd48a7a47088d3d982a403d4f8b`<br>data_agent | [数据专家只读联调](SOURCE_LOCATIONS.md#s03) | `9087468c247c75573c81e65b6dd3087ccfa1251dcfc22c1c2e9e9fd3b12c79fc` | C20<br>VERIFIED | 只读联调结果与历史管理证据归档；文件身份已核，不将联调成功计作科研认证。 |
| S04 | `939f89f126974147bfc6067602796c3a`<br>physics_agent | [物理专家只读联调](SOURCE_LOCATIONS.md#s04) | `ca36889f247216ad0a85f2e1cc93aa4c5d6a327a6879f8fced2b152f8b6c7ef8` | C20 C09<br>VERIFIED | 物理角色联调归档；重复规范边界并入C09/C20，不新增独立科研证据。 |
| S05 | `6ec3234b3edd413f86bbf28de54e4b37`<br>statistics_agent | [统计专家只读联调](SOURCE_LOCATIONS.md#s05) | `60b22679e7ac952e05300b1182e16eafd4a5275dceba9a25d6a6bfad5a434179` | C20 C11<br>VERIFIED | 统计角色联调归档；误差/权限保留与后续统计证据合并，不新增样本或检验。 |
| S06 | `00c370db174640ddb552504d08ad7f40`<br>audit_agent | [审查员只读联调](SOURCE_LOCATIONS.md#s06) | `d3a2b7aaa3ae8c032417a02d11ecc47bf327a095bc3efafea0eac6d2b0475438` | C20<br>VERIFIED | 审查角色联调归档；仅保留管理过程事实，不代表作者批准。 |
| S07 | `dcbd0d8781394846aefedf27333902f8`<br>audit_agent | [系统交叉验收](SOURCE_LOCATIONS.md#s07) | `0680dc51f2e042c84a921e6b77537d42bf95783d385d82e2456b0c07f0861fa1` | C20<br>VERIFIED | 原系统交叉验收的中断证据保留后被S08及接管记录补齐；不能把旧PENDING或旧agent字段当当前状态。 |
| S08 | `5d67d827cbcb4f29a260402fb429e453`<br>audit_agent | [第二阶段交叉审查与修订意见](SOURCE_LOCATIONS.md#s08) | `bd68acab3a9c6640317a8f0003e9b2ce79e613c3a2319bb4d6249a311547d206` | C01 C02 C03 C12 C18 C19 C20<br>PENDING | 保留v13指纹错误、P9目标差异和误差边界；文档修正由X07闭合，全文/硬件/作者同版认证仍未闭合。 |
| S09 | `8664a1a8f50d4e7fab2cfc2967591403`<br>data_agent | [第二阶段文档回读](SOURCE_LOCATIONS.md#s09) | `54eaee83f0e053f00e0780d4b8ec36c915a585d6ba38e996a65c597751593154` | C01 C03 C19<br>VERIFIED | 25文件之外的所引主结果表算术已复算；阈值简称、路径、排版与测试日志问题有后续修订链。未重新提取PDF。 |
| S10 | `69530a5f4b1e423d8f82d8a3048d21f8`<br>data_agent | [数据挖掘路径设计](SOURCE_LOCATIONS.md#s10) | `b24c86bcf8ff4a47f36994b9c51c12188b01b418ab52093a353d17e08d6e21a1` | C04 C06 C10 C11<br>PENDING | 数据质量/太阳项/夏季校正三条设计汇入统一待办；NPZ头和源码可用性不等于原始数据绑定。 |
| S11 | `628ced8b26634fcba1c11d3ffbd69a34`<br>physics_agent | [物理可证伪假设设计](SOURCE_LOCATIONS.md#s11) | `306b75c1a85f5067e0d77fbce0145b469c894913f5e0d162773252d84a307192` | C07 C08 C09 C18<br>PENDING | 物理可证伪设计保留；绝对水平、长周期、负荷及温度因果不能由建议或模板图认定检出。 |
| S12 | `55504198f06e474cbf79fb11ab85ebae`<br>statistics_agent | [统计三项有限实验设计](SOURCE_LOCATIONS.md#s12) | `44aa830e35377dbb0ca532c5188728e51f9c20a73756c354004d58259353aa05` | C11 C14 C16<br>PENDING | 三项有限实验设计保留预定比较和停止条件；不把方法建议、相似数值或新增情景作为放行。 |
| S13 | `7a8cdecb25ba460e8e3c4ef186f85d2d`<br>audit_agent | [独立反证与停止条件设计](SOURCE_LOCATIONS.md#s13) | `d0312cab9287b32bc201ba854437608a5a8c91b708c6eba526dacf40af6bd908` | C02 C08 C12 C14 C18<br>PENDING | 独立反证/停止条件与其他设计合并；错误相位、零对照、噪声及选择效应要求均保留。 |
| S14 | `d3b278fc79434f0fb6c5d645351199cc`<br>statistics_agent | [E1代码实现](SOURCE_LOCATIONS.md#s14) | `309e850f1e470bf69596cb396628a03b2947a3006d5b507e73458ac893626fb3` | C14 C16<br>AUTHOR-REPORTED | E1代码交付/自测是专家记录；本轮不执行。可核读后续保存表，但不接收其结果任务。 |
| S15 | `e30c185da50d466fa3aae7cae1fca5e8`<br>physics_agent | [E2 v1代码实现](SOURCE_LOCATIONS.md#s15) | `119aeea3c94e4edb9d66725ba9e345ea82e89d73f18c8c6489f81db2f6af12ca` | C16<br>AUTHOR-REPORTED | E2 v1交付保留；S17发现R_PRL绑定缺陷后由S18/S19记录v2修复，不以v1自测代替复审。 |
| S16 | `c3459b23d59c4e7198b9dae58092c295`<br>data_agent | [E3代码实现](SOURCE_LOCATIONS.md#s16) | `3456f25dd1372e5f11754fe302b6ebea219d8c86d6c4f33aff57b45974b5e13d` | C16<br>AUTHOR-REPORTED | E3代码交付保留；算法质量关联不等于设备故障判定，不产生新的剔除规则。 |
| S17 | `bdf2bf442b914d5c9a8cc93d9c26e2ff`<br>audit_agent | [E1/E2/E3运行前独立审查](SOURCE_LOCATIONS.md#s17) | `5f8ad718ec180734e6cc9a06cd116272a5e9037b51c329583c3bec706b74160c` | C16<br>AUTHOR-REPORTED | E1/E3条件READY及E2 v1问题完整保留；HIGH/MEDIUM为当时版本结论，后续技术关闭不等于实验认证。 |
| S18 | `6b8c3458250247e98039a58f5bf50f8e`<br>physics_agent | [E2 v2与E4代码修复](SOURCE_LOCATIONS.md#s18) | `ada497f0aa5065e1321771f5340ffe31fe4a174e065eafcb9f7e17f7b88a1662` | C15 C16<br>AUTHOR-REPORTED | E2 v2/E4实现及自测归档；当时四五月月值输入假设被X09/X10更新，保留原报告。 |
| S19 | `12fbb8b1a0404ca5bc2989b5bde090e8`<br>audit_agent | [E2 v2/E4独立复审及E1解释纠正](SOURCE_LOCATIONS.md#s19) | `9fb3bdce858a7a38f8bb9c1f14b9ba72cc323e71efbc4b4afc06f86e14003c99` | C14 C15 C16<br>VERIFIED | 已从保存CSV核对E1 loss/gain解释；v2实现复审属历史证据。R_PRL来源绑定不使同夏季参考成为外部独立锚点。 |
| S20 | `b0ddb4181abb424582dd29e59e472a6d`<br>data_agent | [E1/E3首轮与清晰版图表](SOURCE_LOCATIONS.md#s20) | `92e2e5adf731df817a96c09f6c6d6fb5df7019c7fc9139e20b8a04bc763e20c1` | C14 C16<br>AUTHOR-REPORTED | 首轮/清晰版图交付归档；数值口径服从S19，图像质量未在本轮重新核验。 |
| S21 | `d5ebe91c405e424583990efe2a07f86e`<br>audit_agent | [E2/E4结果独立算术审计](SOURCE_LOCATIONS.md#s21) | `aacb7df81c6e2d8139b2806eb1cb389c6cd75556cc28cc9c898385c475d1f429` | C15<br>BLOCKED | 历史E2/E4算术审计可追溯；E4校正输入后被标为存疑，禁止转成真实五月异常、坏数据或长周期检出。 |
| S22 | `fa4dcaf2b05345a19de73a6a864bdc43`<br>data_agent | [E1图注v2及E2/E4制图](SOURCE_LOCATIONS.md#s22) | `e5d6a5798b182f39a98a4ef95612498c2c6d5f7a1808776b1f818208e210f7c5` | C14 C15 C16<br>AUTHOR-REPORTED | E1图注v2及E2/E4制图记录保留；E4每次复用都须同时携带存疑状态，图的存在不是验收。 |
| S23 | `8ed45fc1bdce42b2afd6fa2f5faa243a`<br>statistics_agent | [E5校准代码实现](SOURCE_LOCATIONS.md#s23) | `8c3bc99ea94d934e7596b7c1d480ea1cb3f11f9167070a07c8217618dd4d3060` | C11 C13 C16<br>AUTHOR-REPORTED | E5代码/13项自测记录仅支持冻结条件设计；不处理等待人工的E5结果，不推成极尾部实验显著性。 |
| S24 | `fc8ffb408b704ff1a0b86c50556266ab`<br>data_agent | [未来校正接入模板与v1校验器](SOURCE_LOCATIONS.md#s24) | `11c712ee8a81d03f2c1bee842e197bc871ad1b8913e6c3f9d5be3a27b0dfdf5c` | C06 C17<br>PENDING | 未来校正模板与v1校验器10项测试报告保留；S25给出online_chain_corrections未校验的反例。 |
| S25 | `ab9c9e4b2ab44a2e9ea1138a7dd59947`<br>audit_agent | [E5与接入工具独立预审](SOURCE_LOCATIONS.md#s25) | `cacb44786999f70417247b34d2c6cbd50705223344a5caf9f68da35137dcdfc6` | C11 C15 C17<br>BLOCKED | E5条件READY与intake NEEDS_FIX同时保留；v2另属TECHNICAL_REVIEW_PENDING，本轮不替其独立复审。 |

重复结论按C编号归并；每个C保留全部来源与对应任务ID。来源数量不等于独立研究或重复实验数量。

| 主张 | 状态 | 统一结论及边界 | 来源/定位 |
|---|---|---|---|
| C01 A=0.86±0.18 | VERIFIED | 保存的本地主P1为0.857260242008892±0.1775932570274874，按两位小数得到0.86±0.18；u=max(scaled LS, day JK)。只核实保存值及算术，不是本轮重拟合。 | [S08](SOURCE_LOCATIONS.md#s08)、[S09](SOURCE_LOCATIONS.md#s09)、[X01](SOURCE_LOCATIONS.md#x01)、[X25](SOURCE_LOCATIONS.md#x25)<br>/P1；v17b p.2；D01/D02 |
| C02 作者同版本独立认证 | PENDING | 主值舍入一致不能认证作者生产包、54段源行/29操作组或全部论文数字。R3自身仍写not certified same-version，G08/M21待认证。 | [S08](SOURCE_LOCATIONS.md#s08)、[S13](SOURCE_LOCATIONS.md#s13)、[X01](SOURCE_LOCATIONS.md#x01)、[X02](SOURCE_LOCATIONS.md#x02)<br>/evidence_scope；/not_run |
| C03 样本与时长口径 | VERIFIED | 当前主汇总与旧SEGMENT_TABLE是不同支持。已逐表求和，保留瞬态前/后、步长折算、成员/唯一行和日历跨度区别，不按时间戳去重。 | [S01](SOURCE_LOCATIONS.md#s01)、[S08](SOURCE_LOCATIONS.md#s08)、[S09](SOURCE_LOCATIONS.md#s09)、[X03](SOURCE_LOCATIONS.md#x03)、[X04](SOURCE_LOCATIONS.md#x04)、[X06](SOURCE_LOCATIONS.md#x06)、[X40](SOURCE_LOCATIONS.md#x40)<br>D06；sample_counts |
| C04 逐文件/组实验身份 | PENDING | 原始行、多段共享、29操作组依赖和配置时间范围尚不能由文件哈希或声明认证；54段和3186滤波点不等于独立重复。 | [S01](SOURCE_LOCATIONS.md#s01)、[S10](SOURCE_LOCATIONS.md#s10)、[X05](SOURCE_LOCATIONS.md#x05)、[X40](SOURCE_LOCATIONS.md#x40)<br>INPUT_MANIFEST；SAMPLE_LEDGER |
| C05 2025频率链已提供 | AUTHOR-REPORTED | PI已给两个站的梳齿数、参考关系、传输+f10M_SH及武汉二分频公式；fbeat是约66 MHz计数值，原拍频约132 MHz。名义10M名称不等于精确10 MHz常数。 | [S01](SOURCE_LOCATIONS.md#s01)、[S02](SOURCE_LOCATIONS.md#s02)、[X11](SOURCE_LOCATIONS.md#x11)、[X26](SOURCE_LOCATIONS.md#x26)<br>PI原文完整链；v17b p.3 |
| C06 2025/2026接口闭合 | PENDING | 需绑定源文件/日期/配置/通道/在线修正和二倍是否已应用。2026约33.6 MHz及因子1的已有记录不得与2025二分频值混用；不改观测、不代入新反演。 | [S01](SOURCE_LOCATIONS.md#s01)、[S10](SOURCE_LOCATIONS.md#s10)、[S24](SOURCE_LOCATIONS.md#s24)、[S25](SOURCE_LOCATIONS.md#s25)、[X05](SOURCE_LOCATIONS.md#x05)、[X11](SOURCE_LOCATIONS.md#x11)、[X26](SOURCE_LOCATIONS.md#x26)<br>D07；具体频率链不扩展为Freq_A通道转换 |
| C07 长链与实验室支路定义 | AUTHOR-REPORTED | PI及PRL描述长链round-trip out-of-loop，无单程测试点；几百米实验室周边支路无监控。Freq_A候选通道尚缺完整接线/分频系数。 | [S11](SOURCE_LOCATIONS.md#s11)、[S13](SOURCE_LOCATIONS.md#s13)、[X12](SOURCE_LOCATIONS.md#x12)、[X13](SOURCE_LOCATIONS.md#x13)、[X45](SOURCE_LOCATIONS.md#x45)、[X46](SOURCE_LOCATIONS.md#x46)<br>X12优先于旧时区/单程假设 |
| C08 排除全部传递支路影响 | BLOCKED | 长链监测不能覆盖未监控实验室支路、单程非互易项或缺测日期；不得自动除2、按相关性选通道/滞后或用RF中心归一化。DDS量化预算不能充当全部噪声上界。 | [S11](SOURCE_LOCATIONS.md#s11)、[S13](SOURCE_LOCATIONS.md#s13)、[X12](SOURCE_LOCATIONS.md#x12)、[X13](SOURCE_LOCATIONS.md#x13)<br>D10；未监测项不能设零 |
| C09 M2+N2估计目标 | VERIFIED | 文档定义为M2/N2相对结构固定的共同尺度；近12h组、日潮组、分段offset和campaign太阳项分别建模。C/S同源，共同相位不是单一时间延迟；b=0包含反相。 | [S02](SOURCE_LOCATIONS.md#s02)、[S04](SOURCE_LOCATIONS.md#s04)、[S11](SOURCE_LOCATIONS.md#s11)、[X19](SOURCE_LOCATIONS.md#x19)、[X25](SOURCE_LOCATIONS.md#x25)、[X27](SOURCE_LOCATIONS.md#x27)、[X28](SOURCE_LOCATIONS.md#x28)<br>仅定义与历史实现身份，不认证硬件符号或作者完整势模板 |
| C10 同步精度与门核 | PENDING | 国内原始记录BJT已由PI确认，不再反复询问时区；UTC派生值不再减8h。PC标签偏差、两计数器同步、门起/中/终点、重叠和死时间仍缺独立证据。 | [S01](SOURCE_LOCATIONS.md#s01)、[S02](SOURCE_LOCATIONS.md#s02)、[S10](SOURCE_LOCATIONS.md#s10)、[X12](SOURCE_LOCATIONS.md#x12)、[X20](SOURCE_LOCATIONS.md#x20)、[X27](SOURCE_LOCATIONS.md#x27)<br>±10min敏感性不构成对时精度，设备相位认证仍BLOCKED |
| C11 噪声模型与误差 | VERIFIED | 保存结果分别给scaled LS、day JK、经验GLS和ADEV GLS；P1协方差为LS，不是max规则的JK总协方差。GLS为固定估计V条件结果，未知共同修正与噪声参数不确定度未全覆盖。 | [S05](SOURCE_LOCATIONS.md#s05)、[S08](SOURCE_LOCATIONS.md#s08)、[S12](SOURCE_LOCATIONS.md#s12)、[S23](SOURCE_LOCATIONS.md#s23)、[S25](SOURCE_LOCATIONS.md#s25)、[X01](SOURCE_LOCATIONS.md#x01)、[X02](SOURCE_LOCATIONS.md#x02)<br>D02；primary_GLS_calibrated；不是噪声模型真实性认证 |
| C12 P6/P8/P9差异 | PENDING | P6 .62与作者.69、P8后.06018与.21、P9 3.9167与2.8均保留。先对齐版本/支持/目标/误差/模拟定义，禁止调参匹配。 | [S08](SOURCE_LOCATIONS.md#s08)、[S13](SOURCE_LOCATIONS.md#s13)、[X01](SOURCE_LOCATIONS.md#x01)、[X25](SOURCE_LOCATIONS.md#x25)、[X28](SOURCE_LOCATIONS.md#x28)、[X30](SOURCE_LOCATIONS.md#x30)<br>D03/D04/D05 |
| C13 作者尾概率及条件校准 | AUTHOR-REPORTED | v17b声称0/20000及单侧p<1.5e-4；本轮不独立认证。R3 Stage4尚未执行；S23/S25 E5代码条件READY不替代同版全54段尾部、全选择或完整硬件误差认证。 | [S08](SOURCE_LOCATIONS.md#s08)、[S23](SOURCE_LOCATIONS.md#s23)、[S25](SOURCE_LOCATIONS.md#s25)、[X02](SOURCE_LOCATIONS.md#x02)、[X25](SOURCE_LOCATIONS.md#x25)、[X28](SOURCE_LOCATIONS.md#x28)<br>不同规模/模型的尾概率不可拼接；E5结果任务仍等待人工 |
| C14 E1内部预测及停止条件 | VERIFIED | 保存348行=29折×12候选。campaign_FIX0在本族的平均loss更低；linear_P45相对自身NULL的gain更大不等于绝对预测更好。interpretation_stopped=true原样保留。 | [S12](SOURCE_LOCATIONS.md#s12)、[S13](SOURCE_LOCATIONS.md#s13)、[S14](SOURCE_LOCATIONS.md#s14)、[S19](SOURCE_LOCATIONS.md#s19)、[S20](SOURCE_LOCATIONS.md#s20)、[S22](SOURCE_LOCATIONS.md#s22)、[X16](SOURCE_LOCATIONS.md#x16)、[X18](SOURCE_LOCATIONS.md#x18)<br>D08；只读汇总，不解除特异性限制 |
| C15 绝对结果及四五月校正 | BLOCKED | S21数值审计作为历史证据保留；E2夏季是条件结果，E4依赖已存疑四五月修正，只是历史场景。不得把均值偏离或LP系数提升为五月故障或新潮汐检出。 | [S18](SOURCE_LOCATIONS.md#s18)、[S19](SOURCE_LOCATIONS.md#s19)、[S21](SOURCE_LOCATIONS.md#s21)、[S22](SOURCE_LOCATIONS.md#s22)、[S25](SOURCE_LOCATIONS.md#s25)、[X09](SOURCE_LOCATIONS.md#x09)、[X10](SOURCE_LOCATIONS.md#x10)、[X15](SOURCE_LOCATIONS.md#x15)、[X39](SOURCE_LOCATIONS.md#x39)<br>D09；当前夏季39—54主线不改变旧54段主结果的历史身份 |
| C16 实现/自测/图交付 | AUTHOR-REPORTED | E2 v1→v2问题及复审链、E1/E3/E5实现与制图交付已归档；本轮没有重跑自测、检查全部图像或把READY转为批准。 | [S14](SOURCE_LOCATIONS.md#s14)、[S15](SOURCE_LOCATIONS.md#s15)、[S16](SOURCE_LOCATIONS.md#s16)、[S17](SOURCE_LOCATIONS.md#s17)、[S18](SOURCE_LOCATIONS.md#s18)、[S19](SOURCE_LOCATIONS.md#s19)、[S20](SOURCE_LOCATIONS.md#s20)、[S22](SOURCE_LOCATIONS.md#s22)、[S23](SOURCE_LOCATIONS.md#s23)<br>只关闭历史叙述重复，不改变任务状态 |
| C17 未来接入校验缺口 | BLOCKED | S24自测与S25反例均保留：v1可遗漏online_chain_corrections却返回结构可用。已有v2另待独立技术复审，本轮不能宣称修复获验收。 | [S24](SOURCE_LOCATIONS.md#s24)、[S25](SOURCE_LOCATIONS.md#s25)<br>D11；TECHNICAL_REVIEW_PENDING保持等待 |
| C18 欧洲参照与新颖性 | PENDING | 文献文本支持欧洲已有动态潮汐、含负荷模型、异种钟、Kalman和同址零对照。可主张的候选差别为沪汉M2+N2与显式太阳项分离及采样辨识；并非已确认优先性或Nature advance。 | [S08](SOURCE_LOCATIONS.md#s08)、[S11](SOURCE_LOCATIONS.md#s11)、[S13](SOURCE_LOCATIONS.md#s13)、[X25](SOURCE_LOCATIONS.md#x25)、[X31](SOURCE_LOCATIONS.md#x31)、[X32](SOURCE_LOCATIONS.md#x32)、[X33](SOURCE_LOCATIONS.md#x33)、[X34](SOURCE_LOCATIONS.md#x34)、[X35](SOURCE_LOCATIONS.md#x35)、[X36](SOURCE_LOCATIONS.md#x36)、[X37](SOURCE_LOCATIONS.md#x37)<br>D12；不同估计目标不可比较A精度胜负 |
| C19 文档/代码来源修订链 | VERIFIED | X07六项当前文档和备份的SHA均与修订记录一致；S08/S09的指纹、阈值、路径、排版/日志问题有可追踪修订。X08是本地commit解释的历史报告，未重做git认证。 | [S08](SOURCE_LOCATIONS.md#s08)、[S09](SOURCE_LOCATIONS.md#s09)、[X07](SOURCE_LOCATIONS.md#x07)、[X08](SOURCE_LOCATIONS.md#x08)、[X38](SOURCE_LOCATIONS.md#x38)<br>不能把文档修正当作科学认证 |
| C20 管理记录与本轮保留 | VERIFIED | 本轮25份文本/SHA/agent/manifest与SQLite一致，11表行内容指纹未变。联调和中断历史记录并入管理证据，不重新创建、派发、批准或运行服务生命周期命令。 | [S03](SOURCE_LOCATIONS.md#s03)、[S04](SOURCE_LOCATIONS.md#s04)、[S05](SOURCE_LOCATIONS.md#s05)、[S06](SOURCE_LOCATIONS.md#s06)、[S07](SOURCE_LOCATIONS.md#s07)、[S08](SOURCE_LOCATIONS.md#s08)<br>run_metadata；ledger_before/after；SQLite 37 REVIEW保留 |

| 补充来源 | 用途与路径 | SHA256 |
|---|---|---|
| X01 | [主估计及P6/P8/P9保存值；不重拟合](SOURCE_LOCATIONS.md#x01) | `1afc144275058f39eeda185ed673e948dcd7dea42835894d3a92bfec1fd2207e` |
| X02 | [稳健性与未执行分支记录](SOURCE_LOCATIONS.md#x02) | `05a66995b3dcee2075a7da1a57e7419a50d40d360c5efbb998cb06c1b8b1e22e` |
| X03 | [本地主结果5个campaign样本汇总](SOURCE_LOCATIONS.md#x03) | `ae80de311df99619ab18ad59e85b46fed117d06d5ccaf4625da4068b292eae8b` |
| X04 | [旧54段样本汇总；不可替代主结果支持](SOURCE_LOCATIONS.md#x04) | `cb4c1c51f42abd69bef74a0536142d1332d1273f423d5c03df87f60e01703e5d` |
| X05 | [历史输入/配置登记；不读取登记中的原始观测](SOURCE_LOCATIONS.md#x05) | `8348f7d4feacb25cd0396d07fc1ee332264887b2c11d7c441949a213eb3a45bc` |
| X06 | [历史摘要算术及夏季跨度](SOURCE_LOCATIONS.md#x06) | `85ec2fd382dad1211669229116eda6728d28a736af229e69383351db76451642` |
| X07 | [S08/S09文档修正前后SHA](SOURCE_LOCATIONS.md#x07) | `033d1bcee8b2b71a5dee9befcaf80adcc7939995438b1d580082c8f47deec544` |
| X08 | [本地运行commit对账历史证据](SOURCE_LOCATIONS.md#x08) | `f16acf9856f6db56a53b2f9928a180ab1efe196f8b7aaf266f2ddd9fc52b5746` |
| X09 | [四五月当前存疑状态](SOURCE_LOCATIONS.md#x09) | `993cdf747875251720b2331902014e436efaf05002def1de11452b54926d5bdc` |
| X10 | [S21审计适用范围更正](SOURCE_LOCATIONS.md#x10) | `535f3bf6c3748898d5402a014ffa63ad2ccd6c5865ab5e42d7dc5824be804cd4` |
| X11 | [2025链PI原话；未绑定具体文件](SOURCE_LOCATIONS.md#x11) | `367874955fb77ef98f93d74e89f27d2b9e44857bbd9fb26d70c6fe89ba5196ae` |
| X12 | [BJT及长链/实验室支路PI更正](SOURCE_LOCATIONS.md#x12) | `194989f34f2dbec1c72e5a595132e5c12861cabeeb60a31bb639ce8c15f0eed6` |
| X13 | [历史PRL链路定义核读](SOURCE_LOCATIONS.md#x13) | `063570302198193b72724b0ba7b7f74098fe0786adf715429d553e04e7dbe7af` |
| X14 | [PRL来源SHA登记](SOURCE_LOCATIONS.md#x14) | `dc959a3586609141c30a6be58ea96496d1f5e02be8122a9222fd28854ae376fe` |
| X15 | [S21既有数值核读；解释必须同时读X09/X10](SOURCE_LOCATIONS.md#x15) | `6036107fa7aef7028886c3b535fac58aed098381c0e4233e60a90edb100892d4` |
| X16 | [S19引用的保存预测损失表](SOURCE_LOCATIONS.md#x16) | `180650ecc073d82293eeefa215b12e3a29de739f3ad4a27ff03f2c6869dabc89` |
| X17 | [S19引用的已有条件校准；不重跑](SOURCE_LOCATIONS.md#x17) | `915bac3eee01fb623f89e9ef7e5d40db908d669036eb64049eaae86df209f556` |
| X18 | [保存interpretation_stopped及停止原因](SOURCE_LOCATIONS.md#x18) | `db73553d245ac2f115bdcf98f1dd4d3444d68fd56ae7da99de26bc4c153cfdd2` |
| X19 | [共同相位/有符号尺度数学定义；不是批准](SOURCE_LOCATIONS.md#x19) | `13983d44700ff0dd9e37640147f1103afa35e3c5f46f653c081e051c167a24f2` |
| X20 | [同步证据/条件传播规范；不是执行授权](SOURCE_LOCATIONS.md#x20) | `82fd9d56566c38349ab67e8b3bc54f186dbdaae36f43ddef17101ca73cb78cbd` |
| X21 | [既有第二阶段证据矩阵，须按后续记录限定](SOURCE_LOCATIONS.md#x21) | `8765f6d1b07306186c924a9dc199623bc1e79cf3b37b74705bb3b15ec454ecad` |
| X22 | [既有缺项清单，须按后续记录更新语义](SOURCE_LOCATIONS.md#x22) | `deeb8217616dae3ac534571993f41ff630caee33a265a3ed3aae6435c76cb0dc` |
| X23 | [所提供PDF版本及逐页提取来源登记](SOURCE_LOCATIONS.md#x23) | `83d6b9d89f042050c448ae27f83ad03b309435bf61fc966f4d460ce00cbae324` |
| X24 | [v17b物理PDF第1页的既有提取文本](SOURCE_LOCATIONS.md#x24) | `ba330574730a78bc4018e37a9b85724ef62627bcc43dfd430714766d5c790104` |
| X25 | [v17b物理PDF第2页的既有提取文本](SOURCE_LOCATIONS.md#x25) | `ca3d4ae75292646fde97b82ee6e1a8ef692aefa3be84963dc62826eab8bf2ba8` |
| X26 | [v17b物理PDF第3页的既有提取文本](SOURCE_LOCATIONS.md#x26) | `eaab807a7cc27eaf0944bccc4d21f4f0cccbfc5bb9afcacc35966a365e6d17bf` |
| X27 | [v17b物理PDF第4页的既有提取文本](SOURCE_LOCATIONS.md#x27) | `2020254fefb87e01367ec9f01f3d9df6fd5f9f55c54c4e9dde5d67d0ffe480a9` |
| X28 | [v17b物理PDF第5页的既有提取文本](SOURCE_LOCATIONS.md#x28) | `36503de390d8709bb7ccab0793eb85a6ed93ad4282fb2c0e40cf7b336be68970` |
| X29 | [v17b物理PDF第6页的既有提取文本](SOURCE_LOCATIONS.md#x29) | `32c4d67d8de7ca14b2f19ce14d71b4bae972163cf92a5a342cd1f79a79b5eff8` |
| X30 | [v17b物理PDF第9页的既有提取文本](SOURCE_LOCATIONS.md#x30) | `5bdfa7df999cbebbabaab5b13563000cdde03f726ffc9eb97bcbf4c57fae42e5` |
| X31 | [欧洲所供版本物理PDF第1页的既有提取文本](SOURCE_LOCATIONS.md#x31) | `74aac95833c98fb87d8e5f010d464f11b16a941074813ca07d67eff690f4da2f` |
| X32 | [欧洲所供版本物理PDF第7页的既有提取文本](SOURCE_LOCATIONS.md#x32) | `2608d18699322dad5ea19709a733ef2ff6b2941bd1555176ca8bbe4c98cebb60` |
| X33 | [欧洲所供版本物理PDF第8页的既有提取文本](SOURCE_LOCATIONS.md#x33) | `f41f7cc4754a023e5fbd1016edfc2b1ebbe58448147e16d2bfa064ffcbd66ab0` |
| X34 | [欧洲所供版本物理PDF第11页的既有提取文本](SOURCE_LOCATIONS.md#x34) | `d3ad0bbacf66d1f5c0c71ef306cebc77dd08cad1a452d87c4ca6041574ee98e6` |
| X35 | [欧洲所供版本物理PDF第13页的既有提取文本](SOURCE_LOCATIONS.md#x35) | `43351c3d7a11163c6460783ab85464e854b20dee73d9ea0bb1fef8b2aead6960` |
| X36 | [欧洲所供版本物理PDF第14页的既有提取文本](SOURCE_LOCATIONS.md#x36) | `7e26a5b806538c8da1447a0c53c2c41156d9dd7fdf3b5b56d419529197aa16fe` |
| X37 | [欧洲所供版本物理PDF第15页的既有提取文本](SOURCE_LOCATIONS.md#x37) | `432605e7aed077e39e37d1b132612676c8958b331f06683e57b8dc34e4f1a640` |
| X38 | [S09缺项后续绑定的历史测试日志；本轮不重跑](SOURCE_LOCATIONS.md#x38) | `906b207ec4a3bbf98f8eb50e2776c8ed684995fd8f62df4817f759895adf1766` |
| X39 | [校正存疑的状态原始更新](SOURCE_LOCATIONS.md#x39) | `a55eb30db73ae0be07ac00dcff8f09c917e3029587537218c3eb01e969103020` |
| X40 | [S01引用历史样本口径](SOURCE_LOCATIONS.md#x40) | `7d7e2137d9067e4ba975a28ff79cfa985f3384c667687e7301bfe10d6a208568` |
| X41 | [S01旧时区审计，当前BJT以X12为准](SOURCE_LOCATIONS.md#x41) | `159271f4ed953e9660c924950a9dc017547fedf4cf428600cdba784b8416083f` |
| X42 | [S02引用旧v1，保留版本差异](SOURCE_LOCATIONS.md#x42) | `cd5b67f7c6468151c5638ae6798f434baceeab371cb7106d585086e45dabc87c` |
| X43 | [v17b原PDF身份，仅哈希核验不重新提取](SOURCE_LOCATIONS.md#x43) | `3f9665b9da7172d9bd4d10e858994137736a0580b6df532c1f3ca2cc43c45482` |
| X44 | [europe原PDF身份，仅哈希核验不重新提取](SOURCE_LOCATIONS.md#x44) | `6e2a3aef4285a8afb63b7af23062ea7ea89c650d40311e8aa3c44235ca867b04` |
| X45 | [PRL main.tex装置及频率关系来源](SOURCE_LOCATIONS.md#x45) | `c0a8ce8e858611c0c0acc74208f9dc626f3bcfb6ecf73326b6b203a7af556ccb` |
| X46 | [PRL supplementary.tex装置及频率关系来源](SOURCE_LOCATIONS.md#x46) | `afbfaeaec7d35adc69ff49af9e842ec6fbe4f69fcd42150393e2555f35ef33ab` |

PDF原件身份与既有来源清单相符；本轮读取既有逐页文本，没有重新提取PDF或逐图视觉认证。图表任务只归档其既有路径/报告，不新增绘图。
