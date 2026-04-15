class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_taken = False

    def take_book(self):
        if self.is_taken:
            print(self.title, "band")
        else:
            self.is_taken = True
            print(self.title, "olindi")

    def return_book(self):
        if not self.is_taken:
            print(self.title, "allaqachon mavjud")
        else:
            self.is_taken = False
            print(self.title, "qaytarildi")

    def show_info(self):
        status = "Band" if self.is_taken else "Mavjud"
        print(self.title, "-", self.author, "-", status)


def main():
    b1 = Book("Python Basics", "Aliyev")
    b2 = Book("HTML Guide", "Karimov")

    b1.show_info()
    b2.show_info()

    b1.take_book()
    b1.take_book()

    b1.return_book()

    b1.show_info()


main()
