print('importing requirements hold on....!')
import tkinter as tk
from tkinterpages import tkinterpage

class MainApp(tk.Tk):
	def __init__(self,*args,**kwargs):
		tk.Tk.__init__(self,*args,**kwargs)
		#show ui
		self.basic_ui()
		self.auto_fill()

	def basic_ui(self):
		print('creating First Interface')
		self.window=tkinterpage.basicUi(self)
		self.window.pack()
		self.window.login.loginbtn['command']=self.onLogin
	def onLogin(self):
		#find results from db
		res=self.window.login.matchWithDb()
		if not res[0]: self.askToCreateNewAc()
		else:
			print('wait a moment...')
			from tkinterpages import dashboard
			self.window.destroy()
			self.dsbrd=dashboard.Dashboard(self,res)
			self.dsbrd.pack(fill='both',expand=True)			
			self.dsbrd.logout.btn['command']=self.logout		
	def auto_fill(self):
		print('checking if auto fill...')
		try:
			from databases.my_sql import dbsys
			dbms = dbsys.DBrowser("databases/my_sql/recent_login_saved.db")
			val= dbms.action("SELECT * FROM recent_login WHERE SN=?",(1,),'fetch')[0]
			self.window.login.ID.entryVar.set(val[0])
			self.window.login.password.entryVar.set(val[1])
			self.window.login.remempsw.invoke()
		except Exception as e:
			print('error',e)
	def askToCreateNewAc(self):
		""" ask to create new login account if user not matched"""
		from tkinterpages.modifiers import okCancel
		ans=okCancel('User not found..','It seems that you have not Registered yet. Regsiter Now!')
		if ans: self.window.onRegister()
	def logout(self):
		self.dsbrd.destroy()
		self.basic_ui()
		self.auto_fill()
#run app
if __name__ == "__main__":
	print('Starting The App : Student Management System')
	app=MainApp()
	app.mainloop()
	from os import startfile
	startfile("Adveriise.png")
	print('Application Closed.. \nHope you liked it!.. \nPlease Share your Feedback with us! \nStudent Management System Designed and Developed by Shubham Chauhan')


