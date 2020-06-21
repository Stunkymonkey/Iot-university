import sqlite3

conn = sqlite3.connect('IoT.db')

c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS sensors (key TEXT PRIMARY KEY, value INT DEFAULT 0)''')
c.execute('''CREATE TABLE IF NOT EXISTS actuators (key TEXT PRIMARY KEY, value INT DEFAULT 0)''')
conn.commit()


def upsert(table, key, value):
    # "CREATE TABLE vocabulary(key TEXT PRIMARY KEY, count INT DEFAULT 1);"
    statement = "INSERT INTO vocabulary(key) VALUES('jovial') ON CONFLICT(key) DO UPDATE SET value=value+1;"
    statement = "INSERT INTO " + table + \
        "(key) VALUES('" + key + "') ON CONFLICT(key) DO UPDATE SET value=" + value + ";"
    print(statement)


def increment(table, key):
    # "CREATE TABLE vocabulary(key TEXT PRIMARY KEY, count INT DEFAULT 1);"
    statement = "INSERT INTO vocabulary(key) VALUES('jovial') ON CONFLICT(key) DO UPDATE SET value=value+1;"
    statement = "INSERT INTO " + table + "(key) VALUES('" + key + "') ON CONFLICT(key) DO UPDATE SET value=value+1;"
    print(statement)


def decrement(table, key):
    # "CREATE TABLE vocabulary(key TEXT PRIMARY KEY, count INT DEFAULT 1);"
    statement = "INSERT INTO vocabulary(key) VALUES('jovial') ON CONFLICT(key) DO UPDATE SET value=value+1;"
    statement = "INSERT INTO " + table + "(key) VALUES('" + key + "') ON CONFLICT(key) DO UPDATE SET value=value-1;"
    print(statement)
