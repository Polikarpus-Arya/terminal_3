from tkinter import *
from terminal_3 import gui_mod
from gui_mod import *
from user_mod import User

import os

user_list = [] # list of user
main_user = None
twd = ''  # Terminal working directory

def init():
	global twd, user_list

	# Get Terminal working directory
	twd = os.getcwd()

	# Get all username available
	for user in os.listdir(twd + "/database/user"):
		user_list.append(user)

# Determine what happen to these method
# None  -> exit the program
# True  -> Successfully login / create account
# False -> change method
return_val = None

def login():

	# Set return value to default
	global return_val
	return_val = None

	# Move cursor to uernamae entry
	def uN_foc(event):
		uName_entry.focus()

	# Move cursor to password entry
	def pw_foc(event):
		passw_entry.focus()

	# Submit data
	def submit(event):
		# Get entry box contents
		tmp_uName = uName_entry.get()
		tmp_passw = passw_entry.get()

		# Check whether the username exist or not
		if not os.path.isfile('database/user/' + tmp_uName):
			message.config(text = 'Username not found!')
			window.update()
			return

		# Delete entry box content
		uName_entry.delete(0, END)
		passw_entry.delete(0, END)
		
		# Set main_user
		tmp_user  = User(tmp_uName)

		# Check whether the password match the username
		if tmp_user.checkPass(tmp_uName, tmp_passw):
			global main_user, return_val
			main_user = tmp_user
			return_val = True
			
			for widget in window.winfo_children():
				widget.destroy()
			window.quit()
		else:
			message.config(text = 'Username and password doesn\'t match!')
			window.update()

	def create_new():
		global return_val
		return_val = False
		for widget in window.winfo_children():
			widget.destroy()
		window.quit()

	window.iconphoto(True, image_icon)
	window.title('Terminal 3.0')
	window.geometry('+600+300')
	window.config(padx = 20, pady = 20, bg = gui_bg)

	# lock window size
	window.resizable(width = False, height = False)

	# Frame
	frame = Frame(window, width = 100, height = 100, bg = gui_bg)
	frame.pack(anchor = CENTER)
	
	# Entry box and button
	uName_entry = Entry(frame, font = (gui_font, 15), width = 20, bg = gui_bg, fg = gui_fg_ins, insertbackground = gui_fg_ins)
	passw_entry = Entry(frame, font = (gui_font, 15), show = '*', bg = gui_bg, fg = gui_fg_ins, insertbackground = gui_fg_ins)
	submit_data = Button(frame, text = 'Login', font = (gui_font, 15),
						pady = 4,
						height = 1,
						width = 10,
						relief = FLAT,
						activebackground = gui_bg,
						activeforeground = gui_fg,
						bg = gui_bg,
						fg = gui_fg,
						command = lambda : submit(submit_data))
	
	# To create new account
	create_button = Button(frame, text = "Create new account",
			font = (gui_font, 10),
			relief = FLAT,
			activebackground = gui_bg,
			activeforeground = gui_fg,
			bg = gui_bg,
			fg = gui_fg,
			justify = RIGHT,
			command = create_new)

	# To pass some message if some error happen
	message = Label(frame, width = 40, height = 1,
					font = (gui_fg, 10),
					relief = FLAT,
					bg = gui_bg,
					fg = gui_fg_err)
	message.config(text = '', justify = 'center')

	# Every component needed
	
	image_login = ImageSize('database/picture/image_login.png', 55)
	
	Label(frame, image = image_login, font = (gui_font, 20),
		bg = gui_bg,
		fg = gui_fg).grid(row = 0, columnspan = 2)
	Label(frame, text = 'Username', font = (gui_font, 15),
		padx = 12, pady = 10,
		bg = gui_bg,
		fg = gui_fg).grid(row = 1, column = 0)
	Label(frame, text = 'Password', font = (gui_font, 15),
		padx = 12, pady = 10,
		bg = gui_bg,
		fg = gui_fg).grid(row = 2, column = 0)

	uName_entry.   grid (row = 1, column = 1)
	passw_entry.   grid (row = 2, column = 1)
	create_button. grid (row = 3, column = 1, sticky = E)
	submit_data.   grid (row = 4, columnspan = 2)
	message.       grid (row = 5, columnspan = 2)

	uName_entry.focus()

	# key binding
	uName_entry.bind('<Return>', pw_foc)
	uName_entry.bind('<Down>'  , pw_foc)
	passw_entry.bind('<Up>'    , uN_foc)
	passw_entry.bind('<Return>', submit)

	window.mainloop()

	return return_val

