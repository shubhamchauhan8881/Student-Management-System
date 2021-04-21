import tkinter as tk
from tkinterpages import customwidgets
from tkinter.ttk import Notebook
from databases.my_sql import dbsys
from tkinterpages.photomanagement import photomanage

class ViewUserIntro(tk.Frame):
	def __init__(self,parent,res,*args, **kwargs):
		tk.Frame.__init__(self,parent, *args, **kwargs)
		#fetch user details from databsase
		res=res[1][0]
		kk={"bg":'#888'}
		self.lbl=customwidgets.PopUpMidContaierFrameWithImage(self,'View User',(788,190),'media/icons/du_swipe_dragger_monkey.png',**kk)
		self.lbl.pack(anchor='nw')
		#info table
		c = "Name : {} {} \n\nMobile : {} \n\nEmail : {}".format(res[1],res[3],res[5],res[6])
		photomanage.PhotoManage.setPhoto( self.lbl.showbtn, photomanage.PhotoManage.BinToImage(res[7]) )
		tk.Label(self.lbl.sub_frame,text=c,justify='left').pack()
	def expand(self,e):self.lbl.set_sub_frame()
	def shrink(self,e):self.lbl.set_sub_frame()

class HomePage(tk.Frame):
	def __init__(self,parent,loginIdPsw,*args, **kwargs):
		tk.Frame.__init__(self,parent, *args, **kwargs)
		self.uid = loginIdPsw

		self.home_pageBAckgroung=tk.PhotoImage(file='media/largeimages/main_bg.png') # 987 x 677
		self.hhh=tk.PhotoImage(file='media/largeimages/statics_bg.png')
		self.mypic=tk.PhotoImage(file='media/largeimages/about.png')
		self.spl=tk.PhotoImage(file='media/largeimages/school_building.png')

		notebook = Notebook(self)
		notebook.pack()

		home=tk.Frame(notebook,bg='#999')
		home.pack()
		notebook.add(home,text='Home')
		#set background
		tk.Label(home,image=self.home_pageBAckgroung).pack(anchor='nw')
		#==============================================
		#" get school data
		dbms= dbsys.DBrowser("databases/my_sql/School_Profile.db")
		s_name,s_adr,s_title,s_board,s_image=dbms.action("SELECT * FROM SchoolProfile ",'','fetch')[0]
	
		schol=tk.Frame(notebook)
		schol.pack()
		tk.Label(schol,image=self.spl).pack()
		notebook.add(schol,text='School Profile')

		user_intro= ViewUserIntro(home,self.uid)
		user_intro.place(x=800,y=100)
		
		statics=tk.Frame(notebook,bg='#888')
		statics.pack()
		notebook.add(statics,text='Statics')

		tk.Label(statics,image=self.hhh).place(x=0)

		about=tk.Frame(notebook,bg='#777')
		about.pack()
		notebook.add(about,text='About')
		tk.Label(about,image=self.mypic).place(x=0)

