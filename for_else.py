# On loops, you can add an `else` clause. This only runs if the loop does not encounter a `break` or an error.
# That means, if the loop completes successfully, the `else` part will run.
"""
This unpopular feature of Python can really come in handy and save you many lines of code.
It simply means, 'If everything goes great with this loop, then run this.
Please note that this doesn't work with `continue`. The else block will always run with continue
"""

cars = ["ok", "ok", "ok", "faulty", "ok", "ok"]

for status in cars:
    if status == "faulty":
        print("Stopping the production line!")
        break

    print(f"This car is {status}.")
else:
    print("All cars built successfully. No faulty cars!")


# Remove the "faulty" and you'll see the `else` part starts running.