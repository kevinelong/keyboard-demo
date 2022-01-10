import curses
import sys


class CursesInterface:
    data = {
        8: "BACKSPACE",
        9: "\t",
        10: "\r\n",
        27: "ESCAPE",
        258: "DOWN",
        259: "UP",
        260: "LEFT",
        261: "RIGHT",
        262: "HOME",
        263: "DELETE",
        331: "INSERT",
        338: "PAGE_DOWN",
        339: "PAGE_UP",
        353: "BACK_TAB",
        360: "END",
    }

    def __init__(self):
        self.screen = curses.initscr()
        curses.noecho()
        curses.cbreak()
        self.screen.keypad(True)

    def get_key(self):
        k = self.screen.getch()
        if k in self.data:
            return self.data[k]
        if k >= ord(" ") and k <= ord("~"):
            return chr(k)
        return f"{k}"

    def restore(self):
        curses.nocbreak()
        self.screen.keypad(0)
        curses.echo()
        curses.endwin()


ci = CursesInterface()
quitting = False
while not quitting:
    key = ci.get_key()
    print(key, end="")
    sys.stdout.flush()
ci.restore()
