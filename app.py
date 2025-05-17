from flask import Flask, render_template

app = Flask(__name__,
            static_folder='src/static',
            template_folder='src/templates')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/accounts')
def accounts():
    return render_template('accounts.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
@app.route('/summary')
def balance_summary():
    from opti_db_setup import get_db_connection
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute('SELECT COALESCE(balance, 0) FROM bank_accounts')
    balances = cursor.fetchall()
    total = sum(float(b[0]) for b in balances)

    conn.close()
    return render_template('summary.html', total_balance="{:,.2f}".format(total))
