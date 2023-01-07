'''Write a Python function to convert more than one list to a nested dictionary.
Original lists:
['S001', 'S002', 'S003', 'S004']
['Adina Park', 'Leyton Marsh', 'Duncan Boyle', 'Saim Richards']
[85, 98, 89, 92]
Nested dictionary:
[{'S001': {'Adina Park': 85}}, {'S002': {'Leyton Marsh': 98}}, {'S003': {'Duncan Boyle': 89}}, {'S004': {'Saim Richards': 92}}]'''
==========================================================================================================================================================================
==========================================================================================================================================================================


def all_lists(l1,l2,l3):
    #using for loop and declaring variables to the items of every list
    result = [{a: {b: c}} for (a, b, c) in zip(l1, l2, l3)] 
    return result
l1 = ['S001', 'S002', 'S003', 'S004']
l2 = ['Adina Park', 'Leyton Marsh', 'Duncan Boyle', 'Saim Richards']
l3 = [85, 98, 89, 92]
print (l1, l2, l3)
print ("\nThe nested dictionary is: ")
print (all_lists(l1,l2,l3))
