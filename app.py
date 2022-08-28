blogs = dict()


def menu():
    print_blogs()


def print_blogs():
    for name, blog in blogs.items():
        print('- {}'.format(blog))
