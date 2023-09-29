machine_status = False

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

while not machine_status:
    # we will write our code here incase if we are to process the data and the build something from the scratch
    # also we can create individual python files for each class and import into main python script and use them
    coffee_maker.report