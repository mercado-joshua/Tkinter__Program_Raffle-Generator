#===========================
# Imports
#===========================

import tkinter as tk
from tkinter import ttk, colorchooser, Menu, Spinbox, scrolledtext, messagebox as mb, filedialog as fd

from random import randint

#===========================
# Main App
#===========================

class App(tk.Tk):
    """Main Application."""

    #===========================================
    def __init__(self):
        super().__init__()

        self.init_config()
        self.init_UI()

    #===========================================
    def init_config(self):
        self.resizable(False, False)
        self.title('Raffle Generator Version 1.0')
        self.style = ttk.Style(self)
        self.style.theme_use('clam')

    def init_UI(self):
        self.frame = ttk.Frame(self)
        self.frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        button = ttk.Button(self.frame, text='pick', command=self.pick)
        button.pack()

        self.winner = tk.StringVar()
        label = ttk.Label(self.frame, font=('Helvatica', 24), textvariable=self.winner)
        label.pack()

    # ------------------------------------------
    def pick(self):
        entries = ['joshua mercado', 'aljon valen', 'joshua mercado', 'richard dayrit', 'aeroll tiosen', 'ronnel garino']

        unique_entries = list(set(entries))

        print(entries)
        print(unique_entries)

        total_entries = len(unique_entries) - 1
        pick = randint(0, total_entries)

        self.winner.set(unique_entries[pick])

#===========================
# Start GUI
#===========================

def main():
    app = App()
    app.mainloop()

if __name__ == '__main__':
    main()