from book import Book
from ebook import EBook
from cafebook import CafeBook
from ebook_with_cafe import EBookWithCafe
from coffee import Coffee
from pastry import Pastry

def main():
    book1 = Book("Poppy War", "Rebecca Kwang")
    ebook1 = EBook("Tomorrow, and tomorrow, and tomorrow", "Gabriel Zavin", 1.2)
    cafe_book1 = CafeBook("Little Prince", "Antonie de Saint-Exupery", 8.99)
    ebook_with_cafe = EBookWithCafe("The Catcher in the Rye", "J.D. Salinger", 0.8, 12.99)

    coffee1 = Coffee("Espresso", "Small", False)
    pastry1 = Pastry("Croissant", 2.50, True)

    # Виклик методів
    print(book1.display_info())
    print(ebook1.display_info())
    print(cafe_book1.display_info())
    print(ebook_with_cafe.display_info())
    print(coffee1.display_info())
    print(pastry1.display_info())

    # Демонстрація поліморфізму
    for item in (book1, ebook1, cafe_book1, ebook_with_cafe, coffee1, pastry1):
        print(item.display_info())

    # Використання статичних методів
    print(Book.book_type())
    print(EBook.book_type())
    print(Coffee.drink_type())
    print(Pastry.food_type())
    print(ebook_with_cafe.display_info())

if __name__ == "__main__":
    main()
