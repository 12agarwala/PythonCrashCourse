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
        userInputBus = input("Please enter the correct bus letter: ")
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

busBAverage = busBCount / len(busB)
if lateValueCounter != 0:
    busBLateAverage = lateValue / lateValueCounter
    print(f"Bus B late average is {round(busBLateAverage)} minutes.")
print(f"Bus B average is {round(busBAverage)} minutes.")

busCAverage = busCCount / len(busC)
if lateValueCounter != 0:
    busCLateAverage = lateValue / lateValueCounter
    print(f"Bus C late average is {round(busCLateAverage)} minutes.")
print(f"Bus C average is {round(busCAverage)} minutes.")

busDAverage = busDCount / len(busD)
if lateValueCounter != 0:
    busDLateAverage = lateValue / lateValueCounter
    print(f"Bus D late average is {round(busDLateAverage)} minutes.")
print(f"Bus D average is {round(busDAverage)} minutes.")

busEAverage = busECount / len(busE)
if lateValueCounter != 0:
    busELateAverage = lateValue / lateValueCounter
    print(f"Bus E late average is {round(busELateAverage)} minutes.")
print(f"Bus E average is {round(busEAverage)} minutes.")

busFAverage = busFCount / len(busF)
if lateValueCounter != 0:
    busFLateAverage = lateValue / lateValueCounter
    print(f"Bus F late average is {round(busFLateAverage)} minutes.")
print(f"Bus F average is {round(busFAverage)} minutes.")

def day():
    internalDay = input('Please enter the day (e.g. mon, thu):')
    while internalDay != 'mon' and internalDay != 'tue' and internalDay != 'wed' and internalDay != 'thu' and internalDay != 'fri':
        print('Invalid day! Please try again:')
        internalDay = input('Please enter the day (e.g. mon, thu):')
    print('Valid value entered.')
    return internalDay


def userDayChecker():
    userDayCheckerDay = day()
    if userDayCheckerDay.lower() == 'mon' and busA[0] < 0:
        print(f"Bus A was {busA[0] * -1} minutes late on Monday.")
    elif userDayCheckerDay.lower() == 'tue' and busA[1] < 0:
        print(f"Bus A was {busA[1] * -1} minutes late on Tuesday.")
    elif userDayCheckerDay.lower() == 'wed' and busA[2] < 0:
        print(f"Bus A was {busA[2] * -1} minutes late on Wednesday.")
    elif userDayCheckerDay.lower() == 'thu' and busA[3] < 0:
        print(f"Bus A was {busA[3] * -1} minutes late on Thursday.")
    elif userDayCheckerDay.lower() == 'fri' and busA[4] < 0:
        print(f"Bus A was {busA[4] * -1} minutes late on Friday.")
    else:
        print(f"Bus A was not late on {userDayCheckerDay.title()}!")

def userDayChecker():
    userDayCheckerDay = day()
    if userDayCheckerDay.lower() == 'mon' and busB[0] < 0:
        print(f"Bus B was {busB[0] * -1} minutes late on Monday.")
    elif userDayCheckerDay.lower() == 'tue' and busB[1] < 0:
        print(f"Bus B was {busB[1] * -1} minutes late on Tuesday.")
    elif userDayCheckerDay.lower() == 'wed' and busB[2] < 0:
        print(f"Bus B was {busB[2] * -1} minutes late on Wednesday.")
    elif userDayCheckerDay.lower() == 'thu' and busB[3] < 0:
        print(f"Bus B was {busB[3] * -1} minutes late on Thursday.")
    elif userDayCheckerDay.lower() == 'fri' and busB[4] < 0:
        print(f"Bus B was {busB[4] * -1} minutes late on Friday.")
    else:
        print(f"Bus B was not late on {userDayCheckerDay.title()}!")

