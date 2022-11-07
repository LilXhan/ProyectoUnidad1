import csv

class Book:

    books = []

    def __init__(self, id="none", title="none", genre="none", isbn="none", publisher="none", author="none"):   
        self.id = id
        self.title = title
        self.genre = genre
        self.isbn = isbn
        self.publisher = publisher
        self.author = author
        
    def print_books_info(self, title, gender, isbn, publisher, author):
        print(f"Los datos del libro {title} son:\n"
                f"Titulo: {title}\n"
                f"Genero: {gender}\n"
                f"ISBN: {isbn}\n"
                f"Editorial: {publisher}\n"
                f"Autor(es): {author}\n")

    def print_books(self, names):
        count = 1
        str_book = ""
        for book in names:
            str_book += f"{count}) {book}.\n"
            count += 1
        return str_book

    def asnwer_add(self, func):
        print(f"No tienes ningun libro para {func}.")
        opcion = input("¿Desea agregar un libro? (Y / N)\n")

        while not opcion.lower() in ("y", "n"):
            opcion = input("Y o N.\n")

        if opcion.lower() == 'y':
            my_class = Book()
            my_class.add_books()
        else:
            my_class = Book()
            my_class.continue_pogram()  

    def read_archive(self):
        try:
            path = input("Ingrese el nombre del archivo en formato csv o txt:\n")
            with open(path, 'r') as file:
                data = csv.reader(file, delimiter=",")
                keys = next(data)
                if len(keys) != 6:
                    print(0/0)
                for line in data:
                    if len(line) != 6:
                        print(0/0)
                    row = zip(keys, line)
                    row = dict(row)
                    Book.books.append(row)
                for book in Book.books:
                    book = book["Title"]
                    print(f"El libro {book} fue agregado con exito!")
        except:
            print('Ups! El formato que mando no parece el adecuado asegurese de ingresar un formato parecido al de "example.csv"\n'
            'que se encuentra en la misma carpeta de este repositorio de github. Tambien asegurese que contenga\n'
            'la misma relacion de datos escritos dentro del archivo que desee insertar.\n')
            book_class = Book()
            book_class.continue_pogram()

    def list_books(self):
        if len(Book.books) != 0:
            #books_list = list(map(lambda x:x["Title"], Book.books))
            #my_class = Book()
            count = 1
            print(f"Los libros que tienes guardado son {len(Book.books)}:")
            for book in Book.books:
                print(f"{count}° libro:")
                my_class = Book()
                my_class.print_books_info(book["Title"], book["Genre"], book["ISBN"], book["Publisher"], book["Author"])
                count += 1
        else:
            my_class = Book()
            my_class.asnwer_add("listar")

    def add_books(self):
        title = input("¿Cual es el nombre del libro?\n")
        genre = input("¿Que tipo de genero es?\n")
        isbn = input("¿Cual es su ISBN?\n")
        publisher = input("¿Cual es la editorial del libro?\n")
        author = input("¿Quien o Quienes son los autores? (Si es mas de un author separar por comas)\n")
        new_book = {}
        new_book["id"] = len(Book.books) + 1
        new_book["Title"] = title
        new_book["Genre"] = genre
        new_book["ISBN"] = isbn
        new_book["Publisher"] = publisher
        new_book["Author"] = author

        book_actual = new_book["Title"]

        Book.books.append(new_book)
        print(f"¡El libro {book_actual} fue agregado con exito!")
        return Book.books

    def delete_books(self):
        if len(Book.books) == 0:
            my_class = Book()
            my_class.asnwer_add("eliminar")
        else:
            books = list(map(lambda x:x["Title"], Book.books))
            
            my_class = Book()

            decision = input("¿Cual libro desea eliminar de la lista? Escoge su número de orden:\n"
                             f"{my_class.print_books(books)}")
            
            list_book = [str(i) for i in range(1, len(books) + 1)]
            while not decision in list_book:
                decision = input(f"Ingresa un número del 1 al {len(books)}:\n")
            
            decision = int(decision)
            print(f"El libro {books[decision - 1]} fue eliminado con exito")
            del Book.books[decision - 1]
            return Book.books
    
    def find_books_title(self):
        if len(Book.books) == 0:
            my_class = Book()
            my_class.asnwer_add("buscar")
        else:
            titles = list(map(lambda x:x["Title"], Book.books))
            ibns = list(map(lambda x: x["ISBN"], Book.books))
            def print_books(list, list_2):
                str = " Libros -> IBNS\n"
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

                my_class = Book()
                my_class.print_books_info(title, gender, isbn, publisher, author)

            except:
                my_class = Book()
                my_class.asnwer_add("buscar con ese nombre")

    def order_books(self):
        if len(Book.books) == 0:
            my_class = Book()
            my_class.asnwer_add("ordenar")
        else:
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
                my_class = Book()
                my_class.continue_pogram()

    def find_books_autor(self):
        if len(Book.books) == 0:
            my_class = Book()
            my_class.asnwer_add("buscar")
        else:
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

                my_class = Book()
                my_class.print_books_info(title, gender, isbn, publisher, author)
            except:
                my_class = Book()
                my_class.asnwer_add("buscar con ese nombre")
    
    def find_books_numbers_autors(self):
        if len(Book.books) == 0:
            my_class = Book()
            my_class.asnwer_add("buscar")
        else:
            try:
                num = input("Ingrese el número de autores:\n")
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

                my_class = Book()
                print(f"Libros que tiene {num} autor(es):\n"
                    f"{my_class.print_books(books_filter)}")
            except:
                print("No hay ningun libro con esa cantidad de autores")
    
    def update_books(self):
        if len(Book.books) == 0:
            my_class = Book()
            my_class.asnwer_add("actualizar")
        else:
            books = list(map(lambda x:x["Title"], Book.books))          
            my_class = Book()

            decision = input(f"Elige uno de estos libros para editar su información:\n"
            f"{my_class.print_books(books)}")

            number_books = [str(i) for i in range(len(books) + 1)]

            while not decision in number_books:
                decision = input(f"Elige uno de estos libros para editar su información:\n"
                f"{my_class.print_books(books)}")  

            decision = int(decision)

            book_edit = list(filter(lambda x:x["Title"] == books[decision - 1], Book.books))
               
            book_name = book_edit[0]["Title"]

            edit = input(f"¿Del libro {book_name} que desea editar?\n"
                            "1) Titulo. \n"
                            "2) Genero.\n"
                            "3) ISBN.\n"
                            "4) Editorial.\n"
                            "5) Autor(es).\n"
                            "Escoja una opcion del 1 al 5:\n")            
            options = [str(i) for i in range(6)]
            while not edit in options:
                        edit = input("Escoja una opcion del 1 al 5:\n")

            count = 0
            for book in Book.books:
                if book["Title"] == book_name:
                    break
                count += 1

            def edit_sel(edit_name, name):
                Book.books[count][edit_name] = input(f"¿El {name} de {book_name} por cual desea cambiarlo?\n")
                new_name = Book.books[count][edit_name]
                # agregar cargando
                return f"¡El {name} del libro {book_name} fue cambiado por {new_name} con exito!"

            if edit == "1":
                print(edit_sel("Title", "titulo"))
            elif edit == "2":
                print(edit_sel("Genre", "genero"))
            elif edit == "3":
                print(edit_sel("ISBN", "ISBN"))
            elif edit == "4":
                print(edit_sel("Publisher", "publicador o la editorial"))
            else:
                author_book = Book.books[count]["Author"] 
                Book.books[count]["Author"] = input(f"Autor(es) de este libro: {author_book} ¿Por cuales deseas cambiarlos?\n"
                                                            "Si es mas de 1 autor, ingresa los nombres separados por coma.\n")
                #agregar cargando
                print(f"Autor(es) del libro {book_name} fue o fueron cambiados con exito!")
                

    def saved_books(self):
        if len(Book.books) == 0:
            my_class = Book()
            my_class.asnwer_add("guardar")
        else:
                filename = input("Ingrese el tipo de extension en el cual desea guardar toda la informacion sobre sus libros:\n"
                                "1) .txt\n"
                                "2) .csv\n")
                
                while not filename in ("1", "2"):
                    filename = input("Ingrese el tipo de extension en el cual desea guardar toda la informacion sobre sus libros:\n"
                                "1) .txt\n"
                                "2) .csv\n"
                                "Escoja entre 1 o 2:\n")

                if filename == "1":
                    filename = ".txt"
                else:
                    filename = ".csv"
                with open(f"saved.{filename}", 'w') as csvfile:
                    csvwriter = csv.writer(csvfile)
                    csvwriter.writerow(Book.books)
                    list = []
                    for book in Book.books:
                        list.append(book.values())
                    csvwriter.writerows(list)
                    print(f"La informacion de sus libros fue guarda en saved{filename}, Gracias por usar mi pograma!")
       
    def continue_pogram(self):
        decision = input("¿Desea continuar el pograma? (Y/N)\n")
        decision = decision.lower()
        while not decision in "yn":
            decision = input("Y(Si) o N(No)\n")
        if decision == 'y':
            run_pogram()
        else:
            saved = input("¿Deseas guardar la informacion de tus libros? (Y/N)\n")
            while not saved.lower() in 'yn':
                saved = input("Ingrese una consonante: Y(Si) o N(No)\n")
            if saved == 'y' and len(Book.books) > 0:
                my_class = Book() 
                my_class.saved_books()
            elif saved == 'n':
                print("Espero que te haya gustado mi pograma.")
                exit()
            else:
                print("No tiene ningun libro para guardar.")
                exit()
    
