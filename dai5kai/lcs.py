# ライブラリのインポート
#import re #正規表現
import sys
#import heapq
#import collections
#import math

def main():
    q = int(input())
    STR = [str.strip("\n") for str in sys.stdin]
    for i in range(q):
        x = STR[2*i]
        y = STR[2*i+1]
        print(lcs(x,y))


def lcs(x, y):
    dp = []
    for y_k in y:
        ps = 0
        for i, pdp in enumerate(dp):
            p = x.find(y_k, ps) + 1 #.find method returns -1 if there is no element
            if not p: break
            dp[i] = min(p,pdp)
            ps = pdp
        else: #else block is executed when for block has done completedly
            p = x.find(y_k, ps) + 1
            if p: dp.append(p)
    return len(dp)


if __name__ == '__main__':
    main()
