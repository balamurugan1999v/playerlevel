a,b1=input().split()
b=int(a)
c=int(b1)
ans=input().split()
s1=[]
r=0
for i in ans:
  if(r<b):
    s1.append(int(i))
    r=r+1
if c in s1:
  print("Yes")
else:
  print("No")
