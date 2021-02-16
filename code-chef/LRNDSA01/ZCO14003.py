n=int(input().strip())
# ll=list(map(int,input().strip().split()))[:n]
l=[]
for i in range(n):
    elem=input().strip()
    l.append(int(elem))
l.sort()
lm=[]
length=len(l)
for i in range(length):
    lm.append(l[i]*(length-i))
print(max(lm))

