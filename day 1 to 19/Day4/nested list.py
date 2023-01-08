# Nested lists
fruits = ['Strawberries', 'Nectarines', 'Apples', 'Grapes', 'Peaches', 'Cherries', 'Pears']
vegetables = ['spinach', 'Tomatoes', 'kale', 'Potatoes']

dirty_dozen = [fruits, vegetables]
print(dirty_dozen)
print(dirty_dozen[0])
print(dirty_dozen[1])
print(dirty_dozen[0][3])

# 0, 3 will print from first list and 3rd item
# 1 3 will print from 2nd list and 3rd item