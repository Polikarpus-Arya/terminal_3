from tkinter import *
from PIL import Image, ImageTk

# 16 pixel = 12 size of font

gui_font 	= 'Ubuntu Mono'
gui_font_qu	= 'Ubuntu Mono'
gui_bg 	 	= '#1A1E24'
gui_fg 	    = '#CCCCCC'
gui_fg_ins  = '#00C800'
gui_fg_err  = '#FFA000'
gui_fg_size = 15

# #C8C800

window = Tk()

def pt_to_px(num):
	# Convert from font size to pixel
	return int(num * 4 / 3)

def px_to_pt(num):
	# Convert from pixel to font size
	return int(num * 3 / 4)

def max_fit_char_h(windowSize, fontSize):
	# Return how many character fit in certain window height
	return int(windowSize / pt_to_px(fontSize))

def max_fit_char_w(windowSize, fontSize):
	# Return how many character fit in certain window width
	return int(windowSize / pt_to_px(fontSize))

def ImageSize(image, *args):
	
	# To provided image object with adjustable
	# size that can be used for tkinter
	
	if len(args) == 1:
		return ImageTk.PhotoImage(Image.open(image).resize((args[0], args[0])))
	else:
		return ImageTk.PhotoImage(Image.open(image).resize((args[0], args[1])))

image_icon  = ImageSize('database/picture/icon.png', 200, 100)
image_login = ImageSize('database/picture/image_login.png', 55)

def get_font_name(widget):
	arg = widget['font']
	font_name = ''
	arg_bool = False
	for ch in arg:
		if ch == '}':
			break
		if arg_bool:
			font_name = font_name + ch
		if ch == '{':
			arg_bool = True 
	return font_name

def conv_char(text):

	if text == 'BackSpace':
		text = 'Bs'
	elif text == 'Next':
		text = 'PgDn'
	elif text == 'Prior':
		text = 'PgUp'
	elif text == 'Return':
		text = 'Rt'
	elif text == 'Delete':
		text = 'DEL'
	elif text == 'Control_R':
		text = 'C-r'
	elif text == 'Control_L':
		text = 'C-l'
	elif text == 'Shift_L':
		text = 'S-l'
	elif text == 'Shift_R':
		text = 'S-r'
	elif text == 'Alt_L':
		text = 'A-l'
	elif text == 'Alt_R':
		text = 'A-r'
	elif text == 'Caps_Lock':
		text = 'Caps'
	elif text == 'Escape':
		text = 'Esc'
	elif text == 'Down':
		text = '↓'
	elif text == 'Up':
		text = '↑'
	elif text == 'Right':
		text = '→'
	elif text == 'Left':
		text = '←'
	elif text == 'greater':
		text = '>'
	elif text == 'less':
		text = '<'
	elif text == 'semicolon':
		text = ';'
	elif text == 'period':
		text = '.'
	elif text == 'bracketleft':
		text = '['
	elif text == 'braceleft':
		text = '{'
	elif text == 'bracketright':
		text = ']'
	elif text == 'braceright':
		text = '}'
	elif text == 'plus':
		text = '+'
	elif text == 'minus':
		text = '-'
	elif text == 'underscore':
		text = '_'
	elif text == 'equal':
		text = '='
	elif text == 'backslash':
		text = '\\'
	elif text == 'bar':
		text = '|'
	elif text == 'slash':
		text = '/'
	elif text == 'question':
		text = '?'
	elif text == 'asciitilde':
		text = '`'
	elif text == 'grave':
		text = '~'
	elif text == 'exclam':
		text = '!'
	elif text == 'at':
		text = '@'
	elif text == 'numbersign':
		text = '#'
	elif text == 'dollar':
		text = '$'
	elif text == 'percent':
		text = '%'
	elif text == 'asciicircum':
		text = '^'
	elif text == 'ampersand':
		text = '&'
	elif text == 'asterisk':
		text = '*'
	elif text == 'parenleft':
		text ='('
	elif text == 'parenright':
		text = ')'
	elif text == 'comma':
		text = ','
	elif text == 'colon':
		text = ':'
	elif text == 'quotedbl':
		text = '"'
	elif text == 'apostrophe':
		text = '\''

	return text