"""
Notice how break actually completes the current iteration before completely exiting the loop.
For "continue", the current iteration is skipped and the loop goes back to the top the moment
the keyword is encountered.
"""

# -- break --
# Exits out of the loop, so that no more iterations occur.

cars = ["ok", "ok", "ok", "faulty", "ok", "ok"]

for status in cars:
    if status == "faulty":
        print("Stopping the production line!")
        break

    print(f"This car is {status}.")

# -- continue --
# Terminates the current iteration and moves onto the next one.

cars = ["ok", "ok", "ok", "faulty", "ok", "ok"]

for status in cars:
    if status == "faulty":
        print("Found faulty car, skipping...")
        continue

    print(f"This car is {status}.")
    print("Shipping new car to customer!")