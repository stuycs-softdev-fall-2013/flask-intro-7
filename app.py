
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>This is the home page </h1>"

@app.route("/about")
def about():
    return "<h1>This is the about page</h1>"
    


if __name__=="__main__":
    app.run(host="0.0.0.0",port=5005)
    
