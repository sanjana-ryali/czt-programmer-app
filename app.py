import tkinter as tk
from tkinter import ttk
from frames import AppWindow

class CZTProgrammerAppWindow(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.geometry("1010x800")
        self.minsize(width=1010, height=800)
        self.maxsize(width=1010, height=800)
        self.title("RENA Programmer For CZT PET")

        container = ttk.Frame(self)
        container.grid(column=0, row=0, sticky="NSEW")

        app = AppWindow(container)
        app.grid(column=0, row=0, sticky="NSEW")

        menubar = tk.Menu(self)
        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label="New", command=self.donothing)
        filemenu.add_command(label="Open", command=self.donothing)
        filemenu.add_command(label="Save", command=self.donothing)
        filemenu.add_command(label="Save as...", command=self.donothing)
        filemenu.add_command(label="Close", command=self.quit)
        menubar.add_cascade(label="File", menu=filemenu)

        toolsmenu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Tools", menu=toolsmenu)

        self.config(menu=menubar)

    def donothing(self):
        print("Do nothing")

root = CZTProgrammerAppWindow()
root.mainloop()