# 分开版构建与渲染核验

结论：通过；未运行科学计算，未改科学正文、数字或图件。

- 基稿：`nature_focused_humanized_20261107T145113Z`，原 46 页 PDF SHA-256 为 `6914c2afe9e9d5112f64d0d2c3f80bdd3f9570d79709d0041286b8235bc6f630`。
- 主稿 PDF 直接抽取原第 1–39 页。逐页 PDF 内容流与原稿完全相同，图表和页码保持；39 页 TEX 独立编译两次通过。DOCX 从原件移除 Supplementary Methods 起的内容，保留 7 个表格；主稿 MD/TEX 同样按已有编译稿截取，未重新分配引用编号。
- SI 共 7 页，独立标题和页码 1–7；SM1–SM7 内容与最终合并 Markdown 中对应文本完全一致，仅新增标题、跨文件导航及实际引用条目。引用保留主稿编号 20、21、22、23、25、29、30。SI 中 Fig./Extended Data/Table 与具名 Methods 小节仍指主稿；导航已说明。
- 实际渲染 SI 全部 7 页并查看总览，另放大检查 SM7 公式页和引用末页；未发现裁切、公式遮挡、孤立小节标题。主稿 Table 1（第 6 页）及末页 Extended Data Table 6（第 39 页）亦重新渲染。SI 本身没有新图或表。
- `figures/` 42 个文件全部与基稿逐字节一致。4 主图、11 ED 图、6 ED 表全部保留。17 项 ED 的期刊格式问题已反馈主 agent，不在本次拆分中擅自删图或拼图。
- `SIGuide.docx` 为英文简短文件指南：文件名、标题及 33 词 summary；说明包含七个方法节、无 supplementary display items。已用 LibreOffice 转成检查 PDF，视觉核验为一页。中文长说明另存 `READING_GUIDE_ZH.docx`，期刊格式边界的标题与整段均为 C00000 红色。SI DOCX 亦可经 LibreOffice 转换为 7 页 PDF，公式/末页引用可编辑且完整。

可复现脚本为 `build_separate.py`；编译日志在 `build/`，图像证据在 `checks/render/`，Word 转 PDF 检查件在 `checks/docx_pdf/`。完整文件哈希见 `SEPARATION_MANIFEST.json`。

重建可用 `python build_separate.py --source /path/to/original_version`；`--source` 需指向完整基稿目录（含 `build_final/` 样式与原作者图文）。主稿 TEX 可在本目录直接运行 `xelatex -no-shell-escape NATURE_ARTICLE_MAIN.tex` 两次。
