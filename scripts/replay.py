"""Replay the corroborating computations for the ultra-log-concavity theorem.

Usage: python3 scripts/replay.py
Runs the exact log-concavity check (n <= 90, l <= 11), the intermediate-claims check
(paths, n <= 18, l <= 3) and the positive control, and compares with verification/logs/.
The theorem is proved analytically; none of this is load-bearing.
"""
import subprocess, sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "verification" / "src"; LOGS = ROOT / "verification" / "logs"
for name in ["exact_logconcavity", "intermediate_claims", "positive_control"]:
    out = subprocess.run([sys.executable, "-I", str(SRC / f"{name}.py")], capture_output=True, text=True, check=True).stdout.strip()
    print(f"[{name}]\n{out}")
    if out != (LOGS / f"{name}.log").read_text().strip(): sys.exit(f"FAIL: {name} output differs from its log")
print("OK: all outputs match verification/logs/")
