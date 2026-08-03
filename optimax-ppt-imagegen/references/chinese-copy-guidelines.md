# Natural Chinese copy guidelines

Use these rules before locking `EXACT_LABELS` unless the user explicitly requires verbatim wording.

## Principles

- Write for an executive audience, not for the implementation team.
- Name what happens or what the reader receives. Prefer an action plus an object, or a clear outcome.
- Keep main labels to 4–8 Chinese characters when practical. Use one short supporting line only when it adds necessary meaning.
- Preserve facts and product meaning. Improve wording without inventing capabilities, results, or maturity.
- Keep established terms such as AI, Agent, API, RiskOps, or a product name only when the intended audience understands them.

## Rewrite patterns

| Avoid | Prefer | Reason |
| --- | --- | --- |
| Wiki 更新门 | 管理知识更新 | State the action; avoid a literal “gate” metaphor. |
| 待办门 | 行动项同步 | State the business result. |
| 简报发布 | 简报生成发布 | Make the full action clear. |
| 事实合并 | 事实核验归并 | Add the essential verification meaning. |
| 管理分析 | 今日管理研判 | Use natural management language. |
| 三路证据 | 信息交叉核验 | Describe the purpose instead of the source count. |
| 三路分析 | 三类管理视角 | Describe the reader's perspective. |
| 优先级抑制 | 优先级排序 | Avoid an engineering control term. |
| 单一写入 | 避免重复创建 | State the practical outcome. |
| 写后验证 | 创建结果确认 | Avoid database-style wording. |
| 双写一致 | 内容一致性 | State the quality requirement. |
| 干系人管理 | 团队跟进重点 | Use concrete management language. |

## Gate terminology

Use “门” or “门禁” only for a real approval or blocking checkpoint. Otherwise choose the actual action:

- validation → 校验, 确认, 核对
- approval → 审批, 审核
- update → 更新, 同步, 沉淀
- publish → 生成发布, 输出
- orchestration → 协同调度, 统一协调
