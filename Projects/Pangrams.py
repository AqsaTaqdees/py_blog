'''Write a Python function to check whether a string is a pangram or not. Pangrams are words or sentences containing every letter of the alphabet at least once.

Example 1: "The quick brown fox jumps over the lazy dog."
Example 2: “My girl wove six dozen plaid jackets before she quit.”
Example 3: “Brown jars prevented the mixture from freezing too quickly.”'''
==========================================================================================================================================================================
==========================================================================================================================================================================


import string
def pangram(str, alphabet=string.ascii_uppercase):  #making all the alphabets to uppercase
    alphabet = set(alphabet)
    print (alphabet)
    if alphabet <= set(str.upper()):
        print ("It's a pangram")
        return True 
    print ("It's not a pangram")
    return False 
#taking input from user                           
print (pangram(input("Sentence: "))) 

