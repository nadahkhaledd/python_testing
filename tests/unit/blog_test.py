from unittest import TestCase
from blog import Blog

class BlogTest(TestCase):
    def test_create_blog(self):
        b = Blog('test', 'test author')

        self.assertEqual('test', b.title)
        self.assertEqual('test author', b.author)
        self.assertListEqual([], b.posts)


