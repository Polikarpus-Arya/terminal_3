from tkinter import *

def cetak(c):
	text.config(state = NORMAL)
	c = str(c) + '\n'
	text.insert(END, c)
	text.config(state = DISABLED)

def com(self):
	if entry.get() == 'print':
		cetak("HAI")
	elif entry.get() == 'exit':
		exit()
	else:
		cetak(1 + 1)
	entry.delete(0, END)

window = Tk()

text = Text(window, font = ('hack', 11), height = 25, state = DISABLED)

entry = Entry(window, font = ('Cascadia', 16), bg = 'black', fg = 'white')
entry.bind('<Return>', com)
text.pack()
entry.pack()

window.mainloop()