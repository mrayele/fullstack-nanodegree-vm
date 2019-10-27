import sqlite3

def main():
    database = r"fsndnotes.db"
    conn = sqlite3.connect(database)
    cur = conn.cursor()
    cur.execute("SELECT * from course")
    rows = cur.fetchall()
    for row in rows:
        print row

if __name__ == '__main__':
    main()
