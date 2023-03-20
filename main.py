import re
from pprint import pprint
# читаем адресную книгу в формате CSV в список contacts_list
import csv
with open("phonebook_raw.csv") as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)
# print(contacts_list)

# TODO 1: выполните пункты 1-3 ДЗ

new_text = []

# С ФИО разобрался
ptrn_name = r"^([а-яёА-ЯЁ]+)\S?\s?([а-яёА-ЯЁ]+)\S?\s?([а-яёА-ЯЁ]+)?"
rplc_name = r"\1,\2,\3"

for i in contacts_list:
    print(str(i))
    sub = re.sub(ptrn_name, rplc_name, str(i))
    # print(sub)
    new_text.append(sub)

pprint(new_text)


# С телефонами разобрался:
ptrn_phone = r"(\+7|8)\s*?\(*?(\d{3,3})\)*?\s*\-?(\d{3,3})\-?(\d{2,2})\-?(\d+)\.?\s?\.?(\(*?(\w+?\.?)\s(\d+)\)?)?"
rplc_phone = r"+7(\2)\3-\4-\5 \7\8"
# меняем формат телефона
# for i in contacts_list:
#     print(str(i))
#     sub = re.sub(ptrn_phone, rplc_phone, str(i))
#     print(sub)
#     new_text.append(sub)


# TODO 2: сохраните получившиеся данные в другой файл
# код для записи файла в формате CSV
with open("AAAAAA.csv", "w") as f:
  datawriter = csv.writer(f)
  # Вместо contacts_list подставьте свой список
  datawriter.writerows(new_text)