file=open("example.txt","w")
file.write("hello AMAN! how are you ")

file=open("example.txt","r")
con = file.read()
print(con)
file.close()
