#Write a Python function that takes a list of words and return the longest word and the length of the longest one.

Longest word: Exercises
Length of the longest word: 9


def find_longest_word(word_list):       #Defining function
    longest_word =  max(word_list, key=len)   
    print ("Longest word:", longest_word)
    print ("Length of longest word:", len (longest_word))
    return longest_word, len(longest_word)
    
txt = input ("Enter the words: ")
word_list = txt.split()              #splits string to list
print ("list of words is:",word_list)  
find_longest_word(word_list)           #Calling the function
