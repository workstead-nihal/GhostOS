from flask import Blueprint, render_template

main = Blueprint('main', __name__)

@main.route('/')
def home():
    return render_template('index.html')

@main.route('/about')
def about():
    return render_template('index.html')  # You can create a separate template for the about page later.

# filepath: /workspaces/GhostOS/app/routes.py
@main.route('/clock')
def clock():
    return render_template('clock.html')

@main.route('/calendar')
def calendar():
    return render_template('calendar.html')

@main.route('/mindmodule')
def mindmodule():
    return render_template('mindmodule.html')

@main.route('/studycore')
def studycore():
    return render_template('studycore.html')

@main.route('/missionlog')
def missionlog():
    return render_template('missionlog.html')