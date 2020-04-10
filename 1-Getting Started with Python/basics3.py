# Conditionals (if/elif/else) - will run commands only if the statement is true
x = 1
lst = ['Corn Flakes', 'Cheerios', 'Special K']

if x == 1: # the == signifies "equal to" - this is in order to distinguish from  = which assigns variables
    print('X is 1.')
else:
    print('X is not 1.')

# elif - shortened "else if"
# in this instance, Python will read the first if statement, then conclude that x is not in the list
# then it will move on to the elif statement and execute that command (X is 1 will print) - and won't read the else statement
# now add the integer 1 to the list and run it again - this time it executes the first command
if x in lst:
    print(str(x) + ' is amazing!') # have to change the type of x to a string so that the strings can concatenate
elif x == 1:
    print('X is 1.')
else:
    print(x)

# Loops: allow you to execute the same commands a set number of times
# the two loops below both print the numbers 0 through 9 to the console

# while loop
y = 0
while y < 10: # while loops will loop while the condition is true, and then break once it becomes false
    print(y)
    y += 1 # the y += 1 is shorthand for y = y + 1

# for loop: i is an arbitrary variable - it can be named anything
for i in range(0, 10): # range from 0 up to but not including 10 - this loop will run 10 times, because there are 10 digits in the range (0, 10)
    print(i)

# for loops are useful for looping through datasets (i.e. lists)
# with this loop, we are generating a copy of the previous list in a new list
new_lst = [] # empty list 
for i in lst: # loops through all the items in lst
    new_lst.append(i) # i attached to the new list at the back
print(new_lst)

# List comprehensions: a handy shortcut for the task above
new_lst = [i for i in lst] # creates new lists in 1 line - you can skip the appending step here
print(new_lst)

# Another example
lst_of_nums = [3, 2, 58, 20]
new_lst_of_nums = [num + 1 for num in lst_of_nums] # you can also modify the elements in the original list
print(new_lst_of_nums)