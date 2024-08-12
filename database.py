import sqlite3

con = sqlite3.connect("ToDoList.db")
cur = con.cursor()
cur.execute("PRAGMA foreign_keys = ON")
con.commit()

cur.execute("DROP TABLE IF EXISTS Task")
cur.execute("DROP TABLE IF EXISTS List")
cur.execute("DROP TABLE IF EXISTS DoFirst")
con.commit()

cur.execute(
    """
    CREATE TABLE Task (
        TID INTEGER PRIMARY KEY AUTOINCREMENT,
        Name TEXT NOT NULL,
        Category TEXT,
        Current BLOB NOT NULL DEFAULT FALSE ,
        List_id INTEGER,
        FOREIGN KEY (List_id) REFERENCES List(LID)
    )
    """
)
con.commit()

cur.execute(
    """
    CREATE TABLE List (
        LID INTEGER Primary Key AUTOINCREMENT,
        Name TEXT NOT NULL,
        Time TEXT NOT NULL
    )
    """
)
con.commit()

cur.execute(
    """
    CREATE TABLE DoFirst (
        Task_id INTEGER PRIMARY KEY,
        Priority INTEGER,
        Deadline TEXT NOT NULL,
        FOREIGN KEY (Task_id) REFERENCES Task(TID)
    )
    """
)
con.commit()