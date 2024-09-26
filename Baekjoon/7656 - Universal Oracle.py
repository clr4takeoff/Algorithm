#S5_7656_Universal Oracle

a=input().split("What")

for i in a:
  if "?" in i:
    idx=0
    print("Forty-two",end="")

    while True:
      letter=i[idx]
      if letter=="?":
        print(".")
        break
      else:
        print(letter,end="")
      
      idx+=1
