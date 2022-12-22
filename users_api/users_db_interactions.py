import psycopg2
import psycopg2.extras as pse  # We'll need this to convert SQL responses into dictionaries
from flask import jsonify

def get_db_connection():
  try:
    conn = psycopg2.connect("dbname=users user=louisglanfield host=localhost")
    return conn
  except:
    print("Error connecting to database.")

def select(query, params=()):
  try:
    conn = get_db_connection()
    with conn.cursor(cursor_factory=pse.RealDictCursor) as cur:
      cur.execute(query, params)
      data = cur.fetchall()
      return jsonify(data)
  except:
    return "Error selecting data", 304

def insert(query, params=()):
  try:
    conn = get_db_connection()
    with conn.cursor() as cur:
      cur.execute(query, params)
      conn.commit()
    return "Insert completed.", 200
  except:
    return "Error inserting data", 304

