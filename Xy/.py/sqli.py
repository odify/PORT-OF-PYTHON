import sqlite3

connect = sqlite3.connect(':memory:')

cursor = connect.cursor()

people_data = {
 1:('Kuba S', 37),
 2:('Lara C', 24),
 3:('Tomy D', 23),
 4:('Nora B', 34),
 5:('Zack S', 44),
 6:('Rana S', 38),
 7:('Rose M', 32),
 8:('Ania L', 28)
}


def create():
    sqlstr = 'CREATE TABLE PEOPLE(ID int AUTO_INCREMENT, Name varchar(255), Age int)'
    cursor.execute(sqlstr)
    connect.commit()





def insert(id, name, age):
    sqlstr = 'INSERT INTO PEOPLE(ID, Name, Age) VALUES ("' + str(id) + '", "' + str(name) + '", ' + str(age) + ')'
    cursor.execute(sqlstr)
    connect.commit()



def filter(f):
    sqlstr = 'SELECT * FROM PEOPLE WHERE ' + f + ' ORDER BY Name'
    print ('Database filtered by:', sqlstr, '\n')
    print ('ID', 'Name            ', '    Age')
    print ("-----------------------------")
    for row in cursor.execute(sqlstr):
        print(('{0:{width}}'.format(row[0], width=2)),
              ('{0:{width}}'.format(row[1], width=20)),
              ('{0:{width}}'.format(row[2], width=2)))
    print('-----------------------------\n')


def display_all():
    sqlstr = 'SELECT * FROM PEOPLE'
    print ('Showing the whole database')
    print ('ID', 'Name            ', '    Age')
    print ("-----------------------------")
    for row in cursor.execute(sqlstr):
        print(('{0:{width}}'.format(row[0], width=2)),
              ('{0:{width}}'.format(row[1], width=20)),
              ('{0:{width}}'.format(row[2], width=2)))
    print('-----------------------------\n')


create()
for k, v in people_data.items():
    insert(k, v[0], v[1])

filter('Age>25')
print('* ' * 19, '\n')
filter('Name LIKE "%k%"')
print('* ' * 19, '\n')
display_all()


cursor.close()

# n = name
# a = age
# insert(9, n, a) 4 new records




