import sqlite3

conn = sqlite3.connect('IoT.db')

c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS sensor (key TEXT PRIMARY KEY, value INT DEFAULT 0)''')
c.execute('''CREATE TABLE IF NOT EXISTS actuator (key TEXT PRIMARY KEY, value BOOLEAN DEFAULT 0)''')
conn.commit()


def upsert(table, key, value):
    c.execute("INSERT INTO " + table + "(key, value) VALUES('" + key + "', " + str(value) + ") ON CONFLICT(key) DO UPDATE SET value=" + str(value) + ";")
    conn.commit()


def increment(table, key):
    c.execute("INSERT INTO " + table + "(key) VALUES('" + key + "') ON CONFLICT(key) DO UPDATE SET value=value+1;")
    conn.commit()


def decrement(table, key):
    c.execute("INSERT INTO " + table + "(key) VALUES('" + key + "') ON CONFLICT(key) DO UPDATE SET value=value-1;")
    conn.commit()


def get(table, key):
    c.execute("SELECT value FROM " + table + " WHERE key='" + key + "';")
    single_row = c.fetchone()
    if single_row is None:
        return None
    else:
        return single_row[0]
