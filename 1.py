import csv

class Book:

    books = []

    def __init__(self, path= "data.csv", id="none", title="none", genre="none", isbn="none", publisher="none", author="none"):   
        self.path = path
        self.id = id
        self.title = title
        self.genre = genre
        self.isbn = isbn
        self.publisher = publisher
        self.author = author
        
    def read_archive(self):
        try:
            with open(self.path, 'r') as file:
                data = csv.reader(file, delimiter=",")
                keys = next(data)
                for line in data:
                    row = zip(keys, line)
                    Book.books.append(dict(row))
            return Book.books
        except:
            print("Ingrese un formato de archivo adecuado (csv).\n")
            run_pogram()

    def list_books(self):
        if len(Book.books) != 0:
            print("Lista de Libros:\n")
            cont = 1
            for book in Book.books:
                book = book["Title"]
                print(f"{cont}) {book}")
                cont += 1
        else:
            print("Agrega mas libros.\n")

    def add_books(self):
        new_book = {}
        new_book["id"] = len(Book.books) + 1
        new_book["Title"] = self.title
        new_book["Genre"] = self.genre
        new_book["ISBN"] = self.isbn
        new_book["Publisher"] = self.publisher
        new_book["Author"] = self.author

        Book.books.append(new_book)
        return Book.books

    def delete_books(self):
        books = list(map(lambda x:x["Title"], Book.books))
        count = 1
        for book in books:
            print(f"{count}) {book}.")
            count += 1
        decision = input("¿Cual libro desea eliminar de la lista?\n"
              "Escoge su número de orden:\n")
        decision = int(decision)

        
        while not decision in range(1, len(books) + 1):
            decision = input(f"Ingresa un número del 1 al {len(books)}:\n")
        
        del Book.books[decision - 1]
        return Book.books
    
    def find_books_title(self):
        titles = list(map(lambda x:x["Title"], Book.books))
        ibns = list(map(lambda x: x["ISBN"], Book.books))
        def print_books(list, list_2):
            str = " Libros -> IBMS\n"
            for x, y in zip(list, list_2):
                str += f" {x} -> {y}.\n"
            return str
        title = input("Ingrese un titulo o ISBN de la siguiente lista:\n"
                     f"{print_books(titles, ibns)}")
        
        def verificar_title(title, books):
            for item in books:
                if title.lower() == item.lower():
                    return item
            return False

        try:
            find_title = list(filter(lambda x:x["Title"] == f"{verificar_title(title, titles)}" or x["ISBN"] == f"{verificar_title(title, ibns)}", Book.books))

            title = find_title[0]["Title"]
            gender = find_title[0]["Genre"]
            isbn = find_title[0]["ISBN"]
            publisher = find_title[0]["Publisher"]
            author = find_title[0]["Author"]

            print(f"Los datos del libro {title} son:\n"
                    f"Titulo: {title}\n"
                    f"Genero: {gender}\n"
                    f"ISBN: {isbn}\n"
                    f"Editorial: {publisher}\n"
                    f"Autor(es): {author}\n")
        except:
            print("El libro no fue encontrado, si gustas puedes agregarlo.")

    def order_books(self):
        if len(Book.books) != 0:
            decision = input("¿Desea ordenar los titulos de los libros por orden alfabetico? (Y/N)\n")
            while not decision.lower() in 'yn':
                decision = input("¿Desea ordenar los titulos de los libros por orden alfabetico?\n"
                             "Y(Si) o (N)No\n")
        if decision == 'y':
            titles = list(map(lambda x:x["Title"], Book.books))
            titles.sort()
            cont = 1
            for book in titles:
                print(f"{cont}) {book}")
                cont += 1
        else:
            run_pogram()

    def find_books_autor(self):
        authors = list(map(lambda x:x["Author"], Book.books))
        publishers = list(map(lambda x:x["Publisher"], Book.books))
        geners = list(map(lambda x:x["Genre"], Book.books))
        def print_books(list, list_2, list_3):
            str = " Autor(es) -> Genero -> Editorial\n"
            for x, y, z in zip(list, list_2, list_3):
                str += f" {x} -> {y} -> {z}.\n"
            return str
        title = input("Ingrese un nombre, genero o editorial de la siguiente lista:\n"
                    f"{print_books(authors, geners, publishers)}")
            
        def verificar_option(title, books):
            for item in books:
                if title.lower() == item.lower():
                    return item
            return False
        def verificar_author(author, books):
            for item in books:
                world = item.lower()
                if world.count(author.lower()):
                    return item
            return False
        try:
            find_title = list(filter(lambda x:x["Author"] == f"{verificar_author(title, authors)}" or
            x["Publisher"] == f"{verificar_option(title, publishers)}" or x["Genre"] == f"{verificar_option(title, geners)}", Book.books))

            title = find_title[0]["Title"]
            gender = find_title[0]["Genre"]
            isbn = find_title[0]["ISBN"]
            publisher = find_title[0]["Publisher"]
            author = find_title[0]["Author"]

            print(f"Los datos del libro {title} son:\n"
                    f"Titulo: {title}\n"
                    f"Genero: {gender}\n"
                    f"ISBN: {isbn}\n"
                    f"Editorial: {publisher}\n"
                    f"Autor(es): {author}\n")
        except:
            print("El libro no fue encontrado, si gustas puedes agregarlo.")
    
    def find_books_numbers_autors(self, num):
        authors = list(map(lambda x: x["Author"], Book.books))
        new_list = []
        list_authors = []
        for author in authors:
            author_v2 = author.split(",")
            if len(author_v2) == int(num):
                new_list.append(author_v2)

        for x in range(len(new_list)):
            var = ",".join(new_list[x])
            find_books_number_authors = next(filter(lambda x:x["Author"] == var, Book.books))
            list_authors.append(find_books_number_authors)

        books_filter = list(map(lambda x:x["Title"], list_authors))

        def print_author(list):
            count = 1
            str = ""
            for item in list:
                str += f"{count}) {item}.\n"
                count += 1
            return str
        print(f"Libros que tiene {num} autor(es):\n"
              f"{print_author(books_filter)}")

    def saved_books(self):
        filename = input("Ingrese el tipo de extension en el cual desea guardar toda la informacion sobre sus libros:\n"
                         "1) .txt\n"
                         "2) .csv\n")
        if filename == "1":
            filename = ".txt"
        else:
            filename = ".csv"
        with open(f"saved.{filename}", 'w') as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerows(Book.books)
            print(f"La informacion de sus libros fue guarda en saved{filename}. Gracias por usar mi pograma!")
    

