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
    try:
        import pandas as pd
        data = pd.read_csv('traffic.csv')

        row = data.sample().iloc[0]

        t1 = int(row[0])
        t2 = int(row[1])

    except Exception as e:
        print("ERROR:", e)
        import random
        t1 = random.randint(10, 100)
        t2 = random.randint(10, 100)

    return jsonify({'road1': t1, 'road2': t2})

import os

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
