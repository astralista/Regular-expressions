import re
from pprint import pprint
# читаем адресную книгу в формате CSV в список contacts_list
import csv
with open("phonebook_raw.csv") as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)
pprint(contacts_list)

# TODO 1: выполните пункты 1-3 ДЗ

# С телефонами разобрался:
pattern_phone = r"(\+7|8)\s*?\(*?(\d{3,3})\)*?\s*\-?(\d{3,3})\-?(\d{2,2})\-?(\d+)\.?\s?\.?(\(*?(\w+?\.?)\s(\d+)\)?)?"
replace = r"+7(\2)\3-\4-\5 \7\8"

# TODO 2: сохраните получившиеся данные в другой файл
# код для записи файла в формате CSV
with open("phonebook.csv", "w") as f:
  datawriter = csv.writer(f, delimiter=',')
  # Вместо contacts_list подставьте свой список
  datawriter.writerows(contacts_list)