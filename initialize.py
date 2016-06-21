import sqlite3
import bcrypt

conn = sqlite3.connect("data.db")

c = conn.cursor()

pw = '123'
pw_hash = bcrypt.hashpw('123'.encode('UTF_8'), bcrypt.gensalt())

c.execute('''
CREATE TABLE IF NOT EXISTS users (
  user TEXT,
  pwhash TEXT
);''')

c.execute('INSERT INTO users (user, pwhash) VALUES (?,?);', ('dan', pw_hash))

conn.commit()
conn.close()
