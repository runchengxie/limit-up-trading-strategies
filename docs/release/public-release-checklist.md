# Public Release Checklist

这是未来创建 clean public tree 前的门禁清单。当前仓库仍是私有研究档案，未满足的项目不能用“已脱敏”代替。

## A. 工作树内容

- [x] README 和策略正文不含已确认的本机下载路径。
- [x] 策略正文不含已确认的个人微信联系方式。
- [ ] 全部 Markdown、TXT、CSV 和 Notebook source 再做路径、邮箱、手机号、token、API key、密码和账号扫描。
- [ ] 对 `.ipynb` 清除不必要的 outputs、execution counts 和环境路径。

## B. 二进制和元数据

- [ ] 检查 XLS/XLSX 的 creator、lastModifiedBy、custom properties、comments 和隐藏工作表。
- [ ] 检查 PNG/WEBP 的 EXIF、软件标记和注释。
- [ ] 不把原始压缩包或可逆推出个人/账户信息的导出物放入 public tree。

## C. Git 历史

- [ ] 决定采用历史重写还是新建 clean public repo；默认推荐后者。
- [ ] 如果重写历史，先备份并通知已有 clone/fork 持有者，再用 `git-filter-repo` 清理路径和邮箱。
- [ ] 清理后检查所有 refs、tags、reflog 和远端缓存策略。
- [ ] 新 public repo 使用 GitHub `noreply` commit email。

## D. 版权、来源与数据

- [ ] 核实聚宽策略原文的再分发许可；作者署名和链接不自动等于代码再许可。
- [ ] 核实数据供应商和平台导出物的再分发限制。
- [ ] public tree 只保留自写代码/说明、必要的派生统计和来源链接。
- [ ] 为第三方材料保留 attribution，但不复制不必要的完整正文或原始附件。

## E. 研究表达

- [ ] 把“回测收益”“可成交收益”“实盘收益”明确区分。
- [ ] 记录信号时点、下单时点、首次可成交时点、成交概率、滑点、费用和排队成本。
- [ ] 分开主板 10%、创业板/科创板 20%、ST 和制度改革前后样本。
- [ ] 使用滚动样本外验证、时间隔离和多重检验控制；不使用随机打乱日期的训练/测试切分。
- [ ] README 明确说明：资料仅供研究，不构成投资建议。
