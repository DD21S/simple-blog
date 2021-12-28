from django.test import TestCase
from django.utils import timezone

from blog.models import Author, Category, Post

class AuthorTestCase(TestCase):
    def setUp(self):
        self.author = Author.objects.create(
            name="John",
            lastname="Room",
            url="https://urlurlurl.url",
        )

    def test_creating_author(self):
        """Checks authors creation"""

        self.assertEqual(self.author.name, "John")
        self.assertEqual(self.author.lastname, "Room")
        self.assertEqual(self.author.url, "https://urlurlurl.url")

class CategoryTestCase(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name="News")

    def test_creating_category(self):
        """Checks categories creation"""

        self.assertEqual(self.category.name, "News")

class PostTestCase(TestCase):
    def setUp(self):
        self.author = Author.objects.create(
            name="John",
            lastname="Room",
            url="https://urlurlurl.url",
        )
        self.post = Post.objects.create(
            name="Hello, Hi, Hey",
            author=self.author,
            description="Bye, Goodbye",
            text_post="Hello, Hi, Hey... Bye, Goodbye",
        )

    def test_creating_post(self):
        """Checks posts creation"""

        self.assertEqual(self.post.name, "Hello, Hi, Hey")
        self.assertEqual(self.post.author, self.author)
        self.assertEqual(self.post.description, "Bye, Goodbye")
        self.assertEqual(self.post.text_post, "Hello, Hi, Hey... Bye, Goodbye")

    def test_readings(self):
        """Check readings"""

        self.assertEqual(self.post.readings, 0)

    def test_readings_counter(self):
        """Check readings counter"""

        self.assertEqual(self.post.readings_counter(), 1)
