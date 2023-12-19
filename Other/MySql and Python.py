'''

https://www.tutorialspoint.com/python_mysql/index.htm

import MySQLdb

#db = MySQLdb.connect(host, username, passwd, dbName, port, socket) - port, socket optional
db = MySQLdb.connect("localhost", "root", "root@123")
cursor = db.cursor()
sql = "CREATE DATABASE TUTORIALS" #Creates new database named Tutorials
cursor.execute(sql)
db.close() #disconnect from server

#other examples of sql
cursor.execute("DROP DATABASE TUTORIALS")

#Sample code to create a table
db = MySQLdb.connect("localhost", "root", "root@123")
cursor = db.cursor()
sql = """CREATE TABLE tutorials_tbl(
			tutorial_id INT NOT NULL AUTO_INCREMENT,
			tutorial_title VARCHAR(100) NOT NULL,
			tutorial_author VARCHAR(40) NOT NULL,
			submission_date DATE,
			PRIMARY KEY (tutorial_id));"""
cursor.execute(sql)
print("tutorials_tbl created successfully")
db.close()

#Create data
#!/usr/bin/python

import MySQLdb

# Open database connection
db = MySQLdb.connect("localhost","root","root@123", "TUTORIALS")

# prepare a cursor object using cursor() method
cursor = db.cursor()

sql = """INSERT INTO tutorials_tbl
         (tutorial_title,tutorial_author, submission_date)
         VALUES ('HTML 5', 'Robert', '2010-02-10'),
         ('Java', 'Julie', '2020-12-10'),
         ('JQuery', 'Julie', '2020-05-10')
         """

# execute SQL query using execute() method.
cursor.execute(sql)

# commit the record
db.commit()

#Get all data from the db
#!/usr/bin/python

import MySQLdb

# Open database connection
db = MySQLdb.connect("localhost","root","root@123", "TUTORIALS")

# prepare a cursor object using cursor() method
cursor = db.cursor()

sql = "Select * from tutorials_tbl"

# execute SQL query using execute() method.
cursor.execute(sql)

# fetch all records from cursor
result = cursor.fetchall()

#Update the table and get the updated row count
#!/usr/bin/python

import MySQLdb

# Open database connection
db = MySQLdb.connect("localhost","root","root@123", "TUTORIALS")

# prepare a cursor object using cursor() method
cursor = db.cursor()

sql = "UPDATE tutorials_tbl set tutorial_title = "Learning Java" where tutorial_id = 2"

# execute SQL query using execute() method.
cursor.execute(sql)

db.commit()

# get the record count updated
print(cursor.rowcount, " record(s) affected")

# disconnect from server
db.close()

#Delete from table and get the row count
#!/usr/bin/python

import MySQLdb

# Open database connection
db = MySQLdb.connect("localhost","root","root@123", "TUTORIALS")

# prepare a cursor object using cursor() method
cursor = db.cursor()

sql = "Delete from tutorials_tbl where tutorial_id = 2"

# execute SQL query using execute() method.
cursor.execute(sql)

db.commit()

# get the record count updated
print(cursor.rowcount, " record(s) affected")

# disconnect from server
db.close()

#Fetch all and iterate over the results
#!/usr/bin/python

import MySQLdb

# Open database connection
db = MySQLdb.connect("localhost","root","root@123", "TUTORIALS")

# prepare a cursor object using cursor() method
cursor = db.cursor()

sql = "Select * from tutorials_tbl Where tutorial_id = 3"

# execute SQL query using execute() method.
cursor.execute(sql)

# fetch all records from cursor
result = cursor.fetchall()

# iterate result and print records
for record in result:
   print(record)

# disconnect from server
db.close()

#where clause
#!/usr/bin/python

import MySQLdb

# Open database connection
db = MySQLdb.connect("localhost","root","root@123", "TUTORIALS")

# prepare a cursor object using cursor() method
cursor = db.cursor()

sql = "Select * from tutorials_tbl Where tutorial_id = 3"

# execute SQL query using execute() method.
cursor.execute(sql)

# fetch all records from cursor
result = cursor.fetchall()

# iterate result and print records
for record in result:
   print(record)

# disconnect from server
db.close()
#output
#(3, 'JQuery', 'Julie', datetime.date(2020, 5, 10))

#like clause
#!/usr/bin/python

import MySQLdb

# Open database connection
db = MySQLdb.connect("localhost","root","root@123", "TUTORIALS")

# prepare a cursor object using cursor() method
cursor = db.cursor()

sql = "Select * from tutorials_tbl Where tutorial_title like 'J%'"

# execute SQL query using execute() method.
cursor.execute(sql)

# fetch all records from cursor
result = cursor.fetchall()

# iterate result and print records
for record in result:
   print(record)

# disconnect from server
db.close()

#Sample output
#(6, 'Java', 'Julie', datetime.date(2020, 12, 10))
#(7, 'JQuery', 'Julie', datetime.date(2020, 5, 10))

#Sort data - order by clause
#!/usr/bin/python

import MySQLdb

# Open database connection
db = MySQLdb.connect("localhost","root","root@123", "TUTORIALS")

# prepare a cursor object using cursor() method
cursor = db.cursor()

sql = "Select * from tutorials_tbl order by tutorial_title asc"

# execute SQL query using execute() method.
cursor.execute(sql)

# fetch all records from cursor
result = cursor.fetchall()

# iterate result and print records
for record in result:
   print(record)

# disconnect from server
db.close()

#sample output
#(1, 'HTML 5', 'Robert', datetime.date(2010, 2, 10))
#(2, 'Java', 'Julie', datetime.date(2020, 12, 10))
#(3, 'JQuery', 'Julie', datetime.date(2020, 5, 10))

#Create a new table to use for join later
create table tcount_tbl(
   tutorial_author VARCHAR(40) NOT NULL,
   tutorial_count int
);

insert into tcount_tbl values('Julie', 2);
insert into tcount_tbl values('Robert', 1);

#Join two tables
#!/usr/bin/python

import MySQLdb

# Open database connection
db = MySQLdb.connect("localhost","root","root@123", "TUTORIALS")

# prepare a cursor object using cursor() method
cursor = db.cursor()

sql = """SELECT a.tutorial_id, a.tutorial_author, b.tutorial_count
				FROM tutorials_tbl a, tcount_tbl b
				WHERE a.tutorial_author = b.tutorial_author"""

# execute SQL query using execute() method.
cursor.execute(sql)

# fetch all records from cursor
result = cursor.fetchall()

# iterate result and print records
for record in result:
  print(record)

# disconnect from server
db.close()


# Sample output
# (1, 'Robert', 1)
# (2, 'Julie', 2)
# (3, 'Julie', 2)

# Transactions are a mechanism that ensures data consistency.
# Transactions have the following four properties −

# Atomicity − Either a transaction completes or nothing happens at all.
# Consistency − A transaction must start in a consistent state and leave the system in a consistent state.
# Isolation − Intermediate results of a transaction are not visible outside the current transaction.
# Durability − Once a transaction was committed, the effects are persistent, even after a system failure.
# The Python DB API 2.0 provides two methods to either commit or rollback a transaction.

# Prepare SQL query to DELETE required records
sql = "Delete from tutorials_tbl where tutorial_id = 2"
try:
	#Execute the SQL command
	cursor.execute(sql)
	#Commit your changes in the database
	db.commit()
except:
	db.rollback()
finally:
	db.close()

#The DB API defines a number of errors that must exist in each database module. The following table lists these exceptions.

Sr.No.	Exception & Description
1
Warning

Used for non-fatal issues. Must subclass StandardError.

2
Error

Base class for errors. Must subclass StandardError.

3
InterfaceError

Used for errors in the database module, not the database itself. Must subclass Error.

4
DatabaseError

Used for errors in the database. Must subclass Error.

5
DataError

Subclass of DatabaseError that refers to errors in the data.

6
OperationalError

Subclass of DatabaseError that refers to errors such as the loss of a connection to the database. These errors are generally outside of the control of the Python scripter.

7
IntegrityError

Subclass of DatabaseError for situations that would damage the relational integrity, such as uniqueness constraints or foreign keys.

8
InternalError

Subclass of DatabaseError that refers to errors internal to the database module, such as a cursor no longer being active.

9
ProgrammingError

Subclass of DatabaseError that refers to errors such as a bad table name and other things that can safely be blamed on you.

10
NotSupportedError

Subclass of DatabaseError that refers to trying to call unsupported functionality.


'''

