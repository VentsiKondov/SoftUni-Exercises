movie_name = input()


student_tickets = []
standard_tickets = []
kids_tickets = []

ticket_counter = 0
all_ticket_counter = 0
while movie_name != 'Finish':
    ticket_number = int(input())
    type_of_ticket = input()
    ticket_counter = 0
    while True:
        if type_of_ticket == "student":
            student_tickets.append(type_of_ticket)
        elif type_of_ticket == "standard":
            standard_tickets.append(type_of_ticket)
        elif type_of_ticket == "kid":
            kids_tickets.append(type_of_ticket)

        if type_of_ticket == "Finish" or ticket_counter == ticket_number:
            print(f"{movie_name} - {(ticket_counter/ ticket_number) * 100:.2f}% full.")
            movie_name = type_of_ticket
            break
        elif type_of_ticket == "End":
            print(f"{movie_name} - {(ticket_counter / ticket_number) * 100:.2f}% full.")
            movie_name = input()
            break


        ticket_counter += 1
        all_ticket_counter += 1
        type_of_ticket = input()




print(f"Total tickets: {all_ticket_counter}")
print(f"{(len(student_tickets) / all_ticket_counter)*100:.2f}% student tickets.")
print(f"{(len(standard_tickets) / all_ticket_counter)*100:.2f}% standard tickets.")
print(f"{(len(kids_tickets) / all_ticket_counter) * 100 :.2f}% kids tickets.")



