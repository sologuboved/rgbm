from goodreads_librarian import Librarian
from global_vars import *
from basic_operations import write_in_txt, dump_json
from searcher import search


class Finder(Librarian):
    def __init__(self, books_json, missing_json):
        super(Finder, self).__init__(books_json)
        self.missing_json = missing_json
        self.namesakes = set()
        self.missing = list()
        self.stopped_at = None

    def find_by_author(self):
        ind = 1
        total = len(self.to_read)
        for book in self.to_read:
            print("%d out of %d" % (ind, total))
            author = book[AUTHOR]
            if author in self.namesakes:
                ind += 1
                continue
            else:
                self.namesakes.add(author)
            author_abbrev = book[ABBREV]
            result = search(author_abbrev, '')
            if ZERO in result:
                self.missing.append(book)
                print(author, book[TITLE], "is missing")
            elif ERROR in result:
                self.stopped_at = ind
                break
            else:
                fname = FOLDER_FOUND + author_abbrev + str(ind) + '.txt'
                write_in_txt(fname, result)
            ind += 1
        print(self.stopped_at)
        dump_json(self.missing, self.missing_json)


if __name__ == '__main__':
    finder = Finder(GR_JSON, MISSING_JSON)
    finder.find_by_author()
