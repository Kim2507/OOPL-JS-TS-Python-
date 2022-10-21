
book1 = {
	"author": "Chris John",
	"title": "See You Tomorrow",
	"price" : 25
}

book2={
	"author": "Mark Liam",
	"title" : "Son of God",
	"price" : 35
}

books = [book1,book2]
print(books) 
def calculate_total(books):
	sum=0;
	for book in books:
		sum +=book.get("price")
	return sum


def calculate_shipping():
	# free shipping if total price > 100
	total_price = calculate_total(books)
	if total_price > 100: return 0
	else : return 3.99




#def main():
decision = input("Do you want to check out?(yes or no): ")
print(decision)

if(decision=="no"):
	print("Come back soon!")
		
else:	
	total_cost= calculate_total(books)+calculate_shipping()
	print(f"Total number of books: {len(books)}")
	print(f"Final total price:{total_cost}")