import tkinter as tk
from tkinter import ttk

class BottomButtonsFrame(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.btn_row = ttk.Button(self, text="Config")
        self.btn_row.grid(column=0, row=0, sticky="W")
        self.load_button = ttk.Button(self, text="Load")
        self.load_button.grid(column=0, row=1, sticky="E")