# 当前 v3.22 PDF 诊断：图4存在实际渲染兼容性问题

**结论：投稿前必须处理。** 这不是可以忽略的 Poppler 提示。当前图4的 PDF 内容含3处缺参数的虚线操作符；Poppler 24.02.0 在第一处错误后停止处理该图的后续内容。实际渲染中，图4只剩最前面的 a、两个分组标题和左侧浅绿色带，结果点、区间、后续标签及整个 b 均没有显示。MuPDF 能容错渲染完整图，因此此前仅依赖 MuPDF 的字体、文字保留和整页检查没有暴露该问题。

本次严格只读：未修改当前 R/H、稿件、图件或原脚本，未修复或重新上传。仅在本次审计目录新增证据和本报告。36份输入PDF的审计前后SHA256一致。

## 定位与对照

检查了当前15张活动图PDF、更新前15张对应图PDF、当前3份稿件PDF及更新前3份稿件PDF，共36份。只有以下两份产生该错误：

| 文件 | 退出码 | stderr |
|---|---:|---|
| 当前 `figures/figure4.pdf` | 0 | `Syntax Error (40074): Too few (1) args to 'd' operator` |
| 当前 `formal_build_01/NATURE_ARTICLE_v3.22.pdf` | 0 | `Syntax Error (3091931): Too few (1) args to 'd' operator` |

更新前的图4、更新前的合并稿及其他对照PDF均没有此提示；当前正文文字版PDF和独立SI也没有此提示。该问题由本次新图4引入，不是原稿已有的错误。退出码0不足以判定PDF内容完整。

复现命令（工作目录为当前项目R）：

```bash
pdftotext -layout figures/figure4.pdf -
pdftotext -layout formal_build_01/NATURE_ARTICLE_v3.22.pdf -
pdftoppm -f 1 -singlefile -r 150 -png figures/figure4.pdf <新审计输出前缀>
pdftoppm -f 13 -l 13 -singlefile -r 100 -png formal_build_01/NATURE_ARTICLE_v3.22.pdf <新审计输出前缀>
```

准确绝对路径、完整命令、stderr、输入SHA256及文字输出哈希记录在 [scan.json](pdf_diagnostic/scan.json)。`pdftotext` 对当前独立图4只输出48字节文字，主要是最前面的标题；MuPDF则能提取完整的45个文字跨度。

## 具体内容流问题

PDF的 `d` 操作符需要 `dashArray` 和 `dashPhase` 两个操作数；当前内容只有数组，缺少相位参数，因此文件内容本身不符合该操作符的语法，并非仅有某个阅读器不喜欢其排版。[Adobe PDF Reference 1.7，Table 4.7](https://opensource.adobe.com/dc-acrobat-sdk-docs/pdfstandards/pdfreference1.7old.pdf)

| 当前独立图4内容流 | 实际指令 | 对应位置 |
|---|---|---|
| xref 15 | `[2 2] d` | a左列竖向参考线 |
| xref 91 | `[2 2] d` | a右列竖向参考线 |
| xref 130 | `[3 2] d` | b中的不确定度水平虚线 |

在合并稿中，这三处均位于第13页的 `Fm3` Form XObject（xref 364）；该页对象为xref 301，页面内容流为xref 365。xref 364解压后对应偏移为478、2956和5188字节。stderr括号内的数值不是页码。完整内容流片段见 [stream_hits.json](pdf_diagnostic/stream_hits.json)，页面资源关系见 [page13_structure.json](pdf_diagnostic/page13_structure.json)。

来源可追溯至当前归档的 `figure_format_sources/figure4_optionB/make_figure4.py`：第37行传入 `dashes='[2 2]'`，第71行传入 `dashes='[3 2]'`，经第32行的封装写入PDF。

## 已实际确认的渲染后果

- [独立图4：Poppler渲染](pdf_diagnostic/figure4_poppler.png)与[MuPDF渲染](pdf_diagnostic/figure4_mupdf.png)直接显示差异。
- [合并稿第13页：Poppler渲染](pdf_diagnostic/combined_page13_poppler.png)中图4同样缺失大部分内容；图注和页眉页脚仍然可见。[MuPDF对照](pdf_diagnostic/combined_page13_mupdf.png)中图和图注完整。
- 这会影响使用相同解析逻辑的阅读、转图或提取流程。未验证Nature投稿系统采用何种引擎，因此不声称其后台一定失败；但现有明确缺图已经足以构成投稿前的文件完整性阻断项。

## 字体、单位与结论边界

本次重新读取了15张活动源图的文字跨度：在MuPDF解析下均为Arial系列，与此前字体审计一致，未发现新的字体系列问题。具体字体、字号范围和文件哈希写入 [PDF_DIAGNOSTIC_CHECKS.json](PDF_DIAGNOSTIC_CHECKS.json)。本轮未重新进行15张图的完整科学单位语义审阅；当前明确的新问题是图4的后续标签和单位在Poppler中随图形一并缺失。MuPDF字号合格不能替代跨引擎渲染完整性检查。

没有发现需要在本诊断中重新计算科学数值的证据。原始科学结果是否成立不属于本次PDF诊断范围。

## 建议，仅报告、未执行

获得修改授权后，应在图4源脚本中提供完整虚线规格，例如 `[2 2] 0` 与 `[3 2] 0`，重新生成图4及受影响的稿件/源码交付，核对结果点、区间和科学内容保持一致，再同时使用MuPDF与Poppler验证。不能仅屏蔽stderr，也不能只检查命令退出码。

软件：Poppler `pdftotext/pdftoppm` 24.02.0；PyMuPDF版本见机器检查JSON。输入路径与全部运行证据均在新审计目录；当前交付文件保持原样。
