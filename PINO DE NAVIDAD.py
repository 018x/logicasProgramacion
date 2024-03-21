def validate_input(size):
    while True:
        try:
            size = int(input("Please enter the desired size for your Christmas tree (must be at least 6): "))
            if size < 6:
                print("The size must be at least 6. Please enter a new size: ")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a number.")
    return size

desired_size = validate_input(0)

# Print the top part of the tree
print("*" * desired_size)

# Print the middle part of the tree
for i in range(desired_size - 2, 0, -1):
    print("*" + " " * (desired_size - 2) + "*")

# Print the bottom part of the tree
print("*" * desired_size)