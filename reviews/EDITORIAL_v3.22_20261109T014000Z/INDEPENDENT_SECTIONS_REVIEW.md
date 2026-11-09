# 活动sections独立审查

审查对象：`editorial_v322_20261109T014000Z/sections`，对照本轮`baseline/sections`。只读审查，没有改稿；图件最终渲染、分页和上传不在本次源文检查范围。

结论：授权范围与主要内容保持，通过以下专项核对；发现的一处低严重度引用顺序歧义已由root修正并复核。当前没有未关闭的sections问题，也没有发现新科学结果改动或SI方法段落丢失。

## 实际问题

**S01，低，已关闭：全记录与April频谱的括号引用顺序。** 首次检查`sections/auxiliary_methods.md:31`为“full-record and April spectra (Extended Data Fig. 2c and Extended Data Fig. 7c)”。依据`sections/extended_data.md:9`，2c是April；依据同文件`:29`，7c是全记录。该反序在基线已存在。root现已只交换括号内顺序为`Extended Data Fig. 7c and Extended Data Fig. 2c`；重新读取活动行31确认修正，不涉及科学内容或阈值改变。

## 已通过的检查

- **摘要、开篇、作者及冻结项目：** `opening.md`、`author_block.md`、`declarations_post.md`、`references.md`与基线逐字节相同。摘要及末句、主结果0.96±0.11和1.00±0.13保持。活动sections没有Author contributions章节；未恢复贡献，也未改通讯占位。
- **A06：** `declarations_pre.md:3,7`的数据和代码获取途径均改为`corresponding author`，两处以外该文件保持原文。
- **有效时长：** 全记录只报545.9 h（`opening.md:3,11`、`results_discussion.md:9`、`methods.md:11`）。Methods明确其为主分析保留一秒样本累加的effective observing time；活动sections不再出现544 h或545 h全记录总长。353 days是calendar span，Methods`:17,35`的353.39/353.3889 d是相同跨度的较精确表达，不是第二套有效时长。`results_discussion.md:17`的274-h明确修饰summer subset，符合用户允许子集较短的指示。`methods.md:11`保留38＋16＝54 segments，不再用两个子集时间推导另一全记录总长。
- **ED数量和首次引用：** `extended_data.md`含8个图像入口及对应图1–8图注，2个表入口及对应表1–2说明。正文/Methods首次图引用依次为1、2（Results`:15`）、3（`:21`）、4/5/6（`:25`）、7（Auxiliary Methods`:3`）、8（`:21`）；首次表引用为1（Results`:9`）、2（`:15`），顺序正确。
- **映射：** 新图1＝旧ED2＋ED7；新图2＝旧ED3＋SI1；新图3–6＝旧ED4/ED5/ED6/SI2；新图7＝旧ED1＋SI3；新图8＝旧SI4。合并图注的panel描述保持全部原解释。表1a/b/c＝旧SI4/EDT3/SIT3；表2a/b/c/d＝旧EDT1/EDT2/SIT1/SIT2。除S01外，逐段阅读未发现错指新编号/子项。表中原值完整性由独立表格来源映射与渲染检查支撑；静态表中的文献上标需按编译引用映射处理，见下述集成事项。
- **SI文字：** 将基线`Supplementary Tables`之前SM1–SM7叙述与当前整个`supplementary_methods.md`比较，仅将旧/新展示项引用标签归一后，文本逐字一致。删除的表格、表注和4张SI图注已转移到新ED项；没有删除SI方法、公式、结果、局限或模拟次数。
- **Methods标题：** `methods.md`四个三级标题长21、32、34、22字符；`auxiliary_methods.md`五个三级标题长35、32、34、39、28字符；全部≤40。SI的SM标题不是主文Methods小标题，未额外施加新要求。

## 明确的集成事项

主稿编译会重排文献，因此源文的`Hou et al.^12^`继续保留source12是正确做法；静态表2b不能由主稿编译器重排，须将其上标单独映射为compiled23。root指出并授权后，表格脚本现已读取冻结`inputs/CITATION_ORDER.json`执行12→23，表格已重建；对应legend源文仍保留12。该项单列为图件集成问题，不是sections源文错误。活动sections图像路径的存在性、成品裁切和全文PDF页面由后续集成门禁验证；本报告不声明整体已可投稿。
