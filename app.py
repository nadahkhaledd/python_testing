from blog import Blog

MENU_PROMPT = 'Enter "c" to create a post, ' \
              '"l" to list blogs, ' \
              '"r" to read one, ' \
              '"p" to create a post ' \
              'or "q" to quit.: '

POST_TEMPLATE = '''
--- {} ---

{}

'''
blogs = dict()


def menu():
    print_blogs()
    selection = input(MENU_PROMPT)

    while selection != 'q':
        if selection == 'c':
            create_blog_request()
        elif selection == 'l':
            print_blogs()
        elif selection == 'r':
            read_blog_request()
        elif selection == 'p':
            create_post_request()
        selection = input(MENU_PROMPT)


def print_blogs():
    for name, blog in blogs.items():
        print('- {}'.format(blog))


def create_blog_request():
    title = input('Enter blog title: ')
    author = input('Enter blog author name: ')

    blogs[title] = Blog(title, author)


def read_blog_request():
    title = input('Enter blog title: ')

    print_posts(blogs[title])


def print_posts(blog):
    for post in blog.posts:
        print_post(post)


def print_post(post):
    print(POST_TEMPLATE.format(post.title, post.content))


def create_post_request():
    title = input('Enter post title: ')
    content = input('Enter post content: ')
