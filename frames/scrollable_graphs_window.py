import tkinter as tk
from tkinter import ttk

from frames.graphs_frame import GraphsFrame


class ScrollableGraphsWindow(tk.Canvas):
    def __init__(self, container, *args, **kwargs):
        super().__init__(container, *args, **kwargs, highlightthickness=0)

        self.g_scr_frame = ttk.Frame(container)
        self.g_scr_frame.columnconfigure(0, weight=1)

        # scrollable_window grows when you add components to it
        self.scrollable_window = self.create_window((0, 0), window=self.g_scr_frame, anchor="nw")
        self.config(borderwidth="5", relief="ridge", width="400", height="650")

        def configure_scroll_region(event):
            self.configure(scrollregion=self.bbox("all"))

        def configure_window_size(event):
            self.itemconfig(self.scrollable_window, width=self.winfo_width())

        self.bind("<Configure>", configure_window_size)
        self.g_scr_frame.bind("<Configure>", configure_scroll_region)
        self.bind_all("<MouseWheel>", self._on_mousewheel)

        scrollbar = ttk.Scrollbar(container, orient="vertical", command=self.yview)
        scrollbar.grid(row=0, column=1, sticky="NS")

        self.configure(yscrollcommand=scrollbar.set)
        self.yview_moveto(1.0)

        # https://stackoverflow.com/a/17457843/1587271

    def _on_mousewheel(self, event):
        self.yview_scroll(-int(event.delta / 120), "units")

    def update_graphs(self):
        # TO-DO add a check to see if graphs exists
        container = ttk.Frame(self.g_scr_frame)
        container.columnconfigure(0, weight=1)
        container.grid(column=0, row=0, sticky="NSEW")

        graphs_frame_1 = GraphsFrame(container)
        graphs_frame_1.grid(column=0, row=0, sticky="NSEW")

        graphs_frame_3 = GraphsFrame(container)
        graphs_frame_3.grid(column=0, row=1, sticky="NSEW")

        graphs_frame_5 = GraphsFrame(container)
        graphs_frame_5.grid(column=0, row=2, sticky="NSEW")

