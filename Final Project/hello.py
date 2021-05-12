from flask import Flask

from flask import render_template
app = Flask(__name__)

@app.route('/hello/')


@app.route('/')
def index():
    return render_templates('index2.html')
    

@app.route('/aboutme/')
def aboutme():
    return render_template('aboutme.html')

@app.route('/resume/')
def resume():
    return render_template('resume.html')

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404
