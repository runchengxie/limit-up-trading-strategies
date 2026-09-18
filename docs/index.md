# 涨停事件研究

这里是项目的公开文档站，记录涨停事件研究的代码基础、研究假设和验证路线。

## 当前代码

仓库提供一个轻量的 Python 包 `limit-up-event-study`，使用合成输入演示以下能力：

- 校验涨停事件的身份、时间、价格和市场分段。
- 把成交概率、滑点、费用和排队成本纳入收益期望。
- 计算多个持有期限的收益、MFE 和 MAE。

代码位于 `src/limit_up_event_study`，测试位于 `tests`。当前版本不下载或打包行情数据，也不提供实盘信号。

## 研究文档

- [打板研究路线](research/strategy-research-roadmap.md)：从事件级数据表到样本外验证的研究顺序。
- [文献与研究假设](references/literature-and-broker-reports.md)：论文、研报线索和可检验假设。
- [维护与验证](maintenance-and-validation.md)：本地检查、CI 和文档构建说明。
- [公共发布清单](release/public-release-checklist.md)：发布代码和研究结果前的检查项目。

## 研究边界

文档中的研究假设不等于已验证的交易策略。使用真实数据时，需要处理点时信息、成交约束、涨跌幅制度、费用、滑点、停牌、样本外区间和多重检验。

项目内容仅供研究和软件开发，不构成投资建议。
