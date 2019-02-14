a=input()
b=input()
c=0
temp=0
y=len(a)
for i in range(0,y-1,1):
    if a[i]==a[i+1] and b[i]==b[i+1]:
        c=c+1
    elif a[i]!=a[i+1] and b[i]!=b[i+1]:
        c=c+1
    elif (a[i]!=a[i+1] and b[i]==b[i+1]) or (a[i]==a[i+1] and b[i]!=b[i+1]):
        temp=1
if temp==1:
          print("no")
else:
          print("yes")
