from werkzeug import urls
import sqlite3
from flask import Flask,render_template,request,redirect
import sqlite3
import random
import string
app=Flask(__name__)

def create_db():
    conn = sqlite3.connect("urls.db")
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS urls(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        short_code TEXT UNIQUE,
        long_url TEXT)
    """)
    conn.commit()
    conn.close()

def generate_short_code():
    characters= string.ascii_letters + string.digits

    short_code= ''.join(
        random.choices(characters, k=5)
    )
    return short_code

@app.route("/", methods=["GET","POST"])
def home():
    short_url = None
    if request.method == "POST":
        long_url = request.form["long_url"]
        conn = sqlite3.connect("urls.db")
        cursor = conn.cursor()
        cursor.execute("SELECT short_code FROM urls WHERE long_url=?",
        (long_url,)
        )   
        result = cursor.fetchone()
        if result:
            short_code = result[0]
        else:
            short_code = generate_short_code()
            cursor.execute(
                "INSERT INTO urls(short_code,long_url) VALUES(?,?)",
                (short_code,long_url)
            )
        short_url = f"http://127.0.0.1:5000/{short_code}"
        conn.commit()
        conn.close()  
    conn = sqlite3.connect("urls.db")
    cursor = conn.cursor()
    cursor.execute("SELECT short_code,long_url FROM urls")  
    urls = cursor.fetchall()
    conn.close()
    return render_template("index.html",short_url=short_url,urls=urls)

@app.route("/<short_code>")
def redirect_url(short_code):
    conn = sqlite3.connect("urls.db")
    cursor = conn.cursor()
    cursor.execute("SELECT long_url FROM urls WHERE short_code=?",
    (short_code,)
    )
    result = cursor.fetchone()
    conn.close()

    if result:
        return redirect(result[0])
    else:
        return "URL not found", 404

create_db()
if __name__ == "__main__":
    app.run(debug=True)
