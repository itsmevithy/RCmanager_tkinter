import mysql.connector as pysql
from bullet import Password

hostname=input("Enter SQL hostname: ")
username=input('Enter user: ')
wrd=Password(prompt='Password: ',hidden='*')
pwd=wrd.launch()

f=open('sqltext.txt','w')
f.write(hostname)
f.write('\n')
f.write(username)
f.write('\n')
f.write(pwd)
f.close()

conn=pysql.connect(host=hostname, user=username, password=pwd,charset='utf8')
if conn.is_connected():
    print('Connection Success')
    cursor=conn.cursor()
    cursor.execute('drop database test')
    print('Existing database deleted')
    cursor.execute('create database test')
    print('Created new database')
    cursor.execute('use test')
    cursor.execute('create table selected(aplno int, Name varchar(25))')
    print('New table created')
    sql='insert into selected values (%s, %s)'
    val=[(12431,'Kruba'),(12432,'Sundhar'),(12433,'Tamil'),(12434,'Avinash'),(12435,'Vidhya')]
    cursor.executemany(sql,val)
    conn.commit()
    print(cursor.rowcount, "record was inserted.")
    cursor.execute('create table waiting(aplno int, Name varchar(25))')
    print('New table created')
    sql='insert into waiting values (%s, %s)'
    val=[(12426,'Shivani'),(12427,'Dhikshita'),(12428,'Shreeman'),(12429,'Pritam'),(12430,'Kaushik')]
    cursor.executemany(sql,val)
    conn.commit()
    print(cursor.rowcount, "record was inserted.")
    cursor.execute('create table rejected(aplno int, Name varchar(25))')
    print('New table created')
    sql='insert into rejected values (%s, %s)'
    val=[(12421,'Mahi'),(12422,'Aaryan'),(12423,'Vaishnavi'),(12424,'Prakshana'),(12425,'Shubha')]
    cursor.executemany(sql,val)
    conn.commit()
    print(cursor.rowcount, "record was inserted.")
    print('All done')
    conn.close()
    print('Connection terminated')
elif not conn.is_connected():
    print("Error connecting to server")
