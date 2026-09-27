#!/usr/bin/env python3
"""Validate project facts and report missing delivery evidence."""
import argparse, json, re
from pathlib import Path

def main():
    ap = argparse.ArgumentParser(); ap.add_argument("manifest"); args = ap.parse_args()
    path = Path(args.manifest); data = json.loads(path.read_text(encoding="utf-8")); errors=[]; warnings=[]
    for key in ["schema_version", "project", "stack", "roles", "features", "deliverables"]:
        if key not in data: errors.append(f"missing required field: {key}")
    for feature in data.get("features", []):
        fid=feature.get("id", "")
        if not re.fullmatch(r"[a-z0-9-]+", fid): errors.append(f"invalid feature id: {fid}")
        for key in ["name", "actor", "status"]:
            if not feature.get(key): errors.append(f"{fid}: missing {key}")
        if not feature.get("tests"): warnings.append(f"{fid}: no tests defined")
        if not feature.get("entities"): warnings.append(f"{fid}: no entities mapped")
    uml_dir=path.parent / "uml"
    if not uml_dir.exists(): warnings.append("uml directory not generated")
    else:
        for feature in data.get("features", []):
            if not (uml_dir / f"{feature['id']}.puml").exists(): warnings.append(f"{feature['id']}: missing sequence diagram")
    result={"manifest":str(path),"ok":not errors,"errors":errors,"warnings":warnings,"feature_count":len(data.get("features",[]))}
    print(json.dumps(result, ensure_ascii=False, indent=2)); return 0 if not errors else 1

if __name__ == "__main__": raise SystemExit(main())
