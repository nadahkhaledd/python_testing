from unittest import TestCase
from blog import Blog


class BlogTest(TestCase):
    def test_blog_post(self):
        b = Blog('test', 'test author')
        b.create_post('post', 'content')

        self.assertEqual(len(b.posts), 1)
        self.assertEqual(b.posts[0].title, 'post')

    def test_json_no_posts(self):
        b = Blog('test', 'test author')
        expected = {'title': 'test', 'author': 'test author',
                    'posts': []
                    }

        self.assertDictEqual(expected, b.json())

    def test_json(self):
        b = Blog('test', 'test author')
        b.create_post('post', 'post content')
        expected = {'title': 'test', 'author': 'test author',
                    'posts': [
                        {'title': 'post', 'content': 'post content'}
                    ]
                    }

        self.assertDictEqual(expected, b.json())
