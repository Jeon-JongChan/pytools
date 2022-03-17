from tkinter import *
import time
from main import *

pos = []
def add_pos_input(idx):
    label = Label(tk, text=' pos')
    label.pack()
    entry = Entry(tk)
    entry.pack()

    temp = []
    temp.append(label)
    temp.append(entry)
    pos.append(temp)

def execute_macro():
    print(1)
tk = Tk()
tk.geometry('400x400')
# >>>>>>>>>> 개체 추가
title_label = Label(tk, text='A3 Inventory Clear')
title_label.pack()

# 현재 마우스 좌표
pos_text = StringVar()
pos_text.set("mouse position")
current_pos = Label(tk, textvariable=pos_text) 
current_pos.pack()

b1 = Button(tk, text='실행 좌표 수동 추가')
b1.pack()
b1.bind('<Button-1>', add_pos_input)

b2 = Button(tk, text='매크로 실행')
b2.pack()
b2.bind('<Button-2>', execute_macro)
# <<<<<<<<<<
# >>>>>>>>>> 디자인
#b1.grid(row=1, column=1, sticky='ew')
#b2.grid(row=1, column=2, sticky='ew')
# <<<<<<<<<<

def update_point():
    idx = 0
    while idx < 1000:
        text = check_point()
        pos_text.set(text)
        time.sleep(10)

tk.after(1000, update_point)

tk.mainloop()

