from flask import Blueprint, render_template

main = Blueprint('main', __name__)

@main.route('/')
def home():
    return render_template('base.html')

@main.route('/about')
def about():
    return render_template('base.html')  # You can create a separate template for the about page later.