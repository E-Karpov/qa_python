import unittest
from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_rating()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()


    class TestBooksCollector(unittest.TestCase):

        def setUp(self):
            self.collector = BooksCollector()

            # добавляем новую книгу
        def test_add_new_book(self):
            self.collector.add_new_book("Книга 1")
            self.assertIn("Книга 1", self.collector.books_genre)
            self.assertEqual(self.collector.books_genre["Книга 1"], "")

            # проверяем, что нельзя добавить книгу с названием длиннее 40 символов
        def test_add_new_book_invalid_length(self):
            self.collector.add_new_book("К" * 41)  # Длина больше 40 символов
            self.assertNotIn("К" * 41, self.collector.books_genre)

            # устанавливаем книге жанр
        def test_set_book_genre(self):
            self.collector.add_new_book("Книга 2")
            self.collector.set_book_genre("Книга 2", "Фантастика")
            self.assertEqual(self.collector.get_book_genre("Книга 2"), "Фантастика")

            # выводим список книг с определённым жанром
        def test_get_books_with_specific_genre(self):
            self.collector.add_new_book("Книга 3")
            self.collector.set_book_genre("Книга 3", "Ужасы")
            self.collector.add_new_book("Книга 4")
            self.collector.set_book_genre("Книга 4", "Комедии")
            books = self.collector.get_books_with_specific_genre("Ужасы")
            self.assertEqual(books, ["Книга 3"])

            # получаем словарь books_genre
        def test_get_books_genre(self):
            self.collector.add_new_book("Книга 5")
            self.collector.set_book_genre("Книга 5", "Детективы")
            self.assertEqual(self.collector.get_books_genre(), {"Книга 5": "Детективы"})

            # возвращаем книги, подходящие детям
        def test_get_books_for_children(self):
            self.collector.add_new_book("Книга 6")
            self.collector.set_book_genre("Книга 6", "Мультфильмы")
            self.collector.add_new_book("Книга 7")
            self.collector.set_book_genre("Книга 7", "Ужасы")
            books_for_children = self.collector.get_books_for_children()
            self.assertEqual(books_for_children, ["Книга 6"])

            # добавляем книгу в Избранное
        def test_add_book_in_favorites(self):
            self.collector.add_new_book("Книга 8")
            self.collector.add_book_in_favorites("Книга 8")
            self.assertIn("Книга 8", self.collector.favorites)

            # удаляем книгу из Избранного
        def test_delete_book_from_favorites(self):
            self.collector.add_new_book("Книга 9")
            self.collector.add_book_in_favorites("Книга 9")
            self.collector.delete_book_from_favorites("Книга 9")
            self.assertNotIn("Книга 9", self.collector.favorites)

            # получаем список Избранных книг
        def test_get_list_of_favorites_books(self):
            self.collector.add_new_book("Книга 10")
            self.collector.add_book_in_favorites("Книга 10")
            favorites = self.collector.get_list_of_favorites_books()
            self.assertEqual(favorites, ["Книга 10"])

            # проверяем, что нельзя добавить одну и ту же книгу несколько раз
        def test_add_duplicate_book_to_favorites(self):
            self.collector.add_new_book("Книга 11")
            self.collector.add_book_in_favorites("Книга 11")
            self.collector.add_book_in_favorites("Книга 11")  # Повторное добавление
            self.assertEqual(len(self.collector.favorites), 1)

    if __name__ == "__main__":
        unittest.main()