from flask import Flask, render_template, redirect, url_for, request, flash, session
import json
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'

USERS_FILE = 'users.json'
STORIES_FILE = 'stories.json'

def load_data(file):
    if os.path.exists(file):
        with open(file, 'r') as f:
            return json.load(f)
    return {}

def save_data(file, data):
    with open(file, 'w') as f:
        json.dump(data, f, indent=4)

@app.route('/')
def home():
    stories = load_data(STORIES_FILE)
    return render_template('home.html', stories=stories)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        users = load_data(USERS_FILE)
        if username in users:
            flash('Username is already taken!', 'danger')
        else:
            users[username] = password
            save_data(USERS_FILE, users)
            flash('Account created successfully!', 'success')
            return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        users = load_data(USERS_FILE)
        if username in users and users[username] == password:
            session['username'] = username
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('home'))

@app.route('/post_story', methods=['GET', 'POST'])
def post_story():
    if 'username' not in session:
        return redirect(url_for('login'))

    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']

        stories = load_data(STORIES_FILE)
        story_id = len(stories) + 1
        stories[story_id] = {
            'title': title,
            'content': content,
            'username': session['username']
        }
        save_data(STORIES_FILE, stories)
        flash('Story posted successfully!', 'success')
        return redirect(url_for('home'))
    return render_template('post_story.html')

if __name__ == '__main__':
    app.run(debug=True)