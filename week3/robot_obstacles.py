print("How many obstacles must I avoid?")
obstacles_to_avoid = int(input())

obstacles_avoided = 0

print()

while obstacles_avoided < obstacles_to_avoid:
    obstacles_avoided = obstacles_avoided + 1
    print("Avoiding...", end="")

    print(f"Done! {obstacles_avoided} obstacles avoided.")


