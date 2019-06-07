a=int(input())
b=0
if (a%2)==0:
  i=a-2
  b=b+2
else:
  i=a-1
  b=b+1
while(i!=0):
  b=b+1
  i=i-2
print(b)
