#!/usr/bin/env python3
"""Terminal progress bar library."""
import sys,time,shutil
class ProgressBar:
    def __init__(self,total,width=None,prefix="",suffix="",fill="█",empty="░"):
        self.total=total;self.width=width or min(40,shutil.get_terminal_size().columns-30)
        self.prefix=prefix;self.suffix=suffix;self.fill=fill;self.empty=empty
        self.current=0;self.start=time.time()
    def update(self,n=1):
        self.current=min(self.current+n,self.total)
        pct=self.current/self.total;filled=int(self.width*pct)
        bar=self.fill*filled+self.empty*(self.width-filled)
        elapsed=time.time()-self.start
        rate=self.current/elapsed if elapsed>0 else 0
        eta=(self.total-self.current)/rate if rate>0 else 0
        sys.stderr.write(f"\r{self.prefix} |{bar}| {pct:.0%} [{self.current}/{self.total}] {rate:.0f}/s ETA:{eta:.0f}s {self.suffix}")
        sys.stderr.flush()
        if self.current>=self.total: sys.stderr.write("\n")
    def __enter__(self): return self
    def __exit__(self,*a): pass
def main():
    print("Downloading files...")
    with ProgressBar(100,prefix="Progress") as pb:
        for i in range(100): time.sleep(0.02);pb.update()
    print("\nProcessing items...")
    with ProgressBar(50,width=30,fill="▓",empty="░") as pb:
        for i in range(50): time.sleep(0.03);pb.update()
if __name__=="__main__": main()
