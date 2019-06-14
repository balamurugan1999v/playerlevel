a=input()
s1=[]
co=0
for i in a:
  s1.append(i)
b=len(s1)
for i in range(b-1):
  co=0
  for j in range(b):
    if i!=j:
      if s1[i]==s1[j]:
        co=1
        break
  if co==1:
    break
if co==1:
  print('yes')
else:
  print("no")
