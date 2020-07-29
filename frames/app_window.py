import tkinter as tk
from tkinter import ttk
from .graphs_frame import GraphsFrame
from .bottom_buttons_frame import BottomButtonsFrame
from .scrollable_graphs_window import ScrollableGraphsWindow


class AppWindow(ttk.Frame):

    def __init__(self, parent):
        super().__init__(parent)

        self.rowconfigure(0, weight=0)
        self.rowconfigure(1, weight=1)

        # add graph window

        # Left Graph Column widgets
        self.spin_box_frame1 = ttk.Frame(self)
        self.spin_box_frame1.grid(column=0, row=0, pady=(10, 10))
        self.create_node_spin_box(self.spin_box_frame1)
        self.create_board_spin_box(self.spin_box_frame1)

        self.left_graph_frame = ttk.Frame(self)
        self.left_graph_frame.grid(column=0, row=1)

        self.scroll_frame1 = ScrollableGraphsWindow(self.left_graph_frame, "nw")
        self.scroll_frame1.grid(column=0, row=0, sticky="NSEW")

        self.scroll_frame1.update_graphs()

        # Middle Column widgets (un-zoom buttons and spinbox)
        self.middle_frame = ttk.Frame(self)
        self.middle_frame.grid(column=1, row=1)

        self.unzoom_button_top_left = ttk.Button(self.middle_frame, text="Unzoom")
        self.unzoom_button_top_left.grid(column=0, row=0, sticky="NW", pady=(0, 250))

        self.unzoom_button_top_right = ttk.Button(self.middle_frame, text="Unzoom")
        self.unzoom_button_top_right.grid(column=1, row=0, sticky="NE", pady=(0, 250))

        self.plotuv_spinbox_frame = ttk.Frame(self.middle_frame)
        self.plotuv_spinbox_frame.grid(column=0, row=1, sticky="EW", columnspan=2, pady=(0, 250))
        self.create_leftcol_spin_box(self.plotuv_spinbox_frame)
        self.create_rightcol_spin_box(self.plotuv_spinbox_frame)
        selected_option = tk.StringVar()
        self.plotuv_checkbutton = ttk.Checkbutton(
            self.plotuv_spinbox_frame,
            text="Plot UV",
            onvalue="On",
            offvalue="Off",
            variable=selected_option
        )
        self.plotuv_checkbutton.grid(row=2, columnspan=2)

        self.unzoom_button_bottom_left = ttk.Button(self.middle_frame, text="Unzoom")
        self.unzoom_button_bottom_left.grid(column=0, row=2, sticky="SW")

        self.unzoom_button_bottom_right = ttk.Button(self.middle_frame, text="Unzoom")
        self.unzoom_button_bottom_right.grid(column=1, row=2, sticky="SE")

        # Right Graph column widgets
        self.spin_box_frame1 = ttk.Frame(self)
        self.spin_box_frame1.grid(column=2, row=0, pady=(10, 10))
        self.create_node_spin_box(self.spin_box_frame1)
        self.create_board_spin_box(self.spin_box_frame1)

        self.right_graph_frame = ttk.Frame(self)
        self.right_graph_frame.grid(column=2, row=1)

        self.scroll_frame2 = ScrollableGraphsWindow(self.right_graph_frame, "nw")
        self.scroll_frame2.grid(column=0, row=0, sticky="NSEW")

        self.scroll_frame2.update_graphs()

        # Bottom buttons frame spanning 3 columns
        self.bottom_frame = BottomButtonsFrame(self)
        self.bottom_frame.grid(column=0, row=3, columnspan=3, sticky="NSEW")

    def create_node_spin_box(self, graph_frame):
        n_spinbox_label = ttk.Label(graph_frame, text="Node: ")
        n_spinbox_label.grid(row=0, column=0)

        initial_value = tk.StringVar(value=2)
        n_spin_box = tk.Spinbox(
            graph_frame,
            from_=0,
            to=30,
            textvariable=initial_value,
            width=3,
            wrap=False)
        n_spin_box.grid(row=0, column=1)

    def create_board_spin_box(self, graph_frame):
        b_spinbox_label = ttk.Label(graph_frame, text="Board: ")
        b_spinbox_label.grid(row=0, column=2)

        initial_value = tk.StringVar(value=3)
        b_spin_box = tk.Spinbox(
            graph_frame,
            from_=0,
            to=30,
            textvariable=initial_value,
            width=3,
            wrap=False)
        b_spin_box.grid(row=0, column=3)

    def create_leftcol_spin_box(self, plotuv_frame):
        n_spinbox_label = ttk.Label(plotuv_frame, text="Left Col:")
        n_spinbox_label.grid(row=0, column=0, padx=(0, 20))

        initial_value = tk.StringVar(value=2)
        n_spin_box = tk.Spinbox(
            plotuv_frame,
            from_=0,
            to=30,
            textvariable=initial_value,
            width=3,
            wrap=False)
        n_spin_box.grid(row=1, column=0, padx=(0, 30))

    def create_rightcol_spin_box(self, plotuv_frame):
        n_spinbox_label = ttk.Label(plotuv_frame, text="Right Col:")
        n_spinbox_label.grid(row=0, column=1, padx=(20, 0))

        initial_value = tk.StringVar(value=2)
        n_spin_box = tk.Spinbox(
            plotuv_frame,
            from_=0,
            to=30,
            textvariable=initial_value,
            width=3,
            wrap=False)
        n_spin_box.grid(row=1, column=1, padx=(30, 0))
