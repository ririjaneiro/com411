# Ask user to enter their name
print("What is your name?")
name = input()
print(f"It is nice to meet you {name}")

# Prompt the user for an eye character and read the response
eye = input("Please enter a character for the eye: ")

print("\nThe robot's expression is now as follows:")
# Display the ASCII robot using the user's custom character for the eyes
print(f"[{eye}_{eye}]")
print("/ | \\")
print("| = |")
print("/ | \\")
print("_/ \\_")