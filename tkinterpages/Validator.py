from tkinter import messagebox
def alrt(fill_it,err=None):
	msg=messagebox.showinfo(title="Alert!", message=err, detail=fill_it)
	return msg
	
class Validator:
	def mobileNumb(tagName,maxinput=10):
		if tagName.get().isdigit() == False:
			v=tagName.get()[:-1]
			tagName.set(v)
		elif tagName.get().isalpha() == True:
			tagName.set('')
		elif tagName.get()[0] in ['1','2','3','4','5']:
			tagName.set("")
		elif len(tagName.get()) > 10:
			print('Mobile Number Cant be more than 10')
			v=tagName.get()[:maxinput]
			tagName.set(v)
		else:
			return False
	def limitedNum(tagName,maxinput=12 ):
		if len(tagName.get())==0:
			pass
		elif tagName.get().isdigit() == False:
			tagName.set('')
		elif len(tagName.get()) > 10:
			v=tagName.get()[:maxinput]
			tagName.set(v)
		else:
			pass
	def onlyChar(tagName):
		if tagName.get().isdigit() == False:
			pass
		else:
			v=tagName.get()[:-1]
			tagName.set(v)

	def formValidate(tagList):
		
		for eachtag in tagList:
			if eachtag.get() == "":
				alrt('Please Fill the details')
				eachtag.focus_set()
				eachtag['bg']='#eee'
				break
			else:
				pass