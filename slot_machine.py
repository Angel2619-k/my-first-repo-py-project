#Slot Machine 
#Try your luck
import random
result = ['🍒','🍇', '🍉', '7️⃣']

fresult = [random.choice(result)for _ in range(3)]

print(" | ".join(fresult))

if fresult == ['7️⃣','7️⃣','7️⃣']:
  print("Jackpot! 💰")
elif fresult == ['🍒','🍒','🍒']:
  print("You won! , $5 ")
elif fresult == ['🍇','🍇','🍇']:
  print("You won! , $15 ")
elif fresult == ['🍉','🍉','🍉']:
  print("You won! , $50 ")
else :
  print( "Thanks for playing!")

