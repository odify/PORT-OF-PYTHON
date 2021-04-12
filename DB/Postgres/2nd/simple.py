import psycopg2


def connect():

	try:

		conn = psycopg2.connect(database ="test",
							user = "admin123",
							password = "123password",
							host = "localhost",
							port = "5432")

		cur = conn.cursor()
	
	except (Exception, psycopg2.DatabaseError) as error:
		
		print ("Error", error)
	

	return conn, cur


def create_table():


	conn, cur = connect()

	try:
		# the test database contains a table called emp
		# the schema : (id INTEGER PRIMARY KEY,
		# name VARCHAR(10), salary INT, dept INT)
		# create the emp table

		cur.execute('CREATE TABLE emp (id INT PRIMARY KEY, name VARCHAR(10),
									salary INT, dept INT)')

		# the commit function permanently
		# saves the changes made to the database
		# the rollback() function can be used if
		# there are any undesirable changes and
		# it simply undoes the changes of the
		# previous query
	
	except:

		print('error')

	conn.commit()

def insert_data(id = 1, name = '', salary = 1000, dept = 1):

	conn, cur = connect()

	try:
		cur.execute('INSERT INTO emp VALUES(%s, %s, %s, %s)',
									(id, name, salary, dept))
	
	except Exception as e:

		print('error', e)
	conn.commit()


def fetch_data():

	conn, cur = connect()

	try:
		cur.execute('SELECT * FROM emp')
	
	except:
		print('error !')

	data = cur.fetchall()


	return data

def print_data(data):

	print('Query result: ')
	print()

	for row in data:


		print('id: ', row[0])
		print('name: ', row[1])
		print('salary: ', row[2])
		print('dept: ', row[3])
		print('--------------------------------')


def delete_table():

	conn, cur = connect()

	try:

		cur.execute('DROP TABLE emp')

	except Exception as e:
		print('error', e)

	conn.commit()


if __name__ == '__main__':


	create_table()

	insert_data(1, 'xy', 1000, 2)
	insert_data(2, 'xxy', 100000, 2)
	insert_data(3, 'xxxy', 100, 3)
	insert_data(4, 'xxxxy', 10000, 4)

	data = fetch_data()

	print_data(data)

	delete_table()
