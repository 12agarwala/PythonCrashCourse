person = int(input("Please enter your age only in whole numbers. For example, 11, not 11 years and 4 four months. : "))
if person < 3:
    print("Your ticket is free")
elif person <13:
    print("Your ticket costs $10")
else:
    print("Your ticket costs $15")
