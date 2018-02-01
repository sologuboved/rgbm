from datetime import datetime
from unidecode import unidecode
from basic_operations import *
from global_vars import *


class Librarian(object):
    def __init__(self, books_json, shelf, starting_date):
        self.books_json = books_json
        self.shelf = shelf
        self.starting_date = starting_date
        self.to_read = list()
        self.collect_books()

    def __str__(self):
        string = ''
        ind = 1
        for book in self.to_read:
            string += "%d\nauthor: %s\ntitle: %s\n<%s>\n<%s>\n\n" % (ind,
                                                                     book[AUTHOR], book[TITLE],
                                                                     book[ABBR_AUTHOR], book[ABBR_TITLE])
            ind += 1
        return string

    def collect_books(self):
        all_books = load_json(self.books_json)
        for book in all_books:
            if self.shelf in book[SHELVES]:
                try:
                    starting_date = datetime.strptime(self.starting_date, "%d.%m.%Y")
                except TypeError:
                    starting_date = None
                if starting_date:
                    date = datetime.strptime(book[DATE], "%b %d, %Y")  # "Jan 01, 1995"
                    if date < starting_date:
                        continue
                author = book[AUTHOR]
                title = book[TITLE]
                abbr_author = ''.join(char if char != "'" else " " for char in unidecode(author.split(',')[0]))
                abbr_title = ''.join([unidecode(char) for char in title.split(':')[0] if char.isalnum() or char == ' '])
                self.to_read.append({AUTHOR: author,
                                     TITLE: title,
                                     ABBR_AUTHOR: abbr_author,
                                     ABBR_TITLE: abbr_title})

    def find_namesakes(self):
        names = dict()
        for book in self.to_read:
            name = book[ABBR_AUTHOR]
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
    grb = Librarian(GR_JSON, TO_READ_SHELF, None)
    print(grb)
