
class User:

    def __init__(self,name):
        self.name = name
        self.is_logged_in = False

def check_auth(function):

    def wrapper(user: User):
        if user.is_logged_in:
            return function(user)
        else:
            raise PermissionError (f'The user: "{user.name}" is not logged in."')
    return wrapper

@check_auth
def create_blog(user: User):
    return  f'{user.name} created the blog.'

def wrap_with_tags(function):
    def wrapper(tag: str):
        return f'<{tag}>{function(tag)}<{tag}>'
    return wrapper

@wrap_with_tags
def say_hello_html(tag):
    return "Hello World!"

if __name__ == '__main__':
    # print(say_hello_html('i'))
    u = User('Safian')
    u.is_logged_in = True
    print(create_blog(u))
