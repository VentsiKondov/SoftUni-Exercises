championship_stage = input()
type_of_ticket = input()
number_of_tickets = int(input())
photo_with_trophy = input()
price_photo = 40
ticket_sum = 0
free_photos = False

if championship_stage == 'Quarter final':
    if type_of_ticket == 'Standard':
        ticket_sum = 55.5 * number_of_tickets
    elif type_of_ticket == 'Premium':
        ticket_sum = 105.2 * number_of_tickets
    elif type_of_ticket == 'VIP':
        ticket_sum = 118.9 * number_of_tickets
elif championship_stage == 'Semi final':
    if type_of_ticket == 'Standard':
        ticket_sum =  75.88 * number_of_tickets
    elif type_of_ticket == 'Premium':
        ticket_sum = 125.22 * number_of_tickets
    elif type_of_ticket == 'VIP':
        ticket_sum = 300.4 * number_of_tickets
elif championship_stage == 'Final':
    if type_of_ticket == 'Standard':
        ticket_sum = 110.1 * number_of_tickets
    elif type_of_ticket == 'Premium':
        ticket_sum = 160.66 * number_of_tickets
    elif type_of_ticket == 'VIP':
        ticket_sum = 400 * number_of_tickets

if ticket_sum > 4000:
    ticket_sum *= 0.75
    free_photos = True
elif 2500<ticket_sum<=4000:
    ticket_sum *= 0.9

if photo_with_trophy == "Y":
    if not free_photos:
        ticket_sum += number_of_tickets * price_photo


print(f'{ticket_sum:.2f}')