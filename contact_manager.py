import csv
from tabulate import tabulate


def add_contact(data: list[str]) -> None:
    """
    Записывает данные о контакте в CSV-файл.

    Возвращает: None
    """
    with open('contacts.csv', 'a', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        # Если телефонная книга не имеет ни одной записи
        if csvfile.tell() == 0:
            writer.writerow(
                ['Фамилия', 'Имя', 'Отчество', 'Название организации', 'Рабочий телефон', 'Сотовый телефон'])
        writer.writerows(data)


def read_contact() -> list[list]:
    """
    Считывает данные из CSV-файла и возвращает список со вложенными списками, которые представляют контакты.

    Возвращает: Контакты в виде списка со вложенными списками, 3 контакта на одной странице.
    """
    with open('contacts.csv', 'r') as csvfile:
        reader = csv.reader(csvfile)
        contacts = [row for row in reader]
        if not contacts:
            print('Телефонная книга пустая.')
        return contacts


def search_contact(keyword: str):
    """
    Ищет контакты в CSV-файле по заданному ключевому слову и выводит соответствующие результаты.

    Возвращает: список/списки с информацией о искомых контактах.
    """
    found_results = False
    found_contacts = []

    with open('contacts.csv', 'r', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if keyword in row:
                found_contacts.append(row)
                found_results = True

    if found_results:
        print(tabulate(found_contacts, headers="firstrow", tablefmt="grid"))
    else:
        print('Записи с таким ключом нет, попробуйте снова.')


def edit_contact(contact_index: int, new_data: list[str]) -> None:
    """
    Редактирует контакт в CSV-файле по указанному индексу.

    Возвращает: None
    """
    contacts = read_contact()
    if 0 <= contact_index < len(contacts):
        contacts[contact_index] = new_data
        with open('contacts.csv', 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerows(contacts)
        print('Запись успешно обновлена.')
    else:
        print('Неверный индекс контакта.')


def delete_contact(contact_index: int) -> None:
    """
    Удаляет контакт из CSV-файла по указанному индексу.

    Возвращает: None
    """
    contacts = read_contact()
    if 0 <= contact_index < len(contacts):
        deleted_contact = contacts.pop(contact_index)
        with open('contacts.csv', 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerows(contacts)
        print(f'Контакт {deleted_contact} успешно удалён.')
    else:
        print('Неверный индекс контакта.')
