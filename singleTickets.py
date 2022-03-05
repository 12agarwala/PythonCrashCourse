def singleTicket():
    numberTickets = [0, 0, 0]
    while True:
        singleTicketType = input("What type of single tickets do you want? ")
        if singleTicketType.lower() == "adult" or singleTicketType.lower() == "senior" or singleTicketType.lower() == "child":
            break
        else:
            print("Please enter the correct ticket type: ")
    while True:
        ticketNumber = int(input("How many", singleTicketType, "tickets do you want? "))
        if ticketNumber.isnumeric():
            break
        else:
            print("Please enter the correct number: ")
    if singleTicketType == "adult":
        numberTickets[0] = numberTickets[0] + ticketNumber
    elif singleTicketType == "senior":
        numberTickets[1] = numberTickets[1] + ticketNumber
    elif singleTicketType == "child":
        numberTickets[2] = numberTickets[2] + ticketNumber
    return
