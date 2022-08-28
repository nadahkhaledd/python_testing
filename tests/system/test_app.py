from unittest import TestCase
from unittest.mock import patch
import app
from blog import Blog

class AppTest(TestCase):
    def test_print_blog(self):
        b = Blog('Test', 'test author')
        app.blogs = {'Test': b}
        with patch('builtins.print') as mocked_print:
            app.print_blogs()
            mocked_print.assert_called_with('- Test by test author (0 posts)')