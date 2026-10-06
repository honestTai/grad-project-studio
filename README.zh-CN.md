<div align="center">

[English](README.md) · **简体中文**

[HRouter](https://hrouter.net/home) · [All public projects](https://github.com/honestTai) · [Star & Fork trends](#project-activity)

</div>

[![Repository summary](https://raw.githubusercontent.com/honestTai/honestTai/main/assets/badges/grad-project-studio.svg)](#project-activity)

# Grad Project Studio

Grad Project Studio 是一个面向计算机类系统设计项目的开源 Codex 工作流插件。它把题目、技术栈、用户模板和真实项目证据组织成一个项目事实模型，再围绕这个模型协助完成代码、PlantUML 图、系统设计报告和答辩 PPT。

> **HRouter.net 赞助项目**  
> 本工作流由 [HRouter.net](https://HRouter.net) 赞助，面向需要稳定 AI 开发与文档工作流的开发者开放源码。

## 它解决什么问题

很多系统设计材料的问题不是缺少文字，而是代码、数据库、截图、论文和 PPT 彼此对不上。Grad Project Studio 把每个功能作为一条可追溯链管理：

```text
需求 → 功能设计 → 数据库 → PlantUML → 代码 → 测试 → 浏览器截图 → 论文 → PPT
```

第一版包含：

- 多轮需求澄清提示词，支持用户只提供题目、提纲或技术栈。
- 普通管理系统、小程序、数据分析、推荐系统和微服务项目的模板化路由。
- `project.json` 项目事实模型，保存角色、功能、实体、流程、技术栈和交付物。
- PlantUML 时序图、ER 图和架构图的可重复生成脚本。
- 代码仓库扫描，收集页面、接口、数据库、测试和注释证据。
- 报告和答辩 PPT 的内容骨架，支持用户自有模板作为优先输入。
- 质量门禁，检查功能是否有实现、测试、图、截图和论文映射。
- Codex、Claude Code、Cursor、OpenCode、Gemini CLI 等 Agent 的适配说明。

## 关于 AIGC 文本检测

插件支持基于真实项目事实的自然化写作：减少空泛套话，改变机械重复的句式，加入项目中的接口、字段、异常处理、测试结果和截图证据，并保留生成过程和修改记录。

不同平台使用的检测工具、阈值和误报情况都不稳定，插件不承诺任何工具的固定检测结果，也不把绕过检测作为产品保证。推荐用户结合使用方规定审阅和修改最终材料。

## 快速开始

```powershell
cd plugins/grad-project-studio
python scripts/new_project.py --title "基于SpringBoot与uni-app的校园互助系统" --stack springboot,uni-app,mysql
python scripts/generate_plantuml.py .grad-project/project.json
python scripts/validate_project.py .grad-project/project.json
```

生成的 `.grad-project/` 目录包含项目事实模型、PlantUML 源文件、证据索引和交付物清单。Codex 使用本插件时，先加载 `skills/grad-project-studio/SKILL.md`，再根据用户输入进入需求澄清、实现或交付阶段。

## 推荐工作流

1. 输入题目、技术栈、已有提纲或现有代码。
2. Agent 询问角色、功能、后台、数据、权限和用户自有模板；信息不足时给出适合系统设计项目的建议。
3. 用户确认功能清单和自有模板。
4. Agent 实现项目，补充注释、单元测试、接口测试和运行说明。
5. 使用 Kimi WebBridge 进行真实页面操作并采集截图证据。
6. 生成 PlantUML 图、报告内容和答辩 PPT 内容。
7. 运行一致性检查，确认代码、截图、报告和 PPT 使用相同的项目事实。

## 开源协议

本项目使用 MIT License，见 [LICENSE](LICENSE)。欢迎提交用户模板、功能模板、测试适配器和其他 Agent 的入口文件。

## 赞助与支持

本项目由 [HRouter.net](https://HRouter.net) 赞助。HRouter.net 提供面向开发者的 AI 中转服务和工作流支持。

---

<a id="project-activity"></a>

## 项目动态 · Project activity

当前 Star / Fork 数量与留存事件历史，计划每日更新。

[![Star and Fork history for grad-project-studio](https://raw.githubusercontent.com/honestTai/honestTai/main/assets/metrics/grad-project-studio.svg)](https://github.com/honestTai/honestTai/blob/main/data/README.md)

[每日实测趋势](https://raw.githubusercontent.com/honestTai/honestTai/main/assets/metrics/grad-project-studio-daily.svg) · [数据口径](https://github.com/honestTai/honestTai/blob/main/data/METHODOLOGY.zh-CN.md) · [全部公开项目](https://github.com/honestTai)

<sub>历史曲线仅重建当前仍保留的 Star 与可见 Fork，并非过去每日净总量。每日实测总量自 2026-10-06 开始，不伪造回填。</sub>
