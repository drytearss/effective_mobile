from contact_manager import add_contact, read_contact, search_contact, delete_contact, edit_contact
from tabulate import tabulate

if __name__ == '__main__':
    choice = input('Выберите действие:\n'
                   '1. Добавить контакт\n'
                   '2. Посмотреть телефонную книгу\n'
                   '3. Найти контакт\n'
                   '4. Редактировать контакт\n'
                   '5. Удалить контакт\n')

    if choice == '1':
        data = []
        fields = ['фамилию', 'имя', 'отчество', 'название организации', 'рабочий телефон', 'сотовый телефон']

        while True:
            contact = [input(f'Введите {field}: ') for field in fields]
            data.append(contact)
            answer = input('Хотите добавить еще одного пользователя? (y/n): ')
            if answer.lower() != 'y':
                print('Пользователь успешно добавлен!')
                break

        add_contact(data)

    elif choice == '2':
        contacts = read_contact()
        page_size = 3
        page_number = 1

        def display_page(page_data):
            table_data = []
            table_data.extend(page_data)
            print(tabulate(table_data, headers="firstrow", tablefmt="grid"))

        while True:
            start_index = (page_number - 1) * page_size
            end_index = start_index + page_size
            current_page = contacts[start_index:end_index]
            display_page(current_page)
            answer = input('Введите номер страницы для перехода (q - выход): ')
            if answer == 'q':
                break

            elif answer.isdigit():
                new_page_number = int(answer)
                max_page_number = len(contacts) // page_size + 1
                if 1 <= new_page_number <= max_page_number:
                    page_number = new_page_number
                else:
                    print('Неверный номер страницы.')

    elif choice == '3':
        keyword = input('Введите ключевое слово для поиска: ')
        search_contact(keyword)

    elif choice == '4':
        contacts = read_contact()
        for idx, contact in enumerate(contacts):
            print(f'Индекс: {idx}, Контакт: {contact}')
        index_to_edit = int(input('Введите индекс контакта, который вы хотите отредактировать: '))
        if 0 <= index_to_edit < len(contacts):
            new_data = []
            for field in contacts[index_to_edit]:
                new_value = input(f'Введите новое значение для {field}: ')
                new_data.append(new_value)
            edit_contact(index_to_edit, new_data)
        else:
            print('Неверный индекс контакта.')

    elif choice == '5':
        contacts = read_contact()
        for idx, contact in enumerate(contacts):
            print(f'Индекс: {idx}, Контакт: {contact}')
        index_to_delete = int(input('Введите индекс контакта, который вы хотите удалить: '))
        if 0 <= index_to_delete < len(contacts):
            delete_contact(index_to_delete)
        else:
            print('Неверный индекс контакта.')

    else:
        print('Неверный выбор.')