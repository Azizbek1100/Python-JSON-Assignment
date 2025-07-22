import os

if not os.path.exists('students.json'):
    with open('students.json', 'w', encoding='utf-8') as file:
        json.dump([], file, ensure_ascii=False, indent=4)

    print("❗️students.json fayli topilmadi — yangi bo‘sh fayl yaratildi.")
else:
    print("✅ students.json fayli mavjud — hech qanday o‘zgarish kiritilmadi.")
