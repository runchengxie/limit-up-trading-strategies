# Public 文档与 Pages 迁移设计

## 目标

以 `limit-up-trading-strategies-public` 为唯一对外项目，把 archive 版本中适合公开的文档维护成果迁移到 public，并补齐 MkDocs 文档站与 GitHub Pages 自动部署，同时保留现有 Python 代码、测试和 CI。

## 迁移范围

### 迁移到 public

- 中文 README，准确描述 public 仓库现有的事件研究代码、测试和研究边界。
- 现有文献、研究路线和公开发布说明的中文润色。
- `AGENTS.md`，记录项目性质、验证命令和公开仓库变更原则。
- `mkdocs.yml`、文档依赖、文档首页和维护验证页。
- GitHub Pages workflow，使用 MkDocs 构建并通过 GitHub Actions 发布。

### 留在 archive

- 原始策略 TXT、Notebook、Excel、CSV、图片、日志和其他研究产物。
- archive 的历史 Git 对象、私有脱敏记录和内部 Superpowers 计划。
- 任何第三方策略全文或尚未确认再分发授权的原始材料。

## 兼容与安全约束

- 不覆盖 public 的 `src/`、`tests/`、`pyproject.toml` 和现有 CI。
- MkDocs 只读取 public 的 `docs/`，导航只引用 public 中现有的 Markdown 页面和新增的公共维护页。
- Pages workflow 只部署 MkDocs 生成的 `site/`，不把仓库根目录或私有 archive 数据上传为站点内容。
- 保留现有 Python 3.11/3.12 测试矩阵和 `python -m compileall -q src tests` 检查。

## 验证

- `python -m pytest -q`
- `python -m compileall -q src tests`
- `mkdocs build --strict`
- GitHub Actions 的 Python CI 和 Pages workflow 均成功运行。

## 分支与交付

在 public 仓库创建独立功能分支，提交后创建 PR 合并到 `main`。archive 仓库不再因为本次迁移产生新改动。
