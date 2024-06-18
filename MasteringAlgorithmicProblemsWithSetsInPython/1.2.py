"""
1.2 Space Anagram Solver Challenge

Problem: Find the unique words in the first array that can rearrange their letters to match at least one word in the second array. Like transforming 'cinema' into 'iceman'. Cool, right?

The input will be two lists of words; they can be of any size, and words may repeat. As for the output, we need a list of unique words from the first list that have anagrams in the second one. Make sure the spaceship does not crash into an asteroid, and check that there aren't any duplicate words in the output. As for edge cases, watch out for case sensitivity and one-letter words!
"""
def find_anagram_words(list_1, list_2):
    #Create sets of tuples to hold the alphabetically-organized terms in each list
    organized1 = set()
    organized2 = set()
    
    #Add the sorted tuples for each list to their respective sets
    for word in list_1:
        organized1.add(tuple(sorted(word)))
        
    for phrase in list_2:
        organized2.add(tuple(sorted(phrase)))
        
    #Find the common tuples in each list and add them to a new set
    common = organized1 & organized2
    
    #Initialize list to hold the answers
    answers = []
    
    #Run through list 1 again and check if the sorted tuples for each word in the list match a tuple in the common set. If yes, then add it to the answer list
    for e in list_1:
        if tuple(sorted(e)) in common:
            answers.append(e)
    
    #Return the answer list
    return answers
    

#Test cases
print(find_anagram_words(['cinema', 'iceman'], ['iceman', 'cinema'])) # should return ['cinema', 'iceman']
print(find_anagram_words(['test', 'stet'], ['tent', 'nett'])) # should return []
print(find_anagram_words(['hello', 'world'], ['dolly', 'sir'])) # should return []