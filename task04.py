import json

name = input("Ismingiz: ")
surname = input("Familiyangiz: ")
age = int(input("Yoshingiz: "))

new_student = {"name": name, "surname": surname, "age": age}

with open('students.json', 'r+', encoding='utf-8') as file:
    data = json.load(file)
    data.append(new_student)
    file.seek(0)
    json.dump(data, file, ensure_ascii=False, indent=4)

print("Foydalanuvchidan olingan ma’lumot yozildi:")
print(f"{name} {surname} - {age} yosh")
