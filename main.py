import data
from data import resources, menu
# TODO : 1) print report   
# TODO : 2) check resources sufficient ? 
# TODO : 3) process coins 
# TODO : 4) check transaction successful? 
# TODO : 5) make a coffee 


def print_report(): #print all resource and money
    print("risorse rimaste")
    show_resource()
    print(f"Money: {data.cassa}")
    print()

def show_resource(): #used by report to print remaing resource
    for ingredient in resources:
        print(f"{ingredient}: {resources[ingredient]}")

def check_resource_sufficient(chosen_drink):#cehck if there're anough resources to make chosen drink

    for remaining in menu[chosen_drink]["ingredients"]:
        if resources[remaining] - menu[chosen_drink]['ingredients'][remaining] <= 0:
           return False

    return True

def refresh_resources(chosen_drink):# Update ingredient quantities ---->  resource_in_stock[drink]['ingredients'][ingrediente]

    for ingredient in menu[chosen_drink]["ingredients"]:
        the_resource = menu[chosen_drink]['ingredients'][ingredient]  #it get ingredient quantities of choosen drink
        # update of ingredient stock
        resources[ingredient] -= the_resource

def process_coin(chosen_drink):#ceck if are enough money
    price = menu[chosen_drink]["cost"]#it get price of chosen drink
    print(f"il costo della bevanda: {price}")
    money = check_transaction_succesful(price)
    if money >= price:
        data.cassa += price
        return money - price
    else:
        return "Sorry that's not enough money"

def check_transaction_succesful(price): #ask money  to pay chosen drink
    PENNY = 0.01
    NIKEL = 0.05
    DIME = 0.10
    QUARTER = 0.25
    quarters = float(input("how many quarters?"))
    dime = float(input("how many dime?"))
    nikel = float(input("how many nikel?"))
    penny = float(input("how many penny?"))
    sum = (quarters * QUARTER) + (dime * DIME) + (nikel * NIKEL) + (penny * PENNY)
    return sum

#start
on_off = False
while on_off != True:
    chosen = input("what would you like? (espresso/latte/cappuccino):")
    if chosen == "report":
        print_report()
    elif chosen == "off":
        on_off = True
    else:
        rest = process_coin(chosen)
        if type(rest) != str:
            print(f"the rest: {rest}")

            if check_resource_sufficient(chosen):
                refresh_resources(chosen)
                print(f"enjoy your {chosen}")
            else:
                print("resources not found")
                on_off = True

        else:
            print(rest) #Sorry that's not enough money
