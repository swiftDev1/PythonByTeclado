#MY MAIN TAKEAWAY
"""
Firstly, python uses "and" and "or" not && or |.
Also it uses "True" and "False" in sentence case not in lowercase.
Take note of the internal working of these functions. "and" is more interested 
in ensuring that both conditions are truthy before it ever returns you a True.
So if the first one is False, it simply return you the first value without bothering
to check the second one. But if the first one is Truthy, it returns the second value.
For "or", it returns the first value if it's true and doesn't bother to check the second
value. But if the first value is falsy, it returns the second value.
Notice how I'm saying return the second `value` not necessarily return True or False.
That's because that's what is being retuened actually. This knowledge can come in
handy in certain programming scenarios.
To check if a value is truthy or falsy, simply pass it through `bool`
"""



# Python has two keywords, `and` and `or`
# Here's how to use them:

age = int(input("Enter your age: "))
can_learn_programming = age > 0 and age < 150

print(f"You can learn programming: {can_learn_programming}")


# -- or --

age = int(input("Enter your age: "))
usually_not_working = age < 18 or age > 65

print(f"At {age}, you are usually not working: {usually_not_working}")

# That could be better re-written to:

age = int(input("Enter your age: "))
usually_working = age > 17 and age < 66  # Notice the changes to the numbers!

print(f"At {age}, you are usually working: {usually_not_working}")


# How they work internally
# `and` gives you the first value if it is falsy, otherwise gives you the second value
# `or` gives you the first value if it is truthy, otherwise gives you the second value

# How to tell if a value is "truthy" or "falsy"?
# Pass it through `bool()`.

print(bool(35))
print(bool("Rolf"))
print(bool(0))
print(bool(""))

# More examples linked in the resources section of the lecture

# --

print("" or "Rolf")  # Rolf, because "" is falsy
print("" and "Rolf")  # "", because it is falsy

print("Rolf" or "")  # "Rolf", because it is truthy
print("Rolf" and "")  # "", because "Rolf" is not falsy