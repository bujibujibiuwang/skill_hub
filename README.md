# My Skill Hub

统一维护个人 Agent Skills 的 Git 仓库。当前只管理 `business-algorithm-visualizer`。

## Skill 导航

| Skill | 分类 | 适用场景 | 来源 |
|---|---|---|---|
| [business-algorithm-visualizer](skills/business-algorithm-visualizer/SKILL.md) | business-communication | 将供应链、物流、库存、路由、分货、预测和优化逻辑转成业务可理解的图示与解释 | `/Users/zoeywang/Documents/Codex/2026-11-09/referenced-chatgpt-conversation-this-is-an/outputs/business-algorithm-visualizer` |

## 常用命令

```bash
python3 scripts/skill-manager.py validate
python3 scripts/skill-manager.py search algorithm
python3 scripts/skill-manager.py scan ~/.codex/skills ~/.claude/skills
python3 scripts/skill-manager.py conflicts ~/.codex/skills ~/.claude/skills
python3 scripts/skill-manager.py install business-algorithm-visualizer
python3 -m unittest discover -s tests -v
```

全局安装采用 symlink，目标为 `~/.codex/skills/business-algorithm-visualizer`，不会覆盖已有目录。

## 维护规范

请先阅读 [AGENTS.md](AGENTS.md)，再修改 Skill 或索引。完整盘点见 [reports/inventory-2026-11-13.md](reports/inventory-2026-11-13.md)。
