a=int(input())
d=0
while(a!=0):
    b=a%10
    c=b*b
    d=c+d
    a=a//10
print (d)
