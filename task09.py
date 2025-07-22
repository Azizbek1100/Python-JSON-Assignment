import json

with open('students.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

print(f"Talabalar soni: {len(data)} ta")