# main.py 
#----------------------------------------------------------------------#
#
#
#
#----------------------------------------------------------------------#

from math import floor
from sqlite3 import OperationalError
import string, sqlite3
from urllib.parse import urlparse
import http.server
import socketserver
from flask import Flask, request, render_template, redirect



#Assuming urls.db is in your app root folder
def table_check():
    create_table = """
        CREATE TABLE WEB_URL(
        ID INT PRIMARY KEY     AUTOINCREMENT,
        URL  TEXT    NOT NULL
        );
        """
    with sqlite3.connect('urls.db') as conn:
        cursor = conn.cursor()
        try:
            cursor.execute(create_table)
        except OperationalError:
            pass

# Base62 Encoder and Decoder
def toBase62(num, b = 62):
    if b <= 0 or b > 62:
        return 0
    base = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    r = num % b
    res = base[r];
    q = floor(num / b)
    while q:
        r = q % b
        q = floor(q / b)
        res = base[int(r)] + res
    return res

def toBase10(num, b = 62):
    base = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    limit = len(num)
    res = 0
    for i in range(limit):
        res = b * res + base.find(num[i])
    return res

app = Flask(__name__)

# REDIRECTING 

@app.route('/<short_url>')
def redirect_short_url(short_url):
    decoded_string = toBase10(short_url)
    redirect_url = 'https://marvelapp.com/asdf'
    with sqlite3.connect('urls.db') as conn:
        cursor = conn.cursor()
        select_row = """
                SELECT URL FROM WEB_URL
                    WHERE ID=%s
                """%(decoded_string)
        result_cursor = cursor.execute(select_row)
        try:
            redirect_url = result_cursor.fetchone()[0]
        except Exception as e:
            print(e)
    return redirect(redirect_url)



if __name__ == '__main__':
    # This code checks whether database table is created or not
    table_check()
    app.run(port = 8000, debug=True)   
    
    