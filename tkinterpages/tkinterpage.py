import tkinter as tk
from tkinterpages import customwidgets, modifiers
from tkinterpages.photomanagement import photomanage
from tkinter.messagebox import askokcancel,showinfo
from databases.my_sql import dbsys

class ask_id_password(tk.LabelFrame):
	"""  asks to create """
	def __init__(self,parent,*args, **kwargs):
		tk.LabelFrame.__init__(self,parent, *args, **kwargs)
		
		self.avail=False

		self.container=tk.Frame(self,height=270,width=400,bd=3,relief='groove')
		self.container.pack()
		
		id_guidelines="* Can contain text,numbers\n* Some special characters . _ \n* Upper or lower case"
		tk.Label(self.container,justify='left',text=id_guidelines).place(x=20,y=95)

		self._id=customwidgets.LabeledEntryErrorDisplay(self.container, "Enter your desirable login id: ")
		self._id.place(x=20,y=30)
		self._id.entry['width']=44
		self._id.entryVar.trace('w',self.check_if_avail)

		self.ok_btn=tk.Button(self.container,text='Regsiter now',state='disabled',bg='#1ff',font=('',13),height=1,width=20)
		self.ok_btn.place(x=5,y=180)

		self.status=tk.Label(self.container,font=('',9),text='Status: - - - - ')
		self.status.place(x=270,y=100)

		self.cncl_btn=tk.Button(self.container,text='Cancel',bg='coral',font=('',13),height=1,width=20)
		self.cncl_btn.place(x=200,y=180)

	def check_if_avail(self,a,b,c):
		qry="""SELECT USER_ID FROM userRegister WHERE USER_ID=? """

		dbms= dbsys.DBrowser("databases/my_sql/Login_Register_data.db")	
		res = dbms.action(qry,(self._id.entryVar.get(),), 'fetch')

		if len(self._id.entryVar.get())<4:
			self.status.config(text='Status: too short',fg='#ff5555')
			self.avail=False
		
		elif len(self._id.entryVar.get())==0:
			self.status.config(text='Status: - - - -',fg='#ff5555')
			self.avail=False
		
		else:
			if res==[]:
				self.status.config(text='Status: available',fg='green')
				self.avail=True
				self.ok_btn['state']='normal'
			else:
				self.status.config(text='Status: already taken',fg='coral')
				self.avail=False
				self.ok_btn['state']='disabled'
				
