import curses
from curses import wrapper
from curses.textpad import Textbox , rectangle
import time

x , y = 0, 0
def main(stdscr):

    curses.echo()
    win = curses.newwin(3,18,2,2)
    box = Textbox(win)
    rectangle(stdscr, 2, 2 ,10,10)

    stdscr.refresh()
    
    box.edit()
    text = box.gather().strip().replace("\n","")

    stdscr.getch()

   


wrapper(main)