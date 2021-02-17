import math as m

t=int(input())
while(t>0):
    n=int(input())
    profits=[]
    while(n>0):
        s,p,v=map(int,input().split())
        if(p>s):
            profits.append((p//(s+1))*v)
        else:
            profits.append(0)
        n-=1
    print(max(profits))
    t-=1
