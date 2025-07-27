# Task 1: Read a File and Handle Errors 
# Problem Statement:  Write a Python program that:
# 1.   Opens and reads a text file named sample.txt.
# 2.   Prints its content line by line.
# 3.   Handles errors gracefully if the file does not exist.

Step:1 there we are using error Exception handling Statment for showing appropriate message for
       diffrent situation if user does not have file in same directory.
Step:2 in "try" Statement we are using open() with "with" which are recommended way to handle file operations.
step:3 there we are using "For loop" to read Document and print line by line.
step:4 next we are using Except "FileNotFoundError:" to print a message when program does not found any file Simple.txt. 
step:5 in next line one more Except "Exception as r" using for read mode.
step:6 print('\n') for one line space.

# Task 2: Write and Append Data to a File
 
# Problem Statement: Write a Python program that:
# 1.   Takes user input and writes it to a file named output.txt.
# 2.   Appends additional data to the same file.
# 3.   Reads and displays the final content of the file.

step:1 first we are taking one veriable its contain values which are move from open("output.txt,"w").
step:2 taking second veriable "L" which contain input from user.
step:3 print("data successfully written to output.txt.")
step:4 print('\n') for one line space.
step:5 take "g" which contain input str from user for append in existing text in output file.
step:6 print("Data successfully appended")
step:7 with open("output.txt", "w") as file1: (there we open output file in write mode.)
step:8 file1.write(L)----(apply write() on file1 for add value contain by "L".
step:9 file1.write("\n")----(for add one line Space in document) 
step:10 file1.writelines(g)----(apply writelines() on file1 for append value which are contain by "g".)
step:11 file1.close() close document after all text add in document
step:12 file1 = open("output.txt", "r+") ((there we open output file in  reading and writing mode.)
step:13 print("\n")---(for one line space.)
step:14 print ("Final Content of output.txt:")
step:15 print(file1.read())----(file1 opwn in read mode)
step:16 print()


