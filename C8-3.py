def make_shirt(size, message):
    print("The shirt is", size, "and has a message on it saying", message)

S = int(input("Please enter the size of your shirt: "))
M = input("Please enter the message you want on your shirt: ")
make_shirt(message=M, size=S)
