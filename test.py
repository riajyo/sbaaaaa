import curses
from curses import wrapper
from curses.textpad import Textbox , rectangle
import time

def abc(stdscr):
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
    print(Name,Category,List_id)

def bcd():
    print("Action for String 2 executed!")

def cde():
    print("Action for String 3 executed!")

def main(stdscr):
    # Clear the screen
    stdscr.clear()

    # Define the clickable strings and their coordinates
    functions = [
        {"text": "Click me 1!", "y": 1, "x": 0, "action": abc},
        {"text": "Click me 2!", "y": 3, "x": 0, "action": bcd},
        {"text": "Click me 3!", "y": 5, "x": 0, "action": cde},
    ]

    # Initialize colors
    curses.start_color()
    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLUE)  # Highlight color
    curses.curs_set(0)  # Hide the cursor

    current_selection = 0  # Track the currently selected string

    while True:
        # Clear the screen
        stdscr.clear()

        # Display the clickable strings
        for index, item in enumerate(functions):
            if index == current_selection:
                stdscr.attron(curses.color_pair(1))  # Apply highlight
                stdscr.addstr(item["y"], item["x"], item["text"], curses.A_BOLD)
                stdscr.attroff(curses.color_pair(1))  # Remove highlight
            else:
                stdscr.addstr(item["y"], item["x"], item["text"])

        stdscr.refresh()

        # Get user input
        key = stdscr.getch()

        # Handle user input
        if key == curses.KEY_UP:
            current_selection = (current_selection - 1) % len(functions)  # Move up in the list
        elif key == curses.KEY_DOWN:
            current_selection = (current_selection + 1) % len(functions)  # Move down in the list
        elif key == 10:  # Enter key
            # Call the action for the currently selected string
            functions[current_selection]["action"](stdscr)

        # Exit on pressing 'q' or 'ESC'
        if key in (ord('q'), 27):  # 27 is the escape key
            break

    # Wait for the user to press a key before exiting
    stdscr.getch()

# Run the curses application
curses.wrapper(main)