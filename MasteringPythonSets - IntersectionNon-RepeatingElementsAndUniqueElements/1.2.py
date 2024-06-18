"""
1.2 Identifying Duplicate Integers in a List

Problem: Alright, Voyager, here's your next mission. Your objective is to identify all the elements in a list of integers that are repeating their ugly mugs more than once. They could be negative and in no particular order, just to keep you on your toes!

Your final output should be a list of these duplicate numbers. The order? Doesn't matter!
"""
def repeating_elements(nums):
    #Define sets to hold the repeating and unique integers
    repeating = set()
    unique = set()
    
    #Run through list using a for loop, append terms to each list according to how many times they appear
    for i in(nums):
        #If an integer appears for the first time, add it to the unique set
        if i not in unique:
            unique.add(i)
        #Else that means that the integer has already showed up before and is repeating, so add to the repeating set
        else:
            repeating.add(i)
    
    #After running through the list, return the repeating set in the form of a list
    return list(repeating)

#Test cases
print(repeating_elements([9, 8, 7, 8, 7, 6, 5]))  # expected output : [8, 7]
print(repeating_elements([-1, 2, 3, -1, 2, 3]))   # expected output : [-1, 2, 3]
print(repeating_elements([1, 2, 3, 4, 5]))        # expected output : []