file1=open(r"C:\Users\sony\Desktop\hello.txt","w")
l=["hello \n","how are u\n", "covid'19"]
s="\ni m bhoomi"

# Writing a string to file
file1.write(s)

# Writing multiple strings
# at a time
file1.writelines(l)

# Closing file
file1.close()
