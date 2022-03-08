def groupTickets():
    numberTickets = [0, 0]
    while True:
        groupTicketType = input("What type of group tickets do you want? ")
        if groupTicketType.lower() == "family" or groupTicketType.lower() == "group":
            break
        else:
            print("Please enter the correct ticket type")
    while True:
        ticketNumber = input("How many " + groupTicketType + " tickets do you want? ")
        if ticketNumber.isnumeric():
            ticketNumber = int(ticketNumber)
            break
        else:
            print("Please enter the correct number")
    if groupTicketType == "family":
        numberTickets[0] = numberTickets[0] + ticketNumber
    elif groupTicketType == "group":
        numberTickets[1] = numberTickets[1] + ticketNumber
    return numberTickets
