#!/usr/bin/python2.7

import MySQLdb

### PART 0 ### Connecting to DB
db = MySQLdb.connect('localhost', 'root', 'cisco', 'python')

if db == None:
	print "Connection failed"
else:
	print "All good !"

cursor = db.cursor()

cursor.execute("SELECT VERSION();")
data = cursor.fetchall()
print data

### PART 1 ### Creating a Table and checking it

sql = """CREATE TABLE TEST (
			NAME CHAR(20) NOT NULL,
			AGE INT,
			GENDER CHAR(1),
			INTEREST CHAR(20));"""

try:
	print "Adding to the Database"
	cursor.execute("DROP TABLE IF EXISTS TEST")
	cursor.execute(sql)
	db.commit()
except:
	print "Error at sql query"
	db.rollback()

cursor.execute("SHOW TABLES;")
data = cursor.fetchall()
print data

### PART 2 ### Adding data to the table

sql = """INSERT INTO TEST (NAME, AGE, GENDER, INTEREST) VALUES ("Ramon", 23, "M", "Money")"""

try:
	cursor.execute(sql)
	db.commit()
except:
	print "Error at sql query"
	db.rollback()


cursor.execute("SELECT * FROM TEST;")
data = cursor.fetchall()

### PART 3 ### Adding data to the table via scripting
data_add = (("Adi", 21, "M", "Impact"), ("Bia", 24, "F", "Love"), ("Glore", 34, "F", "Apple"))

for person in data_add:
	cursor.execute('INSERT INTO TEST (NAME, AGE, GENDER, INTEREST) values ("%s", "%d", "%s", "%s")' % (person[0], person[1], person[2], person[3]))
	db.commit()
	print "Job done"


print data

#cursor.execute("DROP TABLE IF EXISTS TEST")
db.close()