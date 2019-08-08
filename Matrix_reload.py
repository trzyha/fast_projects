import tkinter as tk
from random import randrange
from time import sleep

pos_y = -20 
WIDTH = 400
HEIGHT = 400
BLACK = '#000000'
GREEN = '#99ff66'
GREEN_L = '#e6ffe6'
GREEN_D = '#009900'
GREEN_SHADES = ['#99ff99','#33ff33','#00cc00','#006600','#003300']
root = tk.Tk()
root.title("~-_-=MATRIX=-_-~")
root.geometry(f'{WIDTH}x{HEIGHT}')
root.minsize(width=WIDTH, height=HEIGHT)

canvas = tk.Canvas(root, width=800, height=600)
canvas.configure(background=BLACK)
canvas.pack()

class Matrix_text:
    def __init__(self):
        self.m_text = ''.join(str(chr(randrange(40,300))) for i in range(randrange(5,20)))
        self.m_text_print = canvas.create_text(randrange(5,HEIGHT-10),-120,anchor='nw',text="\n".join(self.m_text), fill=GREEN_SHADES[randrange(0,4)])
        self.yspeed = (randrange(0,20))

    def move(self):
        canvas.move(self.m_text_print, 0, self.yspeed)
        pos = canvas.coords(self.m_text_print)
        if pos[1] >= HEIGHT+200:
            canvas.move(self.m_text_print, 0, -HEIGHT-200+self.yspeed)

dropping_text = []
for i in range (50):
    dropping_text.append(Matrix_text())

while True:
    for dropp_text in dropping_text:
        dropp_text.move()
    root.update()
    sleep(0.001)

root.mainloop()
