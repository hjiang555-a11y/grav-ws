# v3.22 初投排版实际检查

检查对象：formal_build_01 下的合并PDF、独立文字稿PDF、独立SI，及投稿信和Word编辑稿。这里只认证本轮编辑排版，不代表作者事实、科学主张或提交手续已经闭合。

- 合并PDF 47页；文字及图注稿PDF 24页；独立SI 14页；cover letter PDF 1页。
- A4、正文12 pt、双倍行距、连续行号、页码；作者块10 pt紧凑排列，使批准摘要完整置于第一页。主图尺寸、图内布局、顺序不变，图注与对应图同页。
- 查看全稿联系表、第一页及主图/表的清晰页面。无空白意外页或可见文字截断；自动检查全部文本边界，未发现越出页面的文字。部分单独图表页保留空白，为完整图注和分开展示保留可读性。
- XeLaTeX两轮编译无Overfull、Missing character、LaTeX Warning或Font Warning。参考文献35篇首次出现连续1–35，主图首次出现1–4。
- Title、188词摘要、Table 1、展示方程保持；66个图目录文件逐字节一致；112个旧版冻结文件哈希一致。
- Word伴随稿保留149个可编辑数学对象及1个可编辑Table 1，无图像替代公式。LibreOffice实际打开转换后28页，投稿信Word为1页，无页面越界文字。Word字体替代和分页依本地软件而异，正式版面以合并PDF为准。
- 通讯标记及贡献段在成稿可见，均明确待作者确认；尚不能把它们称为已确认的投稿元数据。

工具：Python 3.12.3；pandoc 3.1.3；XeLaTeX；python-docx 1.2.0；PyMuPDF/Pillow；LibreOffice。默认解释器为 /data/AI_Research/environments/python/sci/bin/python，PDF检查使用 tide-review-20261108T121212Z 环境。详细程序与JSON记录随源包保留。LibreOffice提示java helper不可用，但PDF转换成功，未将提示解释为转换失败。

保留第一次排版试件：formal_build_preflight_01、visual_check_preflight_01；作者块略压紧后的正式输出在formal_build_01。未修改任何图件或摘要文字。
