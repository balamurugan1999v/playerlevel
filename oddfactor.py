a=int(input())
j=a
for i in range(1,j+1):
  if (a%i)==0:
    if(i%2)!=0:
      print(i,end=" ")
