# v67 投稿前待补信息

本文件与论文分开，避免稿面反复出现占位符；删除占位符不表示以下事项已经完成。v67 是科学内容和格式修订稿，尚不是完整可提交稿。

## 必须由作者确认

1. 本篇作者名单、排序、共同贡献与通讯作者。已找到 PRL 的 35 位作者及三位通讯作者，但没有材料证明名单可直接用于本篇。六个单位沿用此前授权的 PRL 来源。
2. 本篇作者贡献、基金适用性及利益冲突声明。不能自动转写 PRL 基金，也不能替全体作者声明没有利益冲突。
3. 本篇实际的作者复核范围，尤其 v29 主估计、残差重采样、模拟覆盖和图 2 源数据。AI 用途已实写在 Methods，但不代替作者复核声明。
4. 可供编辑/审稿人访问的数据和可执行代码包及真实链接/DOI。当前私有 GitHub 仅存稿件与报告，不等同于主要分析复现数据。正文按此前要求保留向通讯作者提出请求的渠道描述；这尚未完成投稿访问安排。
5. v29 主分析所用 gravity-toolkit 版本、提交或环境记录，以及载荷 Love 数文件标识。官方文档提供的 DOI 10.5281/zenodo.5156864 是全版本概念 DOI。已补入引用，但没有虚构运行版本或版本 DOI。

## 已有来源（只读）

- PRL 作者与基金：`/home/room115/gravitation-whsh/paper/overleaf-prl/main.tex`。
- 同事 Nature 待确认清单：`/home/room115/gravitation-whsh/paper/nature/opencode-period-offset-20261105/AUTHOR_CONFIRMATIONS.md`。
- gravity-toolkit 官方引文：https://gravity-toolkit.readthedocs.io/en/latest/project/Citations.html 。当下文档版本不能证明历史主分析的安装版本。
- FES2022 官方建议引用：https://www.aviso.altimetry.fr/fr/donnees/produits/produits-auxiliaires/maree-oceanique-fes/publication-fes22.html 。数据集采用 CNES 2024、Version 2024、DOI 10.24400/527896/A01-2024.004；不再用 FES2014 论文支持 FES2022 产品。

## 保留的科学资料问题（本轮不重算）

- Fig. 2 误差棒固定非月潮拟合项，未传播全 nuisance 协方差。本轮采用用户允许的展示定位，未把其当第二条显著性证据。
- 原图 campaign 整数小时相加为 545 h，正文总量为 544 h。可能与取整有关，但缺少逐段表无法确认；本轮未自行调整数字。
- v29 的主要源数据、源代码和软件环境尚未形成我们已执行验证的完整包。当前只能称 PDF 数值核验及编辑验收，不能称从原始计数器完整复现。
