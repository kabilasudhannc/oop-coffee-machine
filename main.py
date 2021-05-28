from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()


def coffee_machine():
    try:
        choices = input(f'What would you like? ({menu.get_items()}): ').lower()

        if choices == 'off':
            print('Bye.')
            return

        elif choices == 'report':
            coffee_maker.report()
            money_machine.report()

        elif choices in menu.get_items().split('/'):
            ingredients = menu.find_drink(choices)
            menu_item = MenuItem(ingredients.name, ingredients.ingredients['water'], ingredients.ingredients['milk'],
                                 ingredients.ingredients['coffee'], ingredients.cost)

            if coffee_maker.is_resource_sufficient(menu_item) and money_machine.make_payment(menu_item.cost):
                coffee_maker.make_coffee(menu_item)

        else:
            print('The item you entered is not available.')

    except:
        print('Something went wrong. Try again.')

    coffee_machine()


coffee_machine()
