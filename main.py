import data
from data import resources, menu
# TODO : 1) print report   \/
# TODO : 2) check resources sufficient ? \/
# TODO : 3) process coins \/
# TODO : 4) check transaction successful? \/
# TODO : 5) make a coffee \/


def print_report(): #stampa tutte le risorse del distributore, compresa la cassa
    print("risorse rimaste")
    show_resource()
    print(f"Money: {data.cassa}") #i soldi che abbiamo accumolato dalla vendita di bevande
    print()

def show_resource(): #biene utilizzato da report per stampare gli ingredienti rimasti nel distributore
    for ingredient in resources:
        print(f"{ingredient}: {resources[ingredient]}")

def check_resource_sufficient(chosen_drink):#controlla se è rimasta quantita di prodotto dopo il prelievo

    for remaining in menu[chosen_drink]["ingredients"]:
        if resources[remaining] - menu[chosen_drink]['ingredients'][remaining] <= 0:
           return False

    return True

def refresh_resources(chosen_drink):# aggiorna le quantità degli ingredienti  ---->  resource_in_stock[drink]['ingredients'][ingrediente]

     #accede alle quantità delle bevane in menu e aggiorna lo stock di ingredienti
    for ingredient in menu[chosen_drink]["ingredients"]:
        the_resource = menu[chosen_drink]['ingredients'][ingredient]  #accede alle quantita dell'ingrediente della bevanda scelta
        # aggiorna lo stock di ingredienti
        resources[ingredient] -= the_resource

def process_coin(chosen_drink):
    price = menu[chosen_drink]["cost"]
    print(f"il costo della bevanda: {price}")
    money = check_transaction_succesful(price) #qui controlla se i soldi inseriti sono sufficenti
    if money >= price:
        data.cassa += price
        return money - price
    else:
        return "Sorry that's not enough money"

def check_transaction_succesful(price):
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
    choose = input("what would you like? (espresso/latte/cappuccino):")
    if choose == "report":
        print_report()
    elif choose == "off":
        on_off = True
    else:
        rest = process_coin(choose)
        if type(rest) != str:
            print(f"the rest: {rest}")

            if check_resource_sufficient(choose):
                refresh_resources(choose)
                print(f"enjoy your {choose}")
            else:
                print("resources not found")
                on_off = True

        else:
            print(rest) #Sorry that's not enough money