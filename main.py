from pprint import pprint
import re
# читаем адресную книгу в формате CSV в список contacts_list
import csv
with open("phonebook_raw.csv") as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)
print(contacts_list)

# TODO 1: выполните пункты 1-3 ДЗ

# регулярки:
ptrn_phone = r"(\+7|8)\s*?\(*?(\d{3,3})\)*?\s*\-?(\d{3,3})\-?(\d{2,2})\-?(\d+)\.?\s?\.?(\(*?(\w+?\.?)\s(\d+)\)?)?"
rplc_phone = r"+7(\2)\3-\4-\5 \7\8"
# закончились регулярки

# убираем разнобой в ФИО, приводим телефоны к одному виду
rplc_data = []
for i in contacts_list:
    name = ' '.join(i[:3]).split(' ')
    phone = re.sub(ptrn_phone, rplc_phone, i[5])
    r_data = [name[0], name[1], name[2], i[3], i[4], phone, i[6]]
    rplc_data.append(r_data)

# pprint(rplc_data)

# убираем дубликаты
d = {}
for i in rplc_data:
    key = i[0] + i[1]  # объединяем 'lastname' и 'firstname' для формирования ключа
    if key not in d:
        d[key] = []
    d[key].append(i)

# объединяем дубликаты
merged_data = []
for key in d:
    if len(d[key]) == 1:
        merged_data.append(d[key][0])
    else:
        merged_record = d[key][0]
        for i in range(1, len(d[key])):
            for j in range(len(merged_record)):
                if merged_record[j] == '' and d[key][i][j] != '':
                    merged_record[j] = d[key][i][j]
            merged_record[5] = merged_record[5] + ', ' + d[key][i][5]
        merged_data.append(merged_record)

result = sorted(merged_data, key=lambda x: x[0])

# TODO 2: сохраните получившиеся данные в другой файл
with open("phonebook.csv", "w") as f:
  datawriter = csv.writer(f)
  datawriter.writerows(result)