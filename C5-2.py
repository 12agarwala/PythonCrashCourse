password = "A1234d%"
while True:
    guess = input("Write password for log-in: ")
    if guess == password.lower() or guess == password.upper():
        print("Correct password")
        break
    else:
        print("Incorrect password, please try again: ")
