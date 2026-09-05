#!/usr/bin/env python3
"""Bootstrap the project environment for research and ESP32 deployment."""

from __future__ import annotations

import os
import subprocess
import sys
import venv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VENV_DIR = ROOT / ".venv"
REQ_FILE = ROOT / "requirements.txt"


def python_bin() -> Path:
    if os.name == "nt":
        return VENV_DIR / "Scripts" / "python.exe"
    return VENV_DIR / "bin" / "python"


def ensure_virtualenv() -> Path:
    if not VENV_DIR.exists():
        print(f"[setup] Creating virtual environment at {VENV_DIR}")
        venv.EnvBuilder(with_pip=True).create(VENV_DIR)

    exe = python_bin()
    if not exe.exists():
        raise FileNotFoundError(f"Virtual environment is missing the Python interpreter: {exe}")
    return exe


def ensure_project_structure() -> None:
    folders = [
        ROOT / "data" / "raw",
        ROOT / "data" / "processed" / "train",
        ROOT / "data" / "processed" / "val",
        ROOT / "data" / "processed" / "test",
        ROOT / "experiments" / "configs",
        ROOT / "experiments" / "logs",
        ROOT / "experiments" / "plots",
        ROOT / "experiments" / "results",
        ROOT / "models" / "fp32",
        ROOT / "models" / "int8",
        ROOT / "models" / "optimized",
        ROOT / "models" / "pruned",
        ROOT / "training" / "models",
    ]

    for folder in folders:
        folder.mkdir(parents=True, exist_ok=True)


def run_command(command: list[str], description: str) -> None:
    print(f"\n[setup] {description}")
    completed = subprocess.run(command, cwd=str(ROOT), text=True)
    if completed.returncode != 0:
        raise subprocess.CalledProcessError(completed.returncode, command)


def install_dependencies(python_exe: Path) -> None:
    if not REQ_FILE.exists():
        raise FileNotFoundError(f"Requirements file not found: {REQ_FILE}")

    run_command([str(python_exe), "-m", "pip", "install", "--upgrade", "pip"], "Upgrading pip")
    run_command([str(python_exe), "-m", "pip", "install", "-r", str(REQ_FILE)], "Installing project dependencies")


def validate_setup(python_exe: Path) -> None:
    run_command([str(python_exe), "-m", "pytest", "-q"], "Running project validation tests")


def main() -> int:
    try:
        ensure_project_structure()
        python_exe = ensure_virtualenv()
        install_dependencies(python_exe)
        validate_setup(python_exe)
    except Exception as exc:  # pragma: no cover - CLI safety net
        print(f"\n[setup] Setup failed: {exc}", file=sys.stderr)
        return 1

    print("\n[setup] Environment ready.")
    print(f"Python executable: {python_exe}")
    print("Next: activate the venv and run scripts/training commands from the project root.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
