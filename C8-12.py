def sandwich_toppings (type, size, *toppings):
    print("Your sandwich type is", type, "the bread size is", size, "and the following toppings")
    print(toppings)
#main program start here
bread_type = input("Please enter what type of bread you want for your sandwich: ")
bread_size = input("Please enter your prefered bread size: ")
toppings = []
while True:
    top = input("Please enter sandwich toppings (enter done if finished): ")
    if top.lower() != 'done':
        toppings.append (top)
    else:
        break
sandwich_toppings(bread_type, bread_size, toppings)
