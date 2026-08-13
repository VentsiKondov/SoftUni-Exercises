company_name = input()
elder_tickets = int(input())
kid_tickets = int(input())
price_for_elder_ticket = float(input())
tax = float(input())

kid_ticket_price = price_for_elder_ticket * 0.3
total_price_for_elders = price_for_elder_ticket + tax

profit = 0.2 * (kid_tickets * (kid_ticket_price + tax) + (elder_tickets * total_price_for_elders))

print(f'The profit of your agency from {company_name} tickets is {profit:.2f} lv.')