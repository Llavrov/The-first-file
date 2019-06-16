import tkinter as tk 
HEIGHT = 220
WIDTH = 220
root = tk.Tk()

canvas = tk.Canvas(root,  height=HEIGHT, width=WIDTH, bg='black')
canvas.pack()

background_image = tk.PhotoImage(file='background_image.png')
background_label = tk.Label(root, image=background_image)
background_label.place(x=0, y=0, relheight=1, relwidth=1)

def button_cliked():
    num2 = int(label['text'])
    if b == "+":
        a = sm(num1, num2)
        label['text'] = str(a)
    elif b == "-":
        a = sub(num1, num2)
        label['text'] = str(a)
    elif b == "/":
        a = div(num1, num2)
        label['text'] = str(a)
    elif b == "*":
        a = mul(num1, num2)
        label['text'] = str(a)

      


def button_cliked1():
    label['text'] += str('1')

def button_cliked2():
    label['text'] += str('2')

def button_cliked3():
    label['text'] += str('3')

def button_cliked4():
    label['text'] += str('4')

def button_cliked5():
    label['text'] += str('5')

def button_cliked6():
    label['text'] += str('6')

def button_cliked7():
    label['text'] += str('7')

def button_cliked8():
    label['text'] += str('8')

def button_cliked9():
    label['text'] += str('9')

def button_cliked0():
    label['text'] += str('0')

def button_clikedzero():
    label['text'] = str('')


def button_clikedsub():
    global num1
    global b
    b = "-"
    num1 = int(label['text'])
    print(num1)
    label['text'] = str('')
    print(num1)

def button_clikedsm():
    global num1
    global b
    b = "+"
    num1 = int(label['text'])
    print(num1)
    label['text'] = str('')
    print(num1)

def button_clikeddiv():
    global num1
    global b
    b = "/"
    num1 = int(label['text'])
    print(num1)
    label['text'] = str('')
    print(num1)

def button_clikedmul():
    global num1
    global b
    b = "*"
    num1 = int(label['text'])
    print(num1)
    label['text'] = str('')
    print(num1)

def sm(x, y):
    return x + y

def div(x, y):
    return x / y

def sub(x, y):
    return x - y

def mul(x, y):
    return x * y



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

lower_frame = tk.Frame(root, bg='gray', bd=2.5)
lower_frame.place(relx=0.1, rely=0.4, relheight=0.5, relwidth=0.8)

button = tk.Button(lower_frame, text='1', bg='lightsteelblue', command=button_cliked1)
button.place(relheight=0.35, relwidth=0.25)

button = tk.Button(lower_frame, text='2', bg='lightsteelblue', command=button_cliked2)
button.place(relx=0.2 , rely=0 ,relheight=0.35, relwidth=0.25)

button = tk.Button(lower_frame, text='3', bg='lightsteelblue', command=button_cliked3)
button.place(relx=0.4, rely=0 ,relheight=0.35, relwidth=0.25)
#разделение   ---============================================================
button = tk.Button(lower_frame, text='4', bg='lightsteelblue', command=button_cliked4)
button.place(relx=0 , rely=0.3 ,relheight=0.35, relwidth=0.25)

button = tk.Button(lower_frame, text='5', bg='lightsteelblue', command=button_cliked5)
button.place(relx=0.2 , rely=0.3 ,relheight=0.35, relwidth=0.25)

button = tk.Button(lower_frame, text='6', bg='lightsteelblue', command=button_cliked6)
button.place(relx=0.4 , rely=0.3 ,relheight=0.35, relwidth=0.25)
#разделение   ---============================================================
button = tk.Button(lower_frame, text='7', bg='lightsteelblue', command=button_cliked7)
button.place(relx=0 , rely=0.6 ,relheight=0.35, relwidth=0.25)

button = tk.Button(lower_frame, text='8', bg='lightsteelblue', command=button_cliked8)
button.place(relx=0.2 , rely=0.6 ,relheight=0.35, relwidth=0.25)

button = tk.Button(lower_frame, text='9', bg='lightsteelblue', command=button_cliked9)
button.place(relx=0.4 , rely=0.6 ,relheight=0.35, relwidth=0.25)
#==============================================================================
button = tk.Button(lower_frame, text='0', bg='lightsteelblue', command=button_cliked0)
button.place(relx=0.7 , rely=0 ,relheight=0.35, relwidth=0.25)
#=============================
button = tk.Button(lower_frame, text='-', bg='lightsteelblue', command=button_clikedsub)
button.place(relx=0.7 , rely=0.35 ,relheight=0.25, relwidth=0.15)

button = tk.Button(lower_frame, text='+', bg='lightsteelblue', command=button_clikedsm)
button.place(relx=0.7 , rely=0.6 ,relheight=0.25, relwidth=0.15)

button = tk.Button(lower_frame, text='*', bg='lightsteelblue', command=button_clikedmul)
button.place(relx=0.85 , rely=0.35 ,relheight=0.25, relwidth=0.15)

button = tk.Button(lower_frame, text='/', bg='lightsteelblue', command=button_clikeddiv)
button.place(relx=0.85 , rely=0.6 ,relheight=0.25, relwidth=0.15)

#==========================
button = tk.Button(lower_frame, text='rep', bg='lightsteelblue', command=button_clikedzero)
button.place(relx=0.7 , rely=0.85 ,relheight=0.1, relwidth=0.30)

if __name__ == '__main__':
    root.mainloop()