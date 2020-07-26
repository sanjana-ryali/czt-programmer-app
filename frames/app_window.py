import tkinter as tk
from tkinter import ttk
from .graphs_frame import GraphsFrame
from .bottom_buttons_frame import BottomButtonsFrame
from .scrollable_graphs_window import ScrollableGraphsWindow

class AppWindow(ttk.Frame):

    def __init__(self, parent):
        super().__init__(parent)

        self.rowconfigure(0, weight=1)

        # add graph window

        self.main_graph_frame1 = ttk.Frame(self)
        self.main_graph_frame1.grid(column=0, row=0, sticky="NSEW")

        self.scroll_frame1 = ScrollableGraphsWindow(self.main_graph_frame1)
        self.scroll_frame1.grid(column=0, row=0, sticky="NSEW")

        self.scroll_frame1.update_graphs()

        self.dummy_frame = ttk.Frame(self)
        self.dummy_frame.grid(column=1, row=0, sticky="NSEW")

        self.unzoom_button = ttk.Button(self.dummy_frame, text="Unzoom")
        self.unzoom_button.grid(column=0, row=0, sticky="EW")

        self.main_graph_frame2 = ttk.Frame(self)
        self.main_graph_frame2.grid(column=2, row=0, sticky="NSEW")

        self.scroll_frame2 = ScrollableGraphsWindow(self.main_graph_frame2)
        self.scroll_frame2.grid(column=0, row=0, sticky="NSEW")

        self.scroll_frame2.update_graphs()

        # add bottoms buttons frame
        self.bottom_frame = BottomButtonsFrame(self)
        self.bottom_frame.grid(column=0, row=1, columnspan=3, sticky="S")




