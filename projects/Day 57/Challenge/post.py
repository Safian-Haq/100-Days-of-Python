class Post:

    def __init__(self, blog: dict):
        self.post_id = blog['id']
        self.title = blog['title']
        self.subtitle = blog['subtitle']
        self.body = blog['body']
