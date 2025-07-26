# Task 1: Read a File and Handle Errors 
# Problem Statement:  Write a Python program that:
# 1.   Opens and reads a text file named sample.txt.
# 2.   Prints its content line by line.
# 3.   Handles errors gracefully if the file does not exist.

try:
    with open('Simple.txt', 'r') as file:
        for line in file:
            print(line.strip()) 
except FileNotFoundError:
    print("Error: The file 'Simple.txt' was not found.")
except Exception as r:
    print(f"An error occurred: {r}")

print("\n")

# Task 2: Write and Append Data to a File
 
# Problem Statement: Write a Python program that:
# 1.   Takes user input and writes it to a file named output.txt.
# 2.   Appends additional data to the same file.
# 3.   Reads and displays the final content of the file.

file1 = open("output.txt", "w")
L = input("Enter Text to write to the file:")
print("data successfully written to output.txt.")
print("\n")
g=input("Enter additional text to append:")
print("Data successfully appended")
with open("output.txt", "w") as file1:
    file1.write(L)
    file1.write("\n")
    file1.writelines(g)
    file1.close() 
 
file1 = open("output.txt", "r+")
print("\n")
print("Final Content of output.txt:")
print(file1.read())
print()