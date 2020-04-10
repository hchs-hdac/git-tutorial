# Putting it all together with functions!
# Python allows you to define your own custom functions with custom parameters

# def command tells Python you're defining a new function
# Best practice is to make concise function names that quickly explain what your function will be used for
def add_numbers(num1, num2): # num1 and num2 here are arguments (or parameters) required in order for the function to operate
    return num1 + num2 # this function adds the given arguments together and returns the sum

# here we are calling the function with the arguments 3 and 4, 
# meaning that we want the function to run and return 3 + 4.
sum_ = add_numbers(3, 4) 
print(sum_)

# sidenote: the reason we're using sum_ as the variable name instead of sum
# is because Python has a builtin function called sum - this way Python doesn't get confused

# Practice: write your own function that will square any number you put in
