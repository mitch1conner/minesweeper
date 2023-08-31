from tkinter import Button
from tkinter import Label
import random
import settings_ms
import ctypes
import sys

class Cell:
    all=[]
    cell_count=settings_ms.CELL_COUNT
    cell_count_label_obj=None
    def __init__(self,x,y,is_mine=False):
        self.is_mine=is_mine
        self.cell_btn_object=None
        self.x=x
        self.y=y
        self.is_opened=False
        self.is_mine_candidate=False
        Cell.all.append(self)
    def create_btn_obj(self,location,):
        btn=Button(location,
                   height=4
                   ,width=8)
        self.cell_btn_object=btn
        
        #bind= binds referenced action with function
        #'<Button-1>=left click
        # Not calling the function only referencing so no ()
        #after method 
        
        btn.bind('<Button-1>',self.left_click_actions) 
        btn.bind('<Button-3>',self.right_click_actions)
    
    @staticmethod
    def create_cell_count_label(location):
        lbl=Label(location,bg="#263b39",fg="white",text=f"Cells Left:{Cell.cell_count}",width=12,height=12)
        Cell.cell_count_label_obj=lbl
    
    def left_click_actions(self,event): 
        #one more additional parameter
        #event carries meta data
        #<ButtonPress event state=Mod1 num=1 x=19 y=15>
        
        if self.is_mine:
            self.show_mine()
        else:
            if self.surrounded_cells_mine_length==0:
                for cell_obj in self.surrounded_cells:
                    cell_obj.show_cell()

            self.show_cell()
        if Cell.cell_count==settings_ms.MINES_COUNT:
            ctypes.windll.user32.MessageBoxW(0,'Congratulations!',"Game Over",0)
        #Cancel Left and Right Click Actions if cell is already opened:
        self.cell_btn_object.unbind('<Button-1>')
        self.cell_btn_object.unbind('<Button-3>')
    def get_cell_axes(self,x,y):
        #Return a cell object based on the values of x and y
        for cell in Cell.all:
            if cell.x== x and cell.y==y:
                return cell
    
    
    @property
    def surrounded_cells(self):
        cells=[
        self.get_cell_axes(self.x-1,self.y-1),
        self.get_cell_axes(self.x-1,self.y),
        self.get_cell_axes(self.x-1,self.y+1),
        self.get_cell_axes(self.x,self.y-1),
        self.get_cell_axes(self.x+1,self.y-1),
        self.get_cell_axes(self.x+1,self.y),
        self.get_cell_axes(self.x+1,self.y+1),
        self.get_cell_axes(self.x,self.y+1)                  
                          ]
        cells=[cell for cell in cells if cell is not None]
        return cells
    
    def show_cell(self):
        if not self.is_opened:
            Cell.cell_count -=1
            self.cell_btn_object.configure(text=self.surrounded_cells_mine_length)
            #Replace the text of cell count label with newer count
            if Cell.cell_count_label_obj:
                Cell.cell_count_label_obj.configure(text=f"Cells Left:{Cell.cell_count}")
            self.cell_btn_object.configure(bg='SystemButtonFace')
        #Mark the Cell as opened
        self.is_opened=True
    @property
    def surrounded_cells_mine_length(self):
        counter=0
        for cell in self.surrounded_cells:
            if cell.is_mine:
                counter+=1
        return counter   
    
    def show_mine(self):
        self.cell_btn_object.configure(bg="red")
        ctypes.windll.user32.MessageBoxW(0,"You clicked on the mine","Game Over",0)
        sys.exit()
    def right_click_actions(self,event):
        if not self.is_mine_candidate:
            self.cell_btn_object.configure(bg="blue")
            self.is_mine_candidate=True
        else:
            self.cell_btn_object.configure(bg="SystemButtonFace")
            self.is_mine_candidate=False

    @staticmethod
    def randomize_mines():
        #sample method 
        #random.sample(list or etc,amount
        picked_cells=random.sample(Cell.all,settings_ms.MINES_COUNT)
        for picked_cell in picked_cells:
            picked_cell.is_mine=True
    
    def __repr__(self):
        return f"Cell({self.x},{self.y})"
    