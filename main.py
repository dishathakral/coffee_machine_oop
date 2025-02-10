from menu import Menu,MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu=Menu()
coffee_maker=CoffeeMaker()
money_machine=MoneyMachine()
make_coffee=True
menu_list=menu.get_items().split('/')
while make_coffee:
    options=menu.get_items()
    drink=input(f'What would you like?{options}:').lower()
    if drink=='report':
        coffee_maker.report()
        money_machine.report()
    elif drink=='off':
        make_coffee=False
    else:
        coffee=menu.find_drink(drink)
        if coffee:
            if coffee_maker.is_resource_sufficient(coffee)  and money_machine.make_payment(coffee.cost):
                coffee_maker.make_coffee(coffee)
            else:
                print(f"Sorry, we don't have {drink}. Please choose from the available options.")
