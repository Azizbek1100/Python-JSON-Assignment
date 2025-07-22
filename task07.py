import json

with open('students.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

average_age = sum(s['age'] for s in data) / len(data)
print(f"O‘rtacha yosh: {average_age:.1f}")