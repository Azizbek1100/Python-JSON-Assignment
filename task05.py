import json

with open('students.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

print("20 yoshdan katta talabalar:")
for student in data:
    if student['age'] > 20:
        print(f"{student['name']} {student['surname']} - {student['age']} yosh")