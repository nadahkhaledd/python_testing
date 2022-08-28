MENU_PROMPT = 'Enter "c" to create a post, '\
                      '"l" to list blogs, '\
                      '"r" to read one, '\
                      '"p" to create a post '\
                      'or "q" to quit.: '
blogs = dict()


def menu():
    print_blogs()
    selection = input(MENU_PROMPT)



def print_blogs():
    for name, blog in blogs.items():
        print('- {}'.format(blog))
