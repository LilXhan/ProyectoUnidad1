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
            
    run_pogram()