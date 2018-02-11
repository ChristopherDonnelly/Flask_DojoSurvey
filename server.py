from flask import Flask, render_template, request, redirect, url_for, session, flash
import re

# create a regular expression object that we can use run operations on
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

app = Flask(__name__)

app.secret_key = 'AdvancedFormValidationKey'

@app.route('/')

def display_index():

    locations = ['Seattle', 'Silicon Valley', 'Los Angeles', 'Dallas', 'Tulsa', 'Chicago', 'Washington DC']
    languages = ['JQuery', 'Java', 'Javascript', 'C Sharp', 'Python', 'iOS Swift']

    if not 'name' in session:
        session['name'] = ''
    if not 'comment' in session:
        session['comment'] = ''

    for loc in locations:
        if not loc in session:
            session[loc] = ''

    for lang in languages:
        if not lang in session:
            session[lang] = ''

    return render_template('index.html')

@app.route('/results', methods=['POST'])
def results():

    locations = ['Seattle', 'Silicon Valley', 'Los Angeles', 'Dallas', 'Tulsa', 'Chicago', 'Washington DC']
    languages = ['JQuery', 'Java', 'Javascript', 'C Sharp', 'Python', 'iOS Swift']

    valid = True
    items = 'first'

    session['location'] = request.form['location']
    session['language'] = request.form['language']
    
    for loc in locations:
        if session['location'] == loc:
            session[loc] = 'selected'
        else:
            session[loc] = ''

    for lang in languages:
        if session['language'] == lang:
            session[lang] = 'selected'
        else:
            session[lang] = ''

    if len(request.form['name']) < 1:
        flash("Name cannot be empty!", 'red')
        valid = False
        items = 'second'
    else:
        session['name'] = request.form['name']

    if len(request.form['comment']) < 1:
        flash("Comments cannot be blank!", 'red '+items)
        valid = False
    elif len(request.form['comment']) > 120:
        session['comment'] = request.form['comment']
        flash("comment cannot be more than 120 characters!", 'red '+items)
        valid = False

    if valid:
        name = request.form['name']
        location = request.form['location']
        language = request.form['language']
        comment = request.form['comment']

        session.pop('name')
        session.pop('location')
        session.pop('language')
        session.pop('comment')

        for loc in locations:
            session.pop(loc)

        for lang in languages:
            session.pop(lang)

        return render_template('results.html', name = name, location = location, language = language, comment = comment)
    else:
        return redirect('/')

@app.route('/home', methods=['POST'])

def redirect_url(default='display_index'):
    return redirect(url_for(default))

app.run(debug=True)