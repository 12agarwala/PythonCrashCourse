import datetime
import time

# Single tickets function: adults, seniors and children (day 1 and 2 options)
def singleTickets():
    numberTickets = [0, 0, 0, 0, 0, 0]
    dummy = "y"
    while dummy == "y":
        # Will keep asking user until correct response is given (string input)
        while True:
            singleTicketType = input("What type of single tickets do you want? ")
            if singleTicketType.lower() == "adult" or singleTicketType.lower() == "senior":
                break
            else:
                print("Please enter the correct ticket type")
        # Will keep asking user until correct response is given (int input)
        while True:
            ticketNumber = input("How many " + singleTicketType + " tickets do you want? ")
            if ticketNumber.isnumeric():
                ticketNumber = int(ticketNumber)
                break
            else:
                print("Please enter the correct number")
        # Will keep asking user until correct response is given (string input but stored as integer)
        while True:
            numberOfDays = input("How many number of days do you want tickets for (1 or 2)? ")
            if numberOfDays == "1" or numberOfDays == "2":
                numberOfDays = int(numberOfDays)
                break
            else:
                print("Please enter the correct number of days")
        if singleTicketType == "adult":
            numberTickets[0] = numberTickets[0] + ticketNumber
            numberTickets[3] = numberOfDays
        elif singleTicketType == "senior":
            numberTickets[1] = numberTickets[1] + ticketNumber
            numberTickets[4] = numberOfDays
        dummy = input("Do you want to buy more single tickets (y, n)? ")
    totalAdultTickets = numberTickets[0] + numberTickets[1]
    # Children tickets is asked after adults and seniors because an adult can bring up to two children. Because each
    # adult can only bring up to two children, validation is required to ensure availability of children tickets.
    # i.e. 2 adult tickets can grant up to 4 child tickets, not 5 or more.
    childTicket = input("Do you want to buy children tickets (y, n)? ")
    if childTicket.lower() == "y":
        # For child tickets, the number of days is not asked because it is expected that children will be with adults
        # at all times. If adult books a 2 day-ticket then child will stay for 2 days.
        while True:
            cTickets = input("How many children tickets do you want to buy? ")
            if cTickets.isnumeric():
                if int(cTickets) <= (2*totalAdultTickets):
                    numberTickets[2] = numberTickets[2] + int(cTickets)
                    numberTickets[5] = numberOfDays
                    break
                # If the user bought 2 adult tickets and tried to buy 5 child tickets, an error message will pop up
                # saying that they can't bring more than 4 children.
                else:
                    print("You can't bring more than", (2*totalAdultTickets), "children.")
    return numberTickets


# Group tickets function: family and group (day 1 and 2 options)
def groupTickets():
    numberTickets = [0, 0, 0, 0]
    dummy = "y"
    s = 1
    while dummy == "y":
        # Will keep asking user until correct response is given (string input)
        while True:
            groupTicketType = input("What type of group tickets do you want? ")
            # If user wants to buy a family ticket, a message will pop up saying that a family ticket means up to 2
            # adults/seniors and 3 children.
            if groupTicketType.lower() == "family":
                print("A maximum of 2 adults and 3 children can go on this ticket. ")
                break
            elif groupTicketType.lower() == "group":
                s = 1
                break
            else:
                print("Please enter the correct ticket type")
        # Will keep asking user until correct response is given (int input)
        while s == 1:
            ticketNumber = input("How many " + groupTicketType + " tickets do you want to buy? ")
            if ticketNumber.isnumeric():
                ticketNumber = int(ticketNumber)
                s = 1
                break
            else:
                print("Please enter the correct number")
        # Will keep asking user until correct response is given (int input)
        while True:
            numberOfDays = input("How many number of days do you want tickets for (1 or 2)? ")
            if numberOfDays == "1" or numberOfDays == "2":
                numberOfDays = int(numberOfDays)
                break
            else:
                print("Please enter the correct number of days")
        if groupTicketType == "family":
            numberTickets[0] = numberTickets[0] + 1
            numberTickets[2] = numberOfDays
        elif groupTicketType == "group":
            numberTickets[1] = numberTickets[1] + ticketNumber
            numberTickets[3] = numberOfDays
        dummy = input("Do you want to buy more group tickets (y, n)? ")
    return numberTickets


