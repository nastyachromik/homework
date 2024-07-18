lib = ['abc', 'bbb', '421', 64554, 3432, 'vcc', 'fef', 'ppop']
import math
class Pagination:
    def __init__(self, alphabet, div):
        self.current_page = 0
        self.book = {}
        self.total_pages = math.ceil(len(alphabet) / div)
        for i in range(self.total_pages):
            try:
                self.book[i+1] = alphabet[i*div:i*div+div]
            except:
                self.book[i+1] = alphabet[i * div:]
    def view(self):
        for key in self.book:
            print(self.book[key])

    def next_page(self):
        if not(self.current_page == self.total_pages):
            self.current_page += 1
            return self

    def prev_page(self):
        if self.current_page == 0:
            print('Для начала используйте функцию next_page')
        elif self.current_page != 1:
            self.current_page -= 1
            return self.book[self.current_page]
        return self

    def first_page(self):
        self.current_page = 1

    def last_page(self):
        self.current_page = self.total_pages

    def go_to_page(self, num):
        if 1 <= num <= self.total_pages:
            self.current_page = num
        else:
            print('Некорректные данные')

    def get_visible_items(self):
        if self.current_page == 0:
            print('Для начала используйте функцию next_page')
        else:
            return self.book[self.current_page]


book1 = Pagination(lib,3)
book1.next_page().next_page()
print(book1.get_visible_items())
