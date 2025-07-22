import json
import csv

with open('students.json', 'r', encoding='utf-8') as json_file:
    data = json.load(json_file)

with open('students.csv', 'w', newline='', encoding='utf-8') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(['Ism', 'Familiya', 'Yosh'])
    for student in data:
        writer.writerow([student['name'], student['surname'], student['age']])

print("Ma’lumotlar CSV formatga o‘tkazildi va students.csv fayliga yozildi.")
