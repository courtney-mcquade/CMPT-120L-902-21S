from flask import Flask

from flask import render_template
app = Flask(__name__)

@app.route('/hello/')


@app.route('/')
def index():
    return 'Courtneys Website'
    

@app.route('/aboutme/')
def aboutme():
    return render_template('aboutme.html')

@app.route('/resume/')
def resume():
    return render_template('resume.html')