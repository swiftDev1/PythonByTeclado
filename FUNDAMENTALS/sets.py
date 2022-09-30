"""
Sets are used when you want absolutely no repetition. It is defined with curly braces.
You can run .append and .remove functions on sets but if the element already exists,
it will be skipped without throwing any errors. Even if you define a set and there are
duplicate elements inside, it will simply eliminate the extras without raising issues.
Also, sets are unordered.
"""

# -- Defining sets --

art_friends = {"Rolf", "Anne", "Anne"}
science_friends = {"Jen", "Charlie"}

# -- Adding to a set --

art_friends.add("Jen")

print(art_friends)

# -- No duplicate items --

art_friends.add("Jen")

print(art_friends)  # Same as before, "Jen" was not added twice

# -- Removing from a set --

science_friends.remove("Charlie")

print(science_friends)