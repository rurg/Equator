from typing import Dict

documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"},
    {"type": "Electronic COVID-19 Key", "number": "666"}
]
directories = {
    '1': ['2207 876234', '11-2'],
    '2': ['10006'],
    '3': ['666'],
    '4': []
}

#Вывод именов все владельцев документов и проверка наличия поля "name"
def exception():
    docs = documents
    try:
        for i in docs:
            print(f'"{i["name"]}"')
    except KeyError:
        print('Поле имени отсутствует')


# Вывод списка в виде списка определенного формата :)
def listed():
    docs = documents
    for i in docs:
        print(f'{i["type"]} "{i["number"]}" "{i["name"]}"')

def shelf(input_docnumber):
    # определение номера полки по номеру докумен
    global shelf_number_info #переменная,которую я непременно использую вовне функции
    for shelf_number, doc_number in directories.items():
        if input_docnumber in list(doc_number):
            print(f'Это лежит на {shelf_number} - й полке')
            shelf_number_info = shelf_number

# for elem in a:
#    print(elem, end=' ')
def add_doc():
    type_new,number_new,name_new = map(str, input('Введите данные через запятую: ').split(','))
    while True:
        shelf_new = input('Введите номер полки, куда положить документ')
        if shelf_new not in directories:
            print ('Такой полки не существует')
        else:
            break
    documents.append({"type": type_new, "number": number_new, "name": name_new})
    list_for_append = (directories[shelf_new]).append(number_new)
    print('Документы теперь выглядят так:', documents)
    print('ПОлки теперь выглядят так', directories)


def i_d_like_to_move_it(number_to_move):
    shelf(number_to_move)
    while True:
        shelf_move_to = input('Введите номер полки, на которую перекинуть: ')
        if shelf_move_to not in directories:
            print ('Такой полки не существует')
        else:
            break
    #list_for_append = (directories[shelf_move_to]).append(number_to_move)
    directories[shelf_move_to].append(number_to_move)
    directories[shelf_number_info].remove(number_to_move)
    print('выглядит это теперь так: ', directories)

#i_d_like_to_move_it('11-2')



# print(list(documents.values())[1])
# list(documents.values())[-1]


# my_dict = {'key': 'value'}
# key_exists = my_dict.has_key('key')  # Устаревший способ.
# key_exists = 'key' in my_dict  # Актуальный способ.

def is_it_doc_exist(input_docnumber):
    #    nonlocal input_docnumber
    for document in documents:
        if document['number'] == input_docnumber:
            return True
        else:
            number_not_exist = True
    if number_not_exist:
        return False


def people(input_docnumber):
    #   print(input_number) Функция вывода ФИО по номер документа

    for document in documents:
        if document['number'] == input_docnumber:
            print(document['name'])


def command_menu():  # обработчик команд
    while True:
        user_input = input('Введи команду: ')
        if user_input.lower() == 'p':
            user_input_number = input('Введи номер документа: ')
            if is_it_doc_exist(user_input_number) == False:
                print('такого документа нет')
            else:
                people(user_input_number)
        # ввод команды для обработки определения полки по номеру документа
        if user_input == 's':
            user_input_number = input('Введи номер документа: ')
            if is_it_doc_exist(user_input_number) == False:
                print('такого документа нет')
            else:
                #                user_shelf = input('Введи номер полки,куда поставить твое барахло: ')
                shelf(user_input_number)
        #отработка перемещений между полками(по номеру документа  - откуда и указать куда)
        if user_input.lower() == 'm':
            user_input_number = input('Введи номер документа: ')
            if is_it_doc_exist(user_input_number) == False:
                print('такого документа нет')
            else:
                i_d_like_to_move_it(user_input_number)
        if user_input == 'l':  # команда на вывод списка документов
            listed()
        if user_input == 'a':  # команда на добавление документов
            add_doc()
        if user_input == 'x':  # команда на добавление документов
            exception()
        elif user_input == 'q':
            print('bye')
            break

try:
    command_menu()
except KeyError:
    print('Имечко для последнего документа отсутствуююет')