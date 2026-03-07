# Planet Weight Calculated

ew = float(input(" Enter Your weight is :"))



pn = int(input("Enter your planet number : "))

if pn == 1:
  dw = ew * 0.38
  print( dw)
elif pn ==2 :
  dw = ew * 0.91
  print(dw)
elif pn == 3:
  dw = ew * 0.38
  print( )
elif pn == 4:
  dw = ew * 2.53
  print( dw )
elif pn ==5 :
  dw = ew *1.07 
  print(dw )
elif pn == 6:
  dw = ew * 0.89
  print(dw)
elif pn ==7 :
  dw = ew * 1.14
  print( dw)
else:
  print("Invalid planet number")
