s1=[]
n=int(input())
sets=input().split()
for i in sets:
  s1.append(i)
for i in range(0,n-1,1):
  b=0
  for j in range(0,n,1):
    if i!=j:
      if s1[i]==s1[j]:
        b=b+1
  if b==0:
      print (s1[i])
      break
