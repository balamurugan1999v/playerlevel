a,b=input().split()
c=int(a)
d=int(b)
if c<d:
  t=c
  c=d
  d=t
y=(c*d)+1
for i in range(c,y,1):
  if (i%c)==0 and (i%d)==0:
    print (i)
    break
