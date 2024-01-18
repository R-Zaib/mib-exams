# create a class for bookpublisher with a name and give it functionality to add or publish books
# https://stackoverflow.com/questions/6161799/append-list-within-classes-python
class BookPublisher:
    def __init__(self, name):
        self.name = name
        self.books_published = []

    def publish_book(self, book):
        self.books_published.append(book)
        
    def show_published_books(self):
        for book in self.show_published_books:
            print(book)


class Fiction:
    def __init__(self, title, description, price):
        self.title = title
        self.description = description
        self.price = price
        return
    
    def __str__(self):
        return f'"{self.title}" - "{self.price}" "{self.description}"'

class Dictionary:
    def __init__(self, source_language, target_language, price):
        self.source_language = source_language
        self.target_language = target_language
        self.price = price
        # using this dictionary to store values

        self.translations = {}

# https://www.askpython.com/python/list/adding-tuples-to-lists
    
    def add_translation(self, *translation_args):
        for translation_tuple in translation_args:
            key_source_lan = translation_tuple[0]
            value_target_lan = translation_tuple[1]
            self.translations[key_source_lan] = value_target_lan

        return

    def __str__(self):
        header = f"{self.source_language} - {self.target_language} dictionary - {self.price}"
        words = [f"{key_source_lan} - {value_target_lan}" for key_source_lan, value_target_lan in self.translations.items()]
        representation = [header] + words

        return '\n'.join(representation)


    
eng_hungarian = Dictionary("eng", "urdu", 10)
eng_hungarian.add_translation(('apple', 'alma'), ('table', 'asztal'))
print(eng_hungarian)

    
