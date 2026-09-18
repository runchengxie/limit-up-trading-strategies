# 维护与验证

## 安装开发依赖

项目要求 Python 3.11 或更高版本。安装测试和代码质量检查依赖：

```bash
python -m pip install -e ".[test,dev]"
```

构建文档站前安装固定版本的 MkDocs 依赖：

```bash
python -m pip install -r requirements-docs.txt
```

## 本地检查

每次修改代码后运行：

```bash
python -m pytest -q
python -m compileall -q src tests
python -m ruff check src tests
```

每次修改文档或 `mkdocs.yml` 后运行：

```bash
mkdocs build --strict
```

`mkdocs build --strict` 会把文档警告视为错误。生成的 `site/` 目录只用于本地预览，不提交到 Git。

## 自动化检查

`.github/workflows/ci.yml` 在 Python 3.11 和 3.12 上运行测试、字节码编译和 Ruff。`.github/workflows/docs.yml` 构建 MkDocs 站点，并在 `main` 分支构建成功后发布到 GitHub Pages。

文档站只发布 `mkdocs.yml` 导航中列出的页面。`docs/superpowers/` 中的设计和执行记录保留在仓库中，但不会进入公开站点。

## 修改边界

- 不把私有 archive 的原始策略、数据导出物、交易日志和 Notebook 输出复制到公共仓库。
- 修改公共 API 时，同时更新测试、README 和相关文档。
- 研究结果需要写明数据来源、截止日期、成交假设、制度分层和样本外范围。
- 第三方论文、研报和数据只保留必要的来源信息，发布前核对授权条件。
