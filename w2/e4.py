import_budget = int(input("Enter the movie import budget: "))
n_adult_tickets = int(input("Enter the number of adult tickets sold: "))
n_child_tickets = int(input("Enter the number of child tickets sold: "))

ADULT_TICKET_PRICE = 10
CHILD_TICKET_PRICE = 5

adult_revenue = n_adult_tickets * ADULT_TICKET_PRICE
child_revenue = n_child_tickets * CHILD_TICKET_PRICE

total_revenue = adult_revenue + child_revenue
profit = total_revenue * 0.9 - import_budget

print(f"Total revenue: ${total_revenue}")
print(f"Profit: ${profit}")