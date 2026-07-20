student = {
    "name":"Ganesh",
    "age":25,
    "city":"Nashik"
}
print(student)

print(student["name"])
print(student["age"])
print(student["city"])

student["city"]="Pune"
print(student)
print(student["city"])


student["course"]="Python"
print(student)
print(student["course"])

del student["age"]
print(student)
