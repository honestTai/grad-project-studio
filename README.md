<div align="center">

**English** · [简体中文](README.zh-CN.md)

[HRouter](https://hrouter.net/home) · [All public projects](https://github.com/honestTai) · [Star & Fork trends](#project-activity)

</div>

[![Repository summary](https://raw.githubusercontent.com/honestTai/honestTai/main/assets/badges/grad-project-studio.svg)](#project-activity)

# Grad Project Studio

**Keep the code, diagrams, evidence, report, and presentation in sync.**

An open-source Codex workflow plugin for computer-science system-design projects. It organizes the topic, technology stack, user-provided templates, and real project evidence into a shared project fact model, then assists with implementation, PlantUML diagrams, reports, and defense presentations.

> Sponsored by [HRouter.net](https://hrouter.net). Open-source workflows for developers who need consistent AI-assisted implementation and documentation.

## What it solves

The hard part is not producing more text: it is making the code, database, screenshots, report, and slides agree. Each feature is tracked through an evidence chain:

```text
Requirements → Feature design → Database → PlantUML → Code → Tests → Screenshots → Report → Slides
```

- Multi-round requirement clarification, even when the starting point is only a title or technology stack.
- Workflow templates for management systems, Mini Programs, data analysis, recommendation systems, and microservices.
- A `project.json` fact model covering roles, features, entities, flows, technologies, and deliverables.
- Repeatable generation of PlantUML sequence, ER, and architecture diagrams.
- Repository scanning for page, API, database, test, and comment evidence.
- Report and presentation outlines, with the user's own templates taking priority.
- Quality gates for implementation, tests, diagrams, screenshots, and report mappings.
- Agent adaptation notes for Codex, Claude Code, Cursor, OpenCode, and Gemini CLI.

## Writing and AI-text detection

Writing should be grounded in real project facts: concrete APIs, fields, exception handling, test results, and screenshots, with generation and revision records retained. Avoid generic filler and repetitive phrasing.

Detection tools, thresholds, and false positives vary. This plugin does **not** guarantee a detection result or promise to bypass detection. Review and adapt all deliverables under the rules of the institution or organization receiving them.

## Quick start

```powershell
cd plugins/grad-project-studio
python scripts/new_project.py --title "Campus mutual-aid system with Spring Boot and uni-app" --stack springboot,uni-app,mysql
python scripts/generate_plantuml.py .grad-project/project.json
python scripts/validate_project.py .grad-project/project.json
```

The generated `.grad-project/` directory contains the fact model, PlantUML sources, evidence index, and deliverable inventory. In Codex, load `skills/grad-project-studio/SKILL.md` inside the plugin before entering clarification, implementation, or delivery.

## Recommended workflow

1. Provide a topic, stack, outline, or existing code.
2. Clarify roles, features, administration, data, permissions, and user templates.
3. Confirm the feature list and templates before implementation.
4. Implement the project with comments, unit/API tests, and run instructions.
5. Capture evidence from actual browser interactions using Kimi WebBridge.
6. Generate diagrams, report content, and presentation content.
7. Validate that code, screenshots, report, and slides use the same facts.

## License and support

[MIT License](LICENSE). Contributions of templates, test adapters, and agent entry points are welcome.

Sponsored by [HRouter.net](https://hrouter.net), which provides model access and workflow support for developers.

---

<a id="project-activity"></a>

## Project activity

Star / Fork totals and retained-event history, scheduled to refresh daily.

[![Star and Fork history for grad-project-studio](https://raw.githubusercontent.com/honestTai/honestTai/main/assets/metrics/grad-project-studio.svg)](https://github.com/honestTai/honestTai/blob/main/data/README.md)

[Observed daily totals](https://raw.githubusercontent.com/honestTai/honestTai/main/assets/metrics/grad-project-studio-daily.svg) · [Methodology](https://github.com/honestTai/honestTai/blob/main/data/METHODOLOGY.md) · [All public projects](https://github.com/honestTai)

<sub>Historical curves reconstruct currently retained stars and visible forks, not historical net totals. Separate daily observations start on 2026-10-06; no fabricated backfill.</sub>
