# -*- coding: utf-8 -*-
"""
Created on Mon Apr 25 20:44:46 2022

@author: Batman
"""

from tkinter import *
import settings
import utils
from cell import Cell

root = Tk()
# Settings for the window
root.configure(bg='black')
root.geometry(f'{settings.WIDTH}x{settings.HEIGHT}')
root.title("Cut's MineSweeper")
root.resizable(False, False)

top_frame = Frame(root,
                  bg='lightblue',
                  width=settings.WIDTH,
                  height=utils.height_prct(25)
                  )
top_frame.place(x=0, y=0)

game_title = Label(
        top_frame,
        bg='lightblue',
        fg='black',
        text="Cut's MineSweeper",
        font=('', 48)
    )
game_title.place(
        x=utils.width_prct(12),
        y=utils.height_prct(5)
    )

left_frame = Frame(root,
                   bg='salmon',       # Change later to black
                   width=utils.width_prct(25),
                   height=utils.height_prct(75)
                   )
left_frame.place(x=0, y=utils.height_prct(25))

center_frame = Frame(root,
                     bg='yellow',     # Change later to black
                     width=utils.width_prct(75),
                     height=utils.height_prct(75)
                     )
center_frame.place(
    x=utils.width_prct(25),
    y=utils.height_prct(25)
)

for x in range(settings.GRID_SIZE):
    for y in range(settings.GRID_SIZE):
        c = Cell(x, y, root)
        c.create_button(center_frame)
        c.btn.grid(column=x, row=y)

Cell.create_cell_count_label(left_frame)
Cell.cell_count_label.place(x=0, y=0)

Cell.randomize_mines()

# Run the window
root.mainloop()
