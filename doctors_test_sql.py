#https://www.tutorialspoint.com/flask/flask_sqlite.htm
#https://www.pythoncentral.io/advanced-sqlite-usage-in-python/0
#http://www.numericalexpert.com/blog/sqlite_blob_time/sqlite_time_etc.html

import sqlite3
from datetime import date, datetime

conn = sqlite3.connect('database.db', detect_types=sqlite3.PARSE_DECLTYPES|sqlite3.PARSE_COLNAMES)
#parse column types to ensure date-time handled correctly.
print ("Opened database successfully")
c = conn.cursor()
c.execute('CREATE TABLE doctors(id integer primary key, name TEXT, start_time TIMESTAMP, end_time TIMESTAMP)')
#c.execute('DROP TABLE booking')
c.execute('CREATE TABLE booking(id integer primary key, doctorsid INTEGER, patientname TEXT, start_time TIMESTAMP, patientemail TEXT, patientMobile TEXT)')

#name, start_time, end_time
print ("Table created successfully")
conn.commit()
conn.close()
#----------------------------------
conn = sqlite3.connect('database.db', detect_types=sqlite3.PARSE_DECLTYPES|sqlite3.PARSE_COLNAMES)
c = conn.cursor()
c.execute("INSERT INTO doctors(name, start_time, end_time) values (?, ?, ?)", ("Fred Smith","2019-05-13 12:00:00", "2019-05-13 13:00:00"))
c.execute("INSERT INTO doctors(name, start_time, end_time) values (?, ?, ?)", ("Peter Johnson","2019-05-13 09:00:00", "2019-05-13 11:00:00"))
conn.commit()
conn.close()
#----------------------------------
# Retrieve the inserted object
conn = sqlite3.connect('database.db', detect_types=sqlite3.PARSE_DECLTYPES|sqlite3.PARSE_COLNAMES)
c = conn.cursor()
c.execute('''SELECT start_time FROM doctors''')
row = c.fetchone()
print('The date is {0} and the datatype is {1}'.format(row[0], type(row[0])))
conn.close()
#-----------------------------------
conn = sqlite3.connect('database.db', detect_types=sqlite3.PARSE_DECLTYPES|sqlite3.PARSE_COLNAMES)
c = conn.cursor()
c.execute('''SELECT * FROM doctors''')
rows = c.fetchall()
for row in rows:
    print(row)
    print(row[2], type(row[2]), row[3])

conn.close()
#-----------------------------------
