# v3.24 cover letter交付说明

按当前v3.24正文生成英文cover letter，包含六位推荐审稿人。按最新指示删除Andrew D. Ludlow。Jun Ye、Tara M. Fortier、Sébastien Bize和Helen S. Margolis的姓名、邮箱和推荐理由采用用户原话；Laura C. Sinclair使用用户补充的邮箱及自由空间光学链路、光钟比对理由。

## 核查与范围

按用户最新指示，将欧洲相关研究一句恢复为此前consolidated_20261108T011413Z/editorial/COVER_LETTER_DRAFT.md中的“An independent study has also reported…”说法，说明这是另一项独立研究。参考编号采用纯文本arXiv形式便于PDF与Word一致排版。仅此一句改变；六位推荐审稿人及其他正文保持不变。

- 当前正文、Methods、SI和图件均未修改；记录全部13个section文件的SHA-256。
- 两项响应数值、545.9小时有效时间、353天跨度、基线与链路长度均对照当前稿件。
- 未声称海洋负荷单独检测，未声称太阳频率成分排除了实验室扰动；SNR偏差原因保持可能解释。
- 通讯作者尚未确定，签名留待填写；未代作者声称全部作者已批准投稿、独家审理或不存在利益冲突。
- 原v3.22 cover letter保留。仅准备材料并同步至已授权的私有GitHub仓库，未投稿或联系推荐审稿人。

## 官方来源

用户新增论文的[Nature作者信息](https://www.nature.com/articles/s41586-026-11072-8#author-information)明确列出两位通讯作者K. J. Arnold（cqtkja@nus.edu.sg）与M. D. Barrett（phybmd@nus.edu.sg），用户明确选择后一位，因此仅将M. D. Barrett加入推荐名单。前版六人信件保存在before_additional_referees。

Laura的邮箱和研究领域与[NIST个人页面](https://www.nist.gov/people/laura-sinclair)一致；自由空间链路方向另见[NIST项目介绍](https://www.nist.gov/programs-projects/optical-two-way-time-frequency-transfer)。用户最初保留的四位推荐人联系信息依用户提供，未宣称本轮逐项核实。

[Nature初次投稿说明](https://www.nature.com/nature/for-authors/initial-submission)说明cover letter可用于向编辑披露相关工作；本信保留共享夏季记录及相关欧洲网络研究说明。

## 复现

build_letter.py使用科学Python环境的python-docx生成Word，Pandoc与XeLaTeX生成PDF。再次运行前应采用新交付目录，避免覆盖现有文件。
