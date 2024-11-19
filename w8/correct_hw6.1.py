def main():
    more_bill = True
    while more_bill:
        bill_amount = get_bill()
        tip_percent = get_tip()

        final_bill, tip = calculate_bill(bill_amount, tip_percent)
        
        print(f'Tip: ${tip:.2f}')
        print(f'Total amount (bill + tip): ${final_bill:.2f}')

        more_bill = input('Are there more customers? (yes or no) ') == 'yes'

def get_bill():
    invalid = True
    while invalid:
        bill_amount = float(input('Enter the amount of the bill: '))
        if bill_amount > 0:
            invalid = False
        else:
            print('Invalid amount. Please enter a positive number.')
    return bill_amount

def get_tip():
    tip_percent = input('Enter the tip percentage: ')
    if tip_percent:
        return float(tip_percent)
    
    return 0.15

def calculate_bill(bill_amount, tip_percent):
    tip = bill_amount * tip_percent
    return bill_amount + tip, tip

####
main()