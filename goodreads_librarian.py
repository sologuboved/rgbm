from basic_operations import *
from global_vars import *


class Librarian(object):
    def __init__(self, books_json):
        self.books_json = books_json
        self.to_read = list()
        self.collect_books()

    def __str__(self):
        string = ''
        ind = 1
        for book in self.to_read:
            string += "%d\nauthor: %s\ntitle: %s\n, %s\n\n" % (ind, book[AUTHOR], book[TITLE], book[ABBREV])
            ind += 1
        return string

    def collect_books(self):
        all_books = load_json(self.books_json)
        for book in all_books:
            if TO_READ_SHELF in book[SHELVES]:
                self.to_read.append({AUTHOR: book[AUTHOR], TITLE: book[TITLE], ABBREV: book[AUTHOR].split(',')[0]})

    def find_namesakes(self):
        names = dict()
        for book in self.to_read:
            name = book[ABBREV]
            books_by = names.get(name, list())
            books_by.append((book[AUTHOR], book[TITLE]))
            names[name] = books_by
        for name in names:
            books_by = names[name]
            if len(books_by) > 1:
                print(name)
                print()
                for book in books_by:
                    author, title = book
                    print(author)
                    print(title)
                    print()
                print('----------------')
                print()


if __name__ == '__main__':
    grb = Librarian(GR_JSON)
    grb.find_namesakes()
