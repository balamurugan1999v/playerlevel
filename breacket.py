a=input()
b=0
c=0
for i in a:
  if i=='(':
    b=b+1
  if i==')':
    c=c+1
if c==b:
  print ("yes")
else:
  print("no")
