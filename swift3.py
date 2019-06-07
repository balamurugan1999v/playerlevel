a=input()
for i in a:
  o=ord(i)
  if (o>=65 and o<88) or (o>=97 and o<120):
    o=o+3
    print(chr(o),end="")
  else:
    o=o-23
    print(chr(o),end="")
