# 公共仓库协作说明

## 项目范围

本仓库维护涨停事件研究的公开代码、研究假设和可复现说明。代码使用合成输入，当前不下载、存储或分发行情数据，也不提供实盘交易信号。

私有 archive 仓库中的原始策略文本、数据导出物、Notebook 输出、交易记录和内部材料不属于本仓库的发布内容。除非明确授权，不要复制到这里。

## 开发约定

- Python 版本要求为 3.11 或更高版本。
- 源代码位于 `src/limit_up_event_study`，测试位于 `tests`。
- 新增行为先补充测试，再修改实现。
- 公共 API 的变更需要同步更新 README、API 示例和相关测试。
- 文档以中文为主。类名、函数名、命令、文件名、论文标题和必要的英文专有名词保留原文。
- Markdown 使用中文标点，避免不必要的强调、长句和模板化总结。

## 本地检查

```bash
python -m pip install -e ".[test,dev]"
python -m pytest -q
python -m compileall -q src tests
python -m ruff check src tests
mkdocs build --strict
```

提交前还要运行 `git diff --check`，确认没有空白字符错误，也不要提交 `site/`、缓存、虚拟环境或本地数据文件。
