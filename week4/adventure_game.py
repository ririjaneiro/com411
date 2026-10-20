def identity():
    see = input("What do you see?\n")
    if see == "a large boulder":
        return "It's time to run!"
    else:
        return "We will be fine."

print(identity())