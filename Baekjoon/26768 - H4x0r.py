#B4_26768_H4x0r

d={"a":4, "e":3, "i":1, "o":0, "s":5}
a=list(input())
for i in range(len(a)):
  if a[i] in d:
    a[i]=str(d[a[i]])
print("".join(a))
