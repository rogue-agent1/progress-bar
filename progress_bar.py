#!/usr/bin/env python3
"""progress_bar - Progress bar utility."""
import sys,argparse,json,time
def bar(current,total,width=40,fill="█",empty="░"):
    pct=current/total if total else 0
    filled=int(width*pct)
    return f"|{fill*filled}{empty*(width-filled)}| {pct*100:.1f}% ({current}/{total})"
def main():
    p=argparse.ArgumentParser(description="Progress bar")
    p.add_argument("current",type=int);p.add_argument("total",type=int)
    p.add_argument("--width",type=int,default=40)
    p.add_argument("--animate",action="store_true")
    p.add_argument("--json",action="store_true")
    args=p.parse_args()
    if args.animate:
        for i in range(args.total+1):
            print(f"\r{bar(i,args.total,args.width)}",end="",flush=True)
            time.sleep(args.current/1000)
        print()
    elif args.json:
        print(json.dumps({"current":args.current,"total":args.total,"percentage":round(args.current/args.total*100,1),"bar":bar(args.current,args.total,args.width)}))
    else:
        print(bar(args.current,args.total,args.width))
if __name__=="__main__":main()