'''
https://learnsql.com/cookbook/how-to-create-a-table-with-a-foreign-key-in-sql/#:~:text=To%20create%20a%20new%20table,the%20referenced%20column%20in%20parentheses.

create table table_name (column1 datatype, column2 datatype)
create table Employee(EmpId int PRIMARY KEY, EmpName varchar(255))

CREATE TABLE Student(id INT PRIMARY KEY, first_name VARCHAR(100) NOT NULL, last_name VARCHAR(100) NOT NULL, city_id INT, FOREIGN KEY (city_id) REFERENCES city(id));

OR

CREATE TABLE Student(id INT PRIMARY KEY, first_name varchar(100) NOT NULL, last_name VARCHAR(100) NOT NULL, 
score_id INT, subject_id INT, 
		CONSTRAINT fk_student_score_subject_id
		FOREGIEN KEY (subject_id, score_id) REFERENCES score_subject(subject_id, score_id));


CREATE TABLE student (
id INT PRIMARY KEY,
first_name VARCHAR(100) NOT NULL,
last_name VARCHAR(100) NOT NULL,
city_id INT,
      CONSTRAINT fk_student_city_id
      FOREIGN KEY (city_id) REFERENCES city(id)
);

existing table
ALTER TABLE student
ADD FOREIGN KEY (city_id) REFERENCES city(id);

ALTER TABLE student
      ADD CONSTRAINT fk_student_city_id
      FOREIGN KEY (city_id) REFERENCES city(id)
'''

