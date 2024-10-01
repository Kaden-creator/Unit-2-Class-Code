'''
Name: Kaden Meir
Date:10/1/24
Description: Practice
'''
ingredient_1 = input("Name a ingredient that you want in your salad:")
ounces_1 = float(input(f"How many ounces of {ingredient_1} do you want?:"))

ingredient_2 = input("Name a ingredient that you want in your salad:")
ounces_2 = float(input(f"How many ounces of {ingredient_2} do you want?:"))

ingredient_3 = input("Name a ingredient that you want in your salad:")
ounces_3 = float(input(f"How many ounces of {ingredient_3} do you want?:"))

num_serving = int(input("What is the amount of servings you want?: "))

total_ingredient_1 = ounces_1*num_serving
total_ingredient_2 = ounces_2*num_serving
total_ingredient_3 = ounces_3*num_serving

print(f"Total ounces of {ingredient_1}: {total_ingredient_1:.2f}")
print(f"Total ounces of {ingredient_2}: {total_ingredient_2:.2f}")
print(f"Total ounces of {ingredient_3}: {total_ingredient_3:.2f}")