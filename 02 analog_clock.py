import time
import tkinter as tk

WIDTH = 400
HEIGHT = 400

oval_sec_size = 150
oval_min_size = 100
oval_hour_size = 80

global sec_jump
sec_jump = 0
init_sec = time.strftime('%S')
init_sec = int(init_sec)*6
print(init_sec)


root = tk.Tk()
root.configure(background='white')
canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT)
canvas.pack()


def tick(time1=''):
    # get the current local time from the PC
    time2 = time.strftime('%H:%M:%S')
    add_sec = time.strftime('%S')
    # if time string has changed, update it
    if time2 != time1:
        time1 = time2
        clock.config(text=time2)
        add_sec = int(add_sec)*6
        
    if add_sec>0:
        global sec_arc
        sec_arc = canvas.create_arc(WIDTH/2 - oval_sec_size, HEIGHT/2 - oval_sec_size, WIDTH/2 + oval_sec_size,HEIGHT/2 + oval_sec_size, start=90, extent=-add_sec, fill="red", outline='red', style='', width=1)
    else:
        canvas.delete(sec_arc)
        root.update()

            
            
    
    # calls itself every 200 milliseconds
    # to update the time display as needed
    clock.after(300, tick)


root.resizable(False, False)
clock = tk.Label(root, font=('times', 20, 'bold'), bg='white')
clock.pack()
canvas.create_window(WIDTH/2,HEIGHT/2, window=clock)

root.update()
tick()
root.mainloop()