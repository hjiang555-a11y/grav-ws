# v3.22 F1 源包范围修复记录

基线：`e272360`。范围仅为终审 `FINAL_REVIEW.md` 的 F1 Minor；不涉及科学分析或论文内容。

## 实际修改

- `scripts/prepare_delivery.py` 的源码路径集合新增 `validate_editorial.py`、`inspect_pdf.py`、`check_word.py`、`check_source_rebuild.py`，保留三个既有构建/导出脚本。
- 内嵌源码 README 逐项解释可运行条件：冻结 v3.21 工作站基线及绝对路径哈希证据、生成的 `formal_build_01` 文件、PyMuPDF/Pillow、已有 LibreOffice 预览，以及源包重建检查所需的原项目 `evidence/BRANCH_METADATA.json` 和真实交付目录。明确仅打包 `evidence/APPROVED_ABSTRACT_SOURCE.md` 到原 evidence 路径，已有 JSON/审阅记录不能代替全部工作站输入。
- README 保留从源码重建排版的入口；不声称所有审计在解压源码包中独立可运行，不预先宣称重建成功。
- `FORMAT_CHECK_ZH.md` 无需修改：其“详细程序与JSON记录随源包保留”的承诺由新增脚本纳入清单落实。

## 实际验证

使用 `/data/AI_Research/environments/python/sci/bin/python`：

1. `ast.parse` 解析修改后的脚本成功。
2. 仅提取并执行 AST 中构造 `paths` 的区段，提供 `R` 和 `re`，未执行顶层交付目录创建、复制、打包、manifest 或其他交付代码。
3. 实际得到 **40** 个源码路径；全部存在、位于项目内且相对路径唯一。
4. 脚本集合精确为 **7** 项：三个 builder/exporters 及四个审计程序；逐项在内嵌 README 出现。
5. evidence 原路径纳入集合精确为 `evidence/APPROVED_ABSTRACT_SOURCE.md`；README 对未打包的基线、预览及交付元数据披露与清单一致。
6. README 检查覆盖 v3.21 基线、`BASELINE_V321_HASHES.json`、`formal_build_01`、PyMuPDF、Pillow、LibreOffice、`evidence/word_preview_01`、`evidence/BRANCH_METADATA.json`、`evidence/source_rebuild_01` 和非全便携声明，全部通过。
7. `git diff --check` 通过。

## 边界及后续

本轮未运行 `prepare_delivery.py`、任一审计脚本或排版构建，未生成/修改源码 ZIP、最终 PDF、Word、图件、稿件源文或科学结果。`check_source_rebuild.py` 当前为整合者提供的未跟踪脚本，本提交只引用其打包路径，不将该脚本或其他整合者未跟踪产物提交。实际源码包生成、独立排版重建、交付清单和私有推送由整合者执行后据实登记。

提交范围严格为 `scripts/prepare_delivery.py` 与本报告。工作树中其他已有/并行变动不属于本修复。
