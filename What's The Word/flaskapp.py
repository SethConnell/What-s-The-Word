from flask import Flask, request, url_for, redirect, render_template

app = Flask(__name__)

@app.route('/')
def my_form():
    return render_template('index.html')

@app.route('/search')
def search():
    return render_template('search.html')

@app.route('/search', methods=['POST'])
def my_form_post():
    if flask.request.method == 'POST':
        description = request.form['desc']
        return description

if __name__ == '__main__':
    app.run()