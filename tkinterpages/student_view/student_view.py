import tkinter as tk
from tkinterpages import customwidgets
from databases.my_sql import dbsys

class StudentViewUpdateFrame(tk.Frame):
	def __init__(self,parent,studenstregId,*args, **kwargs):
		tk.Frame.__init__(self,parent,*args, **kwargs)

		self.st_uid = studenstregId
		self.container=  tk.Frame(self,**kwargs)
		self.container.place(x=0)
		#clas of admission
		json_load = self.read_json()

		for i in range(len(json_load)):
			json_load[i]['uid']=self.st_uid
		
		CLASSES	= ['Nursey','LKG','UKG','1','2','3','4','5','6','7','8','9','10','11','12']
		customwidgets.DBLabeledEntry(self.container, "Class ",json_load[0]).place(x=5,y=20)
		customwidgets.LabeledEntry(self.container,"Student Registered Id").place(x=250,y=20)
		customwidgets.DBDateentry(self.container,'Date Of Birth',json_load[1]).place(x=490,y=20)
		self.name_of_student=customwidgets.DBLabeledEntry(self.container,"Name of the child",json_load[2])
		self.name_of_student.entry['width']=80
		self.name_of_student.place(x=5,y=100)
		#gender and age
		#mobile and email and nationaliyt and adhar
		customwidgets.DBLabeledEntry(self.container,'Child\'s Adhar No.',json_load[3]).place(x=5,y=180)
		customwidgets.DBLabeledEntry(self.container,'Child\'s Mobile No.',json_load[4]).place(x=250,y=180)
		customwidgets.DBLabeledEntry(self.container,'Child\'s Email',json_load[5]).place(x=490,y=180)
		customwidgets.DBLabeledEntry(self.container,'Father\'s First Name',json_load[6]).place(x=5,y=280)
		customwidgets.DBLabeledEntry(self.container,'Father\'s Last Name',json_load[7]).place(x=250,y=280)
		customwidgets.DBLabeledEntry(self.container,'Father\'s Mobile no.',json_load[8]).place(x=490,y=280)
		customwidgets.DBLabeledEntry(self.container,'Father\'s DOB',json_load[9]).place(x=5,y=380)
		customwidgets.DBLabeledEntry(self.container,'Father\'s email ',json_load[10]).place(x=250,y=380)
		#mother
		customwidgets.DBLabeledEntry(self.container,'Mother\'s First Name',json_load[11]).place(x=5,y=480)
		customwidgets.DBLabeledEntry(self.container,'Mother\'s Last Name',json_load[13]).place(x=250,y=480)
		customwidgets.DBLabeledEntry(self.container,'Mother\'s  DOB',json_load[13]).place(x=490,y=480)
		
		tk.Button(self, text='Reload Page',font=('',15),height=2,width=15,command=self.set_after_update).place(x=660,y=600)
		self.set_after_update()
	def read_json(self):
		from json import loads
		with open("tkinterpages/student_view/update_query.json") as f:
			d = f.read()
			f.close()
			return loads(d)
	def set_after_update(self):
		qry=""" SELECT St_class,St_RegistrationId, St_dob, St_Name, St_adhar, St_Mobile, St_Email, F_firstName, F_lastName,F_mobile ,F_dob, F_email FROM MyStudentDetails WHERE St_RegistrationId = ? """
		dbms = dbsys.DBrowser('databases/my_sql/Admission_Data_merged.db')	
		res=dbms.action(qry,(self.st_uid,), 'fetch')

		if res == []:print('Seems we have no records')
		else:res = list(res[0])

		mqry=""" SELECT M_firstName ,M_lastName, M_dob FROM MyStudentMotherDetails WHERE St_RegistrationId = ? """
		dbms = dbsys.DBrowser('databases/my_sql/Admission_Data_merged.db')
		res.extend( list(dbms.action(mqry,(self.st_uid,), 'fetch')[0]) )

		lbls = self.container.place_slaves()[::-1]		
		for i in range(15):
			lbls[i].entryVar.set( res[i] )
			try:
				lbls[i].cnclbtn.invoke()
			except:pass


