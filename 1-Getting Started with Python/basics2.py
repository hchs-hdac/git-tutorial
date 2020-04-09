# Mutable datatypes: list, dict
# Lists: groupings of items of any datatype separated by commas
lst = [1, 2, 3.0, 'Hello World!', [4, 5, 6]] # lists are denoted by square brackets

# Dictionaries: grouping of items (any datatype) based on key-value pairs separated by commas
# Keys are used as index values (more later!) 
dct = {'key': 'value', 13: ['Hello World!', 'bee', 'brain'], 'hi': 6633} 

# Indexing: grabbing specific elements from lists/dictionaries based on a designated index value
# Python starts indexing at 0 - for example, the first element in a list will be index 0, not index 1

# List indexing
print(lst[0]) # first element in lst - returns 1
print(lst[4][1]) # the second element inside the list [4, 5, 6] which is inside the original list

# Dictionary indexing -- by key
print(dct['key'])
print(dct[13][2])

# Slicing: extracting pieces from a datatype (i.e. string, list)
string = 'Hello World!'
print(string[0:3]) # prints the first 3 elements (the elements with indices 0 to 3, excluding 3)
print(string[:3]) # same as previous line - Python assumes you're starting at the beginning, so the 0 isn't necessary
print(string[:]) # prints the whole string beginning to end
print(string[::2]) # prints every other character in the string beginning to end
print(string[::-1]) # prints whole string backwards
