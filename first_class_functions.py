'''
Functions are first class citizens in Python. This means that just like strings, integers and anything else 
really, we can pass functions to variables, we can pass them in as arguments to other functions, use them 
as values in lists, dictionaries, etc.
'''
def greet():
    print("Hello")

'''To call the function we need to include the paranthesis even if it's empty. If we just type greet
it won't give you any output as the function is not run. But this is a valid python syntax.
this means the entire function itself and this value can be assigned to a variable'''

hello = greet
hello()  #prints "Hello"

