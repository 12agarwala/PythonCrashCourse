busA = []
busB = []
busC = []
busD = []
busE = []
busF = []

userInputBus = 'x'


def bus():
    global userInputBus
    while userInputBus.lower() != 'a' and userInputBus.lower() != 'b' and userInputBus.lower() != 'c' and userInputBus.lower() != 'd' and userInputBus.lower() != 'e' and userInputBus.lower() != 'f':
        print('Invalid input! Please enter the correct bus letter.')
        userInputBus = input("Please enter the correct bus letter (in lowercase letters): ")
    print("Valid input entered.")


bus()

storedValue = 0
lateValue = 0
lateValueCounter = 0
for i in range(5):
    try:
        inputBusValue = int(input(f"Please enter a number for bus {userInputBus.title()}: "))
    except ValueError:
        inputBusValue = int(input(f"Please enter a NUMBER for bus {userInputBus.title()}: "))
    if userInputBus == 'a':
        busA.append(inputBusValue)
    elif userInputBus == 'b':
        busB.append(inputBusValue)
    elif userInputBus == 'c':
        busC.append(inputBusValue)
    elif userInputBus == 'd':
        busD.append(inputBusValue)
    elif userInputBus == 'e':
        busE.append(inputBusValue)
    elif userInputBus == 'f':
        busF.append(inputBusValue)
    if inputBusValue < 0:
        lateValueCounter += 1
        lateValue += inputBusValue
print(busA)
# End of Task 1

forBusCounter = 0
busACount = 0
busBCount = 0
busCCount = 0
busDCount = 0
busECount = 0
busFCount = 0
for i in range(6):
    if i == 0:
        forBusCounter = busA
    elif i == 1:
        forBusCounter = busB
    elif i == 2:
        forBusCounter = busC
    elif i == 3:
        forBusCounter = busD
    elif i == 4:
        forBusCounter = busE
    elif i == 5:
        forBusCounter = busF
    else:
        print("Error in forBusCounter function")
    for n in forBusCounter:
        busACount = busACount + n

busAAverage = busACount / len(busA)
if lateValueCounter != 0:
    busALateAverage = lateValue / lateValueCounter
    print(f"Bus A late average is {round(busALateAverage)} minutes.")
print(f"Bus A average is {round(busAAverage)} minutes.")


def day():
    internalDay = input('Please enter the day (e.g. mon, thu):')
    while internalDay != 'mon' and internalDay != 'tue' and internalDay != 'wed' and internalDay != 'thu' and internalDay != 'fri':
        print('Invalid day! Please try again:')
        internalDay = input('Please enter the day (e.g. mon, thu):')
    print('Valid value entered.')
    return internalDay


def userDayChecker():
    userDayCheckerDay = day()
    if userDayCheckerDay == 'mon' and busA[0] < 0:
        print(f"Bus A was {busA[0] * -1} minutes late on Monday.")
    elif userDayCheckerDay == 'tue' and busA[1] < 0:
        print(f"Bus A was {busA[1] * -1} minutes late on Tuesday.")
    elif userDayCheckerDay == 'wed' and busA[2] < 0:
        print(f"Bus A was {busA[2] * -1} minutes late on Wednesday.")
    elif userDayCheckerDay == 'thu' and busA[3] < 0:
        print(f"Bus A was {busA[3] * -1} minutes late on Thursday.")
    elif userDayCheckerDay == 'fri' and busA[4] < 0:
        print(f"Bus A was {busA[4] * -1} minutes late on Friday.")
    else:
        print(f"Bus A was not late on {userDayCheckerDay.title()}!")


userDayChecker()
userChecker = input(f"Would you like to input another value (y/n)? ")
while True:
    if userChecker == 'n':
        print("Thank you for using this service.")
        break
    elif userChecker == 'y':
        userDayChecker()
    userChecker = input(f"Would you like to input another value?")
