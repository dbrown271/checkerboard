from flask import Flask, render_template, redirect, session, request
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', x = 8, y = 8, color0 = 'red', color1 = 'black')


@app.route('/<num>')
def index2(num):
    return render_template('index.html', x = int(num), y = 8, color0 = 'red', color1 = 'black')


@app.route('/<num1>/<num2>')
def index3(num1, num2):
    return render_template('index.html', x = int(num1), y = int(num2), color0 = 'red', color1 = 'black')




if __name__=="__main__":
    app.run(debug=True)