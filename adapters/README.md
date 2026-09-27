# Agent 适配器

核心工作流在 `skills/grad-project-studio/`，不同 Agent 只需要加载同一份 Skill 和脚本。

建议入口：

- Codex：在项目根 `AGENTS.md` 中引用本 Skill。
- Claude Code：在 `CLAUDE.md` 中引用本 Skill。
- Cursor：复制为 `.cursor/rules/grad-project-studio.mdc`。
- OpenCode：复制到 `.opencode/skills/grad-project-studio/SKILL.md`。
- Gemini CLI：在 `GEMINI.md` 中引用本 Skill。

平台入口只处理加载方式，项目事实模型、生成规则、质量门禁和证据格式保持一致。
