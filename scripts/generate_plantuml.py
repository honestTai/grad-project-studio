#!/usr/bin/env python3
"""Generate editable PlantUML source from a project fact model."""
import argparse, json, re
from pathlib import Path

def ident(value): return re.sub(r"[^A-Za-z0-9_]", "_", value)

def main():
    ap = argparse.ArgumentParser(); ap.add_argument("manifest"); ap.add_argument("--output")
    args = ap.parse_args(); manifest = Path(args.manifest); data = json.loads(manifest.read_text(encoding="utf-8"))
    root = Path(args.output) if args.output else manifest.parent / "uml"; root.mkdir(parents=True, exist_ok=True)
    stack = ", ".join(data.get("stack", {}).values()) or "待确认"
    (root / "architecture.puml").write_text(f"@startuml\ntitle {data['project']['title']} 系统架构\n[前端] --> [后端服务]\n[后端服务] --> [数据库]\nnote right: 技术栈：{stack}\n@enduml\n", encoding="utf-8")
    er = ["@startuml", f"title {data['project']['title']} ER 图"]
    for entity in data.get("entities", []):
        er.append(f"entity \"{entity.get('label', entity['name'])}\" as {ident(entity['name'])} {{")
        for field in entity.get("fields", []): er.append(f"  * {field['name']} : {field.get('type','TEXT')} {field.get('key','')}")
        er.append("}")
    er.append("@enduml\n"); (root / "er.puml").write_text("\n".join(er), encoding="utf-8")
    for feature in data.get("features", []):
        lines = ["@startuml", f"title {feature['name']} 时序图", f"actor ActorUser as \"{feature.get('actor','用户')}\"", "boundary Frontend as \"前端\"", "control Controller as \"控制器\"", "control Service as \"服务层\"", "database Database as \"数据库\""]
        lines.append(f"ActorUser -> Frontend: {feature['name']}请求"); lines.append("Frontend -> Controller: 调用接口"); lines.append("Controller -> Service: 执行业务校验")
        for step in feature.get("main_flow", []): lines.append(f"Service -> Database: {step}")
        lines += ["Database --> Service: 返回结果", "Service --> Controller: 业务结果", "Controller --> Frontend: 响应数据", "Frontend --> ActorUser: 展示结果", "@enduml\n"]
        path = root / f"{feature['id']}.puml"; path.write_text("\n".join(lines), encoding="utf-8")
        data.setdefault("deliverables", {}).setdefault("uml", []).append(str(path))
    manifest.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"generated PlantUML in {root}")

if __name__ == "__main__": main()
