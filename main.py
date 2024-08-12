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
con = sqlite3.connect("tasks.db")
cur = con.cursor()

# Create database tables if they don't exist
# Ref:
# - https://www.sqlite.org/datatype3.html
# - https://sqlite.org/foreignkeys.html


# Initialize the database tables if not exist
# You can complte this step by executing the SQL queries exported from the SQLite3 Editor.


# Display all tasks
def display_tasks():
    # Execute and fetch the results from the database
    cur.execute("SELECT * From Task")  


# Add a new task ()
def add_task(task):
    # Execute and commit the changes to the database
    cur.execute("INSERT INTO Task Values (Name , Category, Current)") 

# delete task
def del_task(task):
    ...

# update task
def up_task():
    ...

# list the uncompleted task
def uncompleted(task):
    ...



# Main loop
while True:
    pass  
    # Print user menu
    # ...

    # Read user choice
    # ...

    # Perform the selected action
    # ...

# Close the database connection
con.close()
