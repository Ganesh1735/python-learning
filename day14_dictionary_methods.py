student = {
    "name":"Ganesh",
    "age":25,
    "city":"Nashik"
}
print(student)
print(student.keys())
print(student.values())
print(student.items())
print(student.get("name"))
print(student.get("age"))
student.update({"age":26})
student.update({"college":"SPPU"})
print(student)