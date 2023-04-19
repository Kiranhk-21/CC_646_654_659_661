import mysql.connector

mydb = mysql.connector.connect(host = "localhost",
                               user = "root",database="todo_list")
cursor = mydb.cursor()

def create_table():
	cursor.execute('CREATE TABLE IF NOT EXISTS todo_list(task TEXT,task_status TEXT,task_due_date DATE)')


def add_data(task,task_status,task_due_date):
	cursor.execute('INSERT INTO todo_list(task,task_status,task_due_date) VALUES (?,?,?)',(task,task_status,task_due_date))
	mydb.commit()


def view_all_data():
	cursor.execute('SELECT * FROM todo_list')
	data = cursor.fetchall()
	return data

def view_all_task_names():
	cursor.execute('SELECT DISTINCT task FROM todo_list')
	data = cursor.fetchall()
	return data

def get_task(task):
	cursor.execute('SELECT * FROM todo_list WHERE task="{}"'.format(task))
	data = cursor.fetchall()
	return data

def get_task_by_status(task_status):
	cursor.execute('SELECT * FROM todo_list WHERE task_status="{}"'.format(task_status))
	data = cursor.fetchall()


def edit_task_data(new_task,new_task_status,new_task_date,task,task_status,task_due_date):
	cursor.execute("UPDATE todo_list SET task =?,task_status=?,task_due_date=? WHERE task=? and task_status=? and task_due_date=? ",(new_task,new_task_status,new_task_date,task,task_status,task_due_date))
	mydb.commit()
	data = cursor.fetchall()
	return data

def delete_data(task):
	cursor.execute('DELETE FROM todo_list WHERE task="{}"'.format(task))
	mydb.commit()