from module1 import*

strany={"Эстония": "Таллин", "Австрия": "Вена", "Бельгия": "Брюссель", "Германия": "Берлин", "Лихтенштейн": "Вадуц", "Нидерладны": "Амстердам",  
           "Франция": "Париж", "Болгария": "София", "Польша": "Варшава", "Чехия": "Прага", "Албания": "Тирана", "Босния и Герцеговина": "Сараево",
           "Северная Македония": "Скопье", "Сербия": "Белград"}
print(strany)
while True:
    print("uznatstolicy - Узнать столицу,\nadd - Добавить страну в список,\nchange - Изменить страну или столицу в списке,\ntest - ТЕСТ")
    typing=input()
    if typing.lower=="uznatstolicy":
        v=input("Страна по стoлице(1) или стoлицу по стране(2)?")
        goroda(strany,v)
    elif typing.lower=="add":
        addstrana(strany)