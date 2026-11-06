# v69：警报调查、技术处置与一轮 Nature 修订

**结论：代码身份警报已关闭，连续性判据的错误解释已纠正；另发现并修复本侧上一版书目生成错误。没有发现此次代码版本差异改变观测或拟合系数。实验零点连续性尚未建立，不能随软件警报一起改成“通过”。**

新版题目为 **Tidal potential measured on a coastal–inland optical-clock baseline**。PDF、Word和英文Markdown已生成。它替代上一版合成工作稿供作者阅读，仍明确标为WORKING DRAFT：正式R7移交和v68共同输入重放尚未完成，因此本轮没有私自确定唯一主估计器。

## 警报处置

| 项目 | 调查结果 | 本轮状态 |
|---|---|---|
| R7 `template.py` 与历史登记哈希不同 | 从精确历史提交和源包找回原文件；差异只有注释/文档字符串。可执行AST一致，360,000点时间合成、3,299行模板取样和主系数旧新差均为0 | **已关闭代码身份警报**；保留历史哈希，追加版本关系 |
| `absolute_continuity_supported=true` | 原判据只比较一个与三个夏季截距下的半日尺度，差0.02019，小于工作误差0.16113；不能认证中断前后零点 | **解释已纠正**；敏感性PASS，绝对及期内重锁连续性均NOT_ESTABLISHED，而非已发现不连续 |
| 本侧上一版参考文献2–6错误 | 全文数字列表解析把扩展数据目录当成书目，覆盖正确条目 | **已修复**；限定书目区段、拒绝重复，4项防回归测试通过；最终22条参考文献按首次引用排序，并逐项核对内容 |
| 原设计37.2 mHz换算文字 | `37.2e−3 / 429.228e12 = 8.6667e−17`，原文误写为8.67e−14 | **本轮记录已纠正**；该项未在早期R7相对链数值施加，不能据此声称拟合错1000倍 |

68个历史登记文件：67个身份直接吻合，1个为已解释的纯说明文字版本变化，未解释哈希差异为0。详见[总对账状态](verification/ALARM_STATUS_RECONCILED.json)、[代码版本证明](reports/code_lineage/CODE_LINEAGE_CLOSURE.md)、[连续性及物理边界](reports/physics_boundary/PHYSICS_BOUNDARY_CLOSURE.md)、[书目错误修复](reports/REFERENCE_PARSER_CLOSURE.md)。原始登记及对方代码均未改写。

## 两组半日响应与题目

去掉Lunar，符合实际联合模型的测量对象。R7同一设计在投影其他列后，两组半日模板仍为秩2，系数相关为−0.3572，VIF为1.1463，支持分别估计两组响应。

- 月球组：M₂＋N₂。
- 邻近半日组：S₂＋K₂；S₂为太阳分潮，K₂有日月共同作用。

英文主文写为“positive, separately estimated semidiurnal responses”。不把组内固定相位/相对振幅的估计写成四个分潮各自自由检出。已有R7条件覆盖模拟针对月球系数，不能直接给邻近组或双响应联合检验背书；本轮没有从标准误换算新的检测概率。较弱的全日组已在联合模型中，不作为额外否定半日结果的条件。

## 一轮 Nature 评价及修改

使用实际安装的ECC article-writing与scientific-thinking-scholar-evaluation，完成一次完整评价和修改；没有假称调用未安装的Humanizer。开头先解释相对钟速率、光纤网络与势传感，再引出12.42 h和12 h的相位变化。技术桥接、信息份额和估计器选择细节移入Methods，正文围绕地理、观测、两组响应和实测对照展开。

摘要133词，主文1,395词，Methods连同作者声明2,022词。四幅主图、一个扩展谱图、三张扩展表保持各自观测和归算身份；没有为了换标题重设参数或拼接误差。Stahl等作为独立同期、地理互补的研究引用。完整[评审意见](reviews/nature_reader/NATURE_READER_REVIEW.md)与[修改响应](reports/NATURE_REVIEW_RESPONSE.md)随包保存。

## 数据与验收范围

这是同一钟比对的重复时间观测，不是两项独立实验。R7重放使用3,299个十分钟输出、43个观测UTC日、8期；v68仍为原稿报告的54段/约544 h，最终主链尚未完成同支撑重放。不得将两套归算平均或合并显著性。

摘要数值的来源表见[data/ABSTRACT_NUMBER_LEDGER.csv](data/ABSTRACT_NUMBER_LEDGER.csv)：v68的0.97±0.14与0.90±0.29为源稿报告；R7的0.99±0.12与1.13±0.29已在保存表上独立复算。负荷约三分之一是预测RMS比例，单列负荷0.89±0.55未分辨。两个模型的物理模板、权重和误差规则没有混用。

PDF与Word均零编译警告；最终PDF19页，无空白/孤行页和越界文字。Word保留80个原生可编辑公式、5幅图和3张表。全记录相位图保留3,299行，各箱支持数及投影传播后的协方差验收通过。最终PDF首页、正文末页、真实书目页和相位图已视觉检查。

运行环境为Python3.12.3、NumPy2.5.3、pandas2.3.3、pyTMD3.0.9；计算单BLAS线程。代码和确切输入SHA256在各证明JSON内。本轮没有修改原始数据、原稿、对方工作树、数据库或运行服务。既往归算保持其固定误差方法；本轮数值工作主要是版本等价核验、设计秩和判据反例，不新增主科学估计。

## 仍须补齐

1. 正式 `merge_v68_r7/opencode/R7_HANDOFF.md`；本轮交付时尚未收到。已有中间文件不冒充正式移交。
2. v68最终逐行掩码、三角滤波成员、直接势模板及重采样链，以便完成同原始支撑、同物理模板对账。
3. 期内重锁/中断前后零点和钟修正记录。软件敏感性不能补造这些实测证据。
4. 作者贡献、资助、利益声明、通信作者及审稿可访问的数据/代码地址。

以上未完成项不影响本轮代码警报闭环和写稿交付，但限制“唯一最终合稿”和“可提交版”的认定。未对外投稿。

## 重建入口

从本目录运行（输出目录必须是尚不存在的新目录）：

```bash
PYTHONDONTWRITEBYTECODE=1 /home/room115/pytorch_env/bin/python -B assemble_working.py
PYTHONDONTWRITEBYTECODE=1 /home/room115/pytorch_env/bin/python -B render_working.py NATURE_ARTICLE_v69_WORKING.md render_new
PYTHONDONTWRITEBYTECODE=1 /home/room115/pytorch_env/bin/python -B verify_release.py render_new
PYTHONDONTWRITEBYTECODE=1 /home/room115/pytorch_env/bin/python -B analysis/verify_bibliography_release.py render_new
```

版本警报脚本分别位于 `reports/code_lineage/`、`reports/physics_boundary/`，完整运行日志和输入哈希已保存。`sources`只读链接指向上一轮冻结输入；该依赖在修订包中明确登记，修订包不冒充完整原始科研数据包。
