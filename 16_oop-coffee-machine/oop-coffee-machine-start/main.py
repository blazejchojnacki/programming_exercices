from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

cof_menu = Menu()
maker = CoffeeMaker()
machine = MoneyMachine()

while True:
    option = input("What would you like? (" + cof_menu.get_items() + "): ")

    if option == "off":
        break
    elif option == "report":
        maker.report()
        machine.report()
    elif type(cof_menu.find_drink(option)) == MenuItem:
        coffee = cof_menu.find_drink(option)
        if maker.is_resource_sufficient(coffee):
            if machine.make_payment(coffee.cost):
                maker.make_coffee(coffee)
