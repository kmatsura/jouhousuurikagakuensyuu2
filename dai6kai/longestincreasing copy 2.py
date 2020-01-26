# -*- coding: utf-8 -*-
"""
aaa
"""
#import re #正規表現
import sys
#import heapq
#import collections
#import math

def main():
    length = int(input())
    X = [0] * length
    for i, line in enumerate(sys.stdin): 
        X[i] = int(line)
    print(LIS(X))

def LIS(X):
    res = 0
    N = len(X)
    dp = [1] * N
    for i in range(N):
        for j in range(i):
            if i == 0: dp[0] = 1
            elif X[i] > X[j]: dp[i] = max(dp[i], dp[j]+1)
        res = max(res, dp[i])
    return res  

    
if __name__ == '__main__':
    main()