def create_account():

	# Set return value to default
	global return_val
	return_val = None

	# Move cursor to uernamae entry
	def uN_foc(event):
		uName_entry.focus()

	# Move cursor to password entry
	def pw_foc(event):
		passw_entry.focus()

	# Move cursor to retype entry
	def rt_foc(event):
		retry_entry.focus()

	# Submit data
	def submit(event):
		# Get entry box contents
		tmp_uName = uName_entry.get()
		tmp_passw = passw_entry.get()
		tmp_retry = retry_entry.get()

		# Check whether the retry_entry and password are the same
		if tmp_passw != tmp_retry:
			message.config(text = 'Confirmation password doesn\'t match the password')
			return

		if os.path.isfile('database/user/' + tmp_uName):
			message.config(text = 'Username already exist! Login instead?')
			return

		# Delete entry box content
		uName_entry.delete(0, END)
		passw_entry.delete(0, END)
		retry_entry.delete(0, END)
		
		# Set main_user
		global main_user, return_val
		main_user  = User(tmp_uName, tmp_passw)

		# Return True
		return_val = True
		for widget in window.winfo_children():
			widget.destroy()
		window.quit()

	def login_instead():
		global return_val
		return_val = False
		for widget in window.winfo_children():
			widget.destroy()
		window.quit()

	window.iconphoto(True, image_icon)
	window.title('Terminal 3.0')
	window.geometry('+600+300')
	window.config(padx = 20, pady = 20, bg = gui_bg)

	# lock window size
	window.resizable(width = False, height = False)

	# Frame
	frame = Frame(window, width = 100, height = 100, bg = gui_bg)
	frame.pack(anchor = CENTER)
	
	# Entry box and button
	uName_entry = Entry(frame, font = (gui_font, 15), width = 20, bg = gui_bg, fg = gui_fg_ins, insertbackground = gui_fg_ins)
	passw_entry = Entry(frame, font = (gui_font, 15), show = '*', bg = gui_bg, fg = gui_fg_ins, insertbackground = gui_fg_ins)
	retry_entry = Entry(frame, font = (gui_font, 15), show = '*', bg = gui_bg, fg = gui_fg_ins, insertbackground = gui_fg_ins)
	submit_data = Button(frame, text = 'Create', font = (gui_font, 15),
						pady = 4,
						height = 1,
						width = 10,
						relief = FLAT,
						activebackground = gui_bg,
						activeforeground = gui_fg,
						bg = gui_bg,
						fg = gui_fg,
						command = lambda : submit(submit_data))
	
	# To create new account
	login_button = Button(frame, text = "Already have an account?",
			font = (gui_font, 10),
			relief = FLAT,
			activebackground = gui_bg,
			activeforeground = gui_fg,
			bg = gui_bg,
			fg = gui_fg,
			justify = RIGHT,
			command = login_instead)

	# To pass some message if some error happen
	message = Label(frame, width = 40, height = 1,
					font = (gui_fg, 10),
					relief = FLAT,
					bg = gui_bg,
					fg = gui_fg_err)
	message.config(text = '', justify = 'center')

	# Every component needed
	Label(frame, image = image_login, font = (gui_font, 20),
		bg = gui_bg,
		fg = gui_fg).grid(row = 0, columnspan = 2)
	Label(frame, text = 'Username', font = (gui_font, 15),
		padx = 12, pady = 10,
		bg = gui_bg,
		fg = gui_fg).grid(row = 1, column = 0)
	Label(frame, text = 'Password', font = (gui_font, 15),
		padx = 12, pady = 10,
		bg = gui_bg,
		fg = gui_fg).grid(row = 2, column = 0)
	Label(frame, text = 'Retype Password', font = (gui_font, 15),
		padx = 12, pady = 10,
		bg = gui_bg,
		fg = gui_fg).grid(row = 3, column = 0)

	uName_entry.   grid (row = 1, column = 1)
	passw_entry.   grid (row = 2, column = 1)
	retry_entry.   grid (row = 3, column = 1)
	login_button.  grid (row = 4, column = 1, sticky = E)
	submit_data.   grid (row = 5, columnspan = 2)
	message.       grid (row = 6, columnspan = 2)

	uName_entry.focus()

	# key binding
	uName_entry.bind('<Return>', pw_foc)
	uName_entry.bind('<Down>'  , pw_foc)
	passw_entry.bind('<Up>'    , uN_foc)
	passw_entry.bind('<Down>'  , rt_foc)
	passw_entry.bind('<Return>', rt_foc)
	retry_entry.bind('<Up>'    , pw_foc)
	retry_entry.bind('<Return>', submit)

	window.mainloop()

	return return_val

def _exit():
	pass