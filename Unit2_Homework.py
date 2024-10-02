'''
Name: Kaden Meir
Date: 9/26/24
Description: Unit 2 Homework 1
'''

print('Problem 1'.center(20,'-'))
print("My first idea is where you are a student making choices on what you want to do. You will go through a full week of school aand see where things end up. ")

print("For my second idea I was thinking of making it so you were the president of what ever place you choose. You will make decide on what to do for them.") 

print("For my final idea I was thinking of have a horror based game where you are stuck in space with a monster and your decision will cause you to live, die, or thrive in space.")

title = r"""
 _____ _            _____ _             _            _     _     _  __     
|_   _| |          /  ___| |           | |          | |   | |   (_)/ _|    
  | | | |__   ___  \ `--.| |_ _   _  __| | ___ _ __ | |_  | |    _| |_ ___ 
  | | | '_ \ / _ \  `--. | __| | | |/ _` |/ _ | '_ \| __| | |   | |  _/ _ \
  | | | | | |  __/ /\__/ | |_| |_| | (_| |  __| | | | |_  | |___| | ||  __/
  \_/ |_| |_|\___| \____/ \__|\__,_|\__,_|\___|_| |_|\__| \_____|_|_| \___|
                                                                           
                                                                        
"""
print(title)

portland_seatle = input("") 
car_gas = input("how many miles per gallon does you car gets, whole numbers please: ")
cost_gas = input("how much a gallon of gas is near your house, don't need whole numbers: ")
car_hold = input("how many gallons of gas does your car holds: ")
total_cost = portland_seatle*cost_gas/car_gas
print(f"The total cost of your trip will be: {total_cost}")