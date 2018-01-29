from goodreads_librarian import Librarian
from global_vars import *
from basic_operations import write_in_txt, dump_json
from searcher import search


class Finder(Librarian):
    def __init__(self, books_json, missing_json):
        super(Finder, self).__init__(books_json)
        self.missing_json = missing_json
        self.namesakes = set()
        self.stopped_at = None

    def find_by_author(self, starting_index=1):
        ind = starting_index
        total = len(self.to_read)
        for book in self.to_read[(ind - 1):]:
            print("%d out of %d" % (ind, total))
            author = book[AUTHOR]
            if author in self.namesakes:
                ind += 1
                continue
            else:
                self.namesakes.add(author)
            author_abbrev = book[ABBREV]
            title = book[TITLE]
            result = search(author_abbrev, '')
            if ZERO in result:
                print(author, title, "is missing")
            elif ERROR in result:
                self.stopped_at = ind
                break
            else:
                fname = FOLDER_FOUND + author_abbrev + str(ind) + '.txt'
                write_in_txt(fname, author + '\n' + title + '\n\n' + result)
            ind += 1
        print(self.stopped_at)


if __name__ == '__main__':
    finder = Finder(GR_JSON, MISSING_JSON)
    finder.find_by_author(44)