class Register_new_user(tk.Frame):
	def __init__(self,parent, *args, **kwargs):
		tk.Frame.__init__(self,parent)
		self._p=parent
		self.returnDetails=('email','Psw')
		#icons
		self.bgimage=tk.PhotoImage(file=r'media/ui/dds.png')
		self.closeico=tk.PhotoImage(file=r'media/icons/c1.png')
		self.sbmit=tk.PhotoImage(file=r'media/ui/sm.png')
		#bg laebl	
		self.container = tk.Label(self,image=self.bgimage,bd=3,relief='sunken')
		self.container.pack()
		color = self.container['bg']
		#close button
		self.closeBtn = tk.Button(self, image=self.closeico,bd=0,width=18,height=20, command=self.destroy)
		self.closeBtn.place(x=865,y=5)

		self.imageLabel=customwidgets.ImageLabel(self, 'Upload Image')
		self.imageLabel.place(x=220,y=50)

		self.fname = customwidgets.LabeledEntryErrorDisplay(self, "First name",**{"bg":color})
		self.lname = customwidgets.LabeledEntryErrorDisplay(self, "Last name",**{"bg":color})
		self.email = customwidgets.LabeledEntryErrorDisplay(self, "Email",**{"bg":color})
		self.email.entry['width']=35
		self.psw = customwidgets.LabeledEntryErrorDisplay(self, "Password",**{"bg":color})
		self.re_psw = customwidgets.LabeledEntryErrorDisplay(self, "Retype password",**{"bg":color})
		self.re_psw.entry['show']='*'
		self.psw.entry['show']='*'
		#submit button
		self.sbmit_button = tk.Button(self,image=self.sbmit,command=self.onSubmitClick,bd=0)
		self.sbmit_button.place(x=230,y=500)

		#placing entries
		self.fname.place(x=130,y=260)
		self.lname.place(x=290,y=260)
		self.email.place(x=130,y=325)
		self.psw.place(x=130,y=400)
		self.re_psw.place(x=290,y=400)
		#binding validation 
		self.fname.entryVar.trace('w',lambda a,b,c:modifiers.only_str(self.fname.entryVar))
		self.lname.entryVar.trace('w',lambda a,b,c:modifiers.only_str(self.lname.entryVar))
		
		self.psw.entry.bind('<ButtonPress-3>', modifiers.show_password)
		self.psw.entry.bind('<ButtonRelease-3>', modifiers.hide_password)
		
		self.re_psw.entry.bind('<ButtonPress-3>', modifiers.show_password)
		self.re_psw.entry.bind('<ButtonRelease-3>', modifiers.hide_password)
		
		self.email.entry.bind('<FocusOut>',self.valid_email)
		
		self.re_psw.entryVar.trace('w',self.compr)
		
		self.psw.entryVar.trace('w',self.lenvalid)
		#all entris   checkit
		self.chit=[self.fname,self.lname,self.email,self.psw, self.re_psw]

	def compr(self,a,b,c):
		if self.re_psw.entryVar.get()==self.psw.entryVar.get():
			self.re_psw.errormessage.configure(text='matched',fg='green')
		else:self.re_psw.errormessage.configure(text='mismatched',fg='red')
	def lenvalid(self,a,b,c):
		v=len(self.psw.entryVar.get())
		if v<8:
			self.psw.errormessage.configure(text=f'less than 6,  still:{v}',fg='red')
		else:self.psw.errormessage.configure(text='use specail chars if you wants',fg='green')
	def checkIfEmpty(self):
		err=0
		for i in self.chit:
			if i.entryVar.get()=='':
				err=1
				i.errormessage['text']='required field*'
				break
		return err
	def matchpasswrd(self):
		if self.psw.entryVar.get()!=self.re_psw.entryVar.get():
			self.re_psw.errormessage['text']='password mismatched'
		elif len(self.psw.entryVar.get())<6:
			self.re_psw.errormessage['text']='should not be less than 6 digits'
		else:
			return True
	def valid_email(self,event=None):
		email=self.email.entryVar.get()
		vlidate=modifiers.check_email(email)
		if vlidate==False:
			self.email.errormessage['text']='enter a valid email'
			return False
		else:
			self.email.errormessage['text']=''
			return True
		# return True if vlidate==True else False
	def onSubmitClick(self):
		if self.checkIfEmpty()==0 and self.matchpasswrd()==True and self.valid_email()==True:
			print('ready to add')
			self.askforId=ask_id_password(self.container.master)
			self.askforId.place(x=300,y=80)
			self.sbmit_button['state']='disabled'
			self.askforId.ok_btn['command']=self.user_register_succes
			self.askforId.cncl_btn['command']=self.user_register_cncl
		else:
			print('Fill form correctly')
	def user_register_succes(self):
		if self.askforId._id.entryVar.get()=='':
			self.askforId._id.errormessage['text']='this is required field'
		else:
			#if avail==True
			if self.askforId.avail:
				#show a loading window
				data_tobe_added=(
					self.askforId._id.entryVar.get(),
					self.fname.entryVar.get(),
					self.lname.entryVar.get(),
					self.email.entryVar.get(),
					self.psw.entryVar.get(),
					photomanage.PhotoManage.imgBin(self.imageLabel.pth),
					)
				
				qry="""INSERT INTO userRegister(USER_ID, FNAME, LNAME, EMAIL, PSW, IMAGE) VALUES(?,?,?,?,?,?)"""
				
				dbms = dbsys.DBrowser("databases/my_sql/Login_Register_data.db")

				if  dbms.action(qry,data_tobe_added,'updt'):
					self.askforId.destroy()
					showinfo(title='Cheers!',message="User was registered", detail= "Go back and Login Now")
				else:
					print('something went wrong')
	def user_register_cncl(self):
		self.askforId.destroy()
		customwidgets.alert_CloseLabel(self,'Registration terminated').place(x=215,y=460)
		self.sbmit_button['state']='normal'


