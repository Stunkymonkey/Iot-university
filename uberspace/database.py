import sqlite3

conn = sqlite3.connect('IoT.db')

c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS sensors (key TEXT PRIMARY KEY, value INT DEFAULT 0)''')
c.execute('''CREATE TABLE IF NOT EXISTS actuators (key TEXT PRIMARY KEY, value INT DEFAULT 0)''')
conn.commit()


def upsert(table, key, value):
    c.execute("INSERT INTO " + table + "(key) VALUES('" + key + "') ON CONFLICT(key) DO UPDATE SET value=" + value + ";")
    conn.commit()


def increment(table, key):
    c.execute("INSERT INTO " + table + "(key) VALUES('" + key + "') ON CONFLICT(key) DO UPDATE SET value=value+1;")
    conn.commit()


def decrement(table, key):
    c.execute("INSERT INTO " + table + "(key) VALUES('" + key + "') ON CONFLICT(key) DO UPDATE SET value=value-1;")
    conn.commit()
