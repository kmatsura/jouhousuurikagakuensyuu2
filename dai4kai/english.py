# ライブラリのインポート
#import re #正規表現
import sys
#import heapq
#import collections
#import math

def main():
    y = ""
    for x in sys.stdin: y += x
    a = list(y.strip("\n").split(" "))
    print(max(a, key=a.count), max(a, key=len))
    
if __name__ == '__main__':
    main()
