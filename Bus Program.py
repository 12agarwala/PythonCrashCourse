busA = []
busB = []
busC = []
busD = []
busE = []
busF = []

userInputBus = ''


def bus():
    global userInputBus
    userInputBus = input("Please enter the correct bus letter: ")
    while userInputBus.lower() != 'a' and userInputBus.lower() != 'b' and userInputBus.lower() != 'c' and userInputBus.lower() != 'd' and userInputBus.lower() != 'e' and userInputBus.lower() != 'f':
        print('Invalid input! Please enter the correct bus letter.')
        userInputBus = input("Please enter the correct bus letter: ")
    print("Valid input entered.")


def weekChecker():
    if userInputBus == 'a':
        return busA
    elif userInputBus == 'b':
        return busB
    elif userInputBus == 'c':
        return busB
    elif userInputBus == 'd':
        return busB
    elif userInputBus == 'e':
        return busB
    elif userInputBus == 'f':
        return busB


bus()

storedValue = 0
lateValue = 0
lateValueCounter = 0
for i in range(20):
    try:
        inputBusValue = int(input(f"Please enter a number for bus {userInputBus.title()}: "))
    except ValueError:
        continue
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
print(userInputBus)
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
        busBCount = busBCount + n
        busCCount = busCCount + n
        busDCount = busDCount + n
        busECount = busECount + n
        busFCount = busFCount + n

busAverage = busACount / len(weekChecker())

if lateValueCounter != 0:
    busLateAverage = lateValue / lateValueCounter
    print(f"Bus {userInputBus.title()} late average is {round(busLateAverage)} minutes.")
print(f"Bus {userInputBus.title()} average is {round(busAverage)} minutes.")


def day():
    internalDay = input('Please enter the day (e.g. mon, thu):')
    while internalDay != 'mon' and internalDay != 'tue' and internalDay != 'wed' and internalDay != 'thu' and internalDay != 'fri':
        print('Invalid day! Please try again:')
        internalDay = input('Please enter the day (e.g. mon, thu):')
    print('Valid value entered.')
    return internalDay


def userDayChecker():
    userDayCheckerDay = day()
    if userDayCheckerDay.lower() == 'mon' and weekChecker()[0] < 0:
        print(f"Bus {userInputBus.title()} was {weekChecker()[0] * -1} minutes late on Monday.")
    elif userDayCheckerDay.lower() == 'tue' and weekChecker()[1] < 0:
        print(f"Bus {userInputBus.title()} was {weekChecker()[1] * -1} minutes late on Tuesday.")
    elif userDayCheckerDay.lower() == 'wed' and weekChecker()[2] < 0:
        print(f"Bus {userInputBus.title()} was {weekChecker()[2] * -1} minutes late on Wednesday.")
    elif userDayCheckerDay.lower() == 'thu' and weekChecker()[3] < 0:
        print(f"Bus {userInputBus.title()} was {weekChecker()[3] * -1} minutes late on Thursday.")
    elif userDayCheckerDay.lower() == 'fri' and weekChecker()[4] < 0:
        print(f"Bus {userInputBus.title()} was {weekChecker()[4] * -1} minutes late on Friday.")
    elif userDayCheckerDay.lower() == 'mon2' and weekChecker()[5] < 0:
        print(f"Bus {userInputBus.title()} was {weekChecker()[5] * -1} minutes late on Monday Week 2.")
    elif userDayCheckerDay.lower() == 'tue2' and weekChecker()[6] < 0:
        print(f"Bus {userInputBus.title()} was {weekChecker()[6] * -1} minutes late on Tuesday Week 2.")
    elif userDayCheckerDay.lower() == 'wed2' and weekChecker()[7] < 0:
        print(f"Bus {userInputBus.title()} was {weekChecker()[7] * -1} minutes late on Wednesday Week 2.")
    elif userDayCheckerDay.lower() == 'thu2' and weekChecker()[8] < 0:
        print(f"Bus {userInputBus.title()} was {weekChecker()[8] * -1} minutes late on Thursday Week 2.")
    elif userDayCheckerDay.lower() == 'fri2' and weekChecker()[9] < 0:
        print(f"Bus {userInputBus.title()} was {weekChecker()[9] * -1} minutes late on Friday Week 2.")
    elif userDayCheckerDay.lower() == 'mon3' and weekChecker()[10] < 0:
        print(f"Bus {userInputBus.title()} was {weekChecker()[10] * -1} minutes late on Monday Week 3.")
    elif userDayCheckerDay.lower() == 'tue3' and weekChecker()[11] < 0:
        print(f"Bus {userInputBus.title()} was {weekChecker()[11] * -1} minutes late on Tuesday Week 3.")
    elif userDayCheckerDay.lower() == 'wed3' and weekChecker()[12] < 0:
        print(f"Bus {userInputBus.title()} was {weekChecker()[12] * -1} minutes late on Wednesday Week 3.")
    elif userDayCheckerDay.lower() == 'thu3' and weekChecker()[13] < 0:
        print(f"Bus {userInputBus.title()} was {weekChecker()[13] * -1} minutes late on Thursday Week 3.")
    elif userDayCheckerDay.lower() == 'fri3' and weekChecker()[14] < 0:
        print(f"Bus {userInputBus.title()} was {weekChecker()[14] * -1} minutes late on Friday Week 3.")
    else:
        print(f"Bus {userInputBus.title()} was not late on {userDayCheckerDay.title()}!")


userDayChecker()
userChecker = input(f"Would you like to input another value (y/n)? ")
while True:
    if userChecker == 'n':
        print("Thank you for using this service.")
        break
    elif userChecker == 'y':
        userDayChecker()
    userChecker = input(f"Would you like to input another value?")
