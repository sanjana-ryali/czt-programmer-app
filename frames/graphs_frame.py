import tkinter as tk
import pandas as pd

from tkinter import ttk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)

class GraphsFrame(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        fig = Figure(figsize=(4, 3), dpi=100)

        df_tips = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv')

        print(df_tips.head())
        fig.add_subplot(111).hist(df_tips['tip'], bins=5)

        canvas = FigureCanvasTkAgg(fig, self)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)
