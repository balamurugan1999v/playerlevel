a,c=input().split()
b=len(a)
o=0
for i in range(0,b,1):
  if a[i]!=c[i]:
    o=o+1
if o==1:
  print("yes")
else:
  print("no")
