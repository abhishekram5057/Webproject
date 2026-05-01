import os
from flask import Flask, render_template, url_for, request,flash
import sqlite3
import shutil
from detect import Start
import cv2
from werkzeug.utils import secure_filename


app = Flask(__name__)




@app.route('/userlog', methods=['GET', 'POST'])
def userlog():
    return render_template('userlog.html')
    if request.method == 'POST':
        connection = sqlite3.connect('user_data.db')
        cursor = connection.cursor()

        name = request.form['name']
        password = request.form['password']

        query = "SELECT * FROM user WHERE name = ? AND password = ?"
        cursor.execute(query, (name, password))
        result = cursor.fetchone()

        if result:
            return render_template('userlog.html')  # Or redirect to dashboard
        else:
            return render_template('index.html', msg='Incorrect credentials. Try again.')

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
    from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Mango Detection System is running!"