from unittest import TestCase
from blog import Blog


class BlogTest(TestCase):
    def test_blog_post(self):
        b = Blog('test', 'test author')
        b.create_post('post', 'content')

        self.assertEqual(len(b.posts), 1)
        self.assertEqual(b.posts[0].title, 'post')