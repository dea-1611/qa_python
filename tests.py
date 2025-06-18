from main import BooksCollector
class TestBooksCollector:
    def test_add_new_book_add_two_books(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert len(collector.get_books_rating()) == 2




    def test_add_new_book_max_valid_length(self):
        collector = BooksCollector()
        collector.add_new_book('КнигаКнигаКнигаКнигаКнигаКнигаКнигаКнига')
        assert len(collector.get_books_genre()) == 1

    def test_add_new_book_invalid_length(self):
        collector = BooksCollector()
        title_length = "КнигаКнигаКнигаКнигаКнигаКнигаКнигаКнигаК"
        collector.add_new_book(title_length)
        assert title_length not in collector.books_genre

    def test_add_new_book_add_three_books_success(self, collection):
        books = ['Ромео и Джульетта', 'Мастер и Маргарита', 'Король Лев']
        for book in books:
            collection.add_new_book(book)
        assert len(collection.get_books_genre()) == 3

    def test_add_new_book_duplicate(self):
        collector = BooksCollector()
        collector.add_new_book('Идиот')
        collector.add_new_book('Идиот')
        assert len(collector.books_genre) == 1

    def test_set_book_genre_valid(self):
        collector = BooksCollector()
        collector.add_new_book('Дюна')
        collector.set_book_genre('Дюна', 'Фантастика')
        assert collector.get_book_genre('Дюна') == 'Фантастика'

    def test_set_book_genre_invalid(self):
        collector = BooksCollector()
        collector.add_new_book('Warhammer: 40k')
        collector.set_book_genre('Warhammer: 40k', 'Гримдарк фэнтези')
        assert collector.get_book_genre('Warhammer: 40k') == ''

    def test_get_books_books_with_specific_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Как важно быть серьёзным')
        collector.add_new_book('Я, робот')
        collector.set_book_genre('Как важно быть серьёзным', 'Комедии')
        collector.set_book_genre('Я, робот', 'Фантастика')
        assert collector.get_books_with_specific_genre('Комедии') == ['Как важно быть серьёзным']
        assert collector.get_books_with_specific_genre('Фантастика') == ['Я, робот']

    def test_add_book_in_favorites(self, collector):
        collector = BooksCollector()
        collector.add_new_book('Идиот')
        collector.add_book_in_favorites('Идиот')
        favorites = collector.get_list_of_favorites_books()
        assert favorites[0] == 'Идиот'

    def test_add_book_in_favorites_missing_book_not_added(self, collector):
        collector = BooksCollector()
        сollector.add_book_in_favorites('Чума')
        assert len(collector.get_list_of_favorites_books()) == 0

    def test_add_book_in_favorites_double_books_not_added(self, collector):
        collector = BooksCollector()
        collector.add_new_book('12 стульев')
        collector.add_book_in_favorites('12 стульев')
        collector.add_book_in_favorites('12 стульев')
        favorites = collector.get_list_of_favorites_books()
        assert len(favorites) == 1 and favorites[0] == '12 стульев'

    def test_delete_book_from_favorites_book_deleted(self, collector):
        collector = BooksCollector()
        collector.add_new_book('Идиот')
        collector.add_book_in_favorites('Идиот')
        collector.delete_book_from_favorites('Идиот')
        assert len(collector.get_list_of_favorites_books()) == 0

    def test_get_books_for_children(self):
        collector = BooksCollector()
        collector.add_new_book('101 далматинец')
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('101 далматинец', 'Мультфильмы')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Ужасы')
        assert collector.get_books_for_children() == ['Детская книга']