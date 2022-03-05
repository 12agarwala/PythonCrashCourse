def printTable():
   # updateTickets()
    print(f"")
    print('-------------------------------------------------------------------')
    print("| TicketType       | Adult  | Children | Senior | Family | Group  |")
    print("| One day cost     | $20.00 | $12.00   | $16.00 | $60.00 | $15.00 |")
    print("| Two day cost     | $30.00 | $18.00   | $24.00 | $90.00 | $22.50 |")
    print("| ExtraAttractions |                                              |")
    print("| LionFeeding      | PenguinFeeding    | EveningBarbeque          |")
    print("| $2.50            | $2.00             | $5.00                    |")
    print('-------------------------------------------------------------------')

printTable()

ticketType = input("What type of ticket do you want? Group or single: ")
if ticketType == "single":
    singleTickets()
if ticketType == "group":
    groupTickets()


