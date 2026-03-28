#!/usr/bin/env python3
"""Progress bar — terminal progress display with ETA."""
import sys, time
class Progress:
    def __init__(self, total, width=40, label=""):
        self.total=total; self.width=width; self.label=label; self.start=time.time(); self.current=0
    def update(self, n=1):
        self.current+=n; pct=self.current/self.total; filled=int(pct*self.width)
        bar="█"*filled+"░"*(self.width-filled)
        elapsed=time.time()-self.start; eta=(elapsed/self.current*(self.total-self.current)) if self.current else 0
        print(f"\r  {self.label}[{bar}] {pct*100:.0f}% ({self.current}/{self.total}) ETA:{eta:.0f}s",end="",flush=True)
        if self.current>=self.total: print()
def cli():
    n=int(sys.argv[1]) if len(sys.argv)>1 else 50
    p=Progress(n, label="Working ")
    for _ in range(n): time.sleep(0.05); p.update()
    print("  Done!")
if __name__=="__main__": cli()