def extraAttractions(ticketInfo):
    differentAttractions = [0, 0, 0]
    barbecue = 0
    # 2 pathways, 1 for single tickets (len is 4) and 1 for group tickets (len is 6).
    if len(ticketInfo) == 4:
        if ticketInfo[2] == 2 or ticketInfo[3] == 2:
            barbecue = 1
    if len(ticketInfo) == 6:
        if ticketInfo[3] == 2 or ticketInfo[4] == 2:
            barbecue = 1
    dummy = "y"
    while dummy == "y":
        # Will keep asking user until correct response is given (int input)
        while True:
            attractions = input("What type of extra attractions do you want?\n Type 1 for lion feeding, 2 for penguin feeding, 3 for barbecue ")
            if attractions.lower() == "1" or attractions.lower() == "2":
                break
            # This code ensures that evening barbecue is only available for 2-day tickets.
            elif attractions.lower() == "3":
                if barbecue == 1:
                    break
                else:
                    print("Sorry, this attraction is available only for 2 day tickets")
            else:
                print("Please enter the correct attraction number")
        # Will keep asking user until correct response is given (int input)
        while True:
            s_Attractions = input("How many tickets do you want? ")
            if s_Attractions.isnumeric():
                s_Attractions = int(s_Attractions)
                break
            else:
                print("Please enter the correct number")
        if attractions == "1":
            differentAttractions[0] = differentAttractions[0] + s_Attractions
        elif attractions == "2":
            differentAttractions[1] = differentAttractions[1] + s_Attractions
        elif attractions == "3":
            differentAttractions[2] = differentAttractions[2] + s_Attractions
        dummy = input("Do you want to buy any more extra attractions (y, n)? ")
    return differentAttractions


# This function will produce a ticket with an unique booking number (The datetime module).
# Total cost of each attraction is calculated by multiplying the cost of 1 ticket price with total tickets bought.
# This part is only for group tickets.
def bookingInfo(ticket, extra):
    x = datetime.datetime.now()
    lFeeding = extra[0] * 2.5
    pFeeding = extra[1] * 2
    eBarbecue = extra[2] * 5
    fTicketPrice = 0
    gTicketPrice = 0
    if len(ticket) == 4:
        # Price for 2 days family ticket
        if ticket[0] > 0:
            if ticket[2] == 2:
                fTicketPrice = ticket[0] * 90
            else:
                fTicketPrice = ticket[0] * 60
        # Price for 2 days group ticket
        if ticket[1] > 1:
            if ticket[3] == 3:
                gTicketPrice = ticket[1] * 22.5
            else:
                gTicketPrice = ticket[1] * 15

        # Ticket information for group ticket
        bookingId = str(x) + " group"
        print('--------------------------------------------')
        print(bookingId)
        print("| Ticket Type             | Family | Group |")
        print("| Ticket cost             | $", fTicketPrice, "  | $", gTicketPrice, "  |")
        print("| Extra Attractions       |")
        print("| Lion Feeding: $", lFeeding, "   |\n| Penguin Feeding: $", pFeeding, "  |\n| Evening Barbecue: $", eBarbecue, " |")
        print('--------------------------------------------')

    # This part is only for single tickets.
    if len(ticket) == 6:
        x = datetime.datetime.now()
        lFeeding = extra[0] * 2.5
        pFeeding = extra[1] * 2
        eBarbecue = extra[2] * 5
        aTicketPrice = 0
        sTicketPrice = 0
        cTicketPrice = 0
        if len(ticket) == 6:
            # Price for 2 days adult ticket
            if ticket[0] > 0:
                if ticket[3] == 2:
                    aTicketPrice = ticket[0] * 30
                else:
                    aTicketPrice = ticket[0] * 20
            # Price for 2 days senior ticket
            if ticket[1] > 0:
                if ticket[4] == 2:
                    sTicketPrice = ticket[1] * 24
                else:
                    sTicketPrice = ticket[1] * 16
            # Price for 2 days children ticket
            if ticket[2] > 0:
                if ticket[5] == 2:
                    cTicketPrice = ticket[2] * 18
                else:
                    cTicketPrice = ticket[2] * 12

        # Ticket information for single ticket
        bookingId = str(x) + " single                        |"
        print('----------------------------------------------------------')
        print(bookingId)
        print("| Ticket Type             | Adult | Children | Senior |")
        print("| Ticket cost             | $", aTicketPrice, "  | $", cTicketPrice, "     | $", sTicketPrice, "   |")
        print("| Extra Attractions       |")
        print("| Lion Feeding: $", lFeeding, "   |\n| Penguin Feeding: $", pFeeding, "  |\n| Evening Barbecue: $", eBarbecue, " |")
        print('--------------------------------------------')


