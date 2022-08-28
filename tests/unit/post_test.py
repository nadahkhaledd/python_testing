from unittest import TestCase
from post import Post

class PostTest(TestCase):
    def test_create_post(self):
        p = Post('test', 'test content')

        self.assertEqual('test', p.title)
        self.assertEqual('test content', p.content)

