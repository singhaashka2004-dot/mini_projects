# Python program to read a file and handle errors

try:

    file = open("sample.txt", "r")
    print("Contents of sample.txt:\n")
    for line in file:
        print(line.strip())

    file.close()

except FileNotFoundError:
    
    print("Error: The file 'sample.txt' was not found.")
