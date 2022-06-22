from tkinter import *
from gui_mod import *

import subprocess
import os
import _init
import time

_init.init()

# Check whether some username exist
query = 'create' if len(os.listdir('database/user/')) == 1 else 'login'

valid = True

while True:
	# Login or create account
	valid = _init.login() if query == 'login' else _init.create_account()

	if valid == True:
		break
	elif valid == None:
		exit()
	else:
		if query == 'create':
			query = 'login'
		else:
			query = 'create'

print(_init.main_user.getUName())
print(_init.main_user.getPassword())

def _print(args, end = '\n'):
	oShell.insert(END, args + end)

def exe_command(event):
	args = query_box.get('1.0', 'end-1c')
	query_box.delete('1.0', END)
	args = args.replace('\n', '')
	_print(args)
	_print(args)
	_print('\n' + _init.main_user.getUName() + ' -$ ', end = '')
	oShell.see(END)
	print(args)

def update_clock():
	digi = time.strftime('[%A] %H:%M:%S', time.localtime())
	clock.config(text = digi)
	clock.after(1000, update_clock)

def update_char(event):
	char_stat.config(text = conv_char(event.keysym))

def change_font_size(event, change):
	global gui_fg_size
	if change == -1:
		if gui_fg_size > 1:
			gui_fg_size += change
	else:
		gui_fg_size += change
	for widget in window.winfo_children():
		if isinstance(widget, Label) or isinstance(widget, Text) or isinstance(widget, Entry):
			font_name = get_font_name(widget)
			widget.config(font = (font_name, gui_fg_size))
		elif isinstance(widget, Frame):
			for widget2 in widget.winfo_children():
				if isinstance(widget2, Label) or isinstance(widget2, Text) or isinstance(widget2, Entry):
					font_name = get_font_name(widget2)
					widget2.config(font = (font_name, gui_fg_size))

window.title('Terminal 3')
window.iconphoto(True, image_icon)
window.config(padx = 0, pady = 0, bg = 'lightblue')
window.geometry('500x500+100+100')
window.resizable(1, 1)

# Frame
frame_top = Frame(window, bg = gui_bg, width = window.winfo_width(), height = 1)
frame_msc = Frame(window, bg = gui_bg, width = window.winfo_width(), height = 1)
frame_path = Frame(window, bg = gui_bg, width = window.winfo_width(), height = 1)
frame_input = Frame(window, bg = gui_bg, width = window.winfo_width(), height = 1)

# Output shell
oShell = Text(window, bg = gui_bg, fg = gui_fg_ins, font = (gui_font, gui_fg_size),
		border = 0, width = window.winfo_width(), height = window.winfo_screenheight(),
		insertbackground = gui_fg, padx = 20, pady = 20)

oShell.insert('1.0', _init.main_user.getUName() + ' -$ ')

# Character type
char_stat = Label(frame_top, bg = gui_bg, fg = gui_fg_ins, font = (gui_font_qu, gui_fg_size),
			padx = 20, justify = CENTER)


# Date
clock = Label(frame_top, bg = gui_bg, fg = gui_fg_ins, font = (gui_font_qu, gui_fg_size))
update_clock()

# Music status
music_status = Label(frame_msc, bg = gui_bg, fg = gui_fg_ins, font = (gui_font_qu, gui_fg_size))
# music_status.config(text = 'Load: Every Summertime')

# Path
prompt_text = _init.twd + '>'
prompt = Label(frame_path, bg = gui_bg, fg = gui_fg, font = (gui_font, gui_fg_size),
		text = prompt_text, height = 1)

# Input
query_box = Text(frame_input, bg = gui_bg, fg = gui_fg_ins,
			font = (gui_font_qu, gui_fg_size), pady = 10, padx = 20,
			width = 50, height = 1, wrap = NONE, insertbackground = gui_fg_ins)

query_box.focus_force()
query_box.bind('<Return>', lambda event: [exe_command(event), update_char(event)])
query_box.bind('<Key>', update_char)

query_box.bind('<Control-equal>', lambda event : change_font_size(event, 1))
query_box.bind('<Control-minus>', lambda event : change_font_size(event, -1))

frame_top.pack(side = TOP, fill = 'x', expand = True, anchor = N)
frame_msc.pack(side = TOP, fill = 'x', expand = True, anchor = N)
frame_input.pack(side = BOTTOM, fill = 'x', expand = True, anchor = S)
frame_path.pack(side = BOTTOM, fill = 'x', expand = True, anchor = S)

oShell.pack(side = TOP, fill = 'both', expand = True, anchor = 'center')
char_stat.pack(side = RIGHT, fill = 'x')
clock.pack(side = LEFT, padx = 15)
music_status.pack(side = LEFT, padx = 15)
query_box.pack(side = BOTTOM, fill = 'x')
prompt.pack(side = LEFT, anchor = W)

window.update()


window.mainloop()

_init._exit()