import random
import datetime as dt
import requests

from flask import Flask, render_template

## Constants
BLOGS_URL = 'https://api.npoint.io/c790b4d5cab58020d391'
#####################################

app = Flask(__name__)

def get_blogs(blogs_url):

    response = requests.get(blogs_url)
    response.raise_for_status()

    return response.json()


def get_age(target_name):
    response = requests.get(f'https://api.agify.io?name={target_name}')
    response.raise_for_status()
    return response.json()['age']


def get_gender(target_name):
    response = requests.get(f'https://api.genderize.io?name={target_name}')
    response.raise_for_status()
    return response.json()['gender']


@app.route('/')
def home():
    random_number = random.randint(1,10)
    current_year = dt.datetime.now().year
    your_name = 'Safian Haq'
    return render_template('index.html',
                           random_number=random_number, current_year=current_year,
                           your_name = your_name)

@app.route('/guess/<target_name>')
def get_age_by_name(target_name):

    age = get_age(target_name)
    gender = get_gender(target_name)

    return render_template('guess.html',
                           age=age, gender=gender, name=target_name)

@app.route('/blog/')
def blog():
    print('blog')
    blogs = get_blogs(BLOGS_URL)
    return render_template('blog.html',
                           blogs=blogs)

if __name__ == '__main__':
    app.run(debug=True)
