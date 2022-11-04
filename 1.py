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
    run_pogram()