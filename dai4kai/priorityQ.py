# ライブラリのインポート
#import re #正規表現
#import sys
import heapq
#import collections


def main():
    tempheap = []
    while(1):
        instr = input()
        if instr[2] == 'd': break
        if instr[0] == 'i': heapq.heappush(tempheap, -int(instr[7:]))
        else: 
            print(-heapq.heappop(tempheap))

    


    
if __name__ == '__main__':
    main()
