import tkinter as tk
from tkinterpages import customwidgets,tkinterpage
from tkinterpages.dashboard_executables import dashboard_extensions

class Dashboard(tk.Frame):
	def __init__(self,parent, loginIdPsw,*args, **kwargs):
		tk.Frame.__init__(self,parent, *args, **kwargs)
		self._P=parent
		self._P.title('Dashboard')
		self._P.geometry('1200x700+20+0')
		self._P.resizable(0,0)

		self.packed_window = []
		#frames 	# 940x 677
		kw={'height':700,'width':990} #for frames that are in main view excpet navigantion
		self.home_btn_frame = dashboard_extensions.HomePage(self,loginIdPsw,**kw)
		self.student_mng_page=dashboard_extensions.StdMngPage(self,**kw)
		self.user_mng=dashboard_extensions.UpdateUser(self,loginIdPsw,**kw)
		
		left_menu_frame=tk.Frame(self,width=210,height=700,bd=1,bg='#777',relief='ridge')
		left_menu_frame.pack(side='left',fill='y')

		c={'width':200,"compound":'left',"font":('',13),'anchor':'nw','bg':'#777','fg':'white'}
		left_menu_frame_home_button=customwidgets.ExtendedButtonFrame(left_menu_frame,'Home..',
			lambda:self.packer(self.home_btn_frame),'media/icons/dash_menu_btn_col.png',**c)
		left_menu_frame_home_button.place(x=0)
		
		students_corner = customwidgets.ExtendedButtonFrame(left_menu_frame,'Manage Student',
			lambda:self.packer(self.student_mng_page),'media/icons/people_menu_btn_col.png',**c)
		students_corner.place(x=2,y=120)

		user_profile_settings = customwidgets.ExtendedButtonFrame(left_menu_frame,'User Settings',
			lambda:self.packer(self.user_mng),'media/icons/people_stt_menu_col.png',**c)
		user_profile_settings.place(x=2,y=240)
		self.logout =  customwidgets.ExtendedButtonFrame(left_menu_frame,'Log Out',
			None,'media/icons/dash_menu_btn_col.png',**c)
		self.logout.place(x=2,y=625)
		left_menu_frame_home_button.btn.invoke()
	def packer(self,widget):
		if len(self.packed_window) !=0:
			popped=self.packed_window.pop()
			popped.pack_forget()
		self.packed_window.append(widget)
		widget.pack()