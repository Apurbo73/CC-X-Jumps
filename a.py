import math
n = int(input())
for _ in range (n):
    a,b= map(int,input().split())
    if b>a:
        print (a)
    else:
    
        if a%b==0:
            print (int(a/b))
        else:
            d=a%b
            print (int(a/b)+int(d/1))