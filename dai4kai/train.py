# ライブラリのインポート
#import re #正規表現
import sys
#import heapq
#import collections
#import math

def main():
    for x in sys.stdin:
        x = x.strip("\n")
        ans = set()
        try:
            int(x)
            continue
        except:
            for i in range(1,len(x)):
                f, e = x[:i], x[i:]
                fr = f[::-1]
                er = e[::-1]
                ans = ans.union(set([x, f+er, fr+e, fr+er, e+f,er+f, e+fr, er+fr]))
            print(len(ans))


if __name__ == '__main__':
    main()
