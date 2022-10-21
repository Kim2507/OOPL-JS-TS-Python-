# A very simple dictionary

alien_0 = {"color": "green", "points": 5}
print(alien_0["color"])
print(alien_0["points"])

# Adding new key/value pairs

alien_0 = {"color": "green", "points": 5}
alien_0["x_position"] = 0
alien_0["y_position"] = 0
print(alien_0)

# Illustrates how to update key/value pairs

alien_0 = {"x_position": 0, "y_position": 25, "speed": "medium"}
print(f"Original position: {alien_0['x_position']}")

alien_0["x_position"] = alien_0["x_position"] + 5
print(f"New position: {alien_0['x_position']}")

# Illustrates how to iterate all items in a dict

user_0 = {
    "username": "efermi",
    "first": "enrico",
    "last": "fermi",
}

for key, value in user_0.items():
    print(f"Key: {key}, Value {value}")

# Note that you can also use user_0.keys()
# or user_0.values()

# You can store lists inside of dicts!

# Store information about a pizza being ordered.
toppings = ["mushrooms", "extra cheese"]
pizza = {
    "crust": "thick",
    "toppings": toppings,
}

# Summarize the order.
print(f"You ordered a {pizza['crust']}-crust pizza "
    "with the following toppings:")

for topping in pizza["toppings"]:
    print("- " + topping)


# You can even store dicts inside of other dicts!

einstein = {
    "first": "albert",
    "last": "einstein",
    "location": "princeton",
}

mcurie = {
    "first": "marie",
    "last": "curie",
    "location": "paris",
}

users = {
    "aeinstein": einstein,
    "mcurie": mcurie
}

for username, user_info in users.items():
    full_name = f"{user_info['first']} {user_info['last']}"
    print(f"Full name: {full_name.title()}")

# Let's see what happens when we try keys that don't exist
alien_0 = {"color": "green", "points": 5}

print(alien_0["colour"])


# Let's see what happens when we try keys that don't exist
alien_0 = {"color": "green", "points": 5}

# Here we use get instead
color = alien_0.get("colour")
print (color)

# Here we use get with a default value
color = alien_0.get("colour", "blue")
print (color)
