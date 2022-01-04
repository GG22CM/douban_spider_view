from flask import Flask, render_template, request
import sqlite3
import re


app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return render_template("index.html")

@app.route('/home')
def home():
    return hello_world()

@app.route('/table')
def table():
    conn = sqlite3.connect('movie.db')
    cursor = conn.cursor()
    data = cursor.execute('select * from movie250')
    datalist = [item for item in data]
    print(datalist)
    cursor.close()
    conn.close()
    return render_template('table.html', datalist=datalist)

@app.route('/rate')
def rate():
    conn = sqlite3.connect('movie.db')
    cursor = conn.cursor()
    data = cursor.execute('select rate, count(rate) from movie250 group by rate')
    datalist = [item for item in data]
    cursor.close()
    conn.close()
    xVals = [item[0] for item in datalist]
    yVals = [item[1] for item in datalist]
    return render_template('rate.html', xVals=xVals, yVals=yVals)


if __name__ == '__main__':
    app.run()
