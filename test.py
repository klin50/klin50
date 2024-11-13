from flask import Flask
import sqlite3

DB_FILE="discobandit.db"


app = Flask(__name__)
@app.route("/")
def reroute():
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS links(html TEXT);")
    c.execute("INSERT INTO links(html) VALUES (?);", ("MYFIRSTHTML",))
    c.execute('SELECT * FROM links')
    links = c.fetchall()

    print(links)
    print("why is it adding twice")

    db.commit()
    db.close()
    return("this isn't working yet")

@app.route("/story",methods = ["GET","POST"])
def edit():
    text = request.form.get

if __name__ == "__main__":
    app.debug = True 
    app.run()