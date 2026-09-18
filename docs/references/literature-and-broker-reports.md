# 涨停、连板与打板研究参考记录

更新日期：2026-09-18

本页把学术论文、制度研究和券商研报线索分开。论文条目尽量使用 DOI、期刊页或稳定书目信息。券商研报部分很多只能通过转载或摘要页确认，不能把摘要中的回测数字当作已复核结果。

## 一、优先阅读的学术论文

| 主题 | 文献 | 主要用途 | 与本仓库的对应 |
|---|---|---|---|
| 涨跌停与跨日行为 | Chen, Gao, He, Jiang & Xiong，*Daily Price Limits and Destructive Market Behavior*，*Journal of Econometrics*，2019，208(1)，249–264。[书目信息](https://ideas.repec.org/a/eee/econom/v208y2019i1p249-264.html) | 检查涨停日买入、次日卖出与长期反转是否能同时存在 | H1/H4，分别考察 T+1 与 T+20/T+60 |
| 注意力与涨停 | Seasholes & Wu，*Predictable Behavior, Profits, and Attention*，*Journal of Empirical Finance*，2007 | 研究涨停事件带来的散户注意力和短期价格压力 | H3，加入搜索量、股吧热度或替代变量 |
| 涨停与动量 | Liu, Wu & Zhu，*Price Overreaction to Up-limit Events and Revised Momentum Strategies in the Chinese Stock Market*，*Economic Modelling*，2022，114，105910。[DOI/书目信息](https://doi.org/10.1016/j.econmod.2022.105910) | 测试剔除涨停日收益后的动量是否更稳定 | H4，构造 exclude-limit-event momentum |
| 聚合涨停次数 | Cai, Jiang & Liu, “Investor Attention, Aggregate Limit-Hits, and Stock Returns,” *International Review of Financial Analysis*, 2022, 83, 102265. [期刊页](https://www.sciencedirect.com/science/article/pii/S1057521922002216) | 将历史涨停次数作为注意力代理，检验后续反转 | 直接对应 `60/120/250/500` 日涨停次数因子 |
| 制度改革与羊群 | “Could increasing price limits reduce up limit herding? Evidence from China's capital market reform,” *Finance Research Letters*, 2021, 42, 101909. [DOI/期刊页](https://doi.org/10.1016/j.frl.2020.101909) | 识别创业板 2020 年涨跌幅扩大后的行为变化 | 样本分层：主板、创业板、科创板及改革前后 |
| 涨跌停与市场质量 | “Effectiveness of price limits: Evidence from China’s ChiNext market,” *PLOS ONE*, 2023. [期刊页](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0287548) | 检查价格发现延迟、波动转移、交易受阻和磁吸效应 | 回测中加入次日波动、成交可得性和开板行为 |
| 注意力与散户交易 | Barber & Odean，*All That Glitters: The Effect of Attention and News on the Buying Behavior of Individual and Institutional Investors*，*Review of Financial Studies*，2008，21(2)，785–818。[书目信息](https://ideas.repec.org/a/oup/rfinst/v21y2008i2p785-818.html) | 给“涨停是注意力冲击”提供行为金融基础 | H3，避免把成交量直接命名为“主力吸筹” |
| 搜索量与短期延续/反转 | Da, Engelberg & Gao，*In Search of Attention*，*Journal of Finance*，2011，66(5)，1461–1499。[DOI](https://doi.org/10.1111/j.1540-6261.2011.01679.x) | 设计注意力冲击后的多时间尺度收益检验 | H3，比较 T+1、T+5、T+20 |
| 彩票型偏好 | Bali, Cakici & Whitelaw，*Maxing Out: Stocks as Lotteries and the Cross-section of Expected Returns*，*Journal of Financial Economics*，2011，99(2)，427–446。[书目信息](https://ideas.repec.org/a/eee/jfinec/v99y2011i2p427-446.html) | 解释极端上涨、正偏度与中长期低收益的关系 | H4，对比“再次涨停概率”和“长期收益” |
| 价格限制理论 | Subrahmanyam, “Circuit Breakers and Market Volatility: A Theoretical Perspective,” *Journal of Finance*, 1994 | 理解交易受阻、提前交易和涨停附近的价格行为 | 回测中显式记录排队、无法成交和延迟价格发现 |

## 二、可作为研究机制补充的条目

- Kim & Rhee, “Price Limit Performance: Evidence from the Tokyo Stock Exchange,” *Journal of Finance*, 1997：把价格发现延迟、波动转移和交易受阻作为制度评估维度。
- Barber, Odean & Zhu, “Do Retail Trades Move Markets?”, *Review of Financial Studies*, 2009：用于区分散户短期推动与长期反转。
- Baker & Wurgler, “Investor Sentiment and the Cross-Section of Stock Returns,” *Journal of Finance*, 2006：用于市场情绪 regime 设计。
- Zeng & Tang，*Price Limits and Overreacted Trading: Evidence from China*，2022/2023 working-paper version：可作为频繁触板、微盘/成长股和牛市条件效应的补充线索。发布前应以正式期刊版本为准。[SSRN](https://papers.ssrn.com/sol3/Delivery.cfm/SSRN_ID4368803_code5622353.pdf?abstractid=4301723)

## 三、券商研报线索

下列条目适合用来挖掘特征和行业实践，不应直接视为独立学术证据。需要在 public release 前核实原始 PDF、发布日期、作者、数据口径、版权和是否存在转载删节。

| 机构/标题线索 | 适合借鉴的变量 | 当前状态 |
|---|---|---|
| 国金证券《5年200倍的打板策略？涨停板相关研究》（2016） | 首次封板时间、自然板/一字板、摸板、连板数 | 标题和摘要线索已知。原始报告与再分发许可待核验 |
| 东方证券《涨停板事件对股票价格行为的影响》（2020） | 开板后异常收益、磁吸效应、剔除涨停收益的动量 | 适合作为学术论文的工程化补充。原始 PDF 待核验 |
| 国泰君安/国泰海通《个股打板表现复盘》系列 | 炸板率、封单比、集合竞价涨幅、竞价成交占比、连板数 | 系列报告，应逐篇记录日期和版本 |
| 广发证券《基于涨跌停溢出效应的因子研究》（2023） | 关联股、行业/题材扩散、涨停外溢因子 | 需要取得原始报告并核对定义 |
| 开源证券《从涨跌停效应到行业反转》（2023） | 行业聚合、涨跌停事件后的行业反转 | 需要取得原始报告并核对样本期 |
| 开源证券《从涨跌停外溢行为到股票关联网络》（2024） | 共同涨停、资金流、隔夜收益构建关联网络 | 需要取得原始报告并核对数据授权 |

## 四、从文献到本项目的可检验假设

| 假设 | 事件定义 | 结果变量 | 必须控制/分层 |
|---|---|---|---|
| H1 首次触板时间 | 当日第一次触及涨停的分钟 | 次日开盘、10:00、10:30、收盘收益 | 市场情绪、流通市值、板块强度、涨跌幅制度 |
| H2 封板质量 | 封板持续时长、开板次数、最后回封时间、封单变化 | 成交概率与 T+1 溢价 | 委托排队、成交量、板块涨停家数 |
| H3 注意力压力 | 涨停次数、搜索/股吧热度、异常成交量 | T+1/T+5 延续与 T+20/T+60 反转 | 个股规模、波动、市场状态、事件重叠 |
| H4 涨停基因双重性 | 过去 60/120/250/500 日涨停次数 | 再次涨停概率 vs 中长期收益 | 流通盘、成长/微盘、牛熊 regime |
| H5 市场状态条件化 | 涨停家数、炸板率、昨日涨停溢价、最高板高度、晋级率 | 策略收益、成交率、回撤 | 主板/创业板/科创板及制度变更 |
| H6 涨停外溢 | 同题材、行业或历史共同涨停网络中的事件 | 关联股隔夜/次日收益 | 关联强度、共同事件、行业和市场状态 |

## 使用规则

这些资料用于形成研究假设，不构成投资建议。任何“有效因子”都需要在事件时点、真实成交约束、手续费/滑点、滚动样本外和多重检验控制下重新验证。
