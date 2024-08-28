# Import the sqlite3 module
# Ref: https://docs.python.org/3/library/sqlite3.html
import sqlite3
import curses
from curses import wrapper
from curses.textpad import Textbox , rectangle
import time

# Connect to the SQLite database
# You can install SQLite3 Editor for Visual Studio Code to view and edit the database.
# Ref: https://marketplace.visualstudio.com/items?itemName=yy0931.vscode-sqlite3-editor
con = sqlite3.connect("ToDoList.db")
cur = con.cursor()
cur.execute("PRAGMA foreign_keys = ON")
con.commit()

# Create database tables if they don't exist
# Ref:
# - https://www.sqlite.org/datatype3.html
# - https://sqlite.org/foreignkeys.html
cur.execute("DROP TABLE IF EXISTS Task")
cur.execute("DROP TABLE IF EXISTS List")
con.commit()

# Initialize the database tables if not exist
# You can complte this step by executing the SQL queries exported from the SQLite3 Editor.
cur.execute(
    """
    CREATE TABLE Task (
        TID INTEGER PRIMARY KEY AUTOINCREMENT,
        Name TEXT NOT NULL,
        Category TEXT,
        Current BLOB DEFAULT FALSE ,
        List_id INTEGER,
        Priority BLOB DEFAULT FALSE,
        Deadline TEXT NOT NULL,
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
        Duration TEXT NOT NULL
    )
    """
)
con.commit()


# Display all tasks
def display_tasks(stdscr):
    res = cur.execute("SELECT * From Task")
    rows = res.fetchall()
    stdscr.clear()
    if not rows:
        stdscr.addstr(0, 0, "there is no task")
    else:
        for index, row in enumerate(rows):
            stdscr.addstr(index, 0, f"TID: {row[0]:4} Name: {row[1]:10} Category: {row[2]:10} Priority: {row[3]:3} Deadline: {row[4]:10}")
    stdscr.refresh()
    stdscr.getch()


# Display all lists
def display_lists(stdscr):
    res = cur.execute("SELECT * From List")
    rows = res.fetchall()
    stdscr.clear()
    if not rows:
        stdscr.addstr(0, 0, "there is no list")
    else:
        for index, row in enumerate(rows):
            stdscr.addstr(index, 0, f"LID: {row[0]:4} Name: {row[1]:10} Duration: {row[2]:10}")
    stdscr.refresh()
    stdscr.getch()


# Add a new task
def add_task(stdscr):
    stdscr.clear()
    stdscr.addstr(0, 0, "Input the Name:")
    stdscr.refresh()
    Name = stdscr.getstr().decode('utf-8')
    stdscr.clear()
    stdscr.addstr(0, 0, "Input the Category:")
    stdscr.refresh()
    Category = stdscr.getstr().decode('utf-8')
    stdscr.clear()
    stdscr.addstr(0, 0, "Input the List_id:")
    stdscr.refresh()
    List_id = stdscr.getstr().decode('utf-8')
    stdscr.clear()
    stdscr.addstr(0, 0, "Input the priority(True or False):")
    stdscr.refresh()
    priority = stdscr.getstr().decode('utf-8')
    stdscr.clear()
    stdscr.addstr(0, 0, "Input the Deadline:")
    stdscr.refresh()
    deadline = stdscr.getstr().decode('utf-8')
    cur.execute("INSERT INTO Task (Name, Category, List_id) VALUES (?, ?, ?, ?, ?)", (Name, Category, List_id, priority, deadline))

# Add new list
def add_list(stdscr):
    stdscr.clear()
    stdscr.addstr(0, 0, "Input the List_Name:")
    stdscr.refresh()
    List_Name = stdscr.getstr().decode('utf-8')
    stdscr.clear()
    stdscr.addstr(0, 0, "Input the Duration:")
    stdscr.refresh()
    Duration = stdscr.getstr().decode('utf-8')
    stdscr.clear()
    cur.execute("INSERT INTO List (Name , Duration) Values (? , ? )",(List_Name, Duration)) 

# delete task
def del_task(stdscr):
    stdscr.clear()
    stdscr.addstr(0, 0, "Input the Task Name:")
    stdscr.refresh()
    Name = stdscr.getstr().decode('utf-8')
    stdscr.clear()
    cur.execute("DELETE FROM Task WHERE Name = (?)",(Name))

# update task to Complete
def up_task(stdscr):
    stdscr.clear()
    stdscr.addstr(0, 0, "Input the Task Name:")
    stdscr.refresh()
    Name = stdscr.getstr().decode('utf-8')
    stdscr.clear()
    cur.execute("UPDATE Task SET Current = True WHERE Name = (?)",(Name))

# list the uncompleted task
def uncompleted(stdscr):
    cur.execute("SELECT * FROM Task WHERE Current = FALSE")


# Main loop
def main(stdscr):
    functions = [
        {"text": "Display All List", "y": 1, "x": 0, "action": display_lists},
        {"text": "Display All Task", "y": 3, "x": 0, "action": display_tasks},
        {"text": "Add List",         "y": 5, "x": 0, "action": add_list},
        {"text": "Add Task",         "y": 7, "x": 0, "action": add_task},
        {"text": "Delete Task",      "y": 9, "x": 0, "action": del_task},
        {"text": "Update Task",      "y": 11, "x": 0, "action": up_task},
        {"text": "Display Uncompleted Task", "y": 13, "x": 0, "action": uncompleted}
    ]

    curses.start_color()
    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLUE)
    curses.curs_set(0)
    current_selection = 0 
    while True:
        stdscr.clear()
        for index, item in enumerate(functions):
            if index == current_selection:
                stdscr.attron(curses.color_pair(1))
                stdscr.addstr(item["y"], item["x"], item["text"], curses.A_BOLD)
                stdscr.attroff(curses.color_pair(1))
            else:
                stdscr.addstr(item["y"], item["x"], item["text"])

        stdscr.refresh()

        key = stdscr.getch()

        if key == curses.KEY_UP:
            current_selection = (current_selection - 1) % len(functions)
        elif key == curses.KEY_DOWN:
            current_selection = (current_selection + 1) % len(functions)
        elif key == 10:  
            functions[current_selection]["action"](stdscr)

        if key in (ord('q'), 27): 
            break
    stdscr.getch()
       


curses.wrapper(main)
con.close()
