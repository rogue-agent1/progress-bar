#!/usr/bin/env python3
"""Progress bar — customizable terminal progress indicators."""
import sys, time
def bar(current, total, width=40, prefix="", suffix=""):
    pct = current / total if total else 0
    filled = int(width * pct)
    b = "█" * filled + "░" * (width - filled)
    print(f"\r{prefix} |{b}| {pct:.0%} {suffix}", end="", flush=True)
def spinner(duration=5, msg="Loading"):
    chars = "⠋⠙⠹⠸⠼⠴⠦⠧⠇⠏"
    for i in range(duration * 10):
        print(f"\r{chars[i % len(chars)]} {msg}...", end="", flush=True)
        time.sleep(0.1)
    print(f"\r✅ {msg} done!   ")
if __name__ == "__main__":
    mode = sys.argv[1] if len(sys.argv) > 1 else "bar"
    if mode == "bar":
        for i in range(101):
            bar(i, 100, prefix="Progress", suffix=f"{i}/100")
            time.sleep(0.03)
        print()
    elif mode == "spinner":
        spinner()
