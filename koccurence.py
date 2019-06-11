a1,b1=input().split()
a=int(a1)
b=int(b1)
co=0
while(a!=0):
  k=a%10
  a=a//10
  if k==b:
    co+=1
print(co)
