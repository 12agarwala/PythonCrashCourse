usernames = ['admin', 'BigNoseMan444', '420_HBirthday', 'SnotFace42069', 'FartFace222']
while True:
    username = input("Please enter your username to login: ")
    if username == 'admin':
        print("Hello admin, would you like to see a status report?")
    elif username in usernames:
        print("Hello", username, ", thank you for logging in again.")
    else:
        print("Sorry, you are not a valid user.")
    again = input("Do you want to login again? ")
    if again == 'No':
        break
