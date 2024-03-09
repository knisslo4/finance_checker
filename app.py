from flask import Flask, render_template
import pandas as pd
from datetime import datetime, timedelta

app = Flask(__name__)

entries = []

starting_balances = {
    "Checking": 4006.55,
    "Savings": 0,
    "Invested": 2002.48,
    "Taxes": 355.77
}

@app.route('/')
def index():
    balances = starting_balances
    
    return render_template('index.html', balances=balances)

@app.route('/paychecks')
def paychecks():
    one_month_ago = datetime.today() - timedelta(days=30)
    one_month_from_date = datetime.today() + timedelta(days=30)
    paycheck_entries = [entry for entry in entries if 'Paycheck' in entry['Description'] and one_month_ago <= entry['Date'] <= one_month_from_date]
    return render_template('paychecks.html', paycheck_entries=paycheck_entries)

if __name__ == '__main__':
    app.run(debug=True)