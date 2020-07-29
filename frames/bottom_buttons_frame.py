import tkinter as tk
from tkinter import ttk


class BottomButtonsFrame(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.left_frame = ttk.Frame(self)
        self.left_frame.grid(column=0, row=0, sticky="W", padx=(10, 50))

        self.config_label = ttk.Label(self.left_frame, text="Config File: ")
        self.config_label.grid(column=0, row=0, sticky="NSEW")
        self.config_file = ttk.Entry(self.left_frame, width=15)
        self.config_file.grid(column=1, row=0, sticky="NSEW", columnspan=2, padx=(10, 30))

        self.data_label = ttk.Label(self.left_frame, text="Data File: ")
        self.data_label.grid(column=0, row=1, sticky="NSEW")
        self.data_file = ttk.Entry(self.left_frame, width=8)
        self.data_file.grid(column=1, row=1, sticky="NSEW", padx=(10, 0))

        self.load_button = ttk.Button(self.left_frame, text="Load")
        self.load_button.grid(column=2, row=1, sticky="NSEW", padx=(0, 30))

        self.middle_frame = ttk.Frame(self)
        self.middle_frame.grid(column=1, row=0)

        self.log_label = ttk.Label(self.middle_frame, text="Log: ")
        self.log_label.grid(column=0, row=0)

        self.log_textbox = tk.Text(self.middle_frame, width=55, height=3)
        self.log_textbox.grid(column=1, row=0, padx=(0, 50))
        self.log_textbox.config(borderwidth="5")

        self.right_frame = ttk.Frame(self)
        self.right_frame.grid(column=2, row=0, sticky="E")
        self.daqstart_button = ttk.Button(self.right_frame, text="DAQ Start")
        self.daqstart_button.grid(column=0, row=0, sticky="NSEW", pady=(5, 10))
        self.channeledit_button = ttk.Button(self.right_frame, text="Channel Edit")
        self.channeledit_button.grid(column=0, row=1, sticky="NSEW", pady=(0, 10))
        self.plot_button = ttk.Button(self.right_frame, text="Plot")
        self.plot_button.grid(column=0, row=2, sticky="NSEW", pady=(0, 10))
