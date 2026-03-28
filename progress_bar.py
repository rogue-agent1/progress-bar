#!/usr/bin/env python3
"""progress_bar - Pipe-friendly progress bar for CLI tasks."""
import sys, time, os

def bar(current, total, width=40, label=''):
    pct = current / total if total else 0
    filled = int(width * pct)
    b = '█' * filled + '░' * (width - filled)
    sys.stderr.write(f'\r{label}[{b}] {pct*100:5.1f}% ({current}/{total})')
    if current >= total: sys.stderr.write('\n')
    sys.stderr.flush()

def pipe_mode(total=None):
    count = 0
    for line in sys.stdin:
        count += 1
        sys.stdout.write(line)
        if total: bar(count, total)
        else: sys.stderr.write(f'\r  Processed: {count} lines'); sys.stderr.flush()
    if not total: sys.stderr.write('\n')

def demo():
    for i in range(101):
        bar(i, 100, label='Demo: ')
        time.sleep(0.03)

def main():
    args = sys.argv[1:]
    if '-h' in args or '--help' in args:
        print("Usage:\n  cat file | progress_bar.py [-n TOTAL]\n  progress_bar.py --demo"); return
    if '--demo' in args: demo(); return
    total = int(args[args.index('-n')+1]) if '-n' in args else None
    pipe_mode(total)

if __name__ == '__main__': main()
