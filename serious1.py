inventory = {
'gold' : 500,
'pouch' : ['flint', 'twine', 'gemstone'],
'backpack' : ['xylophone', 'dagger', 'bedroll', 'bread loaf']
}

inventory['pocket'] = ['seashell', 'strange berry','lint']
print(inventory)

backpack = inventory['backpack']
backpack.pop(1)
print(inventory)

inventory['gold'] = [500, 50]
print(inventory)
