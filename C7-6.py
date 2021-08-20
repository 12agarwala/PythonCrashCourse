i = 1
while i == 1:
    toppings = input("Please enter the toppings for your pizza: ")
    if toppings == 'quit':
        i = 6
    else:
        print("I will add", toppings, "to the list")
        print("If your are done, type quit")
#or
toppings = 1
while toppings != 'quit':
    toppings = input("Please enter the toppings for your pizza: ")
    print("I will add", toppings, "to the list. Or else type quit")
