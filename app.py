from flask import Flask

app = Flask(__name__)

@app.get("/welcome")
def welcome():
    return """<html><body><h1>Welcome!</h1></body></html>"""

@app.get("/welcome/home")
def welcome_home():
    return """<html><body><h1>Welcome home!</h1></body></html>"""

@app.get("/welcome/back")
def welcome_back():
    return """<html><body><h1>Welcome back!!</h1></body></html>"""