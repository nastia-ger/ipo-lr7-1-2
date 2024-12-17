import json # Импорт модуля для работы с JSON файлами.
number = str(input("Введите номер квалификации: ")) # Запрос ввода номера квалификации.
found = False
print("============== Найдено ==============")
with open('dump.json', encoding= 'utf-8') as file: # Открываем файл dump.json с кодировкой UTF-8.
    file_content = file.read()
    data = json.loads(file_content) # Загрузка содержимого JSON файла в переменную `data`.
    for skill in data: # Перебор всех элементов в загруженных данных (предположительно список словарей).
        if skill["model"] == "data.skill" and skill["fields"]["code"] == number:
            skill_code = skill["fields"]["code"]
            skill_title = skill["fields"]["title"]
            found = True
            # Проверяем, соответствует ли элемент определённым условиям:
            # 1. Ключ 'model' имеет значение 'data.skill'.
            # 2. Поле 'fields' содержит значение для указанного пользователем ключа `code`.
            for prof in data:
                if prof["model"] == "data.specialty":
                    if prof["fields"]["code"] in number:
                        prof_code = prof["fields"]["code"]
                        prof_title = prof["fields"]["title"]
                        prof_type = prof["fields"]["c_type"]
            break
if not  found: # Если ни одного подходящего результата не найдено, выводим соответствующее сообщение.
    print("============== Не найдено ==============")
else: # Если условия выполнены, выводим код и название квалификации.
    print(f"{prof_code} >> Специальность '{prof_title}', {prof_type}")
    print(f"{skill_code} >> Квалификация '{skill_title}'")
