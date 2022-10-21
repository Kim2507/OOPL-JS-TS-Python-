foodRations ={"Name" : "Food Rations","Quantity":6}
waterFlask ={"Name" : "Water Flask", "Quantity":3}
dagger={"Name":"Dagger", "Quantity":12}
helmet={"Name":"Helmet","Quantity":32}

items=[foodRations,waterFlask,dagger,helmet]
def menu():
    i=0
    for item in items:
        #print(item["Name"],": ",item["Quantity"]," pieces.")
        print(f"{i}.{item['Name']}:{item['Quantity']} pieces.")
        i=i+1

"""def choice(user_choice):
    if user_choice =='0':
        print(f"Got it.  You selected {items[0]['Name']}")
    elif user_choice=='1':
        print(f"Got it.  You selected {items[1]['Name']}")
    elif user_choice=='2':
        print(f"Got it.  You selected {items[2]['Name']}")
    elif user_choice=='3':
        print(f"Got it.  You selected {items[3]['Name']}")
    else:
        print("Ok, here is your receipt.")"""
def total(list_items):
    total =0;
    for item in list_items:
        total +=item.get("Quantity")
    return total

print("Welcome to the General Provisions Store!\n")
shopping_cart=[]
quit = False
while quit==False:
    print("What can I get you today?")
    menu()
    user_input = input("Enter 0-4 or q to end: ")
    if user_input=='0':
        shopping_cart.append(items[0])
        print(f"Got it.  You selected {items[0]['Name']}")
    elif user_input=='1':
        shopping_cart.append(items[1])
        print(f"Got it.  You selected {items[1]['Name']}")
    elif user_input=='2':
        shopping_cart.append(items[2])
        print(f"Got it.  You selected {items[2]['Name']}")
    elif user_input=='3':
        shopping_cart.append(items[3])
        print(f"Got it.  You selected {items[3]['Name']}")
    elif user_input=='q':
        quit = True,
        print("Ok, here is your receipt.")
    else:
        print("Your entered invalid number.")


for each in shopping_cart:
    print(f"{each['Name']}:{each['Quantity']} pieces.")

total_cost =total(shopping_cart)
print(f"Today your total is {total_cost} pieces")












