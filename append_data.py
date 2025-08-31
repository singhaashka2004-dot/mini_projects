data = input("Enter some text to write into the file: ")

with open("output.txt", "w") as file:
    file.write(data + "\n")

extra_data = input("Enter more text to append: ")

with open("output.txt", "a") as file:
    file.write(extra_data + "\n")

print("\nFinal contents of output.txt:\n")

with open("output.txt", "r") as file:
    for line in file:
        print(line.strip())
