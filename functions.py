def show_data() -> None:
    """Выводит информацию из справочника"""
    with open ('HWSEM8\\book.txt', 'r', encoding='utf-8') as file:
        for i, v in enumerate(file, start=1):
            print(f'{i}. {v}')
        print('\n')


def add_data() -> None:
    """Добавляет информацию в справочник."""
    fio = input('FIO: ')
    ph_numb = input('ph_numb: ')
    with open ('HWSEM8\\book.txt', 'a', encoding='utf-8') as file:
        file.write(f'\n{fio} | {ph_numb}')


def find_data() -> None:
    """Печатает результат поиска по справочнику."""
    with open ('HWSEM8\\book.txt', 'r', encoding='utf-8') as file:
        data = file.read()
    contact_to_find = input('Введите то, что хотите найти: ')
    result = search(data, contact_to_find)
    print(result)


def search(book: str, info: str) -> list[str]:
    """Находит в списке записи по определенному критерию поиска"""
    book = book.split('\n')
    return list(filter(lambda contact: info.lower() in contact.lower(), book))


def change_data(num):
    """Изменяет данные"""
    new_fio = input('Введите новое ФИО: ')
    new_ph = input('Введите новый номер: ')
    with open ('HWSEM8\\book.txt', 'r', encoding='utf-8') as file:
        line = file.readlines()
    with open('HWSEM8\\book.txt', 'w', encoding='utf8' ) as file:
        x = line[num]
        for lin in line:
            if  x != lin:
                file.write(lin)
            else:
                file.write(new_fio + ' | ' + new_ph )



def del_data(num) -> list[str]:
    """Удаляет данные"""
    with open ('HWSEM8\\book.txt', 'r', encoding='utf-8') as file:
        line = file.readlines()
    with open ('HWSEM8\\book.txt', 'w', encoding='utf-8') as file:
        x = line[num]
        for lin in line:
            if x != lin:
                file.write(lin)
