print("We have run out of Pastrami")
sandwich_orders = ["Cheese", "Pastrami", "Vegetable", "Pastrami", "Nutella", "Peanut Butter", "Pastrami", "PBJ",  "Pastrami","Grilled Cheese"]
finished_sandwiches = []
i = sandwich_orders.count("Pastrami")
while i > 0:
    sandwich_orders.remove("Pastrami")
    i = i-1
for sandwich_order in sandwich_orders:
    print("I made your", sandwich_order, "sandwich")
    finished_sandwiches.append(sandwich_order)
print("I have finished making all your sandwiches", finished_sandwiches)


