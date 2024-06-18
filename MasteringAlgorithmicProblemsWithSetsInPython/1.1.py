"""
1.1 Finding the Last Unique Element in a String List

Problem: Suppose you've got a list of words, let's say ['apple', 'banana', 'apple', 'mango', 'banana']. Each word could be repeated an arbitrary number of times. Think of this list as a conveyor belt in a space-age fruit factory. Now, your task is to identify the last unique fruit on the belt, i.e., the one that didn't repeat. If all the fruits are repeating, then there ain't any unique fruit, and your function should return an empty string ('').

Your function should take a list of strings (the conveyor belt of fruits) as input. Now, a string can be any word, not just a fruit name, and the list can have any number of strings. There could also be an edge case where the list has no strings at all (Empty conveyor belt, eh?). For output, your function should return the last unique string in the list or an empty string if there are not any of them.
"""
def find_unique_string(words):
    #Define new list to hold flipped original list
    flipped = []
    
    #Flip the list so that the last unique element becomes the first unique element. Append to new list
    for i in range((len(words)-1), -1, -1):
        flipped.append(words[i])
    
    #Define 2 sets - one to hold repeating terms, one to hold appeared-at-least-once terms
    repeating = set()
    once = set()
    
    #Go through all the elements in the flipped list
    for j in flipped:
    #If the element is not in the once set, add it to once
        if j not in once:
            once.add(j)
    #Else add it to the repeating set
        else:
            repeating.add(j)
    
    #Go through the flipped list again, checking if each element is part of the repeating list. The first element that is not part of the repeating list is the last unique element in the original list
    #Return the value of that element
    for k in flipped:
        if k not in repeating:
            return k
    
    #Else return an empty string if no unique terms are found
    return ''

#Test cases
print(find_unique_string(['apple', 'banana', 'apple', 'mango', 'banana']))  # It should print: 'mango'
print(find_unique_string(['hello', 'world', 'hello']))  # It should print: 'world'
print(find_unique_string(['hello', 'world', 'hello', 'world']))  # It should print: ''
print(find_unique_string([]))  # It should print: ''
