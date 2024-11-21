
def main():
 while True:
  tip_percentage = 15
  meal = int(input("Enter the meal cost: "))
  tip = int(input("Enter the tip percentage:"))
  total_cost = meal*(tip/100)+meal
 

  if tip < 0 :
   total_cost = meal*(tip_percentage/100)+meal
   print(f"The total cost of the meal is: {total_cost}")
   break
  elif tip > 0: 
   print(f"The total cost of the meal is: {total_cost}")
   break
  elif tip == ValueError:
    #Can't figure this part out
    #keeps giving me value errors and I try to fix it but doesn't work
   print(" Invalid input. Please enter numeric values for meal cost and tip percentage.")
   continue

main()