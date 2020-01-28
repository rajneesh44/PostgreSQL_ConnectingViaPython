"""RETRIEVING DATA"""
import psycopg2

con = psycopg2.connect(database="python_connect", user="postgres", password="rajneesh", host="127.0.0.1", port="5432")
print("Database opened successfully")

cur = con.cursor()
cur.execute("SELECT admission, name, age, course, department from STUDENT")

#fetching data
rows = cur.fetchall()

for row in rows:
	print("ADMISSION =", row[0])
	print("NAME=", row[1])
	print("AGE =", row[2])
	print("COURSE =", row[3])
	print("DEPARTMENT =", row[4], "\n")

print("Operation done successfully")
con.close()