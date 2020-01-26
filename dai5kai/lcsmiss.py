# ライブラリのインポート
import re #正規表現
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
        print(check(x,y)) if len(x) < len(y) else print(check(y, x))

def check(x, y):
    px = 0
    pxs = 0
    py = 0
    l_max = 0
    l = 0
    y_temp = y
    print(x,y)
    print("l;x[px],px,y_temp[py:]")
    while (1):
        if x[px] in y_temp:
            l += 1
            print(l, x[px],y_temp)
            l_max = max(l_max, l)
            py = re.search(x[px],y_temp).span()[1]
            y_temp = y_temp[py:] 
            px += 1
            if px == len(x):
                pxs += 1
                if pxs == len(x): break
                px = pxs
                py = 0
                l = 0
                y_temp = y
        else:
            print(l, x[px],y_temp)
            px += 1
            if pxs == len(x)-1: break
            if px == len(x):
                pxs += 1
                px = pxs
                py = 0
                l = 0
                y_temp = y
        
    return l_max

if __name__ == '__main__':
    main()
