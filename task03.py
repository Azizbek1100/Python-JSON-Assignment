import json

new_student = {"name": "Shahzoda", "surname": "Nazarova", "age": 22}

with open('students.json', 'r+', encoding='utf-8') as file:
    data = json.load(file)
    data.append(new_student)
    file.seek(0)
    json.dump(data, file, ensure_ascii=False, indent=4)

print("Yangi talaba qo‘shildi:")
print(f"{new_student['name']} {new_student['surname']} - {new_student['age']} yosh")
