'''
Build a flask application that accepts a form submission, redirects, and presents the submitted data on a results page.

The goal is to help you get familiar with sending POST requests through a form and displaying that information. Consider the below example as a guide.
'''


# Import Flask to allow us to create our app, and import
# render_template to allow us to render HTML Files.
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)                     # Global variable __name__ tells Flask whether or not we
                                          # are running the file directly or importing it as a module.

@app.route('/')                           # The "@" symbol designates a "decorator" which attaches the
                                          # following function to the '/' route. This means that
                                          # whenever we send a request to localhost:5000/ we will run
                                          # the following "hello_world" function.

def display_index():
    return render_template('index.html')    # Render the template and return it!

@app.route('/results', methods=['GET', 'POST'])
def results():

    if request.method == 'POST':
        name = request.form['name']
        location = request.form['location']
        language = request.form['language']
        comment = request.form['comment']

        return render_template('results.html', name = name, location = location, language = language, comment = comment)
    else:
        return render_template('results.html')

@app.route('/home', methods=['POST'])

def redirect_url(default='display_index'):
    return redirect(url_for(default))

app.run(debug=True)                       # Run the app in debug mode.