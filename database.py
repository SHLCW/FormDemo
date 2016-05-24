import sqlite3

conn = sqlite3.connect("data.db")
c = conn.cursor()


def verify_password(u, p):
    c.execute("SELECT pw FROM users WHERE user=?", (u,))
    pw = c.fetchone()[0]
    if p == pw:
        return True
    else:
        return False

print(verify_password('dan', '123'))
