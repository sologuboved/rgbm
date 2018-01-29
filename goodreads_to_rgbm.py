from goodreads_librarian import Librarian
from global_vars import *
from basic_operations import write_in_txt
from searcher import search


class Finder(Librarian):
    def __init__(self, books_json):
        super(Finder, self).__init__(books_json)
        self.namesakes = set()
        self.missing = list()
        self.stopped_at = None

    def find_by_author(self):
        ind = 1
        for book in self.to_read:
            author = book[AUTHOR]
            if author in self.namesakes:
                ind += 1
                continue
            else:
                self.namesakes.add(author)
            author_abbrev = book[ABBREV]
            res = search(author_abbrev, '')
            if ZERO in res:
                self.missing.append(book)
            elif ERROR in res:
                self.stopped_at = ind
                break
            else:
                fname = FOLDER_FOUND + author_abbrev + str(ind) + '.txt'
                write_in_txt(fname, res)
            ind += 1











if __name__ == '__main__':
    pass
