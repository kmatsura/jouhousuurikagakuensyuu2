# ライブラリのインポート
#import re #正規表現
#import sys
#import heapq
import collections


def main():
    n, q = map(int, input().split())
    deq = collections.deque()
    for i in range(n):
        name, time = input().split()
        deq.append((int(time),name))
    ans = []
    elps = 0
    while deq:
        time, name = deq.popleft()
        if time <= q:
            elps += time
            ans.append((name, elps))
        else:
            elps += q
            deq.append((time-q, name))
    [print(*i) for i in ans]
    


    
if __name__ == '__main__':
    main()
