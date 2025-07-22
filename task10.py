import json

with open('students.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

sorted_students = sorted(data, key=lambda x: x['age'])
for s in sorted_students:
    print(f"{s['name']} - {s['age']} yosh")