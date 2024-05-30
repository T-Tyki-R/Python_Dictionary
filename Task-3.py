# Python Programming Challenges for Customer Service Data Handling

service_tickets = {
    "Ticket001": {"Customer": "Alice", "Issue": "Login problem", "Status": "open"},
    "Ticket002": {"Customer": "Bob", "Issue": "Payment issue", "Status": "closed"}
}


# create a func that'll create a new ticket
def new_ticket():
    user_name = input("May I have your name? ").capitalize()
    user_issue = input("What is the issue? ").capitalize()
    user_ticket_num = len(service_tickets.keys()) + 1

    service_tickets[f"Ticket00{user_ticket_num}"] = {"Customer": user_name, "Issue": user_issue, "Status": "open"}
    return f"{user_name}, this is you ticket number: Ticket00{user_ticket_num}\n" 

def ticket_update():
    user_ticket_num = input("Please enter your ticket number: ").capitalize()

    if user_ticket_num in service_tickets.keys():
        found_ticket = service_tickets[user_ticket_num]
        if found_ticket["Status"] == "open":
            found_ticket["Status"] = "closed"
            return f"Your ticket is now {found_ticket["Status"]}\n"
        else:
            found_ticket["Status"] = "open"
            return f"Your ticket is now {found_ticket["Status"]}\n"
    else:
        print("That ticket isn't in the system\n")

def display_ticket():
    print("1. Display All Tickets\n2. Filter")
    user_choice = int(input(f"How do you want to view the tickets?\nEnter 1 for all tickets\nEnter 2 to filter\nEnter here:  "))
    if user_choice == 1:
        for i, x in service_tickets.items():
            print(f"\n{i}")
            for y in x:
                print(f"{y}: {x[y]}")                
    elif user_choice == 2:
         print("1. Opened Tickets\n2. Closed Tickets")
         user_filter_option = int(input("Enter 1 for opened tickets or 2 for closed tickets: "))
         for i, x in service_tickets.items():
            if user_filter_option == 1 and x["Status"] == "open":
                print(f"{i}")
                for y in x:
                    print(f"{y}: {x[y]}")
            elif user_filter_option == 2 and x["Status"] == "closed":
                print(f"{i}")
                for y in x:
                    print(f"{y}: {x[y]}")
            else:
                print("You picked an invalid option")
    else:
        print("You picked an invalid option")
                
print(new_ticket())
print(ticket_update())
print(display_ticket())