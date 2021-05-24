from flask import Flask
from flask import logging
from flask import render_template
from flask import request
app = Flask(__name__)

@app.route('/hello/')


@app.route('/')
def index():
    app.logger.info("Moving to Index Page");
    return render_template('index.html')
    

@app.route('/aboutme')
def aboutme():
    app.logger.info("Moving to the About Me Page");
    return render_template('aboutme.html')


@app.route('/resume')
def resume():
    app.logger.info("Moving to the Resume Page");
    return render_template('resume.html')

@app.route('/music')
def music():
    app.logger.info("Moving to the Favorite Music Page");
    return render_template('music.html')

@app.route('/contact')
def contact():
    app.logger.info("Moving to the Contact Page");
    return render_template('contact.html')


@app.errorhandler(404)
def page_not_found(error):
    app.logger.info("Moving to the 404 Page");
    return render_template('404.html'), 404
