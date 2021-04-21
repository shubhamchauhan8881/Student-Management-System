from random import randrange,choice
from tkinter import messagebox
from webbrowser import open_new_tab
from tkinter.filedialog import asksaveasfile

def show_password(event):
	widget=event.widget
	widget['show']=''

def hide_password(event):
	widget=event.widget
	widget['show']='*'

def hover_in(event,bg='#8ffff4',fg='black'):
	widget=event.widget
	widget.config(bg=bg)

def hover_out(event,bg='#f0f0ed',fg='black'):
	widget=event.widget
	widget.config(bg=bg)

def ask_close(title='Info',message='Do you want to quit?',detail='This will close the application'):
	ans=messagebox.showinfo(title=title,message=message,detail=detail)
	if ans: return True

def raise_widget(widgetname):
	for each in widgetname:
		each.tkraise()

def open_link(link):
	open_new_tab(link)

def okCancel(message,detail):
	return messagebox.askokcancel(title='Info', message=message,detail=detail)

def only_int(var, limit=10,mob=False):
	v=var.get()
	rep=[str(x) for x in range(6)]
	if not v=='':
		if mob==True: 
			if v[0] in rep: var.set('')
		if v.isdigit():
			var.set(var.get())
		if not v.isdigit():var.set(v[:-1])
		if len(v)==limit+1:var.set(v[:-1])

def only_str(var,case='u'):
	v=var.get()
	if not v=='':
		if not v.isalpha(): var.set(v[:-1])
		else:
			if case=='u':var.set(v.upper())
			elif case=='l':var.set(v.lower())
			elif case=='t':var.set(v.title())

def check_email(email):
	import re
	regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$' 
	if re.search(regex,email): return True
	else: return False