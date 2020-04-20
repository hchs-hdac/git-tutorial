# Foreword 1: lines with a hash at the front (like this one) are comments: 
# Python knows not to run them as code. 
# Comments are used to explain the function of certain lines of code and to 
# comment out lines you don't want to run on a particular iteration.

# Foreword 2: Google and documentation are your friend! This tutorial is more of a follow-along and practice at the end, 
# so don't hesitate to do additional investigation! 


# Setting variables + printing to console
# The print() function prints to console
print('Hello World!')

# variables are set like so: variable_name = value --> the = is the assignment operator, it does not mean "equal to" (more on this later)
num1 = 3
phrase = "The quick brown fox jumped over the lazy dog"

# print variables to console
print(num1)
print(phrase)

# Intro to datatypes: str, int, float
string = 'string' # strings are in single or double quotes
num2 = 7 # python recognizes integers
num3 = 5.4 # python also recognizes decimals, or floating point numbers

# the type function returns the datatype of the variable/element
print(type('Hello World!')) # prints: class <str> (str stands for string)
print(type(string), type(num2), type(num3))

# Basic mathematical operations
print(2 + 2) 
print(2 - 1)
print(3 * 2)
print(45 / 15) # regular division - will return a float
print(45 // 12) # // denotes floor division - no remainder and will return an int
print(45 % 12) # % denotes the remainder function (modulus)
print(4 ** 2) # ** denotes exponent

# Concatenating/joining strings with + operator
string = 'hello'
print(string + 'world!') # smashes the two strings together

num = 1
print('the number is ' + str(num)) # str() changes the datatype of num to a string so they can be concatenated

# Practice 1: Print a variable of your choosing to the console

# Practice 2: Print the remainder of 10 / 4

# Practice 3: Print the string 'tacocat' by joining the strings 'taco' and 'cat' together