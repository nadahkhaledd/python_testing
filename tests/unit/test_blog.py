from unittest import TestCase
from blog import Blog


class BlogTest(TestCase):
    def test_create_blog(self):
        b = Blog('test', 'test author')

        self.assertEqual('test', b.title)
        self.assertEqual('test author', b.author)
        self.assertListEqual([], b.posts)

    def test_repr(self):
        b = Blog('test', 'test author')
        b2 = Blog('test2', 'author 2')
        self.assertEqual(b.__repr__(), 'test by test author (0 posts)')
