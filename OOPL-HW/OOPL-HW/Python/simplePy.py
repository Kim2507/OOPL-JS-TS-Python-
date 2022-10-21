# A simple Python List

fruits = ["orange", "apple", "banana"]
print(fruits)

# Accessing Elements in a List

fruits = ["orange", "apple", "banana"]
print(fruits[0])
print(fruits[1])
print(fruits[2])

# Let's try negative indexing!
print(fruits[-1])

# Modifying Elements in a List

fruits = ["orange", "apple", "banana"]
print(fruits)

# Let's change item 1
fruits[1] = "kiwi"
print(fruits)

# Appending Elements to a List

fruits = ["orange", "apple", "banana"]
print(fruits)

# Let's add a kiwi!
fruits.append("kiwi")
print(fruits)

# Removing Elements from a List

fruits = ["orange", "apple", "banana"]
print(fruits)

# Let's remove item 1
del fruits[1]
print(fruits)


# Popping Elements from a List

fruits = ["orange", "apple", "banana"]
print(fruits)

last_fruit = fruits.pop()
print(f"Yummy {last_fruit}!")
print(fruits)

# Removing Elements by Value

# Note that we now have two apples
fruits = ["orange", "apple", "banana", "apple"]
print(fruits)

# Let's remove "apple"
# Important to note:  this only removes the first apple
# if you want to remove both apples, call remove twice!
fruits.remove("apple")
print(fruits)

# Permanentaly Sorting a List

fruits = ["orange", "apple", "banana"]
print(fruits)

fruits.sort()
print(fruits)



# Permanently Reverse Sorting a List

fruits = ["orange", "apple", "banana"]
print(fruits)

fruits.sort(reverse=True)
print(fruits)

# Temporarily Sorting a List

fruits = ["orange", "apple", "banana"]
sorted_fruits = sorted(fruits)
print(fruits)
print(sorted_fruits)

# Find the Length of a List

fruits = ["orange", "apple", "banana"]
num_items = len(fruits)
print(num_items)