if __name__ == "__main__":
    def run_pogram():
        print("Bienvenido a mi pograma:")
        print("-"*30, "Menú", "-"*30)
        print("1) Leer archivo de disco duro (.txt o csv) que cargue 3 libros.\n"
              "2) Listar libros.\n"
              "3) Agregar libro.\n"
              "4) Eliminar libro.\n"
              "5) Buscar libro por ISBN o por título.\n"
              "6) Ordenar libros por título.\n"
              "7) Buscar libros por autor, editorial o género..\n"
              "8) Buscar libros por número de autores.\n"
              "9) Editar o actualizar datos de un libro (título, género, ISBN, editorial y autores).\n"
              "10) Guardar libros en archivo de disco duro (.txt o csv)\n"
              "11) Salir.")
        option = input("Ingrese una de estas opciones:\n")
        
        list_num = [str(i) for i in range(1, 12)]

        while not option in list_num:
            option = input("Ingrese el número de la opcion entre 1 y 11:\n")
            
        if option == "1":
            my_class = Book()
            my_class.read_archive()
            my_class.continue_pogram()
                
        elif option == "2":
            my_class = Book()
            my_class.list_books()
            my_class.continue_pogram()
                
        elif option == "3":
            my_class = Book()
            my_class.add_books()
            my_class.continue_pogram()
                
        elif option == "4":
            my_class = Book()
            my_class.delete_books()
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
            my_class = Book()
            my_class.find_books_numbers_autors()
            my_class.continue_pogram()

        elif option == "9":
            my_class = Book()
            my_class.update_books()
            my_class.continue_pogram()

        elif option == "10":
            my_class = Book()
            my_class.saved_books()
            my_class.continue_pogram()
        
        else:
            print("Espero que te haya gustado mi programa.")
            exit()
            
    run_pogram()