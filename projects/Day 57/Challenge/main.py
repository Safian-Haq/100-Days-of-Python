from flask import Flask, render_template
from post import Post
import requests

def get_posts():
    response = requests.get('https://api.npoint.io/c790b4d5cab58020d391')
    response.raise_for_status()
    return response.json()

app = Flask(__name__)

@app.route('/')
def home():
    blogs = get_posts()
    return render_template("index.html", blogs=blogs)

@app.route('/post/<post_id>')
def post(post_id):
    print('Searching for posts')
    for post in get_posts():
         if str(post['id']) == post_id:
            target_post = Post(post)
            return render_template('post.html', post=target_post)
    return "ERROR - 404 | POST NOT FOUND"

if __name__ == "__main__":
    app.run(debug=True)
