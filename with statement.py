L = ["This is Delhi \n", "This is Paris \n", "This is London \n"]

# Writing to file
with open(r"C:\Users\sony\Desktop\hello.txt", "w") as file1:
    # Writing data to a file
    file1.write("Hello \n")
    file1.writelines(L)

# Reading from file
with open(r"C:\Users\sony\Desktop\hello.txt", "r+") as file1:
    # Reading form a file
    print(file1.read())