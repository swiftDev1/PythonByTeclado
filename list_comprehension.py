'''
Please follow the examples carefully. This capability often comes in handy.
My suggestion is to first write the for loop, then in front of it, write the
modifications to be made.
'''

#Before list comprehension
numbers = [0, 1, 2, 3, 4]
doubled_numbers = []

for num in numbers:
    doubled_numbers.append(num * 2)

print(doubled_numbers)

# -- List comprehension --

numbers = [0, 1, 2, 3, 4]  # list(range(5)) is better
doubled_numbers = [num * 2 for num in numbers]
# [num * 2 for num in range(5)] would be even better.

print(doubled_numbers)

# -- You can add anything to the new list --

friend_ages = [22, 31, 35, 37]
age_strings = [f"My friend is {age} years old." for age in friend_ages]

print(age_strings)


# -- This includes things like --
names = ["Rolf", "Bob", "Jen"]
lower = [name.lower() for name in names]

# That is particularly useful for working with user input.
# By turning everything to lowercase, it's less likely we'll miss a match.

friend = input("Enter your friend name: ")
friends = ["Rolf", "Bob", "Jen", "Charlie", "Anne"]
friends_lower = [name.lower() for name in friends]

if friend.lower() in friends_lower:
    print(f"I know {friend}!")

#List Comprehension with Conditions
ages = [22, 35, 27, 21, 20]
odds = [n for n in ages if n % 2 == 1]

# -- with strings --

friends = ["Rolf", "ruth", "charlie", "Jen"]
guests = ["jose", "Bob", "Rolf", "Charlie", "michael"]

friends_lower = [f.lower() for f in friends]

present_friends = [
    name.capitalize() for name in guests if name.lower() in friends_lower
]

# -- nested list comprehensions --
# Don't do this, because it's almost completely unreadable.
# Splitting things out into variables is better.

friends = ["Rolf", "ruth", "charlie", "Jen"]
guests = ["jose", "Bob", "Rolf", "Charlie", "michael"]
'''Please completely avoid something like this!!!'''
present_friends = [
    name.capitalize() for name in guests if name.lower() in [f.lower() for f in friends]
]


#Set and Dictionary Comprehension
friends = ["Rolf", "ruth", "charlie", "Jen"]
guests = ["jose", "Bob", "Rolf", "Charlie", "michael"]

friends_lower = {n.lower() for n in friends}
guests_lower = {n.lower() for n in guests}

present_friends = friends_lower.intersection(guests_lower)
present_friends = {name.capitalize() for name in friends_lower & guests_lower}

print(present_friends)

'''
Notice the use of ampersand above.
When used with sets, they(& and |) do the intersection and union operations, respectively.
for example:
>>> set("abcd") & set("cdef")
set(['c', 'd'])
>>> set("abcd") | set("cdef")
set(['a', 'c', 'b', 'e', 'd', 'f'])
'''

# Transforming data for easier consumption and processing is a very common task.
# Working with homogeneous data is really nice, but often you can't (e.g. when working with user input!).

# -- Dictionary comprehension --
# Works just like set comprehension, but you need to do key-value pairs.

friends = ["Rolf", "Bob", "Jen", "Anne"]
time_since_seen = [3, 7, 15, 11]

long_timers = {
    friends[i]: time_since_seen[i]
    for i in range(len(friends))
    if time_since_seen[i] > 5
}

print(long_timers)