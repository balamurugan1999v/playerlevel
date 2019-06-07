a,b1=input().split()
b=int(a)
c=int(b1)
n=0
u=0
while n<=b:
  n=c**u
  u=u+1
  if n==b:
    print("yes")
    break
if n!=b:
  print("no")
