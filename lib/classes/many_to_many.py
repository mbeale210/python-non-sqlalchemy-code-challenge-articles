class Article:
    all = []

    def __init__(self, author, magazine, title):
        if not isinstance(author, Author):
            raise ValueError("Author must be an instance of Author class.")
        if not isinstance(magazine, Magazine):
            raise ValueError("Magazine must be an instance of Magazine class.")
        if not isinstance(title, str) or not (5 <= len(title) <= 50):
            raise ValueError("Title must be a string between 5 and 50 characters.")
        self._title = title
        self.author = author
        self.magazine = magazine
        Article.all.append(self)
    
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        pass
        
class Author:
    def __init__(self, name):
        if not isinstance(name, str) or len(name) == 0:
            raise ValueError("Name must be a non-empty string.")
        self._name = name

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        pass 

    def articles(self):
        return [article for article in Article.all if article.author == self]

    def magazines(self):
        return list(set(article.magazine for article in self.articles()))

    def add_article(self, magazine, title):
        return Article(self, magazine, title)

    def topic_areas(self):
        topics = list(set(magazine.category for magazine in self.magazines()))
        return topics if topics else None

class Magazine:
    def __init__(self, name, category):
        self._name = ""
        self._category = ""
        self.name = name
        self.category = category

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if self._is_valid_name(value):
            self._name = value

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if self._is_valid_category(value):
            self._category = value

    @staticmethod
    def _is_valid_name(name):
        return isinstance(name, str) and 2 <= len(name) <= 16

    @staticmethod
    def _is_valid_category(category):
        return isinstance(category, str) and len(category) > 0

    def articles(self):
        return [article for article in Article.all if article.magazine == self]

    def contributors(self):
        return list(set(article.author for article in self.articles()))

    def article_titles(self):
        titles = [article.title for article in self.articles()]
        return titles if titles else None

    def contributing_authors(self):
        return [author for author in self.contributors() 
                if len([article for article in self.articles() if article.author == author]) > 2] or None