class SearchResultFrame(tk.Frame):
	def __init__(self,parent,*args, **kwargs):
		tk.Frame.__init__(self,parent,bd=2,relief='ridge',*args, **kwargs)
		self.retVal=self.returnValue = None
	
		self.added_frames = []
		#icons 
		self.find = tk.PhotoImage(file=r'media/icons/swipe_tool_search.png')
		self['relief']='ridge'

		self.myframe=tk.Frame(self)
		self.myframe.pack()

		self.canvas=tk.Canvas(self.myframe)
		self.canvas.pack(side="left")

		self.containerFrame=tk.Frame(self.canvas,width=965,height=630)

		myscrollbar=tk.Scrollbar(self.myframe,orient="vertical",command=self.canvas.yview)
		myscrollbar.pack(side="right",fill="y")

		self.canvas.configure(yscrollcommand=myscrollbar.set)
		self.canvas.create_window((0,0),window=self.containerFrame,anchor='nw')

		self.containerFrame.bind("<Configure>",self.scroll)
		tk.Label(self.containerFrame,image= self.find).place(x=450,y=250)
		self.addit([{"id":"0000","clas":"Class","name":"No name","image":photomanage.PhotoManage.imgBin("media/icons/student.png"),"fname":"Father name", "adrs":"address"}])
	
	def scroll(self,event):
		self.canvas.configure(scrollregion=self.canvas.bbox("all"),width=965,height=630	)

	def frame_chhanger(self,valdict):
		for i in self.added_frames:
			self.added_frames.remove(i)
			i.destroy()
			if self.added_frames==[]:
				self.addit(valdict)

	def addit(self,valdict):
		for resources in valdict:
			f = tk.Frame(self.containerFrame,bd=2,relief='ridge',width=965,height=170)
			imglbl = tk.Label(f,text="Student Id:"+resources['id'],compound='top',height=150,width=140,relief='flat')
			imglbl.place(x=5,y=7)

			photomanage.PhotoManage.setPhoto(imglbl,photomanage.PhotoManage.BinToImage(resources['image']))
			kw={'bd':1,'anchor':'nw',"font":('',10),"relief":"flat"}
			tk.Label(f,text='Name : {}'.format(resources['name'] ),**kw).place(x=150,y=10)
			tk.Label(f,text='Class : {}'.format(resources['clas']),**kw).place(x=500,y=10)
			tk.Label(f,text='Father name: {}'.format(resources['fname']),**kw).place(x=150,y=50)
			tk.Label(f,text='Address : {}'.format(resources['adrs']),**kw).place(x=150,y=90)
			b=tk.Button(f,text="   Select   ",command=lambda a=resources['id']:self.reid(a),overrelief='ridge',**kw)
			b.place(x=850,y=135)
			#remove
			f.pack(pady=5,fill='x',anchor='nw',expand=True)
			self.update_idletasks()
			self.added_frames.append(f)
	def reid(self,a):
		from tkinterpages.student_view import student_view
		student_view.StudentView(self.master,a)


class Findframe(tk.Frame):
	def __init__(self,parent, *args, **kwargs):
		tk.Frame.__init__(self,parent, *args, **kwargs)
		self._P =parent
		self.configure(bd=1,relief='ridge')#

		self.name=customwidgets.LabeledEntry(self,'Enter Student name or Student Id ',**kwargs)
		self.name.pack(side='top',fill='x')
		self.name.entryVar.trace('w',self.FindWhileTyping)
		self.name.entry.config(width=120,font=('',14))

		self.view_all= tk.Button(self, text='View All Student', command=lambda:self.FindWhileTyping('a','b','c',True),**kwargs)
		self.view_all.pack()
		
		self.result_frame = SearchResultFrame(self)
		self.result_frame.pack(side='bottom',anchor='nw',expand=True,fill='both')
	
	def FindWhileTyping(self,a,b,c, all_=False):
		dbms= dbsys.DBrowser("databases/my_sql/Admission_Data_merged.db")
		if not all_: 
			myQuery = """
			SELECT St_RegistrationId,St_class,St_Name,St_image,F_firstName,F_lastName,res_Street_adrs,res_District,res_State
			FROM MyStudentDetails
			WHERE St_RegistrationId = ?
			OR  St_Name = ? """
			dvl=dbms.action(myQuery, ( self.name.entryVar.get(),self.name.entryVar.get() ),'fetch')

			if not dvl==[]:
				for s in dvl:
					structured_value_list = []
					value_format={"id":s[0],"clas":s[1],"name":s[2],"image":s[3],"fname":s[4]+' '+s[5], "adrs":s[6]+' '+s[7]}
					structured_value_list.append(value_format)
				self.result_frame.frame_chhanger(structured_value_list)

		else:
			myQuery = """SELECT St_RegistrationId,St_class,St_Name,St_image,F_firstName,F_lastName,res_Street_adrs,res_District,res_State
			FROM MyStudentDetails """
			dvl=dbms.action(myQuery, '','fetch')

			if not dvl==[]:
				structured_value_list = []
				for s in dvl:
					value_format={"id":s[0],"clas":s[1],"name":s[2],"image":s[3],"fname":s[4]+' '+s[5], "adrs":s[6]+' '+s[7]}
					structured_value_list.append(value_format)

				new_window = tk.Toplevel(self.master)
				v = SearchResultFrame(new_window)
				v.pack()
				v.addit(structured_value_list)
			else:
				customwidgets.WindowAlert("No Records found","Heyyi no student details are added yet! Add First to view.",'info')


	

