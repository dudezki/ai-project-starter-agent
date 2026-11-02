#!/usr/bin/env python3
"""Generate a new project scaffold from this repository without overwriting files."""
import argparse
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FILES = ["AGENTS.md", "CLAUDE.md", "docs/PRD.md", "docs/ARCHITECTURE.md",
         "docs/RULES.md", "docs/DESIGN.md", "docs/TASKS.md", "docs/MEMORY.md",
         ".agents/skills/start-project/SKILL.md"]

def main():
    p = argparse.ArgumentParser(description="Scaffold a new AI-guided project")
    p.add_argument("name")
    p.add_argument("--idea", default="TBD — clarify during discovery")
    p.add_argument("--output", type=Path, default=Path.cwd())
    args = p.parse_args()
    name = args.name.strip()
    if not name or "/" in name or "\\" in name or name in (".", ".."):
        p.error("Project name must be a nonempty folder-safe name")
    target = args.output.expanduser().resolve() / name
    if target.exists():
        p.error(f"Destination already exists: {target}. Refusing to overwrite.")
    target.mkdir(parents=True)
    for rel in FILES:
        src = ROOT / rel
        dst = target / rel
        dst.parent.mkdir(parents=True, exist_ok=True)
        content = src.read_text(encoding="utf-8")
        content = content.replace("{{PROJECT_NAME}}", name).replace("{{IDEA}}", args.idea)
        dst.write_text(content, encoding="utf-8")
    print(f"Created {target}")
    print("Next: open with Codex/Claude and say 'Start a project'. Approve scope and architecture before coding.")

if __name__ == "__main__":
    main()
