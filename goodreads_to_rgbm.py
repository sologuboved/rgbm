from goodreads_librarian import Librarian
from basic_operations import write_in_txt
from searcher import *


class Finder(Librarian):
    def __init__(self, books_json, shelf=SOONER_SHELF, starting_date=None):

        super(Finder, self).__init__(books_json, shelf, starting_date)
        self.namesakes = set()

    def find(self, starting_index=1, by_author=True, by_title=True):

        ind = starting_index
        total = len(self.to_read)

        for book in self.to_read[(ind - 1):]:
            print("%d out of %d" % (ind, total))

            author = book[AUTHOR]
            title = book[TITLE]

            if by_author:
                author_abbrev = book[ABBR_AUTHOR]
            else:
                author_abbrev = ''

            if by_title:
                title_abbrev = book[ABBR_TITLE]
            else:
                title_abbrev = ''

            result = search(author_abbrev, title_abbrev)

            num_attempts = 0
            while num_attempts < MAX_ATTEMPTS:
                if UNDERLOADED in result:
                    print('attempt', num_attempts)
                    sleep(LONG_SLEEP)
                    result = search('', title_abbrev)
                    num_attempts += 1
                else:
                    break
            else:
                print("!!!!!!!!!!!", author, '-', title, 'underloaded')

            if result == GLITCH:
                print("!!!!!!!!!!!", author, '-', title, 'glitched')
            elif ZERO in result:
                print(author, '-', title, "is missing")
            elif THERE in result:
                print(author, '-', title)
                fname = FOLDER_FOUND + self.shelf + str(ind) + '.txt'
                write_in_txt(fname, author + '\n' + title + '\n\n' + result)
            else:
                print(author, '-', title, "is plain weird")
                print(result)
                print()

            ind += 1


if __name__ == '__main__':

    finder = Finder(GR_JSON, shelf=TO_READ_SHELF, starting_date='30.01.2018')
    finder.find()
