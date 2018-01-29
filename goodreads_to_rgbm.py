from goodreads_librarian import Librarian
from global_vars import *
from basic_operations import write_in_txt
from searcher import search


class Finder(Librarian):
    def __init__(self, books_json, shelf=SOONER_SHELF, starting_date=None):
        super(Finder, self).__init__(books_json, shelf, starting_date)
        self.namesakes = set()
        # self.stopped_at = None

    def find(self, starting_index=1):
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
            author_abbrev = book[ABBR_AUTHOR]
            title = book[TITLE]
            title_abbrev = book[ABBR_TITLE]
            result = search(author_abbrev, title_abbrev)
            if result == GLITCH:
                print("!!!!!!!!!!! Glitch at", author, '-', title)
            elif UNDERLOADED in result:
                print("!!!!!!!!!!!", author, '-', title, 'underloaded')
                # self.stopped_at = ind
                # break
            elif ZERO in result:
                print(author, '-', title, "is missing")
            else:
                fname = FOLDER_FOUND + self.shelf + str(ind) + '.txt'
                write_in_txt(fname, author + '\n' + title + '\n\n' + result)
            ind += 1
        # print(self.stopped_at)


if __name__ == '__main__':
    finder = Finder(GR_JSON, shelf=RGBM_SHELF)
    finder.find(13)  #13
