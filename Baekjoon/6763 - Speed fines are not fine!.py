#B4_6763_Speed fines are not fine!

a=int(input())
b=int(input())

if a>=b:
  print("Congratulations, you are within the speed limit!")
else:
  if b-a<=20:
    fine=100
  elif b-a<=30:
    fine=270
  else:
    fine=500
  print(f"You are speeding and your fine is ${fine}.")
