# ライブラリのインポート
#import re #正規表現
import sys
#import heapq
#import collections
#import math

def main():
    n, w = map(int, input().split())
    goods = [(0,0)]*n
    for i, inp in enumerate(sys.stdin):
        v, wtmp = map(int, inp.strip("\n").split())
        goods[i] = (v,wtmp)
    dp = [[0 for i in range(w+1)] for j in range(n)]
    for i in range(n):
        for c in range(w+1):
            if i < 0 or c <= 0: dp[0][0] = 0
            elif c - goods[i][1] < 0: dp[i][c] = dp[i-1][c]
            else: dp[i][c] = max(goods[i][0] + dp[i-1][c-goods[i][1]], dp[i-1][c])
    print(dp[n-1][w])



    
if __name__ == '__main__':
    main()
