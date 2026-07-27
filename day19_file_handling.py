#write_mode
file = open("sample.txt","w")

file.write("Hello Ganesh!\n")
file.write("welcome to python file Handling.")

file.close()

print("Data Written Successfully!")

#read_mode
file = open("sample.txt","r")
content = file.read()
print(content)
file.close()

#append_mode
file = open("sample.txt","a")
file.write("\nThis line was added using append mode.")
file.close()
print("Data appended successfully")

#readline
file = open("student.txt","r")
print(file.readline())
print(file.readline())
file.close()

#open
with open("student.txt","r") as file:
    content = file.read()
    print(content)