def userDayChecker():
    userDayCheckerDay = day()
    if userDayCheckerDay.lower() == 'mon' and busC[0] < 0:
        print(f"Bus C was {busC[0] * -1} minutes late on Monday.")
    elif userDayCheckerDay.lower() == 'tue' and busC[1] < 0:
        print(f"Bus C was {busC[1] * -1} minutes late on Tuesday.")
    elif userDayCheckerDay.lower() == 'wed' and busC[2] < 0:
        print(f"Bus C was {busC[2] * -1} minutes late on Wednesday.")
    elif userDayCheckerDay.lower() == 'thu' and busC[3] < 0:
        print(f"Bus C was {busC[3] * -1} minutes late on Thursday.")
    elif userDayCheckerDay.lower() == 'fri' and busC[4] < 0:
        print(f"Bus C was {busC[4] * -1} minutes late on Friday.")
    else:
        print(f"Bus C was not late on {userDayCheckerDay.title()}!")

def userDayChecker():
    userDayCheckerDay = day()
    if userDayCheckerDay.lower() == 'mon' and busD[0] < 0:
        print(f"Bus D was {busD[0] * -1} minutes late on Monday.")
    elif userDayCheckerDay.lower() == 'tue' and busD[1] < 0:
        print(f"Bus D was {busD[1] * -1} minutes late on Tuesday.")
    elif userDayCheckerDay.lower() == 'wed' and busD[2] < 0:
        print(f"Bus D was {busD[2] * -1} minutes late on Wednesday.")
    elif userDayCheckerDay.lower() == 'thu' and busD[3] < 0:
        print(f"Bus D was {busD[3] * -1} minutes late on Thursday.")
    elif userDayCheckerDay.lower() == 'fri' and busD[4] < 0:
        print(f"Bus D was {busD[4] * -1} minutes late on Friday.")
    else:
        print(f"Bus D was not late on {userDayCheckerDay.title()}!")

def userDayChecker():
    userDayCheckerDay = day()
    if userDayCheckerDay.lower() == 'mon' and busE[0] < 0:
        print(f"Bus E was {busE[0] * -1} minutes late on Monday.")
    elif userDayCheckerDay.lower() == 'tue' and busE[1] < 0:
        print(f"Bus E was {busE[1] * -1} minutes late on Tuesday.")
    elif userDayCheckerDay.lower() == 'wed' and busE[2] < 0:
        print(f"Bus E was {busE[2] * -1} minutes late on Wednesday.")
    elif userDayCheckerDay.lower() == 'thu' and busE[3] < 0:
        print(f"Bus E was {busE[3] * -1} minutes late on Thursday.")
    elif userDayCheckerDay.lower() == 'fri' and busE[4] < 0:
        print(f"Bus E was {busE[4] * -1} minutes late on Friday.")
    else:
        print(f"Bus E was not late on {userDayCheckerDay.title()}!")

def userDayChecker():
    userDayCheckerDay = day()
    if userDayCheckerDay.lower() == 'mon' and busF[0] < 0:
        print(f"Bus F was {busF[0] * -1} minutes late on Monday.")
    elif userDayCheckerDay.lower() == 'tue' and busF[1] < 0:
        print(f"Bus F was {busF[1] * -1} minutes late on Tuesday.")
    elif userDayCheckerDay.lower() == 'wed' and busF[2] < 0:
        print(f"Bus F was {busF[2] * -1} minutes late on Wednesday.")
    elif userDayCheckerDay.lower() == 'thu' and busF[3] < 0:
        print(f"Bus F was {busF[3] * -1} minutes late on Thursday.")
    elif userDayCheckerDay.lower() == 'fri' and busF[4] < 0:
        print(f"Bus F was {busF[4] * -1} minutes late on Friday.")
    else:
        print(f"Bus F was not late on {userDayCheckerDay.title()}!")

userDayChecker()
userChecker = input(f"Would you like to input another value (y/n)? ")
while True:
    if userChecker == 'n':
        print("Thank you for using this service.")
        break
    elif userChecker == 'y':
        userDayChecker()
    userChecker = input(f"Would you like to input another value?")
