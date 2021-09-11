def make_shirt(size, message):
    print("The shirt size is:", size, "and has a message on it saying:", message)

S = input("Please enter the size of your shirt (default size is large)")
M = input("Please enter the message you want on your shirt (default text is: 'I Love Python')")
if S == '':
    S = 'large'
if M == '':
    M = 'I Love Python'
make_shirt(message=M, size=S)
