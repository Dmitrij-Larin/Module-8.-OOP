class Book:

    def __init__(self, title, writer, genre, release):
        self.title = title
        self.writer = writer
        self.genre = genre
        self.release = release

    def get_literary_work(self, literary_work):
        if literary_work == "роман":
            return f"Недавно я прочитал {literary_work} \"{self.title}\". Автор данного произведения: {self.writer}"
        elif literary_work == "повесть":
            return f"Недавно я прочитал {literary_work} \"{self.title}\". Автор данного произведения: {self.writer}"
        else:
            pass

    def get_release_date(self, place):
        return f"Эта книга была написана в {self.release} году. Страна написания: {place}."

    def get_genge_of_work(self):
        return f"Жанр данного произведения: {self.genre}"


book_1 = Book("Тёмная башня", "Стивен Кинг", "тёмное фэнтези", 2004)
print(book_1.get_literary_work("роман"))
print(book_1.get_release_date("США"))
print(book_1.get_genge_of_work())
print()
book_2 = Book("Собачье сердце", "Михаил Булгаков", "сатира", 1925)
print(book_2.get_literary_work("повесть"))
print(book_2.get_release_date("СССР"))
print(book_2.get_genge_of_work())
