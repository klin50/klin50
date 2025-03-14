from flask import Flask, render_template, redirect, url_for, request, flash, session
import sqlite3

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
DATABASE = 'site.db'

def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def home():
    conn = get_db_connection()
    stories = conn.execute('SELECT * FROM stories').fetchall()
    conn.close()
    return render_template('home.html', stories=stories)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        conn = get_db_connection()
        user = conn.execute('SELECT * FROM users WHERE username = ?', (username,)).fetchone()
        if user:
            flash('Username is already taken!', 'danger')
        else:
            conn.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, password))
            conn.commit()
            flash('Account created successfully!', 'success')
            return redirect(url_for('login'))
        conn.close()
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        conn = get_db_connection()
        user = conn.execute('SELECT * FROM users WHERE username = ? AND password = ?', (username, password)).fetchone()
        conn.close()
        if user:
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

        conn = get_db_connection()
        conn.execute('INSERT INTO stories (title, content, username) VALUES (?, ?, ?)', (title, content, session['username']))
        conn.commit()
        conn.close()
        flash('Story posted successfully!', 'success')
        return redirect(url_for('home'))
    return render_template('post_story.html')

@app.route('/edit_story/<int:story_id>', methods=['GET', 'POST'])
def edit_story(story_id):
    if 'username' not in session:
        return redirect(url_for('login'))

    conn = get_db_connection()
    story = conn.execute('SELECT * FROM stories WHERE id = ?', (story_id,)).fetchone()

    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        if story['username'] == session['username']:
            conn.execute('UPDATE stories SET title = ?, content = ? WHERE id = ?', (title, content, story_id))
            conn.commit()
            flash('Story updated successfully!', 'success')
            return redirect(url_for('home'))
        else:
            flash('You are not authorized to edit this story.', 'danger')
    conn.close()
    return render_template('edit_story.html', story=story)

if __name__ == '__main__':
    app.run(debug=True)