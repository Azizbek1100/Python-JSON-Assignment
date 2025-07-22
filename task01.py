import json

students = [
    {"name": "Ali", "surname": "Valiyev", "age": 20},
    {"name": "Laylo", "surname": "Karimova", "age": 21},
    {"name": "Bekzod", "surname": "Xolmatov", "age": 19}
]

with open('students.json', 'w', encoding='utf-8') as file:
    json.dump(students, file, ensure_ascii=False, indent=4)

print("Ma’lumotlar students.json fayliga yozildi:")
for s in students:
    print(f"{s['name']} {s['surname']} - {s['age']} yosh")