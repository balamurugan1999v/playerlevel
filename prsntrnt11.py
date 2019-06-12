a1,b1=input().split()
co=0
for i in a1:
  for j in b1:
    if i==j:
      co=1
      break
if co==1:
  print("yes")
else:
  print("no")
