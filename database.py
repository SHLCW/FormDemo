import sqlite3
import bcrypt

# This application shouldn't use multiple threads, but the debugger for Flask will, and therefore you'll want to disable
# checking for multiple threads.
conn = sqlite3.connect("data.db", check_same_thread=False)
c = conn.cursor()


def verify_password(u, p):
    c.execute("SELECT pwhash FROM users WHERE user=?", (u,))
    pw_hash = c.fetchone()[0]
    p_hash = bcrypt.hashpw(p.encode('UTF_8'), pw_hash)
    if p_hash == pw_hash:
        return True
    else:
        return False
