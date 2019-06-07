s1=[]
a=int(input())
b=0
for i in range(2,a+1):
  if(a%i)==0:
    s1.append(i)
for i in s1:
  if (i%2)==0:
    print(i,end=" ")
