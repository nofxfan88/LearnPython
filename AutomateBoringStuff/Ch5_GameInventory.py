def displayInventory(inventory):

    print('Inventory:')
    for item, amount in inventory.items():
        print(str(amount) + ' ' + item)
    print()
    print('Total number of items: ' + str(totalInventory(inventory)))

def totalInventory(inventory):
    total = 0

    for item, amount in inventory.items():
        total += amount

    return total

def addToInventory(inventory, items):

    for item in items:
        inventory.setdefault(item, 0)
        inventory[item] += 1

inventory = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

displayInventory(inventory)

dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

addToInventory(inventory, dragonLoot)
displayInventory(inventory)
