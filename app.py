import tkinter as tk

root = tk.Tk()

root.geometry('800x400')
root.title("this is my smart file saver")

button = tk.Button(text='this is a button!', command=lambda : print('test'), height=5)
button.pack()

root.mainloop()