class StdMngPage(Notebook):
	def __init__(self,parent,*args, **kwargs):
		Notebook.__init__(self,parent, *args, **kwargs)

		self.home_pageBAckgroung=tk.PhotoImage(file='media/largeimages/main_bg.png')
		self.hhh=tk.PhotoImage(file='media/largeimages/statics_bg.png')
		self.mypic=tk.PhotoImage(file='media/largeimages/about.png')
		self.bg=tk.PhotoImage(file='media/ui/g906.png')

		self.find_unique_id = False

		home=tk.Frame(self,bg='#666')
		home.pack()
		self.add(home,text='New Admission')

		tk.Label(home,image=self.bg,relief='flat',bg='#666').place(x=100,y=100)

		self.identryVar=tk.StringVar()
		self.identry = tk.Entry(home,bg='#555',relief='flat',textvariable=self.identryVar,font=("",17),width=25)
		self.identry.place(x=480,y=250)

		self.identryVar.trace_add('write',self.trace)

		self.idstatus = tk.Label(self,text='Status: - - - - ',bg='#222',fg='white')
		self.idstatus.place(x=485,y=345)

		rand_id_button =tk.Button(home,text='   Generate Random Student Id   ',command=self.myRid,relief='flat',bg='#555',fg='white')
		rand_id_button.place(x=485,y=370)

		self.next_btn =tk.Button(home,text='Next',command=self.on_next,relief='flat',width=18,bg='#555',fg='white',state='disabled')
		self.next_btn.place(x=485,y=420)
		#set background
		#==============================================		
		find_studentFrame=tk.Frame(self)
		find_studentFrame.pack()
		self.add(find_studentFrame,text='Find Student') #add frame to notebook

		searchFrame = Findframe(find_studentFrame)
		searchFrame.pack(side='top',fill='x',anchor='nw')

	def on_next(self):
		from tkinterpages.forms.admission_form import admissionform
		admission_form = admissionform.AdmissionForm(self.master,self.identryVar.get()) 
		self.identryVar.set('')

	def trace(self,var,index,mode):
		avl = self.check_if_avail()
		if len(self.identryVar.get()) < 4:
			self.idstatus['text']='Status: too short should be >= 4 digits'
			self.next_btn['state']='disabled'

		elif avl:
			self.next_btn['state']='normal'
			self.idstatus['text']='Status: Available you can proceed forward'

		else:
			self.idstatus['text']='Status: Id is already in use..'
			self.next_btn['state']='disabled'

	def check_if_avail(self):
		qry="""SELECT St_RegistrationId FROM MyStudentDetails WHERE St_RegistrationId=?"""
		
		v=dbsys.DBrowser('databases/my_sql/Admission_Data_merged.db')
		res=v.action(qry,(self.identryVar.get(),),'fetch')

		if res==[]:
			self.find_unique_id=True
			return True
		else:
			self.find_unique_id=False
			return False
	def myRid(self):
		self.find_unique_id=False
		self.random_id_generator()
	def random_id_generator(self):
		from random import randint
		tries = 0
		while not self.find_unique_id:
			if tries < 10:
				new = randint(1000,9999)
				self.identryVar.set(str(new))
				tries += 1
			else:
				self.find_unique_id=True
				break

class DBLabeledEntry(customwidgets.LabeledEntry):
	def __init__(self,parent, lbltext,dbinfo,imglcn='',*args, **kwargs):
		customwidgets.LabeledEntry.__init__(self,parent,lbltext,imglcn,*args, **kwargs)

		self.dbinfo=dbinfo

		self.entryVar.trace("w",lambda a,b,c:self.set_buttons())
		self.entry.configure(**kwargs)

		self.btnF=tk.Frame(parent.master)
		#images
		self.tick = tk.PhotoImage(file="media/icons/tick.png")
		self.ccl = tk.PhotoImage(file="media/icons/cancel.png")

		tk.Button(self.btnF,image=self.tick,command=self.update).pack(side='left')

		self.cnclbtn = tk.Button(self.btnF,image=self.ccl,command=lambda :self.btnF.place_forget())
		self.cnclbtn.pack()

	def set_buttons(self):
		self.btnF.place(x=self.winfo_rootx()-10,y=self.winfo_rooty()+10)
	def update(self):
		from databases.my_sql import dbsys
		# {dbname:'',tablename:'',fieldname:'',uid:''}
		try:
			qry = """ UPDATE %s SET %s = ? WHERE USER_ID = ? AND PSW = ?"""%( self.dbinfo['tablename'], self.dbinfo['fieldname'])
			db  = dbsys.DBrowser(self.dbinfo['dbname'])

			print(qry)
			db.action(qry, (self.entryVar.get(),) +  self.dbinfo['uid']  ,'updt')

			self.btnF.place_forget()
			customwidgets.WindowAlert("Data Changed!","Database was updated successfully!")
		except Exception as e:
			customwidgets.WindowAlert("Failed!",f"There was an error: {e}")


