import tkinter as tk 
HEIGHT = 220
WIDTH = 220
root = tk.Tk()

canvas = tk.Canvas(root,  height=HEIGHT, width=WIDTH, bg='black')
canvas.pack()

background_image = tk.PhotoImage(file='download.png')
background_label = tk.Label(root, image=background_image)
background_label.place(x=0, y=0, relheight=1, relwidth=1)

def button_cliked():
    label['text'] = str('soooo!')

def button_cliked1():
    label['text'] = str('1')
    
def button_cliked2():
    label['text'] = str('2')

def button_cliked3():
    label['text'] = str('3')

def button_cliked4():
    label['text'] = str('4')

def button_cliked5():
    label['text'] = str('5')

def button_cliked6():
    label['text'] = str('6')

def button_cliked7():
    label['text'] = str('7')

def button_cliked8():
    label['text'] = str('8')

def button_cliked9():
    label['text'] = str('9')


frame = tk.Frame(root, bg='gray', bd=3)
frame.place(relx=0.1, rely=0.2, relheight=0.15, relwidth=0.8)
'''
entry = tk.Entry(frame, bg='white', font=40)
entry.place( relheight=1, relwidth=0.6)
'''
button = tk.Button(frame, text='result', bg='blue', command=button_cliked)
button.place(relx=0.7, rely=0, relheight=1, relwidth=0.3)

label = tk.Label(frame, bg='white', anchor='nw')
label.place(relx=0 , rely=0 ,relheight=1, relwidth=0.65)

#lambda: button_cliked(entry.get())

lower_frame = tk.Frame(root, bg='gray', bd=5)
lower_frame.place(relx=0.1, rely=0.4, relheight=0.5, relwidth=0.8)

button = tk.Button(lower_frame, text='1', bg='blue', command=button_cliked1)
button.place(relheight=0.25, relwidth=0.15)

button = tk.Button(lower_frame, text='2', bg='blue', command=button_cliked2)
button.place(relx=0.2 , rely=0 ,relheight=0.25, relwidth=0.15)

button = tk.Button(lower_frame, text='3', bg='blue', command=button_cliked3)
button.place(relx=0.4, rely=0 ,relheight=0.25, relwidth=0.15)
#разделение   ---============================================================
button = tk.Button(lower_frame, text='4', bg='blue', command=button_cliked4)
button.place(relx=0 , rely=0.3 ,relheight=0.25, relwidth=0.15)

button = tk.Button(lower_frame, text='5', bg='blue', command=button_cliked5)
button.place(relx=0.2 , rely=0.3 ,relheight=0.25, relwidth=0.15)

button = tk.Button(lower_frame, text='6', bg='blue', command=button_cliked6)
button.place(relx=0.4 , rely=0.3 ,relheight=0.25, relwidth=0.15)
#разделение   ---============================================================
button = tk.Button(lower_frame, text='7', bg='blue', command=button_cliked7)
button.place(relx=0 , rely=0.6 ,relheight=0.25, relwidth=0.15)

button = tk.Button(lower_frame, text='8', bg='blue', command=button_cliked8)
button.place(relx=0.2 , rely=0.6 ,relheight=0.25, relwidth=0.15)

button = tk.Button(lower_frame, text='9', bg='blue', command=button_cliked9)
button.place(relx=0.4 , rely=0.6 ,relheight=0.25, relwidth=0.15)



root.mainloop()