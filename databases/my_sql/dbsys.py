import sqlite3
class DBrowser:
	def __init__(self,dbname):
		self.db=dbname
		self.db_instance = self.connection()
	def connection(self):
		db=sqlite3.connect(self.db)
		cursor= db.cursor()
		return (db,cursor)
	def action(self, qry,vls,aim):
		d =self.db_instance
		if aim=='':pass
		elif aim=='fetch':
			d[1].execute(qry,vls)
			fd=d[1].fetchall()
			d[0].close()
			return fd
		elif aim=='updt':
			d[1].execute(qry,vls)
			d[0].commit()
			d[0].close()
			return True