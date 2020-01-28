import psycopg2

con = psycopg2.connect(database="python_connect", user="postgres", password="rajneesh", host="127.0.0.1", port="5432")

print("Datbase connected/ opened successfully")

cur = con.cursor()

#execute will be doing the main work 
#cur.execute("INSERT INTO STUDENT (ADMISSION, NAME, AGE, COURSE, DEPARTMENT) VALUES (3420, 'JOHN', 21, 'COMPUTER SCIENCE', 'IT')")
cur.execute("INSERT INTO STUDENT (ADMISSION,NAME,AGE,COURSE,DEPARTMENT) VALUES (3419, 'Abel', 17, 'Computer Science', 'ICT')");
cur.execute("INSERT INTO STUDENT (ADMISSION,NAME,AGE,COURSE,DEPARTMENT) VALUES (3421, 'Joel', 17, 'Computer Science', 'ICT')");
cur.execute("INSERT INTO STUDENT (ADMISSION,NAME,AGE,COURSE,DEPARTMENT) VALUES (3422, 'Antony', 19, 'Electrical Engineering', 'Engineering')");
cur.execute("INSERT INTO STUDENT (ADMISSION,NAME,AGE,COURSE,DEPARTMENT) VALUES (3423, 'Alice', 18, 'Information Technology', 'ICT')");

con.commit()
print("Record inserted successfully")
con.close()
