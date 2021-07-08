from coffee_machine_data import MENU,resources
def insert_coins():
    print('Pls insert Coins! ')
    quarters=float(input('how many quarters?: $'))
    dimes=float(input('how many dimes?: $'))
    nickels=float(input('how many nickles?:$'))
    pennies=float(input('how many pennies?:$'))
    return 0.25*quarters+0.10*dimes+0.05*nickels+0.01*pennies


is_on=True
def check_resources(order_ingredients):
    for key in order_ingredients:
        if resources[key]<order_ingredients[key]:
            print(f'Sorry there is not enough {key}')
            return False
    return True
def use_resources(order_ingredients):
    for key in order_ingredients:
        resources[key]-=order_ingredients[key]
    return resources
profit=0
while is_on:
    user_input=input('What would U like to have today?\nEspresso / Latte / Cappuccino : ').lower()
    if user_input=='report':
        print(f'Water : {resources["water"]}')
        print(f'Milk : {resources["milk"]}')
        print(f'Coffee: {resources["coffee"]}')
        print(f'The current profit is {profit}')
    elif user_input=='off':
        coffee_machine=False
    else:
        amount_intake=insert_coins()
        use_resources(MENU[user_input]['ingredients'])
        drink_cost=MENU[user_input]['cost']
        if amount_intake>=drink_cost:
            profit+=drink_cost
            if amount_intake>drink_cost:
                change=round(amount_intake-drink_cost)
                print(f'The change is {change} $ , Enjoy ur {user_input}')
        check_resources(MENU[user_input]['ingredients'])
        
        

    









