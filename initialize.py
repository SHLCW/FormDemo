import sqlite3

conn = sqlite3.connect("data.db")

c = conn.cursor()

c.execute('''
CREATE TABLE users (
  user TEXT,
  pw TEXT
)''')

c.execute('''
INSERT INTO users
  (user, pw)
VALUES
  ('dan', '123');
''')
