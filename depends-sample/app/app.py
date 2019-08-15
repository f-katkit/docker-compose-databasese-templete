import bottle
import json
import psycopg2

from bottle import route, run, HTTPResponse

con = psycopg2.connect("host=depends-sample_db_1 dbname=sample port=5432 user=postgres password=postgres")
cur = con.cursor()

@route('/')
def index():
    r = HTTPResponse(status=200, body="/")
    r.set_header("Content-Type", "application/json")
    return r

@route('/users')
def index():
    cur.execute('SELECT * from users')
    row = cur.fetchall()
    if len(row) > 0:
        dict = []
        for user in row:
          u = {'id': user[0], 'name': user[1] }
          dict.append(u)

        r = HTTPResponse(status=200, body=json.dumps(dict))
        r.set_header("Content-Type", "application/json")
        return r
    return HTTPError(404, "Page not found")

run(host='0.0.0.0', port=8080)