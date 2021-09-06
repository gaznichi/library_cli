from models import insert_book, delete_book, update_book, get_book
def admin_panel():
    print("""
        1. Создать Книгу
        2. Удалить Книгу
        3. Изменить Книгу
        4. Выйти
    """)
    choice = input("Выберите пункт меню: ")
    if choice == "1":
        title = input("введите название книги ")
        author = input("введите автора книги ")
        year = input("введите год издания ")
        result = insert_book(title, author, year)

        if result == True:
            print(f"Книга {title} успешно добавлена ")
        else:
            print(f"Книга {title} не добавлена, произошла какаято ошибка ")
    
    elif choice == "2":
        title = input("введите название книги ")
        result = delete_book(title)
        if result == True:
            print(f"Книга {title} успешно удалена ")
        else:
            print(f"Книга {title} не удалена, произошла какаято ошибка ")
    
    elif choice == "3":
        title = input("введите название книги ")
        n = get_book(title)
        if n == None:
            print(f"Книга {title} не найдена ")
        else:
            _id,_title, _author, _year = n
            title = input(f"введите новое название книги ({_title}) ")
            if title == '':
                title = _title
            year = input(f"введите новый год издания ({_year}) ")
            if year == '':
                year = _year
            author = input(f"введите нового автора ({_author}) ")
            if author == '':
                author = _author
            result = update_book(_title,title, author, year)
            if result == True:
                print(f"Книга {title} успешно изменена ")
            else:
                print(f"Книга {title} не изменена, произошла какаято ошибка ")
    elif choice == "4":
        print("Bye! ")
        exit()
    
    admin_panel()

    
