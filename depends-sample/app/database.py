import psycopg2
import time

def db_connect():
  con = psycopg2.connect("host=depends-sample_db_1 dbname=sample port=5432 user=postgres password=postgres")
  return con

for _ in range(5):
  try:
    connection = db_connect()
  except Exception as e:
    print(e)
    time.sleep(5)
  else:
    break

cur = connection.cursor()

cur.execute("drop table if exists users")
cur.execute("create table users(id serial primary key, name varchar)")
cur.execute("insert into users (name) values ('JAMES')")
cur.execute("insert into users (name) values ('JOHN')")
cur.execute("insert into users (name) values ('ROBERT')")
connection.commit()
connection.close()

