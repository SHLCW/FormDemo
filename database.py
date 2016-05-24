import sqlite3

# This application shouldn't use multiple threads, but the debugger for Flask will, and therefore you'll want to disable
# checking for multiple threads.
conn = sqlite3.connect("data.db", check_same_thread=False)
c = conn.cursor()


def verify_password(u, p):
    c.execute("SELECT pw FROM users WHERE user=?", (u,))
    pw = c.fetchone()[0]
    if p == pw:
        return True
    else:
        return False
