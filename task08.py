import json

with open('students.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

max_student = max(data, key=lambda x: x['age'])
print(f"Eng katta yoshli talaba: {max_student['name']} - {max_student['age']} yosh")