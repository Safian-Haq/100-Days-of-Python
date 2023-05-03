import requests
import smtplib
from flask import Flask, render_template, request

#################################################################
# CONSTANTS
#################################################################

MY_EMAIL = 'sufian.python@gmail.com'
PASSWORD = "crszpgiqykhtziup"

#################################################################
# FLASK FUNCTIONS
#################################################################
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', blogs=get_blogs())

@app.route('/about.html')
def about():
    return render_template('about.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        email_message(request.form['EMAIL'], request.form['MESSAGE'])
        return render_template('contact.html', submit=True)

    return render_template('contact.html', submit=False)


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

#################################################################
# HELPER FUNCTIONS
#################################################################

def get_blogs():
    return requests.get('https://api.npoint.io/3c3f740d3769373f4a12').json()

def email_message(email, message):
    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.set_debuglevel(1)
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)

        connection.sendmail(
                    from_addr=MY_EMAIL, to_addrs=f'{email}',
                    msg=f'{message}'
                )

if __name__ == '__main__':
    app.run(debug=True)
