import math

seatsRemaining = [480, 480, 480, 480, 480, 480, 480, 640]
maxSeats = [480, 480, 480, 480, 480, 480, 480, 640]
moneyEarned = [0, 0, 0, 0, 0, 0, 0, 0]
userPurchaseTickets = 0
ticketLeaveTime = 0
ticketReturnTime = 0
currentNumber = 0
mostPassengersTrain = ''
mostPassengers = 0
totalUserMoney = 0
saveData = []
discountedPeople = 0


def fetchTakenSeats(variable):
    return maxSeats[variable] - seatsRemaining[variable]


def updateTrain():
    global mostPassengersTrain
    global currentNumber
    global mostPassengers
    currentTimes = []
    for i in range(8):
        if (mostPassengers == (seatsRemaining[i] - maxSeats[i]) * -1) and (seatsRemaining[i] != maxSeats[i]):
            currentNumber = fetchTakenSeats(i)
            currentTimes.append(str(i + 9))
            mostPassengersTrain = ':00 & '.join(currentTimes)
        elif (fetchTakenSeats(i)) > currentNumber:
            currentNumber = fetchTakenSeats(i)
            mostPassengers += fetchTakenSeats(i)
            mostPassengersTrain = i + 9


def getSeatsRemaining(time):
    return seatsRemaining[time - 9]


def seatsDigitChecker(variable):
    if variable == 0:
        return '      '
    elif variable < 10:
        return '     '
    elif variable < 100:
        return '    '
    elif variable < 1000:
        return '   '
    elif variable < 10000:
        return '  '


def moneyDigitChecker(variable):
    if variable < 10:
        return '    '
    elif variable < 100:
        return '   '
    elif variable < 1000:
        return '  '
    elif variable < 10000:
        return ' '


# Data table updates everytime a change is made
def printTable():
    updateTrain()
    print(f"")
# Leave timings - going up the mountain
    print('-------------------------------------------')
    print(f"| Leave  | 09:00  | 11:00 | 13:00 | 15:00 |")
# Total seats for leave timings.
# The user can purchase 1-80 tickets at a time which will be deducted from the total number of tickets.
    print(
        f"| Seats  | {seatsRemaining[0]}{seatsDigitChecker(seatsRemaining[0])} | {seatsRemaining[2]}{seatsDigitChecker(seatsRemaining[2])}| {seatsRemaining[4]}{seatsDigitChecker(seatsRemaining[4])}| {seatsRemaining[6]}{seatsDigitChecker(seatsRemaining[6])}|")
    print(
        f"| Money  | ${moneyEarned[0]}{moneyDigitChecker(moneyEarned[0])} | ${moneyEarned[2]}{moneyDigitChecker(moneyEarned[2])}| ${moneyEarned[4]}{moneyDigitChecker(moneyEarned[4])}| ${moneyEarned[6]}{moneyDigitChecker(moneyEarned[6])}|")
# Total seats for return timings.
# The user can purchase 1-80 tickets at a time which will be deducted from the total number of tickets.
# When user says 4 tickets, it will be 8 (leave and return timings).
    print('-------------------------------------------')
    print(f"| Return | 10:00  | 12:00 | 14:00 | 16:00 |")
    print(
        f"| Seats  | {seatsRemaining[1]}{seatsDigitChecker(seatsRemaining[1])} | {seatsRemaining[3]}{seatsDigitChecker(seatsRemaining[3])}| {seatsRemaining[5]}{seatsDigitChecker(seatsRemaining[5])}| {seatsRemaining[7]}{seatsDigitChecker(seatsRemaining[7])}|")
# Total number of passengers and total amount of money calculated.
    print(
        f"| Money  | ${moneyEarned[1]}{moneyDigitChecker(moneyEarned[1])} | ${moneyEarned[3]}{moneyDigitChecker(moneyEarned[3])}| ${moneyEarned[5]}{moneyDigitChecker(moneyEarned[5])}| ${moneyEarned[7]}{moneyDigitChecker(moneyEarned[7])}|")
    print('-------------------------------------------')

    print(f"             | Total")
    print(f"| Money      | ${sum(moneyEarned)}{moneyDigitChecker(sum(moneyEarned))} ")
    print(
        f"| Passengers | {(sum(seatsRemaining) * -1) + 4000}{seatsDigitChecker((sum(seatsRemaining) * -1) + 4000)}")
    print('-------------------------------------------')
