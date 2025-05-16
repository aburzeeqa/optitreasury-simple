from flask import Flask, render_template
import opti_db_setup  # هذا السطر الجديد لتشغيل إنشاء الجداول

app = Flask(__name__,
            static_folder='src/static',
            template_folder='src/templates')

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
