#!/usr/bin/env python3
"""Collect lightweight, privacy-safe evidence from an existing source tree."""
import argparse, json, re
from pathlib import Path

IGNORE={".git","node_modules","target","dist","build",".grad-project","venv",".venv"}
EXTS={".java",".kt",".py",".js",".ts",".vue",".sql",".xml",".yml",".yaml"}

def main():
    ap=argparse.ArgumentParser(); ap.add_argument("root"); ap.add_argument("--output",default=".grad-project/scan.json"); args=ap.parse_args()
    root=Path(args.root); files=[]; endpoints=[]; tables=[]; tests=[]; comments=0
    for p in root.rglob("*"):
        if not p.is_file() or any(part in IGNORE for part in p.parts) or p.suffix.lower() not in EXTS: continue
        rel=str(p.relative_to(root)); files.append(rel)
        text=p.read_text(encoding="utf-8",errors="ignore"); comments += len(re.findall(r"//|/\*|#", text))
        endpoints += re.findall(r"(?:@(?:Get|Post|Put|Delete|Request)Mapping\s*\(\s*[\"']([^\"']+)|(?:router|app)\.(?:get|post|put|delete)\s*\(\s*[\"']([^\"']+))", text, re.I)
        tables += re.findall(r"\bCREATE\s+TABLE\s+(?:IF\s+NOT\s+EXISTS\s+)?[`\"]?([A-Za-z0-9_]+)", text, re.I)
        if re.search(r"test|spec", p.name, re.I): tests.append(rel)
    result={"root":str(root),"files":files,"file_count":len(files),"comment_markers":comments,"endpoints":[a or b for a,b in endpoints],"tables":sorted(set(tables)),"test_files":tests}
    out=Path(args.output); out.parent.mkdir(parents=True,exist_ok=True); out.write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding="utf-8"); print(json.dumps(result,ensure_ascii=False,indent=2))

if __name__ == "__main__": main()
