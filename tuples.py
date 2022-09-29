"""
Tuples are defined like lists but they use round brackets instead.
Tuples are useful for when you want to keep an array unchanged forever.
Most of the time I'd recommend using tuples over lists, and only use lists
when you specifically want to allow changes. So for tuples, there is nothing
like append or remove
"""

# -- Defining tuples --

short_tuple = "Rolf", "Bob"
a_bit_clearer = ("Rolf", "Bob")
not_a_tuple = "Rolf"

# -- Adding to a tuple --

friends = ("Rolf", "Bob", "Anne")
friends.append("Jen")  # ERROR!


# -- Removing from a tuple --

friends.remove("Bob")  # ERROR!


# Tuples are useful for when you want to keep it unchanged forever.
# Most of the time I'd recommend using tuples over lists, and only use lists when you specifically want to allow changes.
