import tkinter as tk
from tkinter import ttk
import time

HEIGHT = 500
WIDTH = 400
root = tk.Tk()
root.title('Blockchain')

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH, bg='lavender')
canvas.pack()

photo = tk.PhotoImage(file='battery1.png')
label = tk.Label(root, image=photo, bg='lavender')
label.place(relx=0.1, rely=0.4, relheight=0.3, relwidth=0.2)

# background_image = tk.PhotoImage(file='background_image.png')
# background_label = tk.Label(root, image=background_image)
# background_label.place(x=0, y=0, relheight=0.5, relwidth=1)


low2_frame = tk.Frame(root, bg='lavender', bd=3)
low2_frame.place(relx=0.01, rely=0.029, relheight=0.099, relwidth=0.98)

background_image = tk.PhotoImage(file='text.png')
background_label = tk.Label(low2_frame, image=background_image)
background_label.place(x=0, y=0, relheight=1, relwidth=1)

frame = tk.Frame(root, bg='indianred', bd=2)
frame.place(relx=0.1, rely=0.13, relheight=0.1, relwidth=0.8)

entry = tk.Entry(frame, bg='white', font='Times 20')
entry.place(relx=0, rely=0, relheight=0.9, relwidth=0.7)

a = entry.get()


def first1(labels, b):
    l_frame = tk.Frame(root, bg='lavender', bd=1)
    l_frame.place(relx=0.55, rely=0.43, relheight=0.25, relwidth=0.15)
    # labels = [5, 4, 3, 2, 1]
    if b > 15 :
        label['text'] = 'Now battery have ' + str(b - 15) + ' units of energy'
    else:
        label['text'] = 'Now battery have 0 units of energy'

    for i in range(len(labels)):
        cur_label = tk.Label(l_frame, text=labels[i], bg='lavender', anchor='w', font='Times 12')
        cur_label.pack()


# def second2():
#     l_frame = tk.Frame(root, bg='lavender', bd=1)
#     l_frame.place(relx=0.55, rely=0.43, relheight=0.25, relwidth=0.15)
#     labels = [5, 4, 3, 2, 0]
#     label['text'] = 'Now battery have 0 units of energy'
#
#     for i in range(len(labels)):
#         cur_label = tk.Label(l_frame, text=labels[i], bg='lavender', anchor='w', font='Times 12')
#         cur_label.pack()
#
#
# def third3():
#     a = entry.get()
#     b = int(a)
#     l_frame = tk.Frame(root, bg='lavender', bd=1)
#     l_frame.place(relx=0.55, rely=0.43, relheight=0.25, relwidth=0.15)
#     labels = [5, 4, 3, b - 12, 0]
#     label['text'] = 'Now battery have 0 units of energy'
#
#     for i in range(len(labels)):
#         cur_label = tk.Label(l_frame, text=labels[i], bg='lavender', anchor='w', font='Times 12')
#         cur_label.pack()
#
#
# def forth4():
#     a = entry.get()
#     b = int(a)
#     l_frame = tk.Frame(root, bg='lavender', bd=1)
#     l_frame.place(relx=0.55, rely=0.43, relheight=0.25, relwidth=0.15)
#     labels = [5, 4, b - 9, 0, 0]
#     label['text'] = 'Now battery have 0 units of energy'
#
#     for i in range(len(labels)):
#         cur_label = tk.Label(l_frame, text=labels[i], bg='lavender', anchor='w', font='Times 12')
#         cur_label.pack()
#
#
# def fifth5():
#     a = entry.get()
#     b = int(a)
#     l_frame = tk.Frame(root, bg='lavender', bd=1)
#     l_frame.place(relx=0.55, rely=0.43, relheight=0.25, relwidth=0.15)
#     labels = [5, b - 5, 0, 0, 0]
#     label['text'] = 'Now battery have 0 units of energy'
#
#     for i in range(len(labels)):
#         cur_label = tk.Label(l_frame, text=labels[i], bg='lavender', anchor='w', font='Times 12')
#         cur_label.pack()
#
#
# def last(labels):
#     l_frame = tk.Frame(root, bg='lavender', bd=1)
#     l_frame.place(relx=0.55, rely=0.43, relheight=0.25, relwidth=0.15)
#     # labels = [4, 0, 0, 0, 0]
#     label['text'] = 'Now battery have 0 units of energy'
#
#     for i in range(len(labels)):
#         cur_label = tk.Label(l_frame, text=labels[i], bg='lavender', anchor='w', font='Times 12')
#         cur_label.pack()


def button_cliked():
    a = entry.get()
    b = int(a)
    while b >= 1:

        if b >= 15:
            print('15' + '  now battery have ' + str(b - 15) + ' units of energy')

            first1([5, 4, 3, 2, 1], b)


        if b >= 14 and b < 15:

            print(str(b) + ' now battery have 0 units of energy')
            first1([5, 4, 3, 2, 0], b)
            break
        b = b - 1
        time.sleep(1)
        # if b >= 12 and b < 14:
        #     print(str(b) + ' now battery have 0 units of energy')
        #     # third3()
        #
        # if b >= 9 and b < 12:
        #     print(str(b) + ' now battery have 0 units of energy')
        #     # forth4()
        #
        # if b >= 5 and b < 9:
        #     print(str(b) + ' now battery have 0 units of energy')
        #     # fifth5()
        #
        # if b < 5:
        #     print(str(b) + ' now battery have 0 units of energy')
        #     last([4, 0, 0, 0, 0])
        #
        # if b == 0:
        #     print('0 now battery have 0 units of energy')
        #     break
        #
        # b = b - 1
        # time.sleep(1)


low_frame = tk.Frame(root, bg='gray', bd=1)
low_frame.place(relx=0.12, rely=0.31, relheight=0.06, relwidth=0.74)

label = tk.Label(low_frame, text='Now battery have 0 units of energy', bg='white', anchor='nw', fg='blue',
                 font='Times 16')
label.pack()
# label.grid(row=1, column=2)

button = tk.Button(frame, text='Upload', bg='white', command=button_cliked)
button.place(relx=0.75, rely=0, relheight=0.95, relwidth=0.2)

lo_frame = tk.Frame(root, bg='lavender', bd=1)
lo_frame.place(relx=0.35, rely=0.43, relheight=0.25, relwidth=0.15)

labels = ["first-     ", "second-", "third-    ", "fourth-  ", "fifth-     "]

for i in range(len(labels)):
    cur_label = 'label' + str(i)  # label0, label1, label2 ...
    cur_label = tk.Label(lo_frame, text=labels[i], bg='lavender', anchor='w', font='Times 12')
    cur_label.pack()


def numbers(labels):
    l_frame = tk.Frame(root, bg='lavender', bd=1)
    l_frame.place(relx=0.55, rely=0.43, relheight=0.25, relwidth=0.15)
    labels = [0, 0, 0, 0, 0]
    for i in range(len(labels)):
        cur_label = tk.Label(l_frame, text=labels[i], bg='lavender', anchor='w', font='Times 12')
        cur_label.pack()


if __name__ == '__main__':
    root.mainloop()
