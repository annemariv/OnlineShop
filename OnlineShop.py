class Client:
    def __init__(self, id, name, total_sum = 0):
        self.id = id
        self.name = name
        self.total_sum = total_sum
        self.transactions = []

    def make_order(self, item):
        self.transactions.append(Transaction(item.name, item.price, item.currency))
        self.total_sum += item.price

class Items:
    def __init__(self, name, price, currency):
        self.name = name
        self.price = price
        self.currency = currency

class Transaction:
    def __init__(self, item_name, amount, currency):
        self.item_name = item_name
        self.amount = amount
        self.currency = currency

clients = []
clients.append(Client('12345', 'Mari'))
clients.append(Client('98765', 'Karl'))
clients.append(Client('23456', 'Liisa'))

store_items = []
store_items.append(Items('T-shirt', 10, '€'))
store_items.append(Items('Jeans', 20, '€'))
store_items.append(Items('Dress', 15, '€'))
store_items.append(Items('Jacket', 30, '€'))
store_items.append(Items('Hat', 5, '€'))
store_items.append(Items('Hoodie', 18, '€'))

for client in clients:
    print(f'The client {client.id} has entered the store.')

for client in clients:
    print(f'\n{client.name}, welcome to the clothes online shop!')
    print('\nCurrently available clothes:')
    item_index = 0
    for item in store_items:
        item_index += 1
        print(f'  {item_index}. {item.name}: {item.price}{item.currency}')

    while True:
        user_descicion1 = input('\nWould you like to make a purchase (yes/no)? ')
        if user_descicion1.lower() == 'no':
            print('Thank you for visiting!')
            break
        elif user_descicion1.lower() == 'yes':
            while True:
                try:
                    item_choice = int(input('\nEnter the item number you would like to buy (1-6): '))
                    if 0 < item_choice <= len(store_items):
                        selected_item = store_items[item_choice - 1]
                        client.make_order(selected_item)
                        print(f'{selected_item.name} added to the cart.')

                        while True:
                            user_descicion2 = input('\nWould you like to purchase another item (yes/no)? ')
                            if user_descicion2.lower() == 'no':
                                print(f'\nYour cart:')
                                for transaction in client.transactions:
                                    print(f'  {transaction.item_name.lower()}: {transaction.amount}{transaction.currency}')
                                print(f'Total amount to pay is: {client.total_sum}€')
                                print(f'\n{client.name}, thank you for shopping!')
                                break
                            elif user_descicion2.lower() == 'yes':
                                break
                            else:
                                print('Invalid input. Please answer yes or no.')
                        if user_descicion2.lower() == 'no':
                            break
                    else:
                        print('Invalid input. Please enter a number of the item (1-6).')

                except ValueError:
                    print('Invalid input. Please enter a number.')
            break
        else:
            print('Invalid input. Please answer yes or no.')