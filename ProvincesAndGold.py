cardsInHand = input().split()
buyingPower = int(cardsInHand[0]) * 3
buyingPower += int(cardsInHand[1]) * 2
buyingPower += int(cardsInHand[2]) * 1

if(buyingPower >= 8):
    print("Province or Gold")
elif(buyingPower >= 6):
    print("Duchy or Gold")
elif(buyingPower == 5):
    print("Duchy or Silver")
elif(buyingPower >= 3):
    print("Estate or Silver")
elif(buyingPower == 2):
    print("Estate or Copper")
else:
    print("Copper")
