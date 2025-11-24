# shopping cart

# dictionary for inventory
# shopping cart will be a list of items
# need functions
inventory = [
    {"ID": 1, "name": "banana", "price": 0.33},
    {"ID": 2, "name": "apple", "price": 0.55},
    {"ID": 3, "name": "orange", "price": 0.71},
    {"ID": 4, "name": "grape", "price": 1.05},
    {"ID": 5, "name": "mango", "price": 1.53}
]

# initialize an empty shopping cart
# view inventory
shopping_cart = []

def get_item_id(name):
    print(f'Name: {name}')

    id_to_return = 0  # Local variable

    for item in inventory:
        if(item["name"] == name):
            id_to_return = item["ID"]
            break
    return id_to_return

def show_inventory():
    for item in inventory:
        print(f"{item['ID']}: {item['name']} - ${item['price']}")

def add_to_cart(item):
    print(item)
    shopping_cart.append(item)
    print(f'Cart: {shopping_cart}')

def remove_from_cart(item):
    print(item)
    shopping_cart.remove(item)
    print(f'Cart: {shopping_cart}')

def calculate_cart_total(item):
    total = 0
    for item_id in shopping_cart:
        for item in inventory:
            if(item["ID"] == item_id):
                total += item["price"]
                break
    return total

def main():
    print('walk into store')
    show_inventory() 

    # see inventory
    for item in inventory:
        if(item['name'] == 'banana'):
            print(f"{item['price']}")

    # add item to cart
    selected_item = input('What item would you like to add to cart? banana, apple, orange, grape, mango? ')
    print('selected_item: ', selected_item)

    item_id = get_item_id(selected_item)
    add_to_cart(item_id)

    # loop through add cart until user says no
    while True:
        add_more_item = input('Would you like to add another item to cart? (yes/no) ')
        if(add_more_item.lower() == 'yes'):
            selected_item = input('What item would you like to add to cart? banana, apple, orange, grape, mango? ')
            print('selected_item: ', selected_item)

            item_id = get_item_id(selected_item)
            add_to_cart(item_id)
        else:
            print('No more items to add.')
            break
    
    # remove item from cart
    selected_item = input("What item would you like to remove from cart? banana, apple, orange, grape, mango? ")
    print("remove_item: ", selected_item)

    item_id = get_item_id(selected_item)
    remove_from_cart(item_id)

    # loop through add cart until user says no
    while True:
        remove_more_item = input("Would you like to remove another item to cart? (yes/no) ")
        if remove_more_item.lower() == "yes":
            selected_item = input("What item would you like to remove from cart? banana, apple, orange, grape, mango? ")
            print("selected_item: ", selected_item)

            item_id = get_item_id(selected_item)
            remove_from_cart(item_id)
        else:
            print("No more items to remove.")
            break

    # calculate total
    total = calculate_cart_total(shopping_cart)
    print(f'Total so far: ${total}')

    # check-out
    checkout = input('Would you like to check out? (yes/no)')
    if(checkout.lower() == 'yes'):
        print(f'Your total is ${total}. Thank you for shopping!')
    else:
        print('You can continue shopping.')

if __name__ == "__main__":
    main()
    # view cart
    print(f'Final Cart: {shopping_cart}')