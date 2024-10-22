n = 5
revenue = 0

for day in range(1, n + 1):
    n_products = int(input(f'Enter number of products for day {day}: '))
    for p in range(1, n_products + 1):
        price = int(input(f'Enter price for product {p}: '))
        revenue += price

print(f'Total revenue for {n} days is {revenue}')