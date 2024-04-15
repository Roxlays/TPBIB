import json

class Book:
    def __init__(self, nom, tag, image):
        self.__nom = nom
        self.__tag = tag
        self.__image = image

    def __str__(self) -> str:
        return f"Book : {self.__nom} de type {self.__tag}"
    
    @property
    def nom (self):
        return self.__nom
    
    @property
    def tag (self):
        return self.__tag
    
    @property
    def image (self):
        return self.__image

    def default(self, obj):
        if isinstance(obj, Book):
            return{
                'nom': obj.nom,
                'tag': obj.tag,
                'image': obj.image
            }
        return super().default(obj)
    


class Library:
    def __init__(self):
        self.__books = []

    def display_books(self):
        for i in self.__books:
            print(i)

    def add_book(self, book):
        self.__books.append(book)

    def remove_book(self, nom):
        for book in self.__books:
            if (book.nom == nom):
                self.__books.remove(book)

    def save(self):
        pass

        
if __name__ == '__main__':
    lib = Library()
    lib.display_books()
    lib.add_book(Book('fondation', 'sf', 'path/to/image'))
    lib.add_book(Book('test', 'sf', 'test/test' ))
    lib.display_books()
    lib.remove_book('fondation')
    lib.display_books()

        

