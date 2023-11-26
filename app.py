# =========================================================
# >> MODUL
from flask import Flask, render_template, request, redirect, url_for, session, flash
from mysql import connector
from flask_mysqldb import MySQL
from datetime import datetime
import mysql.connector
from datetime import datetime, timedelta
import MySQLdb.cursors
import re
import random
import pytz 
date = datetime.now()
# =========================================================

# =========================================================
# >> OBJECT FLASK APP
app = Flask(__name__)

# =========================================================

# =========================================================
# >> DATABASE
# app.config['MYSQL_HOST'] = "localhost"
# app.config['MYSQL_USER'] = "root"
# app.config['MYSQL_PASSWORD'] = ""
# app.config['MYSQL_DB'] = "db_Students"

# db = connector.connect(
#     host     = "localhost",
#     user     = "root",
#     passwd   = "",
#     database = "db_Students"
# )

app.config['MYSQL_HOST'] = "superdbresource.mysql.database.azure.com"
app.config['MYSQL_USER'] = "grimaim"
app.config['MYSQL_PASSWORD'] = "@Aero1906"
app.config['MYSQL_DB'] = "db_students"
app.config['MYSQL_SSL_CA'] = '../asset/ssl/ca/DigiCertGlobalRootCA.crt.pem'

db = connector.connect(
    host="superdbresource.mysql.database.azure.com",
    user     = "grimaim",
    passwd   = "@Aero1906",
    database = "db_students",
    ssl_ca="../asset/ssl/ca/DigiCertGlobalRootCA.crt.pem", 
    ssl_disabled=False
)

# cnx = mysql.connector.connect(
#     user="grimaim", 
#     password="{your_password}", 
#     host="superdbresource.mysql.database.azure.com", 
#     port=3306, 
#     database="{your_database}", 
#     ssl_ca="{ca-cert filename}", 
#     ssl_disabled=False)

mysql = MySQL(app) 

if db.is_connected():
    print("====================================")
    print("== BERHASIL TERHUBUNG KE DATABASE ==")
    print("====================================")
# =========================================================

# =========================================================
# >> HALAMAN INDEX
@app.route('/')
def index():
    return render_template('index.html')
# =========================================================

# =========================================================
# >> HALAMAN MEMBER
def determine_face(nama):
    if 'Muhammad Rahim' in nama:
        return 'fa-face-grin-tongue-squint'
    elif 'Paul Dava Nando' in nama:
        return 'fa-face-laugh-beam'
    elif 'Roiyan Saputra' in nama:
        return 'fa-face-grimace'
    elif 'Muhammad Reza' in nama:
        return 'fa-face-grin-tongue-wink'
    else:
        return 'fa-question'
    
@app.route('/member', methods=['GET'])
def member():
    cursor = db.cursor()
    query = """
    SELECT nim, nama, kelas, angkatan, email FROM Member;
    """
    cursor.execute(query)
    members = cursor.fetchall()
    cursor.close()
    return render_template('member.html', members=members, determine_face=determine_face)
# =========================================================

# =========================================================
# >> HALAMAN CONTACT
@app.route('/contact')
def contact():
    return render_template('contact.html')
# =========================================================

# =========================================================
# >> HALAMAN FEATURE
@app.route('/feature')
def feature():
    return render_template('feature.html')
# =========================================================

# =========================================================
# >> HALAMAN QUOTES 
def get_time_difference(post_time):
    # Konversi waktu ke UTC
    post_time_utc = post_time.replace(tzinfo=pytz.timezone('UTC'))

    # Konversi ke zona waktu Indonesia
    post_time_id = post_time_utc.astimezone(pytz.timezone('Asia/Jakarta'))

    # Hitung selisih waktu
    current_time = datetime.now(pytz.timezone('Asia/Jakarta'))
    difference = current_time - post_time_id
    seconds_difference = difference.total_seconds()

    if seconds_difference < 60:
        return "a few seconds ago"
    elif 60 <= seconds_difference < 3600:
        minutes = int(seconds_difference / 60)
        return f"{minutes} minutes ago"
    elif 3600 <= seconds_difference < 86400:
        hours = int(seconds_difference / 3600)
        return f"{hours} hours ago"
    else:
        days = int(seconds_difference / 86400)
        return f"{days} days ago"

@app.route('/quotes', methods=['GET'])
def quotes():
    cursor = db.cursor(dictionary=True)
    query = "SELECT * FROM Quotes"
    cursor.execute(query)
    quotes = cursor.fetchall()
    cursor.close()
    for quote in quotes:
        quote['waktuPosting'] = get_time_difference(quote['waktu'])

    return render_template('quotes.html', quotes=quotes)
# =========================================================

# =========================================================
# >> HALAMAN MANAGE QUOTES
@app.route('/manage-quotes/<id_quotes>', methods=['GET'])
def manageQuotes(id_quotes):
    cur = db.cursor()
    cur.execute('SELECT * FROM quotes WHERE id_quotes=%s', (id_quotes,))
    result = cur.fetchall()
    cur.close()
    return render_template('quotesEdit.html', hasil=result)
# =========================================================

# =========================================================
# >> HALAMAN FORM FEATURE (INSERT DATA)
@app.route('/quotesUploud', methods=['POST'])
def quotesUploud():
    author = request.form['author']
    quotes = request.form['quotes']
    cursor = db.cursor()
    query = "INSERT INTO quotes (author, quotes) VALUES (%s, %s)"
    cursor.execute(query, (author, quotes))
    db.commit()
    cursor.close()
    return redirect(url_for('quotes'))
# =========================================================

# =========================================================
# >> HALAMAN MANAGE QUOTES (UPDATE DATA)
@app.route('/manage-quotes/uploud', methods=['POST'])
def manageQuotes_uploud():
    id_quotes = request.form['id_quotes']
    author = request.form['author']
    quotes = request.form['quotes']
    cur = db.cursor()
    sql = "UPDATE quotes SET author=%s, quotes=%s WHERE id_quotes=%s;"
    values = (author, quotes, id_quotes)
    cur.execute(sql, values)
    db.commit()
    return redirect(url_for('quotes'))

# =========================================================

# =========================================================
# >> HALAMAN MANAGE QUOTES (DELETE DATA)
@app.route('/manage-quotes/deleted/<id_quotes>', methods=['GET'])
def manageQuotes_deleted(id_quotes):
    cur = db.cursor()
    cur.execute('DELETE FROM quotes WHERE id_quotes=%s', (id_quotes,))
    db.commit()
    return redirect(url_for('quotes'))
# =========================================================

# =========================================================
# >> APP RUNNING
if __name__ == '__main__':
    app.run()
# =========================================================