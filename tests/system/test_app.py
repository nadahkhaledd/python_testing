from unittest import TestCase
from unittest.mock import patch
import app
from blog import Blog

class AppTest(TestCase):
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

