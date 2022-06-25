import sys
sys.stdin = open('sample_input.txt','r')

t = int(input())
for tc in range(1,t+1):
    price = list(map(int,input().split()))
    plan = list(map(int,input().split()))
    dp = [0]*13
    n = len(price)
    for i in range(n-1,-1,-1):
        if i + 
    print(f'#{tc} {dp}')