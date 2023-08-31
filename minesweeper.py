from tkinter import *
from tkinter import Label
import settings_ms
import utils 
from cell import Cell
import ctypes
from PIL import Image, ImageTk
import photoedit
#instantion of tkinter
root=Tk()       



#Override Settings
#Page width and length --> 'WidthxLength'
root.geometry(f'{settings_ms.WIDTH}x{settings_ms.HEIGHT}') 
#Changing the title of the page
root.title('Minesweeper Game')
#Setting the page to unrotatable one for width other for length
root.resizable(False, False) 
#background change
root.configure(bg="red")
top_frame=Frame(root, bg='black' ,width=settings_ms.WIDTH, height=utils.height_prct(25))
top_frame.place(x=0,y=0) #starting points

game_title=Label(top_frame,bg='black',fg='white',text='Minesweeper Game', font=('Arial',36))
game_title.place(x=utils.width_prct(25),y=0)

left_frame= Frame(root,bg='#263b39',width=utils.width_prct(25),height=utils.height_prct(75))
left_frame.place(x=0 ,y=180)

center_frame=Frame(root,bg="#57b991",width=utils.width_prct(75),height=utils.height_prct(75))
center_frame.place(x=utils.width_prct(25),y=utils.height_prct(25))
image_path = 'C:\\Users\\Administrator\\Desktop\\theme2.png'

# Yeni genişlik ve yükseklik
new_width = 1440
new_height = 200

# Resmi aç ve yeniden boyutlandır
image = Image.open(image_path)
resized_image = image.resize((new_width, new_height))

# Resmi Tkinter için uygun hale getirin
photo = ImageTk.PhotoImage(resized_image)

# Resmi bir etiket (Label) içinde frame'e ekleyin
label_img = Label(top_frame, image=photo)
label_img.photo = photo  # PhotoImage nesnesini korumak için bu satırı ekleyin
label_img.place(x=0, y=0)  # x ve y, resmin konumunu belirtir


for x in range(settings_ms.ROW):
    for y in range(settings_ms.COLUMN):
        c=Cell(x,y)#Coordinate indexing
        c.create_btn_obj(center_frame)
        c.cell_btn_object.grid(row=y,column=x)

Cell.create_cell_count_label(left_frame)
Cell.cell_count_label_obj.place(x=0,y=0)
Cell.randomize_mines()


#buttn1=Button(center_frame , bg="blue",text='First Button')
#buttn1.place(x=0,y=0)
#c1=Cell(x,y)
#c1.create_btn_obj(center_frame)
#c1.cell_btn_object.grid(column=0,row=0)
#c2=Cell()
#c2.create_btn_obj(center_frame)
#c2.cell_btn_object.grid(column=1,row=0)

root.mainloop()