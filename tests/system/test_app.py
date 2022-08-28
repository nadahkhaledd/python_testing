from unittest import TestCase
from unittest.mock import patch
import app
from blog import Blog
from post import Post


class AppTest(TestCase):
    def test_menu_calls_create_blog(self):
        with patch('builtins.input') as mocked_input:
            with patch('app.create_blog_request') as mocked_create_blog_request:
                mocked_input.side_effect = ('c', 'Test create blog', 'test author', 'q')

                app.menu()

                mocked_create_blog_request.assert_called()

    def test_menu_prompt_print(self):
        with patch('builtins.input') as mocked_input:
            app.menu()
            mocked_input.assert_called_with(app.MENU_PROMPT)

    def test_menu_calls_print_blog(self):
        with patch('app.print_blogs') as mocked_print_blogs:
            with patch('builtins.input', return_value='q'):
                app.menu()
                mocked_print_blogs.assert_called()

    def test_print_blog(self):
        b = Blog('Test', 'test author')
        app.blogs = {'Test': b}
        with patch('builtins.print') as mocked_print:
            app.print_blogs()
            mocked_print.assert_called_with('- Test by test author (0 posts)')

    def test_create_blog_request(self):
        with patch('builtins.input') as mocked_input:
            mocked_input.side_effect = ('Test', 'Test author')
            app.create_blog_request()

            self.assertIsNotNone(app.blogs.get('Test'), )

    def test_read_blog_request(self):
        b = Blog('Test', 'test author')
        app.blogs = {'Test': b}
        with patch('builtins.input', return_value='Test'):
            with patch('app.print_posts') as mocked_print_posts:
                app.read_blog_request()
                mocked_print_posts.assert_called_with(b)

    def test_print_posts(self):
        b = Blog('Test', 'test author')
        b.create_post('post', 'post content')
        app.blogs = {'Test': b}

        with patch('app.print_post') as mocked_print_post:
            app.print_posts(b)
            mocked_print_post.assert_called_with(b.posts[0])

    def test_print_post(self):
        p = Post('title', 'post content')
        expected = '''
--- title ---

post content

'''
        with patch('builtins.print') as mocked_print:
            app.print_post(p)

            mocked_print.assert_called_with(expected)

    def test_create_post_request(self):
        b = Blog('Test', 'test author')
        app.blogs = {'Test': b}

        with patch('builtins.input') as mocked_input:
            mocked_input.side_effect = ('Test', 'title', 'content')

            app.create_post_request()

            self.assertEqual(b.posts[0].title, 'title')
            self.assertEqual(b.posts[0].content, 'content')





