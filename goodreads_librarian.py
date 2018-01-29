from basic_operations import *
from global_vars import *


class GRBooks(object):
    def __init__(self, books_json):
        self.books_json = books_json
        self.to_read = list()
        self.collect_books()

    def __str__(self):
        string = ''
        ind = 1
        for book in self.to_read:
            string += "%d\nauthor: %s\ntitle: %s\n\n" % (ind, book[AUTHOR], book[TITLE])
            ind += 1
        return string

    def collect_books(self):
        all_books = load_json(self.books_json)
        for book in all_books:
            if TO_READ_SHELF in book[SHELVES]:
                self.to_read.append({AUTHOR: book[AUTHOR], TITLE: book[TITLE]})


if __name__ == '__main__':
    grb = GRBooks(GR_JSON)
    print(grb)
