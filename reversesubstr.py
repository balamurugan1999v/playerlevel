a,b=input().split()
a1=a[::-1]
b1=b[::-1]
co=0
for i in range(len(b1)):
  if a1[i]==b1[i]:
    co+=1
  else:
    break
if len(b1)==co:
  print("yes")
else:
  print("no")
