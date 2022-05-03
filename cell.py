# -*- coding: utf-8 -*-
"""
Created on Mon Apr 25 21:20:27 2022

@author: Batman
"""
from tkinter import Button, Label
import random
import settings
import ctypes


class Cell:
    allCells = []
    cell_count = settings.CELLS_COUNT
    cell_count_label = None
    root = None

    def __init__(self, x, y, root, is_mine=False):
        self.is_mine = is_mine
        self.is_open = False
        self.is_mine_candidate = False
        self.btn = None
        self.x = x
        self.y = y
        Cell.root = root
        # Append cell to the list of cells
        Cell.allCells.append(self)

    def create_button(self, location):
        btn = Button(location,
                     width=settings.BUTTON_WIDTH,
                     height=settings.BUTTON_HEIGHT
                     # text = f'{self.x}, {self.y}'
                     )
        btn.bind('<Button-1>', self.left_click_action)
        btn.bind('<Button-3>', self.right_click_action)
        self.btn = btn

    @staticmethod
    def create_cell_count_label(location):
        lbl = Label(
                location,
                text=f"Cells left:\n{Cell.cell_count}",
                width=12,
                height=4,
                bg='salmon',
                font=('', 18)
                )
        Cell.cell_count_label = lbl

    def left_click_action(self, event):
        if not self.is_mine_candidate:
            if self.is_mine:
                self.show_mine()
            else:
                self.show_cell()
                # Check if the user already won the game
                if Cell.cell_count == settings.MINES_COUNT:
                    ctypes.windll.user32.MessageBoxW(0, 'You won!',
                                                     'Congratulations', 0)
                    Cell.root.destroy()

    def right_click_action(self, event):
        if not self.is_mine_candidate:
            self.btn.configure(bg='darkgreen')
            self.is_mine_candidate = not self.is_mine_candidate
        else:
            self.btn.configure(bg='SystemButtonFace')
            self.is_mine_candidate = not self.is_mine_candidate

    def show_mine(self):
        self.btn.configure(bg='red')
        ctypes.windll.user32.MessageBoxW(0, 'You fell on a mine!',
                                         'Game over', 0)
        Cell.root.destroy()
        # sys.exit()

    def get_cell_by_coords(self, x, y):
        for cell in Cell.allCells:
            if cell.x == x and cell.y == y:
                return cell
        return None

    @property
    def surrounding_cells(self):
        x = self.x
        y = self.y
        cells = [
                self.get_cell_by_coords(x - 1, y - 1),
                self.get_cell_by_coords(x - 1, y),
                self.get_cell_by_coords(x - 1, y + 1),
                self.get_cell_by_coords(x, y - 1),
                self.get_cell_by_coords(x + 1, y - 1),
                self.get_cell_by_coords(x + 1, y),
                self.get_cell_by_coords(x + 1, y + 1),
                self.get_cell_by_coords(x, y + 1)
            ]
        cells = [cell for cell in cells if cell is not None]
        return cells

    @property
    def surrounding_mines_count(self):
        mine_count = sum([cell.is_mine for cell in self.surrounding_cells])
        return mine_count

    def show_cell(self):
        if not self.is_open:
            self.is_open = True
            Cell.cell_count -= 1
            Cell.cell_count_label.configure(
                text=f"Cells left:\n{Cell.cell_count}"
            )
            self.btn.configure(text=self.surrounding_mines_count)
            self.btn.configure(bg='lightblue')
            if self.surrounding_mines_count == 0:
                for cell in self.surrounding_cells:
                    if not cell.is_mine_candidate and not cell.is_open:
                        cell.show_cell()
        # Cancell all button events
        self.btn.unbind('<Button-1>')
        self.btn.unbind('<Button-3>')

    @staticmethod
    def randomize_mines():
        mined_cells = random.sample(
                Cell.allCells,
                settings.MINES_COUNT
            )
        for cell in mined_cells:
            cell.is_mine = True

    def __repr__(self):
        return f'Cell({self.x}, {self.y})'
