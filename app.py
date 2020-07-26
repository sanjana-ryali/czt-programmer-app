import tkinter as tk
from tkinter import ttk
from frames import AppWindow

class CZTProgrammerAppWindow(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.geometry("1000x800")
        #self.minsize(500, 400)

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