class TooManyBookOnShelfError(Exception):
    pass


class Book():
    def __init__(self, title: str, author: str, price: int, width: int):
        self.title = title
        self.author = author
        self.price = price
        self.width = width


class Shelf():
    def __init__(self, width):
        self.books = []
        self.width = width

    def add_book(self, *args):
        for book in args:
            if self.total_width() + book.width > self.width:
                raise TooManyBookOnShelfError('Too many books!')
            self.books.append(book)

    def total_price(self):
        total_price = 0
        for book in self.books:
            total_price += book.price

        return total_price

    def has_book(self, title):
        return title in (book.title for book in self.books)

    def total_width(self):
        return sum(one_book.width
                   for one_book in self.books)

    def __repr__(self):
        return '\n'.join(b.title for b in self.books)
