import tkinter as tk
from tkinter import messagebox,simpledialog,LabelFrame
from tkinterpages import customwidgets,Validator
from tkinterpages.photomanagement import photomanage
from tkinterpages.forms.forms_attrib import forms_attrib
from tkinter.ttk import Combobox
from databases.my_sql import dbsys

class AdmissionForm(tk.Toplevel):
	def __init__(self,parent,studenstregId,*args,**kwargs):
		tk.Toplevel.__init__(self,parent,*args, **kwargs)
		self._P = parent
		self.geometry('{}x{}+0+0'.format(1200,700))
		self.resizable(0,0)
		self.title('Snehlee Admission Form')
		self.container=  tk.Frame(self)
		self.container.pack(anchor='nw',fill='both',expand=True)
		#databse table stundest id for all
		self.my_student_id = studenstregId
		#show id
		tk.Label(self,text="Student Registration Id: %s"%self.my_student_id,font=('',15),fg='green').place(x=400,y=25)
		#image 
		self.std_image=customwidgets.ImageLabel(self.container,'Choose Student Image')
		self.std_image.imglbl.configure(width=200,height=210)
		self.std_image.place(x=900,y=5)
		#clas of admission
		CLASSES	= ['Nursey','LKG','UKG','1','2','3','4','5','6','7','8','9','10','11','12']
		self.class_selected= customwidgets.cbb(self.container,'Class in which admission is sought for', CLASSES)
		self.class_selected.place(x=10,y=20)

		self.name_of_student=customwidgets.LabeledEntry(self.container,"Name of the child")
		self.name_of_student.entry['width']=80
		self.name_of_student.place(x=10,y=70)
		#gender and age
		GEND=['Male','Female','Rather not say']
		self.std_gender=customwidgets.cbb(self.container,'Gender',GEND)
		self.std_gender.place(x=10,y=120)

		self.std_age=customwidgets.Dateentry(self.container,'Date Of Birth')
		self.std_age.place(x=200,y=120)
		#blood group of child and caste
		BLOOD_GROUPS=['A +ve','A -ve','B +ve','B -ve','O +ve','O -ve','Ab +ve', 'Ab -ve']
		self.std_blood_group= customwidgets.cbb(self.container,'Blood Group of Child',BLOOD_GROUPS)
		self.std_blood_group.place(x=400,y=120)

		CASTES=['General','SC','ST','OBC','EWS','Disable','S.G Child']
		self.std_caste=customwidgets.cbb(self.container,'Caste',CASTES)
		self.std_caste.place(x=10,y=170)
		#mobile and email and nationaliyt and adhar
		self.std_adhar= customwidgets.LabeledEntry(self.container,'Adhar No.')
		self.std_adhar.place(x=10,y=170)

		self.std_mobile=customwidgets.LabeledEntry(self.container,'Child\'s Mobile No.')
		self.std_mobile.place(x=200,y=170)

		self.std_email=customwidgets.LabeledEntry(self.container,'Child\'s Email')
		self.std_email.place(x=400,y=170)

		#mother and Father popup frames
		father_popup_frame_button= customwidgets.PopUpMidContaierFrame(self.container,'Father\'s Details',(100,50))
		father_popup_frame_button.place(x=10,y=220)

		self.father_details=forms_attrib.DetailsFrameEntry(father_popup_frame_button.sub_frame,'Father')
		self.father_details.pack()
		#mother
		mother_popup_frame_button= customwidgets.PopUpMidContaierFrame(self.container,'Mother\'s Details',(100,50))
		mother_popup_frame_button.place(x=200,y=220)
		self.Mother_details=forms_attrib.DetailsFrameEntry(mother_popup_frame_button.sub_frame,'Mother')
		self.Mother_details.pack()
		#name and local address of guardian
		guardian_pop_frame_button=customwidgets.PopUpMidContaierFrame(self.container,'Name and Address of local guardian',(100,50))
		guardian_pop_frame_button.place(x=400,y=220)
		self.Guardian_details=forms_attrib.DetailsFrameEntry(guardian_pop_frame_button.sub_frame,'Guardian')
		self.Guardian_details.pack()
		#lab3el 
		tk.Label(self.container,text='Residential Address: '+' - - '*20).place(x=10,y=262)
		#address of the student
		self.res_full_addrs=customwidgets.LabeledEntry(self.container,'Street Address')
		self.res_full_addrs.entry['width']=75
		self.res_full_addrs.place(x=50,y=290)

		self.res_addrs_district=customwidgets.cbb(self.container,'District',["Mau", "Azamgarh"])
		self.res_addrs_district.place(x=50,y=340)

		self.res_addrs_state=customwidgets.cbb(self.container,'State',["Uttar Pradesh"])
		self.res_addrs_state.place(x=250, y=340)

		self.res_addrs_zipc=customwidgets.LabeledEntry(self.container,'PIN Code/Postal Code')
		self.res_addrs_zipc.place(x=450,y=340)

		tk.Label(self.container,text='Permanent Address: '+' - - '*20).place(x=10,y=410) 
		self.addrs_same = tk.Checkbutton(self.container,text='Same as Residential Address',name="1",command=self.addrs_are_same)
		self.addrs_same.place(x=550,y=412)
		#address of the student
		self.per_full_addrs=customwidgets.LabeledEntry(self.container,'Street Address')
		self.per_full_addrs.entry['width']=75
		self.per_full_addrs.place(x=50,y=440)

		self.per_addrs_district=customwidgets.cbb(self.container,'District',["Mau", "Azamgarh"])
		self.per_addrs_district.place(x=50,y=490)

		self.per_addrs_state=customwidgets.cbb(self.container,'State',["Uttar Pradesh"])
		self.per_addrs_state.place(x=250, y=490)

		self.per_addrs_zipc=customwidgets.LabeledEntry(self.container,'PIN Code/Postal Code')
		self.per_addrs_zipc.place(x=450,y=490)


		tk.Label(self.container,text='Some other details: '+' - - '*20).place(x=10,y=545)
		#bother sister and previose school  and medical 
		brosis_popup_frame_button= customwidgets.PopUpMidContaierFrame(self.container,'Brother And Sister Details',(100,50))
		brosis_popup_frame_button.place(x=50,y=575)

		self.brother_and_sister_details = forms_attrib.AddRemoveEntry(brosis_popup_frame_button.sub_frame,self.my_student_id)
		self.brother_and_sister_details.pack()
		###########################################################################################################
		prev_scl_popup_frame_button= customwidgets.PopUpMidContaierFrame(self.container,'Previous School Details', (100,50))
		prev_scl_popup_frame_button.place(x=370,y=575)

		self.pre_SchoolD=forms_attrib.PrevSchoolDetailsFrame(prev_scl_popup_frame_button.sub_frame)
		self.pre_SchoolD.pack()
		###########################################################################################################
		#name and local address of guardian
		med_pop_frame_button=customwidgets.PopUpMidContaierFrame(self.container,'Medical Details',(100,50))
		med_pop_frame_button.place(x=50,y=610)
		
		###-------------------------------------------------------------------------------------------------------
		#fee structire 
		self.fee_structure_lbl=tk.LabelFrame(self.container,text='Fee Structure',height=360,width=300)
		self.fee_structure_lbl.place(x=860,y=280)

		tk.Label(self.fee_structure_lbl,text='Monthly Fee : ').place(x=5,y=5)
		self.monthly_fee = tk.Entry(self.fee_structure_lbl)
		self.monthly_fee.place(x=100,y=5)
			
		self.Jan =  tk.IntVar()
		self.Feb =  tk.IntVar()
		self.Mar =  tk.IntVar()
		self.Apr =  tk.IntVar()
		self.May =  tk.IntVar()
		self.June = tk.IntVar()
		self.July = tk.IntVar()
		self.Aug =  tk.IntVar()
		self.Sep =  tk.IntVar()
		self.Oct =  tk.IntVar()
		self.Nov =  tk.IntVar()
		self.Dec =  tk.IntVar()

		Apr = tk.Checkbutton(self.fee_structure_lbl,text='Apr',variable=self.Apr).place(x=5,y=30)
		May = tk.Checkbutton(self.fee_structure_lbl,text='May', variable=self.May).place(x=70,y=30)
		June = tk.Checkbutton(self.fee_structure_lbl,text='June', variable=self.June).place(x=128,y=30)
		July = tk.Checkbutton(self.fee_structure_lbl,text='July', variable=self.July).place(x=200,y=30)
		Aug = tk.Checkbutton(self.fee_structure_lbl,text='Aug',variable=self.Aug).place(x=5,y=58)
		Sep = tk.Checkbutton(self.fee_structure_lbl,text='Sep',variable=self.Sep).place(x=70,y=58)	
		Oct = tk.Checkbutton(self.fee_structure_lbl,text='Oct',variable=self.Oct).place(x=128,y=58)
		Nov = tk.Checkbutton(self.fee_structure_lbl,text='Nov',variable=self.Nov).place(x=200,y=58)
		Dec = tk.Checkbutton(self.fee_structure_lbl,text='Dec',variable=self.Dec).place(x=5,y=86)
		Jan = tk.Checkbutton(self.fee_structure_lbl,text='Jan',variable=self.Jan).place(x=70,y=86)
		Feb = tk.Checkbutton(self.fee_structure_lbl,text='Feb',variable=self.Feb).place(x=128,y=86)
		Mar = tk.Checkbutton(self.fee_structure_lbl,text='Mar',variable=self.Mar).place(x=200,y=86)
		tk.Label(self.fee_structure_lbl,text='Mode of Transportation : ',fg='blue').place(x=5,y=120)
		
		mot_cfg={"bg":"#ddd"}
		mot_if_bus= tk.Frame(self.fee_structure_lbl,width=280,height=130,**mot_cfg)
		
		tk.Label(mot_if_bus,text='Bus Charge : ',**mot_cfg).place(x=5,y=5)
		self.bus_charge = tk.Entry(mot_if_bus)
		self.bus_charge.place(x=100,y=5)

		self.Jan_bus =  tk.IntVar()
		self.Feb_bus =  tk.IntVar()
		self.Mar_bus =  tk.IntVar()
		self.Apr_bus =  tk.IntVar()
		self.May_bus =  tk.IntVar()
		self.June_bus = tk.IntVar()
		self.July_bus = tk.IntVar()
		self.Aug_bus =  tk.IntVar()
		self.Sep_bus =  tk.IntVar()
		self.Oct_bus =  tk.IntVar()
		self.Nov_bus =  tk.IntVar()
		self.Dec_bus =  tk.IntVar()
		
		Apr_bus = tk.Checkbutton(mot_if_bus,text='Apr',variable=self.Apr_bus,name="a",**mot_cfg).place(x=5,y=30)
		May_bus = tk.Checkbutton(mot_if_bus,text='May', variable=self.May_bus,**mot_cfg).place(x=70,y=30)
		June_bus = tk.Checkbutton(mot_if_bus,text='June', variable=self.June_bus,**mot_cfg).place(x=128,y=30)
		July_bus = tk.Checkbutton(mot_if_bus,text='July', variable=self.July_bus,**mot_cfg).place(x=200,y=30)
		Aug_bus = tk.Checkbutton(mot_if_bus,text='Aug',variable=self.Aug_bus,**mot_cfg).place(x=5,y=58)
		Sep_bus = tk.Checkbutton(mot_if_bus,text='Sep',variable=self.Sep_bus,**mot_cfg).place(x=70,y=58)
		Oct_bus = tk.Checkbutton(mot_if_bus,text='Oct',variable=self.Oct_bus,**mot_cfg).place(x=128,y=58)
		Nov_bus = tk.Checkbutton(mot_if_bus,text='Nov',variable=self.Nov_bus,**mot_cfg).place(x=200,y=58)
		Dec_bus = tk.Checkbutton(mot_if_bus,text='Dec',variable=self.Dec_bus,**mot_cfg).place(x=5,y=90)
		Jan_bus = tk.Checkbutton(mot_if_bus,text='Jan',variable=self.Jan_bus,**mot_cfg).place(x=70,y=90)
		Feb_bus = tk.Checkbutton(mot_if_bus,text='Feb',variable=self.Feb_bus,**mot_cfg).place(x=128,y=90)
		Mar_bus = tk.Checkbutton(mot_if_bus,text='Mar',variable=self.Mar_bus,**mot_cfg).place(x=200,y=90)
		#mot mode of transportation
		def set_motFrame():
			if self.mot_var.get()=="Bus":mot_if_bus.place(x=10,y=200)
			else:mot_if_bus.place_forget()
		mot_if_bus.place(x=10,y=200)
		self.mot_var = tk.StringVar()
		
		mot_self = tk.Radiobutton(self.fee_structure_lbl,command=set_motFrame, variable=self.mot_var,value="Self", text='Self')
		mot_self.place(x=10,y=145)
		mot_self.invoke()

		mot_bus = tk.Radiobutton(self.fee_structure_lbl,command=set_motFrame, variable=self.mot_var,value="Bus",text='School Bus')
		mot_bus.place(x=10,y=175)
		#button to proceed details
		self.proceed_button = tk.Button(self.container,text='Add Student',command=self.all_entries,bg='#8ff',font=('',14))
		self.proceed_button.place(x=1040, y=660)

		self.wm_protocol("WM_DELETE_WINDOW",self.as_to_close)
	
	def all_entries(self):
		std_entries = [
			self.class_selected.entryVar.get(),
			self.name_of_student.entryVar.get(),
			self.std_gender.entryVar.get(),
			self.std_age.entryVar.get(),
			self.std_blood_group.entryVar.get(),
			self.std_caste.entryVar.get(),
			self.std_adhar.entryVar.get(),
			self.std_mobile.entryVar.get(),
			self.std_email.entryVar.get(),
			photomanage.PhotoManage.imgBin(self.std_image.pth) ]
		
		residential_adr = [
			self.res_full_addrs.entryVar.get(),
			self.res_addrs_district.entryVar.get(),
			self.res_addrs_state.entryVar.get(),
			self.res_addrs_zipc.entryVar.get(),
			self.per_full_addrs.entryVar.get(),
			self.per_addrs_district.entryVar.get(),
			self.per_addrs_state.entryVar.get(),
			self.per_addrs_zipc.entryVar.get()  ]

		father_entries = self.father_details.all_entries()
		std_entries.extend(father_entries)
		std_entries.extend(residential_adr)

		mother_entries = self.Mother_details.all_entries()
		guardian_entries = self.Guardian_details.all_entries()
		brosis_entry  = self.brother_and_sister_details.getValues()
		pre_school = self.pre_SchoolD.all_entries()
		Fee_details= [
		self.monthly_fee.get(),self.bus_charge.get(),self.mot_var.get(),
		self.Jan.get(), self.Feb.get(), self.Mar.get(), self.Apr.get(),self.May.get(), self.June.get(), 
		self.July.get(), self.Aug.get(), self.Sep.get(), self.Oct.get(),self.Nov.get(), self.Dec.get(),
		self.Jan_bus.get(), self.Feb_bus.get(), self.Mar_bus.get(), self.Apr_bus.get(),self.May_bus.get(),
		self.June_bus.get(), self.July_bus.get(),self.Aug_bus.get(), self.Sep_bus.get(), self.Oct_bus.get(), 
		self.Nov_bus.get(), self.Dec_bus.get()		]

		my_list=[std_entries, mother_entries,  guardian_entries, brosis_entry, pre_school, Fee_details]
		for each in my_list:
			each.insert(0,self.my_student_id)
		#add basic datetails
		self.add_to_database(my_list)

	def add_to_database(self,all_data):
		#getting all fields
		student, mother,guardian,brosis,school, fee_val = all_data

		student_query = """
		INSERT INTO MyStudentDetails( 
		St_RegistrationId, St_class, St_Name, St_Gender, St_dob,St_BloodGroup,St_caste,St_adhar,St_Mobile,St_Email,St_image,
		F_firstName,F_midName,F_lastName,F_dob,F_nationality,F_education,F_occupation,F_annualIncome,F_mobile,F_email,F_officeAddrs,F_image,
		res_Street_adrs,res_District,res_State,res_Zip_code,
		per_Street_adrs,per_District,per_State,per_Zip_code )
		VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?) """
		print('adding student details')
		dbms = dbsys.DBrowser('databases/my_sql/Admission_Data_merged.db')
		dbms.action(student_query, tuple(student), 'updt')
		
		mother_query = """
		INSERT INTO MyStudentMotherDetails(
		St_RegistrationId,M_firstName,M_midName,M_lastName,M_dob,M_nationality,M_education,M_occupation,M_annualIncome,M_mobile,
		M_email,M_officeAddrs,M_image)
		VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?) """
		print('adding mother details')
		dbms = dbsys.DBrowser('databases/my_sql/Admission_Data_merged.db')
		dbms.action(mother_query, tuple(mother), 'updt')

		guardian_query = """
		INSERT INTO MyStudentGuardianDetails(
		St_RegistrationId,G_firstName,G_midName,G_lastName,G_dob,G_nationality,G_education,
		G_occupation,G_annualIncome,G_mobile,G_email,G_officeAddrs,G_image )
		VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?) """
		print('adding guardian details')
		dbms = dbsys.DBrowser('databases/my_sql/Admission_Data_merged.db')
		dbms.action(guardian_query,tuple(guardian),'updt')
		
		brosis.remove(brosis[0]) #remove my_student_id
		brosis_query="""
		INSERT INTO MyStudentBotherAndSisters(
		St_RegistrationId,bs_Name,bs_relation,bs_age,bs_class,bs_institution)
		VALUES(?,?,?,?,?,?) """
		print('adding brother and sister details')
		dbms = dbsys.DBrowser('databases/my_sql/Admission_Data_merged.db')
		dbms.action(brosis_query,brosis[0], 'updt')
		
		school_query="""
		INSERT INTO MyStudentPrevSchool(
		St_RegistrationId,
		scl_name,scl_class,scl_marks,scl_grade,scl_yop,scl_anyAwards,scl_address )
		VALUES(?,?,?,?,?,?,?,?) """
		print('adding last school details')
		dbms = dbsys.DBrowser('databases/my_sql/Admission_Data_merged.db')
		dbms.action(school_query, tuple(school), 'updt')

		fee_query = """
		INSERT INTO Fee (
		St_RegistrationId,Monthly_Charge,Bus_charge,Mode_Of_Trans,January,Febraury,March,April,
		May,June,July,August,September,October,November,December,Jan_bus,Feb_bus,March_bus,
		April_bus,May_bus,June_bus,July_bus,August_bus,Sep_bus,Oct_bus,Nov_bus,Dec_bus )
		VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)"""
		print( tuple(fee_val) )
		dbms = dbsys.DBrowser('databases/my_sql/Admission_Data_merged.db')
		dbms.action(fee_query, tuple(fee_val), 'updt')

		ask_ifdone =  messagebox.askyesno(title='Info...',message='Cheers! Student was added Sucessfully',
													   detail='Do you want to close the window?')
		if ask_ifdone:
			self.destroy()
		else:
			self.proceed_button['state']='disabled'

	def addrs_are_same(self):
		a,b,c,d = (
			self.res_full_addrs.entryVar.get(),
			self.res_addrs_district.entryVar.get(),
			self.res_addrs_state.entryVar.get(),
			self.res_addrs_zipc.entryVar.get(),
			)
		self.per_full_addrs.entryVar.set(a)
		self.per_addrs_district.entryVar.set(b)
		self.per_addrs_state.entryVar.set(c)
		self.per_addrs_zipc.entryVar.set(d)
	def as_to_close(self):
		if  messagebox.askyesno(title='Info', message='Do you want to Quit?',detail='If you close all fields will be cleared!\n you will not be able to restore that again..'):self.destroy()	