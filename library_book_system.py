from datetime import date

class LibraryBook:

    fine_per_day = 5   

    def __init__(self, book_name, author):
        self.book_name = book_name
        self.author = author
        self.issue_date = None
        self.return_date = None


    def issue_book(self, issue_date):
        self.issue_date = issue_date
        print(self.book_name, "issued on", self.issue_date)


    def return_book(self):
        self.return_date = date.today()
        print(self.book_name, "returned on", self.return_date)


    def calculate_fine(self):
        allowed_days = 7

        total_days = (self.return_date - self.issue_date).days

        if total_days > allowed_days:
            late_days = total_days - allowed_days
            fine = late_days * LibraryBook.fine_per_day
            print("Late by", late_days, "days")
            print("Total Fine:", fine)
        else:
            print("No fine")


    @classmethod
    def update_fine_per_day(cls, amount):
        cls.fine_per_day = amount
        print("Fine updated to", amount)


b1 = LibraryBook("Python Basics", "ABC Author")
b2 = LibraryBook("Data Structures", "XYZ Author")

b1.issue_book(date(2024, 1, 1))
b1.return_book()
b1.calculate_fine()


