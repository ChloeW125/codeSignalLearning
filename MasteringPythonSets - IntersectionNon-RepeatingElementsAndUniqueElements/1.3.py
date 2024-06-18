"""
1.3 Comparative Analysis of Exclusive Clothing Inventory in Two Stores

Problem: Here's a real-world situation: You're a data analyst for a universal retail conglomerate managing two clothing stores, let's call them Space Threads and Galaxy Garments. You have two lists named inventory1 and inventory2 representing the clothing items from these stores. Now, your prime mission is to figure out the clothes that are exclusive to each store. Note that the letter casing is not important, so items like "t-shirt" and "T-Shirt" are considered the same. Return all exclusive clothes sorted in alphabetical order.

Keep in mind that we're dealing with text data here. The length of these lists can range from as few as no items to as many as a star cluster. There is zero room for error, kid. Now, get to it!

Hint: To compare items, ignoring the casing, convert all elements to uppercase.
"""
def exclusive_products(inventory1, inventory2):
    #Sets for each inventory list
    set1 = set() #For inventory1
    set2 = set() #For inventory2
    
    #Go through the terms in each list and convert them all to uppercase. Then append them each to a set
    for i in inventory1:
        set1.add(i.upper())
        
    for j in inventory2:
        set2.add(j.upper())
        
    #Find the items exclusive to each set and add them to another set
    exclusive1 = set() #For inventory1
    exclusive2 = set() #Foer inventory2
    
    exclusive1 = set1 - set2
    exclusive2 = set2 - set1
    
    #Return the exclusive sets in appropriate order
    return (sorted(exclusive1), sorted(exclusive2))

#Test cases
inventory1 = ["Shirt", "Jeans", "Hat"]
inventory2 = ["jeans", "Belt", "Boots"]
print(exclusive_products(inventory1, inventory2))
# Expected output: (['HAT', 'SHIRT'], ['BELT', 'BOOTS'])

inventory1 = ["T-Shirt", "hoodie", "Backpack"]
inventory2 = ["Backpack", "Hoodie", "t-shirt"]
print(exclusive_products(inventory1, inventory2))
# Expected output: ([], [])

inventory1 = []
inventory2 = ["Dress", "Skirt", "Coat"]
print(exclusive_products(inventory1, inventory2))
# Expected output: ([], ['COAT', 'DRESS', 'SKIRT'])
