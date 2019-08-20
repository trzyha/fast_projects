import time
import tkinter as tk

WIDTH = 400
HEIGHT = 400
WHITE = '#ffffff'
HOUR_COLOR = '#4000bf'
MIN_COLOR = '#73008c'
SEC_COLOR = '#a60059'

empty_center = 80
step = 30
oval_sec_size = empty_center+step
oval_min_size = oval_sec_size+step
oval_hour_size = oval_min_size+step


global sec_jump
sec_jump = 0
init_sec = time.strftime('%S')
init_sec = int(init_sec)*6
print(init_sec)


root = tk.Tk()
root.configure(background=WHITE)
canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, background=WHITE)
canvas.pack()


def tick(time1=''):
    # get the current local time from the PC
    time2 = time.strftime('%H:%M:%S')
    add_sec = time.strftime('%S')
    add_sec = int(add_sec)*6

    add_min = time.strftime('%M')
    add_min = int(add_min)*6

    add_hour = time.strftime('%H')
    add_hour = int(add_hour)*30
    
    hour_arc = canvas.create_arc(WIDTH/2-oval_hour_size, HEIGHT/2-oval_hour_size, WIDTH/2+oval_hour_size,HEIGHT/2+oval_hour_size,
                                 start=90, extent=-add_hour, fill=HOUR_COLOR, outline=HOUR_COLOR, style='', width=0)
    min_arc = canvas.create_arc(WIDTH/2-oval_min_size, HEIGHT/2-oval_min_size, WIDTH/2+oval_min_size,HEIGHT/2+oval_min_size,
                                 start=90, extent=-add_min, fill=MIN_COLOR, outline=MIN_COLOR, style='', width=0)
    sec_arc = canvas.create_arc(WIDTH/2-oval_sec_size, HEIGHT/2-oval_sec_size, WIDTH/2+oval_sec_size,HEIGHT/2+oval_sec_size,
                                 start=90, extent=-add_sec, 
                                 fill=SEC_COLOR, outline=SEC_COLOR, style='', width=0)
       

    canvas.create_oval(WIDTH/2-empty_center, HEIGHT/2-empty_center, WIDTH/2+empty_center, HEIGHT/2+empty_center, fill=WHITE, outline=WHITE)
    # if time string has changed, update it
    if time2 != time1:
        time1 = time2
        clock.config(text=time2)
        # add_sec = int(add_sec)*6
        if add_sec==0:
            canvas.itemconfigure(sec_arc, fill='white', outline='white', start=90, extent=-359)
            root.update()
        elif add_min==0:
            canvas.itemconfigure(min_arc, fill='white', outline='white', start=90, extent=-359)
            root.update()
        elif add_hour==0:
            canvas.itemconfigure(hour_arc, fill='white', outline='white', start=90, extent=-359)
            root.update()
    clock.after(200, tick)
    root.update()

root.resizable(False, False)
clock = tk.Label(root, font=('times', 20, 'bold'), bg='white')
clock.pack()
canvas.create_window(WIDTH/2,HEIGHT/2, window=clock)


tick()
root.mainloop()