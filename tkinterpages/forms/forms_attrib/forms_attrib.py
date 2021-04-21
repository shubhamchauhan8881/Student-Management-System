import tkinter as tk
from tkinterpages import customwidgets
from tkinterpages.photomanagement import photomanage

class DetailsFrameEntry(tk.Frame):
	def __init__(self,parent,personName, *args, **kwargs):
		tk.Frame.__init__(self,parent, *args, **kwargs)
		self.p=parent
		self.backround=tk.PhotoImage(file=r'media/ui/detail_frame.uis')
		
		self.bg=tk.Label(self,image=self.backround)
		self.bg.pack()
		
		self._image=customwidgets.ImageLabel(self,'Choose {} Image'.format(personName))
		self._image.place(x=67,y=65)

		kw={'bg':'#666','fg':'white'}
		INCOME_LIST=['Less than 10,000','10,000-30,000','30,000-60,000','More than 60,000']

		tk.Label(self,text='{} Details'.format(personName), font=('Joker',14), **kw).place(x=345,y=30)

		name=customwidgets.LabeledEntry(self,'First name',**kw)

		m_name=customwidgets.LabeledEntry(self,'Middle name',**kw)
		
		l_name=customwidgets.LabeledEntry(self,'Last name',**kw)
		
		age=customwidgets.Dateentry(self,'Date of birth',**kw)
		age.entry['width']=20
		
		nlty=customwidgets.LabeledEntry(self,'Nationality',**kw)
		
		edu=customwidgets.LabeledEntry(self,'Education',**kw)
		
		occupation=customwidgets.LabeledEntry(self,'Occupation',**kw)
		
		annul_income=customwidgets.cbb(self,'Annul Income',INCOME_LIST,**kw)
		annul_income.entry['width']=20
		
		mobile=customwidgets.LabeledEntry(self,'Mobile Number',**kw)
		
		email=customwidgets.LabeledEntry(self,'Email',**kw)
		
		off_addr = customwidgets.LabeledEntry(self,'Office Address', **kw)
		off_addr.entry['width']=38

		tk.Label(self,text='Note: First name, Last name, DOB, Occupation, Mobile number are required fileds. ',**kw).place(x=310,y=460)
		# -------------- placingd
		name.place(x=310,y=80)
		m_name.place(x=510,y=80)
		l_name.place(x=710,y=80)
		age.place(x=310,y=170)
		nlty.place(x=510,y=170)
		edu.place(x=710,y=170)
		occupation.place(x=310,y=260)
		annul_income.place(x=510,y=260)
		mobile.place(x=710,y=260)
		off_addr.place(x=310, y=350)
		email.place(x=710,y=350)
	def all_entries(self):	 
		vl=[]
		fields=self.place_slaves()[::-1][2:]
		fields.remove(fields[0])
		for lbls in fields:
			vl.append(lbls.entryVar.get().strip())
		imglcn=self._image.pth
		vl.append(photomanage.PhotoManage.imgBin(imglcn))
		return vl


class PrevSchoolDetailsFrame(tk.Frame):
	def __init__(self,parent, *args, **kwargs):
		tk.Frame.__init__(self,parent, *args, **kwargs)
		self.p=parent
		self.backround=tk.PhotoImage(file=r'media/ui/prev_sl_frame.uis')
		self.bg=tk.Label(self,image=self.backround)
		self.bg.pack()
		kw={'bg':'#666','fg':'white'}
		self.CLASSES	= ['Nursey','LKG','UKG','1','2','3','4','5','6','7','8','9','10','11','12']

		last_school_name=customwidgets.LabeledEntry(self,'Name of the School',**kw)
		last_school_class=customwidgets.cbb(self,'Class attended',self.CLASSES,**kw)
		last_school_marks=customwidgets.LabeledEntry(self,'Marks Obtained',**kw)
		last_school_grade=customwidgets.LabeledEntry(self,'Grade',**kw)
		last_school_yop=customwidgets.LabeledEntry(self,'Year of passing', **kw)
		last_school_awards=customwidgets.LabeledEntry(self,'Any awards won in Academics or Sports ',**kw)
		last_school_fullAddrs=customwidgets.LabeledEntry(self,'Full Address',**kw)
		
		tk.Label(self.bg,text='Note: All fileds are necessary excpet Awards hitory..',**kw).place(x=510,y=455)
		#configurations
		last_school_name.entry['width']=58
		last_school_class.entry['width']=20
		last_school_awards.entry['width']=38
		last_school_fullAddrs.entry['width']=58
		# -------------- placingd
		last_school_name.place(x=310,y=80)
		last_school_class.place(x=310,y=170)
		last_school_marks.place(x=510,y=170)
		last_school_grade.place(x=710,y=170)
		last_school_yop.place(x=310,y=260)
		last_school_fullAddrs.place(x=310, y=350)
		last_school_awards.place(x=510, y=260)	
	def all_entries(self):	 
		vl=[]
		for lbls in self.place_slaves()[::-1]:
			vl.append(lbls.entryVar.get().strip())
		return vl
		
