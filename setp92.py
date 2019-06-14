a=int(input())
co=0
dec=0
while a!=0:
  b=a%10
  c=b*(2**co)
  co+=1
  dec+=c
  a=a//10
print(dec)
