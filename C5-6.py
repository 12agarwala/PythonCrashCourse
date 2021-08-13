person = int(input("Please enter your age only in whole numbers. For example, 11, not 11 years and 4 four months. : "))
if person < 2:
    print("You are a baby")
elif person >= 2:
    print("You are a toddler")
elif person >= 4:
    print("You are a kid")
elif person >= 13:
    print("You are a teenager")
elif person >= 20:
    print("You are an adult")
elif person < 65:
    print("You are an adult")
else:
    print("You are an elder")
