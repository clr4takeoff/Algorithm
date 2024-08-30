#B5_30676_이 별은 무슨 색일까

lda=int(input())

if 620<=lda<=780:
  print("Red")
elif 590<=lda<620:
  print("Orange")
elif 570<=lda<590:
  print("Yellow")
elif 495<=lda<570:
  print("Green")
elif 450<=lda<495:
  print("Blue")
elif 425<=lda<450:
  print("Indigo")
else:
  print("Violet")
