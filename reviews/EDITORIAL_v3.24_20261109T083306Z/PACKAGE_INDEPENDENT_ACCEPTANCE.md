# 分立包独立验收

**PASS：未发现实际阻断问题。**

验收对象：`SUBMISSION_FILES_v3.24/`；本次仅检查交付一致性，未改稿件或包内文件。

- 核心19文件齐全：主稿PDF/Word 2项、主图4项、ED图表TIFF 10项、SI 1项、cover letter PDF/Word 2项。
- `SOURCE_MAP.json` 的40条记录全部通过文件存在、大小和SHA256核对；其中31份原样副本与声明源文件逐字节一致。经shared/handoff中转的核心主稿、SI、cover letter另与活动v3.24项目文件核对，一致。
- `MANIFEST_SHA256.txt`生成后已实际运行 `sha256sum --check MANIFEST_SHA256.txt`：43项全部OK。
- 最新cover letter Markdown与活动项目文件完全一致，6位推荐审稿人不变；CSV正常解析为表头加6行，姓名及邮箱相符，无Ludlow或Arnold。
- 三个可选Markdown摘录（Table 1、主图图注、ED图表图注）去除新加独立文件标题后，均为 `formal_build_01/NATURE_ARTICLE_MAIN_v3.24.md` 中的连续原文，来源为已重编号的当前编译稿。
- `00_UPLOAD_GUIDE_ZH.md`清楚区分核心文件、可选摘录、ED备选PDF及完整阅读版：cover letter格式择一、主稿为备选格式、ED同项不重复上传、表与图注不重复追加。没有指示将所有副本当作不同投稿项目上传。
- 指南明确通讯作者待填、作者贡献按用户要求未加入、投稿系统所需作者批准等声明须据实提供，且说明打包不代表已投稿。未冒称所有submission声明已经完成。

本验收不重复科学审稿或重新运行分析；结论针对本次分立交付包一致性，不表示通讯作者占位已填写或已向期刊提交。
