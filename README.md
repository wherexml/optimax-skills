# OptiMax Skills

> OptiMax 维护的可复用 AI Skills，让经过验证的工作方法可以被不同 AI 工具稳定调用。

本仓库用于沉淀 OptiMax 在产品、管理、设计、分析和企业决策等场景中的
标准工作流程。每个 Skill 都是一套独立、可安装、可复用的能力包，包含任务说明、
执行规则、参考资料和必要资产。

## Skills 列表

| Skill | 用途 | 详情 |
| --- | --- | --- |
| `optimax-ppt-imagegen` | 生成风格统一的企业级 PPT 信息图主视觉 | [查看说明](optimax-ppt-imagegen/SKILL.md) |

后续新增的 Skills 将统一收录在这里。

## 快速安装

安装仓库中的指定 Skill：

```bash
npx --yes skills add wherexml/optimax-skills \
  -g --skill <skill-name> --agent '*' -y
```

将 `<skill-name>` 替换为 Skills 列表中的名称。安装完成后，新开一个 AI 会话即可使用。

例如：

```bash
npx --yes skills add wherexml/optimax-skills \
  -g --skill optimax-ppt-imagegen --agent '*' -y
```

## 使用方式

在支持 Skills 的 AI 工具中直接指定需要使用的 Skill，并提供任务目标和必要材料：

```text
使用 $<skill-name> 完成下面的任务：

[任务目标]
[背景材料]
[输出要求]
```

每个 Skill 的输入要求、默认行为和交付标准，请查看对应目录下的 `SKILL.md`。

## 仓库结构

```text
optimax-skills/
├── README.md
└── <skill-name>/
    ├── SKILL.md          # 能力说明、工作流程与验收标准
    ├── agents/           # AI 工具展示信息
    ├── references/       # 规则、模板与参考资料
    ├── assets/           # 图片或其他静态资产
    └── scripts/          # 可选的辅助脚本
```

不同 Skill 可以根据实际需要省略非必要目录。

## 维护原则

- 一个目录只承载一个边界清晰的 Skill。
- `SKILL.md` 是该能力的唯一入口，必须写清适用场景、执行流程和验收标准。
- 示例、模板和静态资产放在 Skill 自己的目录内，不依赖维护者本机路径。
- 不在 Skill 中写入账号、密钥、客户隐私或其他敏感信息。
- 变更后应重新验证安装、资源引用和实际调用结果。
- README 只维护仓库级信息，具体能力说明放在对应 Skill 中。

## 参与完善

欢迎通过 Issue 提交使用反馈、场景建议和问题报告。新增或调整 Skill 时，
请同步维护对应的说明、参考资料和资产，确保其他使用者安装后能够直接调用。

---

由 **OptiMax** 持续维护。
