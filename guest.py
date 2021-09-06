from models import get_all_books

def guest_panel():
    n = input("""
        Добро пожаловать на панель визитора
        1. Список книг
        2. Поиск книги
        3. Выход \n""")

    if n == "1":
        books = get_all_books()
        if books == None:
            print("Нет книг ")
        else:
            for i,j in enumerate(books):
                print(f"{i+1}. {j[1]} {j[2]} {j[3]} год. \n")
    elif n == "2":
        book_name = input("Введите название книги: ")
        books = get_all_books()
        if books == None:
            print("Нет книг ")
        else:
            for i,j in enumerate(books):
                if book_name in [str(k) for k in j]:
                    print(f"{i+1}. {j[1]} {j[2]} {j[3]} год. \n")
    if n == "3":
        print("Bye! ")
        exit()
