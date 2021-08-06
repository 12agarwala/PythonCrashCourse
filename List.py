pizza = ["cheese", "veggie", "chicken", "pepperoni"]
customer = input("Which pizza do you want: ")
if customer.lower() in pizza:
    print("Your order has been placed")
else:
    print("Sorry, we do not have that pizza in our menu")