class LoginPage(tk.Frame):
	def __init__(self,parent, *args, **kwargs):
		tk.Frame.__init__(self,parent, *args, **kwargs)
		self._P=parent
		
		color = self['bg']
		self.entryFrame=tk.Frame(self,bg=color)
		self.entryFrame.place(x=50,y=20)
		#attrib
		self.save_psw= None
		#icons
		self.ln= tk.PhotoImage(file=r'media/ui/ln.png')
		self.rg= tk.PhotoImage(file=r'media/ui/rg.png')

		self.ID =customwidgets.LabeledEntryErrorDisplay(self.entryFrame, 'User id',r'media/icons/icons8-face-id-32.png',**{"bg":color})
		self.ID.entry.configure(width=20,highlightthickness=0)
		self.ID.pack(anchor='nw')

		self.password=customwidgets.LabeledEntryErrorDisplay(self.entryFrame, 'Password',r'media/icons/icons8-password-1-32.png',**{"bg":color})
		self.password.pack(pady=10,anchor='nw')
		self.password.entry.configure(show='*', width=20,highlightthickness=0)
		self.password.errormessage['text']='Right press to show password'
		self.password.entry.bind('<ButtonPress-3>',modifiers.show_password)
		self.password.entry.bind('<ButtonRelease-3>',modifiers.hide_password)
		#bind functions to hide or show password
		self.rememberpsw=tk.IntVar(self.entryFrame)
		self.remempsw=tk.Checkbutton(self.entryFrame,bd=0,text='Save password.?',variable=self.rememberpsw,command=self.showcbwarn,**{"bg":color})
		self.remempsw.pack(anchor='nw')
		
		self.remmsg = tk.Label(self.entryFrame,bd=0, **{"bg":color})
		self.remmsg.pack(anchor='nw')
		
		self.errormessage=tk.Label(self.entryFrame,fg='red', **{"bg":color})
		self.errormessage.pack(pady=10,anchor='nw')



		self.loginbtn=tk.Button(self.entryFrame,image=self.ln,bd=0, activebackground=color, **{"bg":color})
		self.loginbtn.pack(anchor='nw', side='left')
		# tk.Label(self.entryFrame,text='__'*30,fg='blue').pack(anchor='nw',pady=10)

		self.register=tk.Button(self.entryFrame,image=self.rg,fg='blue', activebackground=color ,bd=0,**{"bg":color})
		self.register.pack(side='right', padx=5)


	def showcbwarn(self):
		if self.rememberpsw.get()==1:
			self.alrt=customwidgets.alert_CloseLabel(self.remmsg,text='If you save password someone may see it!', **{"bg":self.entryFrame['bg']})
			self.alrt.pack()
			self.save_psw=True
		else:
			self.save_psw=False
			self.alrt.destroy()
	def matchWithDb(self):
		_qry="""SELECT * FROM userRegister WHERE USER_ID=? AND PSW=? """
		_val=(self.ID.entryVar.get().strip(),self.password.entryVar.get().strip() ,)
		dbms= dbsys.DBrowser("databases/my_sql/Login_Register_data.db")
		res = dbms.action(_qry,_val,'fetch')
		if res==[]:
			return (False,False)
		else:
			if self.save_psw or not self.save_psw:
				dbms = dbsys.DBrowser("databases/my_sql/recent_login_saved.db")
				if self.save_psw:
					dbms.action("UPDATE recent_login SET ID = ?, PSW = ? WHERE SN = ? ",_val+('1',),'updt')
				else:
					dbms.action("UPDATE recent_login SET ID = ?, PSW = ? WHERE SN = ?",('','',1,),'updt')
			return (True,res)


