s1=[]
m=int(input())
a=input().split()
for i in a:
  s1.append(i)
s1.sort()
s1.sort(key=len)
for i in s1:
  print (i,end=" ")
