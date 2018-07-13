# Make special imports from flask module.
from flask import Flask, request, url_for, redirect, render_template

# Defining application.
app = Flask(__name__)

# Added function that converts string into alphabetically formatted list.
def formatWords(string):
    formattedlist = []
    for word in string.split():
        formattedlist.append(word)
    formattedlist.sort()
    return formattedlist
        
# Routing main page of website.
@app.route('/')
def my_form():
    return render_template('index.html')

# Routing search page of website.
@app.route('/search')
def search():
    return render_template('search.html')

# Creating route for POST methods on the search page.
@app.route('/search', methods=['POST'])
def my_form_post():
    if flask.request.method == 'POST':
        description = request.form['desc']
        return description

# Creating special case to ensure app only runs if it is ran directly.
if __name__ == '__main__':
    app.run()
