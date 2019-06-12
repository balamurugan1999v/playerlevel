a1,b1=input().split()
a=int(a1)
b=int(b1)
num=input().split()
r=0
s1=[]
for i in num:
  if r<a:
    s1.append(int(i))
    r=r+1
s1.sort()
print(s1[b-1])
