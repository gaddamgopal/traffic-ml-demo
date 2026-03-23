from flask import Flask, render_template, jsonify
import pandas as pd
import random

app = Flask(__name__)

try:
    data = pd.read_csv('traffic.csv')
except:
    data = None

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get_data')
def get_data():
    if data is not None:
        row = data.sample().iloc[0]
        t1 = int(row[0])
        t2 = int(row[1])
    else:
        t1 = random.randint(10, 100)
        t2 = random.randint(10, 100)

    return jsonify({'road1': t1, 'road2': t2})

if __name__ == '__main__':
    app.run()
