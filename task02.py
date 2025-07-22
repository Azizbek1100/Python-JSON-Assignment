import json

with open('students.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

for student in data:
    print(f"{student['name']} - {student['age']} yosh")