class StudentView(tk.Toplevel):
	def __init__(self,parent, Stid,*args, **kwargs):
		tk.Toplevel.__init__(self,parent,*args,**kwargs)

		#window configurations
		self.title("Student Details Pane")
		self.geometry("1150x680+80+0")
		self.resizable(0,0)

		#class variables
		self.st_uid = Stid
		# get all information
		dbms = dbsys.DBrowser('databases/my_sql/Admission_Data_merged.db')
		self.res=dbms.action(""" SELECT * FROM Fee WHERE St_RegistrationId = ? """,(self.st_uid,), 'fetch')[0]
		#main frames
		
		self.left_pane = tk.Frame(self)
		self.left_pane.pack(side='left',fill='y')
		#=====================
		# content to left_pane
		#=====================
		self.cframe = tk.Frame(self.left_pane) #for canvas
		self.cframe.pack(side='top')
		#images
		self.camimg = tk.PhotoImage(file='media/icons/capture .png')
		self.fileimg = tk.PhotoImage(file='media/icons/folder.png')

		self.canvas = tk.Canvas(self.cframe, bg='#777',width=230,height=180)
		self.canvas.pack()

		from tkinterpages.photomanagement import photomanage
		dbms = dbsys.DBrowser('databases/my_sql/Admission_Data_merged.db')
		img=dbms.action(""" SELECT St_Image, St_Name FROM MyStudentDetails WHERE St_RegistrationId = ? """,(self.st_uid,), 'fetch')[0]
		self.add_image(photomanage.PhotoManage.BinToImage(img[0]))

		self.canvas.create_text((100,170),text=img[1],font=('',15),fill='white')

		self.cam_btn = tk.Button(self.canvas,image=self.camimg,bg='#777',bd=0,command=lambda: self.change_st_image("cam"))
		self.file_btn = tk.Button(self.canvas,image=self.fileimg,bg='#777',bd=0,command=lambda: self.change_st_image("file"))

		self.cam_btn.place(x=190,y=40)
		self.file_btn.place(x=190,y=80)

		self.tglFrame = tk.Canvas(self.left_pane,bg='#777',width=230)
		self.tglFrame.pack(fill='both',expand=True)

		stp = {"bg":"#777","width":218,"height":50,"compound":'left','anchor':'nw',"fg":"white"}
		show_basicinfo= customwidgets.ExtendedButtonFrame(self.tglFrame, 'Student Details',lambda: basic_info_frame.tkraise(), "media/icons/baby.png",**stp)
		show_basicinfo.place(x=2,y=10)

		customwidgets.ExtendedButtonFrame(self.tglFrame, 'Submit Fee',lambda: fee_frame.tkraise(), "media/icons/baby.png",**stp).place(x=2,y=80)
		customwidgets.ExtendedButtonFrame(self.tglFrame, 'Close',lambda :self.destroy(), "media/icons/baby.png",**stp).place(x=2,y=160)
		# £=================================================================================================================
		self.mid_pane = tk.Frame(self,width=230, bg='blue')
		self.mid_pane.pack(fill='both',expand='yes')
		#frames setupes
		fstps = {"width":917,"height":680}

		basic_info_frame = StudentViewUpdateFrame(self.mid_pane,self.st_uid, **fstps)
		basic_info_frame.place(x=0)

		fee_frame = tk.Frame(self.mid_pane,**fstps)
		fee_frame.place(x=0)

		tk.Label(fee_frame,text='Submit Monthly Fee').place(x=10,y=20)
		month = ["January","February","March","April","May","June","July","August","September","October","November","Decemer"]
		self.check_btns_lst =  []
		self.eval_monthly_fee = []
		self.eval_bus_fee = []
		x=40
		y=50
		for i in range(12):
			j=customwidgets.LabeledCheck(fee_frame,month[i])
			j.place(x=x,y=y)
			j.entry.bind("<Button-1>",self.count_monthly_fee)
			x+=70
			self.check_btns_lst.append(j)

		tk.Button(fee_frame, text='Calculate Fee : ',command=self.montlhy_fee_amount).place(x=40,y=120)
		self.total_monthly_fee = tk.Entry(fee_frame, font=('',15))
		self.total_monthly_fee.place(x=140,y=120)
		#bus calculator
		self.bus_frame = tk.Frame(fee_frame, height=200,width=920)
		tk.Label(self.bus_frame,text='Submit Monthly Bus Fee').place(x=10,y=10)
		y=50
		x=40
		for i in range(12):
			j=customwidgets.LabeledCheck(self.bus_frame,month[i])
			j.place(x=x,y=y)
			j.entry.bind("<Button-1>",self.count_bus_fee)
			x+=70
			self.check_btns_lst.append(j)
		tk.Button(self.bus_frame, text='Calculate Fee : ',command=self.bus_fee_amount).place(x=40,y=130)
		self.total_bus_fee = tk.Entry(self.bus_frame, font=('',15))
		self.total_bus_fee.place(x=140,y=130)
		#updaate all changes ========================
		tk.Button(fee_frame, text='Submit Fee',font=('',15),height=2,width=15,command=self.update_fee_details).place(x=660,y=600)
		#get databse info ----------------------------------------
		self.set_checkBoxes()
		basic_info_frame.tkraise()	
		#binding function
	def count_monthly_fee(self, event):
		if event.widget['text'] =='No  ': self.eval_monthly_fee.append(self.res[1])
		else:self.eval_monthly_fee.pop()
	def count_bus_fee(self, event):
		if event.widget['text']=='No  ':self.eval_bus_fee.append(self.res[2])
		else:self.eval_bus_fee.pop()
	def bus_fee_amount(self):
		try:
			expression = " + ".join(self.eval_bus_fee)
			self.total_bus_fee.delete(0, tk.END)
			self.total_bus_fee.insert(0, str(eval(expression)))
		except:self.total_bus_fee.insert(0, "0")
	def montlhy_fee_amount(self):
		try:
			expression = " + ".join(self.eval_monthly_fee)
			self.total_monthly_fee.delete(0, tk.END)
			self.total_monthly_fee.insert(0, str(eval(expression)))
		except:self.total_monthly_fee.insert(0, '0')
	def set_checkBoxes(self):
		dbms = dbsys.DBrowser('databases/my_sql/Admission_Data_merged.db')
		res=dbms.action(""" SELECT * FROM Fee WHERE St_RegistrationId = ? """,(self.st_uid,), 'fetch')[0]
		if res==[]:
			print('Sorry! it seems we dont have any reocrds...!')
		else:
			if res[3]=='Bus':
				self.bus_frame.place(x=0,y=220)
				iterr = list(res)[4:]

				for i in range(24):
					if iterr[i]==1:
						self.check_btns_lst[i].entryVar.set( iterr[i] )
						self.check_btns_lst[i].check()
						self.check_btns_lst[i].entry['state']='disabled'
	def update_fee_details(self):
		get_vals = [x.entryVar.get() for x in self.check_btns_lst]
		get_vals.append(self.st_uid)
		qry = """
		UPDATE Fee 
		SET January = ?, Febraury = ?, March = ?, April = ?, May = ?, June = ?, July = ?, August = ?, September = ?, 
		October = ?, November = ?, December = ?,
		Jan_bus = ?, Feb_bus = ?, March_bus = ?, April_bus = ?, May_bus = ?, June_bus = ?, July_bus = ?, 
		August_bus = ?, Sep_bus = ?, Oct_bus = ?, Nov_bus = ?, Dec_bus = ?
		WHERE St_RegistrationId = ?
		"""
		dbms = dbsys.DBrowser('databases/my_sql/Admission_Data_merged.db')
		dbms.action(qry, tuple(get_vals), 'updt')
		customwidgets.WindowAlert("Databse Updated!","Fee Details Updated Successfuly")
		self.set_checkBoxes()
	def add_image(self,lcn='media/icons/edit_user.png'):
		self.img = tk.PhotoImage(file=lcn).subsample(2,3)
		self.canvas.create_image( (90,80) , image=self.img)
	def change_st_image(self,cheker):
		from tkinterpages.photomanagement import photomanage
		if cheker == "cam":
			v = tk.Label(self)
			lcn=photomanage.PhotoManage.TakePhoto(v)
		elif cheker == "file":
			v = tk.Label(self)
			lcn=photomanage.PhotoManage.choosePhoto(v)
		self.add_image(lcn)
		print('sdfsdfsdfasdfasdfafsdf',self.st_uid)
		dbms=dbsys.DBrowser('databases/my_sql/Admission_Data_merged.db')
		dbms.action(""" UPDATE MyStudentDetails SET St_Image = ? WHERE St_RegistrationId = ?""", (photomanage.PhotoManage.imgBin(lcn),self.st_uid),'updt')
		#show alert
		customwidgets.WindowAlert("Image Changed!","Image was updated successfully!")