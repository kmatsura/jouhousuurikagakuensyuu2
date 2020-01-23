#if 0
所要時間は、25分位であった。input()の代わりにsys.stdinを使うと多少動作が早くなるらしい。あとは、printの中で条件分岐できるのがかっこいいと思った。

#endif

# ライブラリのインポート
#import re #正規表現
import sys
#import heapq
#import collections
#import math

def main():
    s = set()
    for inst in sys.stdin:
        if inst[0] == 'f': print('yes' if inst[5:] in s else 'no')
        else: s.add(inst[7:])
    

if __name__ == '__main__':
    main()
