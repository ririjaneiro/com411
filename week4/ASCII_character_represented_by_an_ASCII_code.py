print("Program Started!")

print("Please enter an ASCII code:")
code = int(input())

if 32 <= code <= 126:
    print(f"The character represented by the ASCII code is {chr(code)}")
else:
    print("The character cannot be displayed")

print("Program Ended!")