# ライブラリのインポート
import re #正規表現

def main():
    stack = []
    input_str = list(map(str,input().split()))
    for i in range(len(input_str)):
        ch = input_str[i]
        if ch == "+":
            stack[-2] = stack[-2] + stack[-1]
            stack.pop() 
        elif ch == "-":
            stack[-2] = stack[-2] - stack[-1]
            stack.pop() 
        elif ch == "*":
            stack[-2] = stack[-2] * stack[-1]
            stack.pop()
        
        else:
            stack.append(int(ch))
    print(stack[0])


    
if __name__ == '__main__':
    main()
