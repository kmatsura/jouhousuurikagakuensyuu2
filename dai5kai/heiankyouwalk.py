# ライブラリのインポート
#import re #正規表現
#import sys
#import heapq
#import collections
#import math

def main():
    n = int(input())
    for x in range(n):
        gx ,gy = map(int,input().split())
        p = int(input())
        Y = [[0 for i in range(gy+1)] for j in range(gx+1)]
        for i in range(gx+1):
            Y[i][0] += 1
        for i in range(gy+1):
            Y[0][i] += 2
        for i in range(p):
            a, b, c, d = map(int,input().split())
            if a == c:
                if b > d: Y[a][b] += 1
                else: Y[c][d] += 1
            else:
                if a > c: Y[a][b] += 2
                else: Y[c][d] += 2
        Z = [[0 for i in range(gy+1)] for j in range(gx+1)]
        for i in range(gx+1):
            for j in range(gy+1):
                s = Y[i][j]
                if (i,j) == (0,0):  Z[0][0] = 1
                elif s == 3: Z[i][j] = 0
                elif s == 2: Z[i][j] = Z[i][j-1]
                elif s == 1: Z[i][j] = Z[i-1][j]
                else: Z[i][j] = Z[i-1][j] + Z[i][j-1]
        print(Z[gx][gy]) if Z[gx][gy]>0 else print("Miserable Hokusai!")



if __name__ == '__main__':
    main()
