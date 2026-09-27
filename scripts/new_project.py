#!/usr/bin/env python3
"""Create a portable Grad Project Studio project fact model."""
import argparse, json, re
from pathlib import Path

PROFILES = {
    "springboot": "Spring Boot", "spring-boot": "Spring Boot", "uni-app": "uni-app",
    "vue": "Vue", "vue.js": "Vue", "mysql": "MySQL", "python": "Python",
    "django": "Django", "flask": "Flask", "redis": "Redis",
}

def slug(value: str) -> str:
    value = re.sub(r"[^\w\-]+", "-", value.lower(), flags=re.UNICODE)
    return re.sub(r"-+", "-", value).strip("-") or "project"

def guess_profile(title: str, stack: list[str]) -> str:
    text = (title + " " + " ".join(stack)).lower()
    if any(x in text for x in ["推荐", "协同过滤", "recommend"]): return "recommendation"
    if any(x in text for x in ["分析", "可视化", "大数据", "爬虫", "spark"]): return "analytics"
    if any(x in text for x in ["小程序", "uni-app", "移动"]): return "mini_program"
    if any(x in text for x in ["微服务", "nacos"]): return "microservice"
    return "crud"

def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--title", required=True)
    ap.add_argument("--stack", default="")
    ap.add_argument("--output", default=".grad-project/project.json")
    ap.add_argument("--school-template")
    args = ap.parse_args()
    stack_tokens = [x.strip() for x in args.stack.split(",") if x.strip()]
    stack = {slug(x): PROFILES.get(x.lower(), x) for x in stack_tokens}
    data = {
        "schema_version": "0.1",
        "project": {"title": args.title, "profile": guess_profile(args.title, stack_tokens), "school_template": args.school_template},
        "stack": stack,
        "roles": ["用户", "管理员"],
        "features": [
            {"id": "auth-login", "name": "登录", "actor": "用户", "description": "用户提交凭据后进入系统", "preconditions": ["用户已注册"], "main_flow": ["输入账号和密码", "服务端校验凭据", "返回登录状态"], "exceptions": ["账号或密码错误", "账号被禁用"], "entities": ["user"], "api": "POST /api/auth/login", "tests": ["正确凭据登录", "错误凭据拒绝"], "status": "planned", "evidence": []},
            {"id": "user-management", "name": "用户管理", "actor": "管理员", "description": "管理员查询、添加、修改和禁用用户", "preconditions": ["管理员已登录"], "main_flow": ["打开用户列表", "查询或编辑用户", "保存变更"], "exceptions": ["重复账号", "无权限"], "entities": ["user"], "api": "GET/POST /api/users", "tests": ["列表查询", "新增用户", "禁用用户"], "status": "planned", "evidence": []}
        ],
        "entities": [{"name": "user", "label": "用户", "fields": [{"name": "id", "type": "BIGINT", "key": "PK"}, {"name": "username", "type": "VARCHAR(64)", "key": ""}, {"name": "status", "type": "BOOLEAN", "key": ""}]}],
        "deliverables": {"report": {"status": "planned", "template": None}, "ppt": {"status": "planned", "slides": 14}, "screenshots": [], "uml": []},
        "audit": {"created_by": "grad-project-studio", "confirmed_by_user": False, "last_verified_at": None}
    }
    out = Path(args.output); out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"created {out}"); return 0

if __name__ == "__main__": raise SystemExit(main())