class CompanyAdvertise(tk.Frame):
	def __init__(self,parent, *args, **kwargs):
		tk.Frame.__init__(self,parent, *args, **kwargs)
		self.configure(height=500,width=372)
		self.compimg= tk.PhotoImage(file=r'media/icons/student.png').subsample(2,2)
		self.companyImage = tk.Label(self,image=self.compimg,compound='top',
			text='Student Management App by Shubham')
		self.companyImage.place(x=80,y=10)
		#============ icons of social media 
		self.fb= tk.PhotoImage(file=r'media/icons/social-media/facebook.png').subsample(2,2)
		self.insta= tk.PhotoImage(file=r'media/icons/social-media/instagram.png').subsample(2,2)
		self.linkedin= tk.PhotoImage(file=r'media/icons/social-media/linkedin.png').subsample(2,2)
		self.phone= tk.PhotoImage(file=r'media/icons/social-media/phone.png').subsample(2,2)
		self.email= tk.PhotoImage(file=r'media/icons/social-media/email.png').subsample(2,2)
		self.whatsapp= tk.PhotoImage(file=r'media/icons/social-media/whatsapp.png').subsample(2,2)
		self.twit= tk.PhotoImage(file=r'media/icons/social-media/twitter.png').subsample(2,2)
		self.browser= tk.PhotoImage(file=r'media/icons/social-media/internet.png').subsample(2,2)
		self.abouimg= tk.PhotoImage(file=r'media/icons/social-media/about.png').subsample(2,2)
		#facebook
		kw={'relief':'flat', "overrelief":'groove','compound':'left'}
		tk.Button(self,image=self.phone,text='Phone ',padx=6,command=self.showPhone, **kw).place(x=30,y=300)
		tk.Button(self,image=self.email,text='Email',padx=6,command=lambda:self.openlink('www.gmail.com'),**kw).place(x=140,y=300)
		tk.Button(self,image=self.whatsapp,text='Whatsapp',command=self.showPhone,**kw).place(x=247,y=300)
		tk.Button(self,image=self.fb,text='Facebook',command=lambda:self.openlink('https://www.facebook.com/elsker.elvish.py/'),**kw).place(x=30,y=350)
		tk.Button(self,image=self.twit,text='Twitter',padx=4,command=lambda:self.openlink('https://twitter.com/i_snehlee?s=20'),**kw).place(x=140,y=350)
		tk.Button(self,image=self.insta,text='Instagram',command=lambda:self.openlink('www.https://www.instagram.com/elsker_elvish.py/'),**kw).place(x=248,y=350)
		tk.Button(self,image=self.browser,text='Website',padx=4,command=lambda:self.openlink('www.google.com'),**kw).place(x=30,y=400)
		tk.Button(self,image=self.linkedin,text='LinkedIn',command=lambda:self.openlink('www.google.com'),**kw).place(x=140,y=400)
		tk.Button(self,image=self.abouimg,text='About ',padx=5,command=lambda:self.openlink('www.google.com'),**kw).place(x=250,y=400)
		#close application
	def openlink(self,link):
		modifiers.open_new_tab(link)
	def showPhone(self):
		showinfo(title='Contact us',message='Use 8881868541 to call and Whatsapp also..')

class basicUi(tk.Frame):
	"""docstring for basicUi"""
	def __init__(self, parent,*args, **kwargs):
		tk.Frame.__init__(self,parent,*args, **kwargs)
		self._P=parent
		self.master.resizable(False,False)
		self.master.geometry('887x577+100+1')
		self.master.title('Student Managemanet System by Shubham')
		self.applogo = tk.PhotoImage(file=r'media/icons/student.png')
		self.master.iconphoto(False,self.applogo)

		# self.bind('<ButtonPress-1>',self.layer_down_repage	)

		self.bg_image=customwidgets.ElskerButton(self, "", "media/gif/sp3.gif", bd=0)
		self.bg_image.pack(fill='both', expand=1)
		

		self.login=LoginPage(self,height=350,width=400, bg='white')
		self.login.place(x=0,y=0)
		# self.login.loginbtn['command']=self.ReturnLoginDetails
		self.login.register['command']=self.onRegister
		#contents to right pane
		self.cmp = customwidgets.PopUpMidContaierFrame(self, "About", (510,25))
		self.cmp.place(x=785,y=550)
		self.cmp.showbtn.configure(bg='#090078', fg='green')
		company_advertise=CompanyAdvertise(self.cmp.sub_frame,width=370,height=500)
		company_advertise.pack()
		# interrupt while closing window
		self.master.protocol('WM_DELETE_WINDOW',self.askclose)
	def askclose(self):
		if askokcancel(title='Info..',message='Close Window',detail='Do you want to quit?'):self._P.destroy()
	def onRegister(self):
		self.Register_new_frame=Register_new_user(self)
		self.Register_new_frame.place(x=0,y=0)