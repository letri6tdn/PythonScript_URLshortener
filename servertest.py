import http.server
import socketserver
import sqlite3

PORT = 8000

Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("serving at port", PORT)
    
    web = input("Please enter your shortened URL code: ")
    
    ecoded_string = toBase10(short_url)
    redirect_url = 'http://localhost:5000'
    with sqlite3.connect('urls.db') as conn:
        cursor = conn.cursor()
        select_row = """
                SELECT URL FROM WEB_URL
                    WHERE ID=%s
                """%(decoded_string)
        result_cursor = cursor.execute(select_row)
        try:
            redirect_url = result_cursor.fetchone()[0]
            print(redirect_url)
        except Exception as e:
            print(e)
    httpd.serve_forever()
    
app = 