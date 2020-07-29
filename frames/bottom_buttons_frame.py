import tkinter as tk
from tkinter import ttk

class BottomButtonsFrame(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.left_frame = ttk.Frame(self)
        self.left_frame.grid(column=0, row=0, sticky="NW")

        self.config_label= ttk.Label(self.left_frame, text="Config File:")
        self.config_label.grid(column=0, row=0, sticky="NW")
        self.config_file = ttk.Entry(self.left_frame, width=15)
        self.config_file.grid(column =1, row=0, sticky="NW")

        self.data_label = ttk.Label(self.left_frame, text="Data File:")
        self.data_label.grid(column=0, row=1, sticky="NW")
        self.data_file = ttk.Entry(self.left_frame, width=15)
        self.data_file.grid(column=1, row=1, sticky="NW")

        self.load_button = ttk.Button(self.left_frame, text="Load")
        self.load_button.grid(column=0, row=2, sticky="NW")

        self.middle_frame = ttk.Frame(self)
        self.middle_frame.grid(column=1, row=0, sticky="NSEW")
s
        self.log_label = ttk.Label(self.middle_frame, text="Log")
        self.log_label.grid(column=0, row=0, sticky="NW")

        self.log_textbox = tk.Text(self.middle_frame, width=15, height=3)
        self.log_textbox.grid(column=1, row=0)
        self.log_textbox.config(borderwidth="5")


        self.right_frame = ttk.Frame(self)
        self.right_frame.grid(column=2, row=0, sticky="NSEW")
        self.daqstart_button = ttk.Button(self.right_frame, text="DAQ Start")
        self.daqstart_button.grid(column=0, row=0, sticky="NW")
        self.channeledit_button = ttk.Button(self.right_frame, text="Channel Edit")
        self.channeledit_button.grid(column=0, row=1, sticky="NW")
        self.plot_button = ttk.Button(self.right_frame, text="Plot")
        self.plot_button.grid(column=0, row=2, sticky="NW")




        ''' self.btn_row = ttk.Button(self, text="Config")
        self.btn_row.grid(column=0, row=0, sticky="W")
        self.load_button = ttk.Button(self, text="Load")
        self.load_button.grid(column=0, row=1, sticky="E") '''