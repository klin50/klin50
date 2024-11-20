from flask import Flask, render_template
import urllib.request
import json

app = Flask(__name__)

@app.route("/")
def nasa():
    with urllib.request.urlopen('https://api.nasa.gov/planetary/apod?api_key=qcOS0PSRF5SfhDAepZCyjfvLVYWAydsFsAEc7wxT') as response:
        html = response.read()
        data = json.loads(html)
        
    return render_template("main.html")
    
if __name__ == "__main__":
    app.debug = True
    app.run()