# Open function to open the file "myfile.txt"
# (same directory) in append mode and store
# it's reference in the variable file1
#append insert text at the end of the file
file1 = open(r"C:\Users\sony\Desktop\hello.txt", "a")

# Writing to file
file1.write("\nWriting to file :) unlock 3 covid bhai ,19 ")

# Closing file
file1.close()