class BrotherSister(tk.Frame):
	def __init__(self,parent,sid,*args, **kwargs):
		tk.Frame.__init__(self, parent, *args, **kwargs)
		kw={'bg':'#666','fg':'white'}
		self['bg']=kw['bg']
		RELN=['Elder Brother','Elder Sister','Younger Brother','Younger Sister']
		self.sid= sid
		self.rowCount = tk.Label(self,bd=0,anchor='center',**kw)
		self.name = customwidgets.LabeledEntry(self, 'Name',**kw)
		self.relation = customwidgets.cbb(self,'Relation',RELN,**kw)
		self.age= customwidgets.LabeledEntry(self,'Age',**kw)
		self.cls= customwidgets.LabeledEntry(self,'Class',**kw)
		self.instn= customwidgets.LabeledEntry(self,'Institution',**kw)
		#packings
		self.rowCount.grid(row=0,column=0)
		self.name.grid(row=0,column=1,pady=1,padx=2)
		self.relation.grid(row=0,column=2,padx=2)
		self.age.grid(row=0,column=3,padx=2)
		self.cls.grid(row=0,column=4,padx=2)
		self.instn.grid(row=0,column=5,padx=2)
	def vals(self):
		v=[self.sid]
		grds=self.grid_slaves()
		grds.pop()
		for e in grds[::-1]:
			v.append(e.entryVar.get())
		return tuple(v)
	
class AddRemoveEntry(tk.Frame):
	def __init__(self, parent,sid,*args, **kwargs):
		tk.Frame.__init__(self, parent,*args, **kwargs)
		self.added_fields=[]
		self.sid = sid

		self.backround=tk.PhotoImage(file=r'media/ui/sample_frame.uis')
		self.bg=tk.Label(self,image=self.backround)
		self.bg.pack()

		self.btn_container=tk.Frame(self,bg='#666')
		self.btn_container.place(x=10,y=80)
		kw={'relief':'flat','bd':2,'overrelief':'ridge','bg':'#666','fg':'white','overrelief':'ridge'}
		self.add_btn=tk.Button(self.btn_container,text='Add One more column',command=self.add,**kw)
		self.rmv_btn=tk.Button(self.btn_container,text='Remove one column',command=self.remove,**kw)
		#pack()
		self.add_btn.pack(side='bottom',expand=1,anchor='center',fill='x')
		self.rmv_btn.pack(side='bottom',expand=1,anchor='center',fill='x')
		self.add()
	def add(self):
		if not len(self.added_fields)==7:
			field=BrotherSister(self.btn_container,self.sid)
			field.rowCount['text']=len(self.added_fields)+1
			field.pack()
			self.added_fields.append(field)
		else:customwidgets.alert_CloseLabel(self,"Can not add more than 7 fields ").place(y=465,x=310)
	def remove(self):
		if not len(self.added_fields)==1:
			rmved_wgt=self.added_fields.pop()
			rmved_wgt.destroy()
	def getValues(self):
		vals=[]
		for e in self.added_fields:
			vl=e.vals()
			vals.append(vl)
		return vals

class Medic(tk.Frame):
	def __init__(self,parent,*args, **kwargs):
		tk.Frame.__init__(self,parent, *args, **kwargs)
		self.background= tk.PhotoImage(file=r'media/ui/prev_sl_frame.uis')
		self.bg= tk.Label(self,image=self.background)
		self.bg.pack()
		self.container=tk.Frame(self,bg='pink',height=300,width=300)
		self.container.place(x=320,y=80)