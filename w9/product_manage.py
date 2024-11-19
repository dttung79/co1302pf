list_products = ['pencil', 'pen', 'notebook', 'eraser', 'sharpener', 'ruler']
list_prices = [0.5, 1.0, 2.5, 0.3, 0.7, 1.2]
list_quantities = [100, 75, 25, 120, 10, 60]
NOT_FOUND = -1

def main():
    running = True
    while running:
        print_menu()
        choice = int(input('Enter your choice: '))
        if choice == 1:     list_all()
        elif choice == 2:   add()
        elif choice == 3:   change_price()
        elif choice == 4:   sell()
        elif choice == 5:   remove()
        elif choice == 6:   running = False 
        else:               print('Invalid choice. Please try again.')

def print_menu():
    print('1. List all products')
    print('2. Add a new product')
    print('3. Change the price of a product')
    print('4. Sell a product')
    print('5. Remove a product')
    print('6. Quit')

def list_all():
    # print header
    print('+-----+----------+-----+----------+')
    print(f'|{"No":^5s}|{"Product":^10s}|{"Price":^5s}|{"Quantity":^10s}|')
    print('+-----+----------+-----+----------+')

    for i in range(1, len(list_products) + 1):
        print(f'|{i:5d}|{list_products[i-1]:^10s}|{list_prices[i-1]:5.2f}|{list_quantities[i-1]:10d}|')
        print('+-----+----------+-----+----------+')

def add():
    # enter product name
    product = input('Enter product name: ').lower()
    # check product name is not in the list
    if find(product) != NOT_FOUND:
        print(f'Product {product} already exists.')
        return
    # enter product price
    price = float(input('Enter product price: '))
    # enter product quantity
    quantity = int(input('Enter product quantity: '))
    # add product information to the lists
    list_products.append(product)
    list_prices.append(price)
    list_quantities.append(quantity)

def find(product):
    for i in range(len(list_products)):
        if list_products[i] == product:
            return i
    return NOT_FOUND

def change_price():
    # enter product name
    product = input('Enter product name: ').lower()
    # check if product exists
    pos = find(product)
    if pos == NOT_FOUND:
        print(f'Product {product} does not exist.')
        return
    # enter new price
    new_price = float(input('Enter new price: '))
    # update price in the list
    list_prices[pos] = new_price

def sell():
    # enter product name
    product = input('Enter product name: ').lower()
    # check if product exists
    pos = find(product)
    if pos == NOT_FOUND:
        print(f'Product {product} does not exist.')
        return
    # enter quantity
    quantity = int(input('Enter quantity: '))
    # check if quantity is enough
    if quantity > list_quantities[pos]:
        print('Not enough quantity.')
        return
    # update quantity in the list
    list_quantities[pos] -= quantity

def remove():
    # enter product name
    product = input('Enter product name: ').lower()
    # check if product exists
    pos = find(product)
    if pos == NOT_FOUND:
        print(f'Product {product} does not exist.')
        return
    # remove product, price, quantity from the lists
    list_products.pop(pos)      # remove product using pop
    del list_prices[pos]        # remove price using del
    del list_quantities[pos]

## call main to run
main()