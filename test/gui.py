from tkinter import *

def resize(ev=None):
	label.config(font='Helvetica -%d bold' %scale.get())

top = Tk()
top.geometry('250x150')

label = Label(top, text='hello world', font='Helvetica -12 bold')
label.pack(fill=Y, expand=1)    #使用pack管理

scale = Scale(top, from_=10, to=40, orient=HORIZONTAL, command=resize)
scale.set(12)
scale.pack(fill=X,expand=1)

quit = Button(top, text='QUIT', command=top.quit, bg='red', fg='white')
quit.pack(fill=X, expand=1)
mainloop()