from flask import Flask, render_template
import random, csv
app = Flask(__name__)

def readfile(f):
    d = {}
    with open (f, 'r') as listfile:
        reader = csv.reader(listfile)
        next(reader)
        for row in reader:
            job = row[0]
            if job == "Total":
                continue
            percent = float(row[1])
            d[job] = percent
    return d
        
        
def sel(d):
    return random.choices(list(d.keys()), weights=d.values(), k=1)[0]

@app.route("/")
def hello_world():
    return "No hablo queso!"

@app.route("/template")
def test_tmplt():
    return render_template('tablified.html', collection1=readfile("data/occupations.csv").keys(), collection2=readfile("data/occupations.csv").values())

if __name__ == "__main__":
    app.debug = True
    app.run()