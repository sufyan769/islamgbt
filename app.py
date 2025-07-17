from flask import Flask, render_template
import psycopg2
import os

app = Flask(__name__)

# الاتصال بقاعدة البيانات
def get_db_connection():
    conn = psycopg2.connect(os.environ['DATABASE_URL'])  # استخدام DATABASE_URL من المتغيرات البيئية
    return conn

# الصفحة الرئيسية
@app.route('/')
def index():
    return render_template('index.html')

# عرض صفحة حديث مفصل
@app.route('/hadith/<int:hadith_id>')
def hadith_page(hadith_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM hadiths WHERE id = %s', (hadith_id,))
    hadith = cursor.fetchone()
    conn.close()
    if hadith:
        return render_template('hadith_page.html', hadith=hadith)
    return "حديث غير موجود", 404

# عرض صفحة فتوى مفصلة
@app.route('/fatwa/<int:fatwa_id>')
def fatwa_page(fatwa_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM fatwas WHERE id = %s', (fatwa_id,))
    fatwa = cursor.fetchone()
    conn.close()
    if fatwa:
        return render_template('fatwa_page.html', fatwa=fatwa)
    return "فتوى غير موجودة", 404

if __name__ == '__main__':
    app.run(debug=True)
