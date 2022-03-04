# Name: Shilpa Kolekar
# Cash Register Program

# This program asks user to enter the cost of the items one at a time
# and when done, displays the number of items and the total cost of them

# locale module is imported to print the amount in currency format
import locale


# class CashRegister track number of items and total cost
class CashRegister:

    # __init__ method to initiate an instance of CashRegister class.
    # The itemCount and totalPrice attributes are passed as argument followed by self

    def __init__(self, itemCount, totalPrice):
        self.itemCount = itemCount
        self.totalPrice = totalPrice

    # getCount method returns the itemCount attribute
    def getCount(self):
        return self.itemCount

    # getTotal method returns the totalPrice attribute
    def getTotal(self):
        return self.totalPrice

    # addItem method increases the totalPrice by the price value passed in
    # and increments the count
    def addItem(self, price):
        self.itemCount += 1
        self.totalPrice += price


# main function
def main():
    # setting locale for all categories to default
    locale.setlocale(locale.LC_ALL, '')
    # instance of CashRegister class
    cash_register = CashRegister(0, 0.00)
    # welcome message and taking user input from screen
    print('Welcome to automated Cash Register System!')

    # loop until user enters 'y' or 'Y'
    while True:
        print('Please enter the cost of an item in the cart one at a time. Enter Y when done.')
        response = input()
        if response.upper() == 'Y':
            break
        try:
            # convert user response to float, call add_item function
            response = float(response)
            cash_register.addItem(response)
        # valueError exception for invalid entry
        except ValueError:
            print('Invalid value entered, Please enter a valid amount')

    # calculate and display total number of items and total price
    count = cash_register.getCount()
    amount = locale.currency(cash_register.getTotal())
    # print message on the screen
    print('Thank you for using automated Cash Register System!')
    print('Total number of items : {:>10}'.format(count))
    print('Total price of items :  {:>10}'.format(amount))


# main function
main()
