file1 = open("output.txt", "w")
name = input("Enter text to write to the file: ")
file1.write(name + "\n")
file1.close()

file1 = open("output.txt", "a")  # append mode
smit = input("Enter additional text to append : ")
file1.write(smit)
file1.close()

file1 = open("output.txt", "r")
reading_file = file1.read()
print(reading_file)
file1.close()

