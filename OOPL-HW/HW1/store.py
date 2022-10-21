foodRations ={"Name" : "Food Rations","Quantity":6}
waterFlask ={"Name" : "Water Flask", "Quantity":3}
dagger={"Name":"Dagger", "Quantity":12}
helmet={"Name":"Helmet","Quantity":32}
#list of items(includes food rations, water flask, dagger, helmet
items=[foodRations,waterFlask,dagger,helmet]
#display menu
def menu():
    i=0
    for item in items:
        print(f"{i}.{item['Name']}:{item['Quantity']} gold pieces.")
        i=i+1


# Total function-calculate total gold pieces that user has purchased
def total(list_items):
    total =0;
    for item in list_items:
        total +=item.get("Quantity")
    return total

#main
print("Welcome to the General Provisions Store!\n")
shopping_cart=[]
quit = False
while quit==False:
    print("What can I get you today?")
    menu()
    user_input = input("Enter 0-4 or q to end: ")
    if user_input=='0':
        shopping_cart.append(items[0])
        print(f"\nGot it.  You selected {items[0]['Name']}")
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
        print("Your enter is invalid.")

#Print all items in shopping cart
for each in shopping_cart:
    print(f"{each['Name']}:{each['Quantity']} gold pieces.")
#Total gold pieces that user has purchased
total_cost =total(shopping_cart)
print(f"Thanks.Today total is {total_cost} gold pieces")
