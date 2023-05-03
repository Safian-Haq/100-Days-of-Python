import requests
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html', blogs=get_blogs())

@app.route('/about.html')
def about():
    return render_template('about.html')

@app.route('/contact.html')
def contact():
    return render_template('contact.html')

@app.route('/post/<post_id>')
def post(post_id):

    target_post = None
    blogs = get_blogs()
    for blog in blogs:
        if int(post_id) == blog['id']:
            target_post = blog
            break
    print(target_post)
    return render_template('post.html', target_post=target_post)


def get_blogs():
    return requests.get('https://api.npoint.io/3c3f740d3769373f4a12').json()


if __name__ == '__main__':
    app.run(debug=True)
