from flask import render_template, url_for, redirect
from . import main

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/crowdfunding')
def crowdfunding():
    return render_template('crowd.html')


@main.route('/platform')
def platform():
    return render_template('platform.html')


@main.route('/what-we-need')
def required():
    return render_template('required.html')

@main.route('/test')
def test():
    return render_template('base.html')
