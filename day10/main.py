class MoneyMachine:
    def report():
        print('Report')



class CoffeeMaker:
    def report():
        print('Report from the coffee maker')

    def is_resource_enuf():
        print('Method to check if the resource is enough')

    def make_coffee():
        print('In the process of making coffee')

class Menu:
    def get_items():
        print('Items from the menu class')
    
    def find_drink(order_num):
        print('Checking the drink based on the order num')

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()