if __name__ == "__main__":
    def run_pogram():
        print("Bievenido a mi pograma:")
        print("-"*10, "Menú", "-"*10)
        print("1) Leer archivo de disco duro (.txt o csv) que cargue 3 libros.\n"
              "2) Listar libros.\n"
              "3) Agregar libro.\n"
              "4) Eliminar libro.\n"
              "5) Buscar libro por ISBN o por título.\n"
              "6) Ordenar libros por título.\n"
              "7) Buscar libros por autor, editorial o género..\n"
              "8) Buscar libros por número de autores.\n"
              "9) Editar o actualizar datos de un libro (título, género, ISBN, editorial y autores).\n"
              "10) Guardar libros en archivo de disco duro (.txt o csv)")
        option = input("Ingrese una de estas opciones:\n")
        
        while not option in '12345678910':
            option = input("Ingrese el número de la opcion:\n")
        
        if option == "1":
            path = input("Ingrese el nombre del archivo:\n")
            my_class = Book(path)
            data = my_class.read_archive()
            for book in data:
                book = book['Title']
                print(f"El libro {book} fue añadido.")
            # my_class.continue_pogram()
            
        elif option == "2":
            my_class = Book()
            my_class.list_books()
            my_class.continue_pogram()
            
        elif option == "3":
            title = input("¿Cual es el nombre del libro?\n")
            genre = input("¿Que tipo de genero es?\n")
            isbn = input("¿Cual es su ISBN?\n")
            publisher = input("¿Cual es la editorial del libro?\n")
            author = input("¿Quien o Quienes son los autores? (Si es mas de un author separar por comas)\n")
            my_class = Book(title=title, genre=genre, isbn=isbn, publisher=publisher, author= author)
            print(my_class.add_books())
            my_class.continue_pogram()
            
        elif option == "4":
            my_class = Book()
            print(my_class.delete_books())
            my_class.continue_pogram()
        
        elif option == "5":
            my_class = Book()
            my_class.find_books_title()
            my_class.continue_pogram()

        elif option == "6":
            my_class = Book()
            my_class.order_books()
            my_class.continue_pogram()
            
        elif option == "7":
            my_class = Book()
            my_class.find_books_autor()
            my_class.continue_pogram()
            
        elif option == "8":
            num = input("Ingrese el número de autores:\n")
            my_class = Book()
            my_class.find_books_numbers_autors(num)
            my_class.continue_pogram()

        else:
            my_class = Book()
            my_class.saved_books()
            
    run_pogram()