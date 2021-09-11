def make_shirt(size, message):
    print("The shirt is:", str(size), "and has a message on it saying:", str(message))

S = str(input("Please enter the size of your shirt (default size is large)"))
M = str(input("Please enter the message you want on your shirt (default text is: 'I Love Python')"))
if S == '':
    S = 'large'
if M == '':
    M = 'I Love Python'
make_shirt(message=M, size=S)