# This function will provide the best ticket option based on the details provided by the user
def bestValue(singleTickets, groupTickets):
    gTickets = [0, 0, 0, 0]
# Group ticket best value
    if singleTickets[0] + singleTickets[1] > 5:
        gTickets[1] = singleTickets[0]
        gTickets[3] = singleTickets[4]
    elif singleTickets[0] >= 4 and singleTickets[3] >= 2:
        gTickets[1] = singleTickets[0] + singleTickets[3]
        gTickets[3] = singleTickets[4]
    elif singleTickets[0] == 5:
        gTickets[1] = 6
        gTickets[3] = singleTickets[4]
    elif singleTickets[1] >= 5 and singleTickets[3] >= 1:
        gTickets[1] = singleTickets[1] + singleTickets[3]
        gTickets[3] = singleTickets[4]
    if groupTickets[1] > 7:
        groupBestValue = float(input("How many children tickets did you buy? "))
        if groupBestValue == (1.5 * groupTickets[1] - groupBestValue):
            gTickets[0] == groupBestValue/3


# Family best value
    if singleTickets[0] == 2 and singleTickets[2] >= 2:
        gTickets[0] = 1
        gTickets[2] = singleTickets[3]
    elif singleTickets[1] == 2 and singleTickets[2] > 2:
        gTickets[0] = 1
        gTickets[2] = singleTickets[4]
    elif singleTickets[0] == 1 and singleTickets[1] == 1 and singleTickets[2] >= 2:
        gTickets[0] = 1
        gTickets[2] = singleTickets[3]

    return gTickets

# This is the table with information for each ticket type and type of extra attraction
def printTable():
    print(f"")
    print('--------------------------------------------------------------------')
    print("| Ticket Type       | Adult  | Children | Senior | Family | Group  |")
    print("| One day cost      | $20.00 | $12.00   | $16.00 | $60.00 | $15.00 |")
    print("| Two day cost      | $30.00 | $18.00   | $24.00 | $90.00 | $22.50 |")
    print("| Extra Attractions |                                              |")
    print("| Lion Feeding      | Penguin Feeding   | Evening Barbeque         |")
    print("| $2.50             | $2.00             | $5.00                    |")
    print('--------------------------------------------------------------------')
# Program starts here


printTable()
extraAttractionTickets = [0, 0, 0]
extraAttractionG = [0, 0, 0]
singleTicketNumbers = [0, 0, 0, 0, 0, 0]
groupTicketNumbers = [0, 0, 0, 0]
ticketType = input("What type of ticket do you want? Group or single: ")
if ticketType.lower() == "single":
    singleTicketNumbers = singleTickets()
    print(singleTicketNumbers)
    buyExtraAttractions = input("Do you want to buy any extra attraction tickets (y, n)? ")
    if buyExtraAttractions.lower() == "y":
        extraAttractionTickets = extraAttractions(singleTicketNumbers)
    else:
        print("Here is your ticket")
    print(singleTicketNumbers)
    bookingInfo(singleTicketNumbers, extraAttractionTickets)
elif ticketType.lower() == "group":
    groupTicketNumbers = groupTickets()
    print(groupTicketNumbers)
    buyExtraAttractions = input("Do you want to buy any extra attraction tickets (y, n)? ")
    if buyExtraAttractions.lower() == "y":
        extraAttractionG = extraAttractions(groupTicketNumbers)
    else:
        print("Here is your ticket")
    print(groupTicketNumbers)
    bookingInfo(groupTicketNumbers, extraAttractionG)
bestTicket = bestValue(singleTicketNumbers, groupTicketNumbers)
if bestTicket[0] >= 1 or bestTicket[1] >= 1:
    bookingInfo(bestTicket, extraAttractionTickets)

