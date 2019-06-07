'''
from tkinter import *

root = Tk()
root.title("Hello World!")
root.geometry('300x40')

def button_clicked():
    print("Hello World!")

def close():
    root.destroy()
    root.quit()

button = Button(root, text="Press Me", command=button_clicked)
button.pack(fill=BOTH)

root.protocol('WM_DELETE_WINDOW', close)
root.mainloop()
'''
import tkinter as tk
HEIGHT = 400
WIDTH = 400
root = tk.Tk()

canvas = tk.Canvas(root,  height=HEIGHT, width=WIDTH)
canvas.pack()# размер окна 

frame = tk.Frame(root, bg="#00FFFF", bd=5)
frame.place(relx=0.15, rely=0.15, relwidth=0.7, relheight=0.15, )
def button_clicked():
    print("Hello World!")

entry = tk.Entry(frame, font=40)
entry.place(relx=0.05, rely=0.12, relwidth=0.3, relheight=0.85) #поле для ввода текста

button = tk.Button(frame, text="touch me", font=40, command=button_clicked)
button.place(relx=0.45, rely=0.17, relwidth=0.45, relheight=0.75) 

'''
button = tk.Button(frame, text="The second", bg="white")
button.place(relx=0.75, rely=0.2, relwidth=0.35, relheight=0.4)

button = tk.Button(frame, text="The first", bg="blue")
button.place(relx=0.2, rely=0.2, relwidth=0.2, relheight=0.2)

button = tk.Button(frame, text="oops!", bg="green")
button.place(relx=0.4, rely=0.4, relwidth=0.2, relheight=0.2) 

button = tk.Button(frame, text="it is crasyy!", bg="black", fg='white')
button.place(relx=0.6, rely=0.4, relwidth=0.2, relheight=0.2)

button = tk.Button(frame, text="The third", bg="orange")
button.place(relx=0.2, rely=0.4, relwidth=0.2, relheight=0.2)

checkbutton = tk.Checkbutton(frame, text='1', bg='green')
checkbutton.pack(side='left', fill='both')#окошко для голосования 

label = tk.Label(frame, text='so, what this happend ?' , bg='blue')
label.grid(row='0', column='0') #поле для ввывода текста

entry = tk.Entry(frame, bg='orange')
entry.grid(row='1', column='0') #поле для ввода текста
'''

root.mainloop()

