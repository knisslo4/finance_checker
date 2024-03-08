from flask import Flask, render_template
import pandas as pd
from datetime import datetime, timedelta

app = Flask(__name__)

starting_balances = {
    "Checking": 5542.10,
    "Savings": 0,
    "Investing": 0,
    "Taxes": 355.77
}

@app.route('/')
def index():
    balances = starting_balances
    
    return render_template('index_html', balances=balances)

if __name__ == '__main__':
    app.run(debug=True)