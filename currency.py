#CodedexCurrency
CO = int(input('What do you have left in pesos? '))
PE = int(input('What do you have left in soles? '))
BR = int (input('What do you have left in reais? '))
uCO =  CO * 0.00026
uPE = PE * 0.29
uBR = BR * 0.19
USD = uCO + uPE + uBR
print (USD)
