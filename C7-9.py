print("We have run out of pastrami")
sandwich_orders = ["Cheese", "Pastrami", "Vegetable", "Pastrami", "Nutella", "Peanut Butter", "Pastrami", "PBJ",  "Pastrami","Grilled Cheese"]
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
for sandwich_order in sandwich_orders:
        print("I made your", sandwich_order, "sandwich")
finished_sandwiches = []