# Train with most passengers will be displayed on the data table
    print(f"| Most Passengers")
    print(f"| Train: {mostPassengersTrain}:00")
    print(f"| Passengers: {mostPassengers}")
    print('-------------------------------------------')
# Total money spent and train ticket timings displayed
    print(f"Your Total | ${totalUserMoney}{moneyDigitChecker(totalUserMoney)}|")
    print(f"Your Buses | {':00 & '.join(set(saveData))}:00 |")
    print('-------------------------------------------')
    print(f"")


def updateMoneyTaken(schedule, groupAmount):
    global discountedPeople
    global totalUserMoney
    global moneyEarned
    moneyEarned[schedule - 9] = groupAmount * 25
    discountedPeople = math.floor(groupAmount / 10)
    moneyEarned[schedule - 9] -= discountedPeople * 25
    totalUserMoney += moneyEarned[schedule - 9]


def tryFunction(inputText, returnText):
    while True:
        try:
            variable = int(input(inputText))
        except ValueError:
            print(returnText)
            continue
        else:
            break
    return variable


def purchaseTickets():
    global seatsRemaining
    global userPurchaseTickets
    global ticketLeaveTime
    global ticketReturnTime
# Here is where the actual code starts. User is asked how many tickets they want (any amount from 1-80).
# If more than 80 is entered, user will keep being asked to enter the correct amount - 1-80 until they do.
    printTable()
    while (userPurchaseTickets < 1) or (userPurchaseTickets > 80):
        userPurchaseTickets = tryFunction("How many tickets do you want to purchase? ", "Please enter a number from 1-80. ")
# Only ticket timings which are available, can be purchased from. User will choose from data table.
# If other number is entered, user will be asked to enter correct timing till they do.
    printTable()
    while True:
        ticketLeaveTime = tryFunction("What time would you like to leave? ", "Please enter a number.")
        if (ticketLeaveTime == 9) or (ticketLeaveTime == 11) or (ticketLeaveTime == 13) or (ticketLeaveTime == 15):
            break
# Data table is updated here depending on user choices.
# Total number of tickets will be reduced and cost fo ticket will be displayed.
    seatsRemaining[ticketLeaveTime - 9] -= userPurchaseTickets
    updateMoneyTaken(ticketLeaveTime, userPurchaseTickets)
    saveData.append(str(ticketLeaveTime))
    printTable()
    while True:
        ticketReturnTime = tryFunction("What time would you like to return? ", "Please enter a number.")
        if (ticketReturnTime == 10) or (ticketReturnTime == 12) or (ticketReturnTime == 14) or (ticketReturnTime == 16):
            break
    seatsRemaining[ticketReturnTime - 9] -= userPurchaseTickets
    updateMoneyTaken(ticketReturnTime, userPurchaseTickets)
    saveData.append(str(ticketReturnTime))
    printTable()


# Once user has gone through whole process, the user will be asked whether or not they want to purchase more tickets.
# If yes, user will be asked again how many ticket they would like to purchase.
# If no, user will be asked if they would like to exit.
# If yes, program will end. If no, cycle will repeat again.
purchaseTickets()
while True:
    userPurchaseTickets = 99
    while True:
        userRePurchase = input("Would you like to purchase more tickets? ('yes' / 'no') ")
        if (userRePurchase == 'yes') or (userRePurchase == 'no'):
            break
    if userRePurchase == 'no':
        while True:
            userExit = input("Would you like to exit? ('yes' / 'no') ")
            if (userExit == 'yes') or (userExit == 'no'):
                break
        if userExit == 'yes':
            print("Thank you for using this Service. ")
            printTable()
            exit()
        elif userExit == 'no':
            print("Please allow the next user to purchase tickets.")
            saveData = []
            totalUserMoney = 0
            purchaseTickets()
    elif userRePurchase == 'yes':
        purchaseTickets()

