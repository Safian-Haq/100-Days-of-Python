from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def recieve_data():
    if request.method == 'POST':
        print(request.form)
        return f"<h1>Name: {request.form['USERNAME']}, Password: {request.form['PASSWORD']}</h1>"

if __name__ == '__main__':
    app.run(debug=True)
