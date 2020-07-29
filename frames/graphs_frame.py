import math
import matplotlib.pyplot as plt
import tkinter as tk
import pandas as pd

from tkinter import ttk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)

class GraphsFrame(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        # read csv file and labels columns
        df_czt = pd.read_csv('data_tiny.dat', header=None, sep='\s+', engine='python')
        df_czt.columns = ['node', 'board', 'Rena', 'channel', 'polarity', 'ADC_e', 'ADC_s', 'ADC_v', 'counter']

        print(df_czt.head())

        # grouping by multiple columns
        grouped = df_czt.groupby(['node', 'board', 'Rena', 'channel', 'polarity'])

        n_sub_plots_cols = 1
        n_sub_plots_rows = math.ceil(grouped.ngroups / n_sub_plots_cols)

        fig, axes = plt.subplots(n_sub_plots_rows, figsize=(30, 30), dpi=100)
        fig.subplots_adjust(hspace=0.5, wspace=0, left=0.1, bottom=0.07, right=0.98, top=0.97)
        axes_list = [item for item in axes]

        # plot column ADC energy
        for key, group in grouped:
            ax = axes_list.pop(0)

            grouped.get_group(key)['ADC_e'].plot(kind='hist', bins=50, ax=ax)

            czt_values = grouped.get_group(key).values[0]

            # min and max
            max_val = grouped.get_group(key)['ADC_e'].max()
            min_val = grouped.get_group(key)['ADC_e'].min()
            y_min, y_max = ax.get_ylim()
            ax.annotate('Max: ' +str(max_val), xy=(3, y_max -(y_max * 0.1)), size=6)
            ax.annotate('Min: ' +str(min_val), xy=(3, y_max -(y_max * 0.2)), size=6)

            # titles
            title = "Node:" + str(czt_values[0]) + " Board:" + str(czt_values[1]) + " Rena:" + str(
                czt_values[2]) + " Channel:" + str(czt_values[3])
            ax.set_title(title, fontsize=6)

            # x and y axis labels
            ax.set_xlabel("ADC value", fontsize=6)
            ax.set_ylabel("Counts", fontsize=6)

            ax.tick_params(labelsize=6)

            ax.autoscale(enable=True, axis='y', tight=False)
            ax.set_xlim(left=0)

            # anode or cathode
            if czt_values[4] == 0:
                ax.set_xlim(right=3450)
            else:
                if czt_values[2] == 1:
                    ax.set_xlim(right=500)
                else:
                    ax.set_xlim(right=650)

        for ax in axes_list:
            ax.remove()

        canvas = FigureCanvasTkAgg(fig, self)
        canvas.get_tk_widget().pack(side="top",fill='both',expand=True)
        # canvas.get_tk_widget().grid(sticky="NSEW")
