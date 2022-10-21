foods = ["pizza", "noodle", "chichker burger","beaf steek", "pasta"]
print(foods)

# Print each item in food
for food in foods:
	print(food)

#Print different slices of foods
foods_sub1 = foods[:4]
foods_sub2 = foods[:-1]
print(foods_sub1)
print(foods_sub2)

#Permamently sort and print 
foods.sort()
print(foods)

#Temporarily Sort and Print 
sorted_foods = sorted(foods)
print(foods)
print(sorted_foods)

#List comprehen
foods_upper = [food.upper() for food in foods]
print(foods_upper)

