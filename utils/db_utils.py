# DB validation logic

import psycopg2
from configs.config import DB_CONNECTION

def query_db(sql):
    conn = psycopg2.connect(DB_CONNECTION)
    cur = conn.cursor()
    cur.execute(sql)
    result = cur.fetchall()
    conn.close()
    return result
