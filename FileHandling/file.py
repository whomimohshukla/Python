

# wirting the file

file=open("./data.txt","w")
file.write("This is the first line\n")
file.write("This is the second line\n")

file.close()


# // reading the file

file=open("./data.txt","r")
print(file.read())
