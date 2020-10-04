#r convert normal string into raw string. without writing r befor file path it will give unicode error
file = open(r'C:\Users\sony\Desktop\hello.txt')

for i in file:
    print(i)