class UpdateUser(tk.Frame):
	def __init__(self,parent,userInfo,*args, **kwargs):
		tk.Frame.__init__(self,parent, *args, **kwargs)
		
		self.uid = userInfo[1][0]
		self.uid= (self.uid[0],self.uid[4])
		#set background
		self.camimg = tk.PhotoImage(file='media/icons/capture .png')
		self.fileimg = tk.PhotoImage(file='media/icons/folder.png')
		self.bg_img = tk.PhotoImage(file='media/largeimages/user_view.png')
		tk.Label(self, image=self.bg_img).pack(anchor='nw')

		v=dbsys.DBrowser('databases/my_sql/Login_Register_data.db')
		res= list(v.action(""" SELECT * FROM userRegister WHERE USER_ID = ? AND PSW = ? """,self.uid,'fetch')[0])

		stp = {"bg":"#020a20","fg":"white"}
		d1 ={
		"dbname":"databases/my_sql/Login_Register_data.db", 
		"tablename":"userRegister",
		"fieldname":"FNAME"}
		d1["uid"]=self.uid

		self.fname = DBLabeledEntry(self,"First Name ",d1,**stp)
		self.fname.place(x=20,y=158)
		self.fname.entryVar.set(res[1])
		self.fname.cnclbtn.invoke()

		d2 ={
		"dbname":"databases/my_sql/Login_Register_data.db", 
		"tablename":"userRegister",
		"fieldname":"LNAME"}
		d2["uid"]=self.uid
		self.lname = DBLabeledEntry(self,"Last Name ",d2,**stp)
		self.lname.place(x=780,y=165)
		self.lname.entryVar.set(res[3])
		self.lname.cnclbtn.invoke()

		d3 ={
		"dbname":"databases/my_sql/Login_Register_data.db", 
		"tablename":"userRegister",
		"fieldname":"MOBILE"}
		d3["uid"]=self.uid
		self.mob = DBLabeledEntry(self,"Mobile",d3,**stp)
		self.mob.place(x=20,y=480)
		self.mob.entryVar.set(res[5])

		self.mob.cnclbtn.invoke()
		
		d4 ={
		"dbname":"databases/my_sql/Login_Register_data.db", 
		"tablename":"userRegister",
		"fieldname":"EMAIL"}
		d4["uid"]=self.uid
		self.email = DBLabeledEntry(self,"Email",d4,**stp)
		self.email.place(x=780,y=478)
		self.email.entryVar.set(res[6])
		self.email.cnclbtn.invoke()

		self.user_img = tk.Label(self,text='Id: '+res[0],compound='top',bg='#143159')
		self.user_img.place(x=390,y=100)

		tk.Button(self,image=self.camimg,bd=0,command=lambda: self.change_user_image("cam"), bg='#143159').place(x=430,y=550)
		tk.Button(self,image=self.fileimg,bd=0,command=lambda: self.change_user_image("file"), bg='#143159').place(x=530,y=550)

		self.set_image(self.user_img, photomanage.PhotoManage.BinToImage(res[7]) )

	def set_image(self,tag,lcn='media/icons/edit_user.png'):
		photomanage.PhotoManage.setPhoto(tag,lcn,2,1)

	def change_user_image(self,cheker):
		from tkinterpages.photomanagement import photomanage
		if cheker == "cam":
			v = tk.Label(self)
			lcn=photomanage.PhotoManage.TakePhoto(v)
		elif cheker == "file":
			v = tk.Label(self)
			lcn=photomanage.PhotoManage.choosePhoto(v)
		self.set_image(self.user_img,lcn)

		dbms=dbsys.DBrowser('databases/my_sql/Login_Register_data.db')
		dbms.action(""" UPDATE userRegister SET IMAGE = ? WHERE USER_ID = ? AND PSW = ?""", (photomanage.PhotoManage.imgBin(lcn),) + self.uid,'updt')
		#show alert
		customwidgets.WindowAlert("Image Changed!","Image was updated successfully!")