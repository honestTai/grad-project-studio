#!/usr/bin/env python3
"""Create a reviewable report, PPT and browser evidence plan from project facts."""
import argparse, json
from pathlib import Path

def main():
    ap=argparse.ArgumentParser(); ap.add_argument("manifest"); ap.add_argument("--output", default=None); args=ap.parse_args()
    manifest=Path(args.manifest); data=json.loads(manifest.read_text(encoding="utf-8")); out=Path(args.output) if args.output else manifest.parent
    out.mkdir(parents=True, exist_ok=True)
    title=data["project"]["title"]; features=data.get("features",[])
    report=[f"# {title} 系统设计交付计划", "", "## 事实来源", "", f"- 项目类型：{data['project'].get('profile','custom')}", f"- 技术栈：{', '.join(data.get('stack',{}).values()) or '待确认'}", f"- 角色：{', '.join(data.get('roles',[]))}", "", "## 报告章节", "", "1. 绪论", "2. 关键技术介绍", "3. 系统分析", "4. 系统设计", "5. 系统实现", "6. 系统测试", "7. 结论与展望", "", "## 功能映射", ""]
    for f in features: report.append(f"- `{f['id']}` {f['name']}：状态 `{f.get('status','planned')}`，接口 `{f.get('api','待补充')}`，实体 `{', '.join(f.get('entities',[])) or '待补充'}`")
    (out/"report_outline.md").write_text("\n".join(report)+"\n", encoding="utf-8")
    ppt=[f"# {title} 答辩 PPT 计划", "", "1. 封面", "2. 目录", "3. 选题背景与意义", "4. 关键技术", "5. 需求分析", "6. 系统架构", "7. 数据库设计", "8. 核心功能设计", "9. 系统实现截图", "10. 系统测试", "11. 总结与展望", "12. 致谢", "", "## 截图页素材", ""]
    for f in features: ppt.append(f"- {f['name']}：对应 `.grad-project/evidence/{f['id']}.png`，操作路径待在浏览器中验证")
    (out/"ppt_outline.md").write_text("\n".join(ppt)+"\n", encoding="utf-8")
    plan={"project":title,"tasks":[{"feature_id":f["id"],"name":f["name"],"actor":f.get("actor"),"url":"待启动","steps":f.get("main_flow",[]),"expected":"功能完成并显示成功结果","screenshot":f"evidence/{f['id']}.png","status":"planned"} for f in features]}
    (out/"screenshot_plan.json").write_text(json.dumps(plan,ensure_ascii=False,indent=2),encoding="utf-8")
    print(f"created delivery plan in {out}")

if __name__ == "__main__": main()
