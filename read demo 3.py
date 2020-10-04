file1 = open(r"C:\Users\sony\Desktop\hello.txt","r+")

print("Output of Read function is ")
print(file1.read())
print()

# seek(n) takes the file handle to the nth
# bite from the beginning.
file1.seek(0)

print("Output of Readline function is ")
print(file1.readline())
print()

file1.seek(0)

# readlines function
print("Output of Readlines function is ")
print(file1.readlines())
print()