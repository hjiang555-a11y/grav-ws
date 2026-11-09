# v3.24 cover letter：11月8日指导文件对齐重写

本次按作者要求重新编写cover letter，依据当前v3.24稿件，以及2026年11月8日《论文主线与贡献：结构化梳理》作者讨论稿。只改投稿信及其说明；论文、Methods、SI、图件和稿件PDF/Word不改。此前信件已完整备份。

## 主线与贡献对齐

| 信件内容 | 11月8日指导 | 当前稿件依据 |
|:--|:--|:--|
| 背景：辨认重叠物理贡献，评估各自精度 | 第1节“一条主线，两个贡献” | Introduction第2–3段 |
| 实验：远程潮汐势差、合成响应、月潮组与太阳频率半日项的分离 | 第2节总体测量与分量识别 | Results，Fig.3，Extended Data Figs.3–6 |
| 方法：We develop a signal-to-noise model；信号、噪声和实际采样 | 第3节一般框架及具体实现 | Discussion式(1)及Methods |
| 模型估计7.17与实测7.02对照；弱分量吻合较差 | 第3节实测对照 | 当前Table 1及其后讨论 |
| 由精度评估连接稳定度、连续记录、相位覆盖和有效时间 | 第6节后续工作 | Discussion未来观测段 |
| 跨学科意义与潮汐背景的潜在应用 | 第1、4、6节；后续作者保留应用的裁定 | 当前摘要及Discussion结尾 |

11月8日文档的历史图号与“白噪声估计”标签不直接搬入新信；采用当前稿件的图表编号和model-estimated口径。指导文件提供逻辑结构，当前稿件提供结果与证据，后续作者指示决定最终范围。

## 写作与证据边界

- 实验保持中心位置；方法由各分量精度不同这一事实引出，再连接观测设计。
- 0.96 ± 0.11、1.00 ± 0.13、545.9 h有效时间、353天跨度、692 km基线及1,350 km光纤链路全部取自当前稿件。
- 新信增加Table 1的7.17、7.02作为方法贡献的实测对照；没有新计算或新结果。
- 未把太阳频率信号写成已排除实验室同频变化；未声称海洋负荷单独检出。混叠及非白噪声仍是可能解释。
- 明确白频率噪声是本次实现；当前对照检验实测幅度下的精度，不声称已经验证时间积累指数。未来观测时间关系保留噪声与采样效率条件。
- 共享274小时夏季记录说明及欧洲独立研究原句保留；不暗示与欧洲团队讨论或合作。
- 六位推荐审稿人、邮箱及理由逐字保留：Jun Ye、Tara M. Fortier、Sébastien Bize、Helen S. Margolis、Laura C. Sinclair、M. D. Barrett。不含Ludlow或Arnold。
- 通讯作者姓名、机构及邮箱仍待作者填写；未编造独家审理、全体作者批准或无利益冲突声明。

## 写作检查与复现

采用academic-humanizer的draft模式，依据规则5、7、8组织有证据的贡献表述与段落逻辑。运行check_revision.py audit并人工核查候选提示。此次为授权的全文重写，不声称词句或数字出现次数与旧信相同；数字的新增仅为已有Table 1对照。

build_letter.py以科学Python环境的python-docx生成Word，以Pandoc和XeLaTeX生成PDF。独立复核报告记录主线、数值、限定及审稿人名单验收。材料同步到已授权的私有GitHub仓库，未投稿或联系审稿人。

指导文件：projects/grav-ws/manuscript_48h/narrative_synthesis_20261108T003041Z/NARRATIVE_SYNTHESIS_ZH.md。
当前稿件：projects/grav-ws/manuscript_48h/editorial_v324_20261109T083306Z/sections/。

此前已核实的推荐人来源：[Laura Sinclair的NIST页面](https://www.nist.gov/people/laura-sinclair)；[M. D. Barrett的论文通讯作者信息](https://www.nature.com/articles/s41586-026-11072-8#author-information)。其余四位信息依用户提供。未宣称本轮重新核验全部联系方式。
