from datetime import datetime
from service import ui_1, ui_2


print("---------------------------------------------------------------------------------------------------------------\n")
print("Вітаю! Ви можете ввести країну та дату - і дізнатися всю інформацію щодо погоди, яка міститься в цій базі даних")
print("\n---------------------------------------------------------------------------------------------------------------\n")

while True:
    country = input("Введіть країну: ").strip()
    if country == "": 
        continue
    if " " in country:  
        country = country.title()
    else:
        country = country.capitalize()
    break

while True:
    date_input = input("Введіть дату у форматі рік-місяць-день: ").strip()
    try:
        date_d = datetime.strptime(date_input, "%Y-%m-%d")   
        break  
    except ValueError:
        print("Помилка, Ви ввели дату не в правильному форматі")

print("\n---------------------------------------------------------------------------------------------------------------\n")
print(f"Ви ввели країну: {country}")
print(f"Ви ввели дату: {date_d.date()}") 
print("\n---------------------------------------------------------------------------------------------------------------\n")


columns_name = ui_1(country, date_d)
if columns_name:
    print(columns_name[0], "|", columns_name[1], "|", columns_name[2], "|", columns_name[3], "|", columns_name[4], "|", columns_name[5], "|", columns_name[6], "|", columns_name[7], "|", columns_name[8], "|", columns_name[9], "|\n\n")

data = ui_2(country, date_d)
if data:
    for i in data:
        print(i[0], "|", i[1], "|", i[2], "|", i[3], "|", i[4], "|", i[5], "|", i[6], "|", i[7], "|", i[8], "|", i[9], "|\n")
else:
    print("Даних для такої країни немає")

print("\n---------------------------------------------------------------------------------------------------------------\n")