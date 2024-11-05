Python 3.9.10 (tags/v3.9.10:f2f3f53, Jan 17 2022, 15:14:21) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import sqlite3
>>> import os
>>> os.chdir(os.path.expanduser("~") + "\\Documents")
>>> conn = sqlite3.connect("17.06.2024.db")
>>> conn.execute("CREATE TABLE IF NOT EXISTS NOTES")
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    conn.execute("CREATE TABLE IF NOT EXISTS NOTES")
sqlite3.OperationalError: incomplete input
>>> conn.execute(
	"CREATE TABLE IF NOT EXISTS NOTES" +
	"(ID INT PRIMARY KEY NOT NULL," +
	"DATE TEXT NOT NULL," +
	"TIME TEXT NOT NULL," +
	"ID_SOV TEXT NOT NULL," +
	"FROM TEXT NOT NULL," +
	"TO TEXT NOT NULL" +
	"MESSAGE TEXT NOT NULL" +
	"NOTE1 CHAR(100)" +
	"NOTE2 CHAR(100));")
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    conn.execute(
sqlite3.OperationalError: near "FROM": syntax error
>>> conn.execute(
	"CREATE TABLE IF NOT EXISTS NOTES" +
	"(id INT PRIMARY KEY NOT NULL," +
	"date TEXT NOT NULL," +
	"time TEXT NOT NULL," +
	"id_sov TEXT NOT NULL," +
	"from TEXT NOT NULL," +
	"to TEXT NOT NULL" +
	"message TEXT NOT NULL" +
	"note1 CHAR(100)" +
	"note2 CHAR(100));")
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    conn.execute(
sqlite3.OperationalError: near "from": syntax error
>>> conn.execute(
	"CREATE TABLE IF NOT EXISTS NOTES" +
	"(id INT PRIMARY KEY NOT NULL," +
	"date TEXT NOT NULL," +
	"time TEXT NOT NULL," +
	"id_sov TEXT NOT NULL," +
	"from TEXT NOT NULL," +
	"to TEXT NOT NULL," +
	"message TEXT NOT NULL," +
	"note1 CHAR(100)," +
	"note2 CHAR(100));")
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    conn.execute(
sqlite3.OperationalError: near "from": syntax error
>>> >>> conn.execute(
	"CREATE TABLE IF NOT EXISTS NOTES" +
	"(id INT PRIMARY KEY NOT NULL," +
	"date TEXT NOT NULL," +
	"time TEXT NOT NULL," +
	"id_sov TEXT NOT NULL," +
	"from TEXT NOT NULL," +
	"to TEXT NOT NULL," +
	"message TEXT NOT NULL," +
	"note1 CHAR(100)," +
	"note2 CHAR(100));")
SyntaxError: invalid syntax
>>> conn.execute(
	"CREATE TABLE IF NOT EXISTS NOTES" +
	"(id INT PRIMARY KEY NOT NULL," +
	"date TEXT NOT NULL," +
	"time TEXT NOT NULL," +
	"id_sov TEXT NOT NULL," +
	"from TEXT NOT NULL," +
	"to TEXT NOT NULL," +
	"message TEXT NOT NULL," +
	"note1 CHAR(100)," +
	"note2 CHAR(100));")
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    conn.execute(
sqlite3.OperationalError: near "from": syntax error
>>> conn.execute(
	"CREATE TABLE IF NOT EXISTS NOTES" +
	"(id INT PRIMARY KEY NOT NULL," +
	"date TEXT NOT NULL," +
	"time TEXT NOT NULL," +
	"id_sov TEXT NOT NULL," +
	#"from TEXT NOT NULL," +
	"to TEXT NOT NULL," +
	"message TEXT NOT NULL," +
	"note1 CHAR(100)," +
	"note2 CHAR(100));")
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    conn.execute(
sqlite3.OperationalError: near "to": syntax error
>>> conn.execute(
	"CREATE TABLE IF NOT EXISTS NOTES" +
	"(id INT PRIMARY KEY NOT NULL," +
	"date TEXT NOT NULL," +
	"time TEXT NOT NULL," +
	"id_sov TEXT NOT NULL," +
	#"from TEXT NOT NULL," +
	#"to TEXT NOT NULL," +
	"message TEXT NOT NULL," +
	"note1 CHAR(100)," +
	"note2 CHAR(100));")
<sqlite3.Cursor object at 0x0000025222E2A570>
>>> >>> conn.execute(
	"CREATE TABLE IF NOT EXISTS NOTES" +
	"(id INT PRIMARY KEY NOT NULL," +
	"date TEXT NOT NULL," +
	"time TEXT NOT NULL," +
	"id_sov TEXT NOT NULL," +
	"from_ TEXT NOT NULL," +
	"to_ TEXT NOT NULL," +
	"message TEXT NOT NULL," +
	"note1 CHAR(100)," +
	"note2 CHAR(100));")
SyntaxError: invalid syntax
>>> conn.execute(
	"CREATE TABLE IF NOT EXISTS NOTES" +
	"(id INT PRIMARY KEY NOT NULL," +
	"date TEXT NOT NULL," +
	"time TEXT NOT NULL," +
	"id_sov TEXT NOT NULL," +
	"from_ TEXT NOT NULL," +
	"to_ TEXT NOT NULL," +
	"message TEXT NOT NULL," +
	"note1 CHAR(100)," +
	"note2 CHAR(100));")
<sqlite3.Cursor object at 0x0000025222E6C8F0>
>>> os.remove("17.06.2024.db")
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    os.remove("17.06.2024.db")
PermissionError: [WinError 32] Процесс не может получить доступ к файлу, так как этот файл занят другим процессом: '17.06.2024.db'
>>> conn.close()
>>> os.remove("17.06.2024.db")
>>> conn.execute(
	"CREATE TABLE IF NOT EXISTS NOTES" +
	"(id INT PRIMARY KEY NOT NULL," +
	"date TEXT NOT NULL," +
	"time TEXT NOT NULL," +
	"id_sov TEXT NOT NULL," +
	"from_ TEXT NOT NULL," +
	"to_ TEXT NOT NULL," +
	"message TEXT NOT NULL," +
	"note1 CHAR(100)," +
	"note2 CHAR(100));")
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    conn.execute(
sqlite3.ProgrammingError: Cannot operate on a closed database.
>>> conn = sqlite3.connect("17.06.2024.db")
>>> conn.execute(
	"CREATE TABLE IF NOT EXISTS NOTES" +
	"(id INT PRIMARY KEY NOT NULL," +
	"date TEXT NOT NULL," +
	"time TEXT NOT NULL," +
	"id_sov TEXT NOT NULL," +
	"from_ TEXT NOT NULL," +
	"to_ TEXT NOT NULL," +
	"message TEXT NOT NULL," +
	"note1 CHAR(100)," +
	"note2 CHAR(100));")
<sqlite3.Cursor object at 0x0000025222E2A570>
>>> conn.close()
>>> 
= RESTART: C:\Users\Titovskiysa\Desktop\Документы участок\Python\Python (раб стола)\Python\SQLiteSimpleEditor\SQLite_Editor_v.0.0.2.py
DELETING FILE C:\Users\Titovskiysa\Documents\SQLite_RedactorFiles\Logs/2024-03-15.cfg
Wrote to Log:	 06:33:08  !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

Wrote to Log:	 06:33:08  Application started

Wrote to Log:	 06:33:08  FindMyDir finished succesfully

Wrote to Log:	 06:33:08  Start of ClearLogs

Wrote to Log:	 06:33:08  ClearLogs finished succesfully

Wrote to Log:	 06:33:08  LogThread started!!!

Wrote to Log:	 06:33:10  Load command

Wrote to Log:	 06:33:16  CopyFile C:\Users\Titovskiysa\Documents\17.06.2024.db to C:\Users\Titovskiysa\Documents\SQLite_RedactorFiles\temp\temp.sql function started

Wrote to Log:	 06:33:16  CopyFile C:\Users\Titovskiysa\Documents\17.06.2024.db to C:\Users\Titovskiysa\Documents\SQLite_RedactorFiles\temp\temp.sql function finished

Wrote to Log:	 06:33:16  DoLoad function successed

Wrote to Log:	 06:33:16  Found several tables in file C:\Users\Titovskiysa\Documents\SQLite_RedactorFiles\temp\temp.sql, tables = ['NOTES']

Wrote to Log:	 06:33:19  AskTable Choosed NOTES

Wrote to Log:	 06:33:19  ReadTableData successed, opening GridFrame

Wrote to Log:	 06:33:21  Grid frame for NOTES in C:\Users\Titovskiysa\Documents\17.06.2024.db opened succesfully

Wrote to Log:	 06:36:34  Start of SaveTemp

Wrote to Log:	 06:36:34  CopyFile C:\Users\Titovskiysa\Documents\SQLite_RedactorFiles\temp\temp.sql to C:\Users\Titovskiysa\Documents\17.06.2024.db function started

Wrote to Log:	 06:36:34  CopyFile C:\Users\Titovskiysa\Documents\SQLite_RedactorFiles\temp\temp.sql to C:\Users\Titovskiysa\Documents\17.06.2024.db function finished

Wrote to Log:	 06:36:34  SaveTemp finished succesfully

Closed
>>> conn = sqlite3.connect("17.06.2024.db")
>>> conn.execute("INSERT INTO NOTES VALUES")
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    conn.execute("INSERT INTO NOTES VALUES")
sqlite3.OperationalError: incomplete input
>>> conn.execute(
	"INSER INTO NOTES VALUES " +
	"(NULL, '17.06.2024', '6-39', '111111', 'ME', 'NOONE', 'MESSAGE 1')" +
	"(NULL, '17.06.2024', '6-40', '111112', 'ME', 'NOONE', 'MESSAGE 2')" +
	"(NULL, '17.06.2024', '6-41', '111113', 'ME', 'NOONE', 'MESSAGE 3', 'SOMENOTE')")
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    conn.execute(
sqlite3.OperationalError: near "INSER": syntax error
>>> conn.execute(
	"INSERT INTO NOTES VALUES " +
	"(NULL, '17.06.2024', '6-39', '111111', 'ME', 'NOONE', 'MESSAGE 1')" +
	"(NULL, '17.06.2024', '6-40', '111112', 'ME', 'NOONE', 'MESSAGE 2')" +
	"(NULL, '17.06.2024', '6-41', '111113', 'ME', 'NOONE', 'MESSAGE 3', 'SOMENOTE')")
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    conn.execute(
sqlite3.OperationalError: near "(": syntax error
>>> conn.execute(
	"INSERT INTO NOTES VALUES " +
	"(NULL, '17.06.2024', '6-39', '111111', 'ME', 'NOONE', 'MESSAGE 1')," +
	"(NULL, '17.06.2024', '6-40', '111112', 'ME', 'NOONE', 'MESSAGE 2')," +
	"(NULL, '17.06.2024', '6-41', '111113', 'ME', 'NOONE', 'MESSAGE 3', 'SOMENOTE')")
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    conn.execute(
sqlite3.OperationalError: no such table: NOTES
>>> 
=================================================== RESTART: C:\Users\Titovskiysa\Desktop\Документы участок\Python\Python (раб стола)\Python\SQLiteSimpleEditor\SQLite_Editor_v.0.0.2.py ===================================================
DELETING FILE C:\Users\Titovskiysa\Documents\SQLite_RedactorFiles\Logs/2024-03-18.cfg
Wrote to Log:	 06:43:49  !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

Wrote to Log:	 06:43:49  Application started

Wrote to Log:	 06:43:49  FindMyDir finished succesfully

Wrote to Log:	 06:43:49  Start of ClearLogs

Wrote to Log:	 06:43:49  ClearLogs finished succesfully

Wrote to Log:	 06:43:49  LogThread started!!!

Wrote to Log:	 06:43:54  Load command

Wrote to Log:	 06:44:01  CopyFile C:\Users\Titovskiysa\Documents\17.06.2024.db to C:\Users\Titovskiysa\Documents\SQLite_RedactorFiles\temp\temp.sql function started

Wrote to Log:	 06:44:01  CopyFile C:\Users\Titovskiysa\Documents\17.06.2024.db to C:\Users\Titovskiysa\Documents\SQLite_RedactorFiles\temp\temp.sql function finished

Wrote to Log:	 06:44:01  DoLoad function successed

Wrote to Log:	 06:44:01  Found several tables in file C:\Users\Titovskiysa\Documents\SQLite_RedactorFiles\temp\temp.sql, tables = ['NOTES']

Wrote to Log:	 06:44:04  AskTable Choosed NOTES

Wrote to Log:	 06:44:04  ReadTableData successed, opening GridFrame

Wrote to Log:	 06:44:06  Grid frame for NOTES in C:\Users\Titovskiysa\Documents\17.06.2024.db opened succesfully

Wrote to Log:	 06:44:07  Start of SaveTemp

Wrote to Log:	 06:44:07  CopyFile C:\Users\Titovskiysa\Documents\SQLite_RedactorFiles\temp\temp.sql to C:\Users\Titovskiysa\Documents\17.06.2024.db function started

Wrote to Log:	 06:44:07  CopyFile C:\Users\Titovskiysa\Documents\SQLite_RedactorFiles\temp\temp.sql to C:\Users\Titovskiysa\Documents\17.06.2024.db function finished

Wrote to Log:	 06:44:07  SaveTemp finished succesfully

Closed
>>> os.chdir(os.path.expanduser("~") + "\\Documents")
>>> conn = sqlite3.connect("17.06.2024.db")
>>> conn.execute(
	"INSERT INTO NOTES VALUES " +
	"(NULL, '17.06.2024', '6-39', '111111', 'ME', 'NOONE', 'MESSAGE 1')," +
	"(NULL, '17.06.2024', '6-40', '111112', 'ME', 'NOONE', 'MESSAGE 2')," +
	"(NULL, '17.06.2024', '6-41', '111113', 'ME', 'NOONE', 'MESSAGE 3', 'SOMENOTE')")
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    conn.execute(
sqlite3.OperationalError: all VALUES must have the same number of terms
>>> conn.execute(
	"CREATE TABLE IF NOT EXISTS NOTES2" +
	"(id INT PRIMARY KEY NOT NULL AUTOINCREMENT UNIQUE," +
	"note2 CHAR(100));")
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    conn.execute(
sqlite3.OperationalError: near "AUTOINCREMENT": syntax error
>>> conn.execute(
	"CREATE TABLE IF NOT EXISTS NOTES2" +
	"(id INT PRIMARY KEY NOT NULL AUTOINCREMENT," +
	"note2 CHAR(100));")
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    conn.execute(
sqlite3.OperationalError: near "AUTOINCREMENT": syntax error
>>> conn.execute(
	"CREATE TABLE IF NOT EXISTS NOTES2" +
	"(id INT PRIMARY KEY AUTOINCREMENT," +
	"note2 CHAR(100));")
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    conn.execute(
sqlite3.OperationalError: AUTOINCREMENT is only allowed on an INTEGER PRIMARY KEY
>>> conn.execute(
	"CREATE TABLE IF NOT EXISTS NOTES2" +
	"(id INTEGER PRIMARY KEY AUTOINCREMENT," +
	"note2 CHAR(100));")
<sqlite3.Cursor object at 0x0000024510EFA500>
>>> conn.execute(
	"INSERT INTO NOTES2 VALUES " +
	"(NULL, '17.06.2024'), (NULL, '18.06.2024'), (NULL, '19.06.2024')")
<sqlite3.Cursor object at 0x0000024511673DC0>
>>> conn.execute(
	"INSERT INTO NOTES2 VALUES " +
	"'20.06.2024')")
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    conn.execute(
sqlite3.OperationalError: near "'20.06.2024'": syntax error
>>> conn.execute(
	"INSERT INTO NOTES2 VALUES " +
	"('20.06.2024')")
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    conn.execute(
sqlite3.OperationalError: table NOTES2 has 2 columns but 1 values were supplied
>>> conn.execute("SELECT * from NOTES2")
<sqlite3.Cursor object at 0x0000024510EFA500>
>>> cursor = conn.execute("SELECT * from NOTES2")
>>> for row in cursor:
	print(str(row))

	
(1, '17.06.2024')
(2, '18.06.2024')
(3, '19.06.2024')
>>> conn.execute("drop table NOTES")
Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    conn.execute("drop table NOTES")
sqlite3.OperationalError: database table is locked
>>> conn.commit()
>>> conn.close()
>>> conn = conn = sqlite3.connect("17.06.2024.db")
>>> conn.execute("drop table NOTES")
<sqlite3.Cursor object at 0x0000024511673E30>
>>> .execute("drop table NOTES2")
SyntaxError: invalid syntax
>>> conn.execute("drop table NOTES2")
<sqlite3.Cursor object at 0x0000024510EFA500>
>>> conn.execute("drop table NOTES")
Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    conn.execute("drop table NOTES")
sqlite3.OperationalError: no such table: NOTES
>>> conn.execute(
	"CREATE TABLE IF NOT EXISTS NOTES" +
	"(id INTEGER PRIMARY KEY AUTOINCREMENT," +
	"date TEXT NOT NULL," +
	"time TEXT NOT NULL," +
	"id_sov TEXT NOT NULL," +
	"from_ TEXT NOT NULL," +
	"to_ TEXT NOT NULL," +
	"message TEXT NOT NULL," +
	"note1 CHAR(100)," +
	"note2 CHAR(100));")
<sqlite3.Cursor object at 0x0000024511673CE0>
>>> conn.execute(
	"INSERT INTO NOTES VALUES " +
	"(NULL, '17.06.2024', '6-39', '111111', 'ME', 'NOONE', 'MESSAGE 1')," +
	"(NULL, '17.06.2024', '6-40', '111112', 'ME', 'NOONE', 'MESSAGE 2')," +
	"(NULL, '17.06.2024', '6-41', '111113', 'ME', 'NOONE', 'MESSAGE 3', 'SOMENOTE')")
Traceback (most recent call last):
  File "<pyshell#66>", line 1, in <module>
    conn.execute(
sqlite3.OperationalError: all VALUES must have the same number of terms
>>> conn.execute(
	"INSERT INTO NOTES VALUES " +
	"(NULL, '17.06.2024', '6-39', '111111', 'ME', 'NOONE', 'MESSAGE 1', NULL, NULL)," +
	"(NULL, '17.06.2024', '6-40', '111112', 'ME', 'NOONE', 'MESSAGE 2', NULL, NULL)" +
	"(NULL, '17.06.2024', '6-41', '111113', 'ME', 'NOONE', 'MESSAGE 3', 'SOMENOTE', NULL)")
Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    conn.execute(
sqlite3.OperationalError: near "(": syntax error
>>> conn.execute(
	"INSERT INTO NOTES VALUES " +
	"(NULL, '17.06.2024', '6-39', '111111', 'ME', 'NOONE', 'MESSAGE 1', NULL, NULL), " +
	"(NULL, '17.06.2024', '6-40', '111112', 'ME', 'NOONE', 'MESSAGE 2', NULL, NULL), " +
	"(NULL, '17.06.2024', '6-41', '111113', 'ME', 'NOONE', 'MESSAGE 3', 'SOMENOTE', NULL)")
<sqlite3.Cursor object at 0x0000024510EFA500>
>>> cursor = conn.execute("SELECT * from NOTES")
>>> for row in cursor:
	print(str(row))

	
(1, '17.06.2024', '6-39', '111111', 'ME', 'NOONE', 'MESSAGE 1', None, None)
(2, '17.06.2024', '6-40', '111112', 'ME', 'NOONE', 'MESSAGE 2', None, None)
(3, '17.06.2024', '6-41', '111113', 'ME', 'NOONE', 'MESSAGE 3', 'SOMENOTE', None)
>>> conn.execute("DELETE FROM NOTES WHERE id_sov=(?)", ("111112",))
<sqlite3.Cursor object at 0x0000024511673EA0>
>>> cursor = conn.execute("SELECT * from NOTES")
>>> for row in cursor:
	print(str(row))

	
(1, '17.06.2024', '6-39', '111111', 'ME', 'NOONE', 'MESSAGE 1', None, None)
(3, '17.06.2024', '6-41', '111113', 'ME', 'NOONE', 'MESSAGE 3', 'SOMENOTE', None)
>>> conn.execute("drop table NOTES")
<sqlite3.Cursor object at 0x0000024511673D50>
>>> conn.execute(
	"CREATE TABLE IF NOT EXISTS NOTES" +
	"(id INTEGER PRIMARY KEY AUTOINCREMENT," +
	"date TEXT NOT NULL," +
	"time TEXT NOT NULL," +
	"id_sov TEXT NOT NULL," +
	"from_ TEXT NOT NULL," +
	"to_ TEXT NOT NULL," +
	"message TEXT NOT NULL," +
	"show_status BOOLEAN NOT NULL CHECK(show_status IN (0, 1))"
	"note1 CHAR(100)," +
	"note2 CHAR(100));")
Traceback (most recent call last):
  File "<pyshell#79>", line 1, in <module>
    conn.execute(
sqlite3.OperationalError: near "note1": syntax error
>>> conn.execute(
	"CREATE TABLE IF NOT EXISTS NOTES" +
	"(id INTEGER PRIMARY KEY AUTOINCREMENT," +
	"date TEXT NOT NULL," +
	"time TEXT NOT NULL," +
	"id_sov TEXT NOT NULL," +
	"from_ TEXT NOT NULL," +
	"to_ TEXT NOT NULL," +
	"message TEXT NOT NULL," +
	"show_status BOOLEAN NOT NULL CHECK(show_status IN (0, 1)),"
	"note1 CHAR(100)," +
	"note2 CHAR(100));")
<sqlite3.Cursor object at 0x0000024511673F10>
>>> conn.execute(
	"INSERT INTO NOTES VALUES " +
	"(NULL, '17.06.2024', '6-39', '111111', 'ME', 'NOONE', 'MESSAGE 1', 1, NULL, NULL)," +
	"(NULL, '17.06.2024', '6-40', '111112', 'ME', 'NOONE', 'MESSAGE 2', 1, NULL, NULL)" +
	"(NULL, '17.06.2024', '6-39', '111111', 'ME', 'NOONE', 'MESSAGE 1', 0, NULL, NULL)," +
	"(NULL, '17.06.2024', '6-40', '111112', 'ME', 'NOONE', 'MESSAGE 2', 0, NULL, NULL)" +
	"(NULL, '17.06.2024', '6-39', '111111', 'ME', 'NOONE', 'MESSAGE 1', 0, NULL, NULL)," +
	"(NULL, '17.06.2024', '6-40', '111112', 'ME', 'NOONE', 'MESSAGE 2', 1, NULL, NULL)" +
	"(NULL, '17.06.2024', '6-41', '111113', 'ME', 'NOONE', 'MESSAGE 3', 1, 'SOMENOTE', NULL)")
Traceback (most recent call last):
  File "<pyshell#81>", line 1, in <module>
    conn.execute(
sqlite3.OperationalError: near "(": syntax error
>>> conn.execute(
	"INSERT INTO NOTES VALUES " +
	"(NULL, '17.06.2024', '6-39', '111111', 'ME', 'NOONE', 'MESSAGE 1', 1, NULL, NULL)," +
	"(NULL, '17.06.2024', '6-40', '111112', 'ME', 'NOONE', 'MESSAGE 2', 1, NULL, NULL)," +
	"(NULL, '17.06.2024', '6-39', '111111', 'ME', 'NOONE', 'MESSAGE 1', 0, NULL, NULL)," +
	"(NULL, '17.06.2024', '6-40', '111112', 'ME', 'NOONE', 'MESSAGE 2', 0, NULL, NULL)," +
	"(NULL, '17.06.2024', '6-39', '111111', 'ME', 'NOONE', 'MESSAGE 1', 0, NULL, NULL)," +
	"(NULL, '17.06.2024', '6-40', '111112', 'ME', 'NOONE', 'MESSAGE 2', 1, NULL, NULL)," +
	"(NULL, '17.06.2024', '6-41', '111113', 'ME', 'NOONE', 'MESSAGE 3', 1, 'SOMENOTE', NULL)")
<sqlite3.Cursor object at 0x0000024511673EA0>
>>> cursor = conn.execute("SELECT * from NOTES")
>>> for row in cursor:
	print(row)

	
(1, '17.06.2024', '6-39', '111111', 'ME', 'NOONE', 'MESSAGE 1', 1, None, None)
(2, '17.06.2024', '6-40', '111112', 'ME', 'NOONE', 'MESSAGE 2', 1, None, None)
(3, '17.06.2024', '6-39', '111111', 'ME', 'NOONE', 'MESSAGE 1', 0, None, None)
(4, '17.06.2024', '6-40', '111112', 'ME', 'NOONE', 'MESSAGE 2', 0, None, None)
(5, '17.06.2024', '6-39', '111111', 'ME', 'NOONE', 'MESSAGE 1', 0, None, None)
(6, '17.06.2024', '6-40', '111112', 'ME', 'NOONE', 'MESSAGE 2', 1, None, None)
(7, '17.06.2024', '6-41', '111113', 'ME', 'NOONE', 'MESSAGE 3', 1, 'SOMENOTE', None)
>>> cursor = conn.execute("SELECT WHERE show_status=1 from NOTES")
Traceback (most recent call last):
  File "<pyshell#87>", line 1, in <module>
    cursor = conn.execute("SELECT WHERE show_status=1 from NOTES")
sqlite3.OperationalError: near "WHERE": syntax error
>>> conn.execute("SELECT FROM NOTES WHERE show_status=(?)", (1,))
Traceback (most recent call last):
  File "<pyshell#88>", line 1, in <module>
    conn.execute("SELECT FROM NOTES WHERE show_status=(?)", (1,))
sqlite3.OperationalError: near "FROM": syntax error
>>> conn.execute("SELECT * FROM NOTES WHERE show_status=(?)", (1,))
<sqlite3.Cursor object at 0x0000024510EFA500>
>>> cursor = conn.execute("SELECT * FROM NOTES WHERE show_status=(?)", (1,))
>>> for row in cursow:
	print(str(cursor))

	
Traceback (most recent call last):
  File "<pyshell#93>", line 1, in <module>
    for row in cursow:
NameError: name 'cursow' is not defined
>>> for row in cursor:
	print(str(cursor))

	
<sqlite3.Cursor object at 0x0000024511673F10>
<sqlite3.Cursor object at 0x0000024511673F10>
<sqlite3.Cursor object at 0x0000024511673F10>
<sqlite3.Cursor object at 0x0000024511673F10>
>>> for row in cursor:
	print(str(row))

	
>>> cursor = conn.execute("SELECT * FROM NOTES WHERE show_status=(?)", (1,))
>>> for row in cursor:
	print(str(row))

	
(1, '17.06.2024', '6-39', '111111', 'ME', 'NOONE', 'MESSAGE 1', 1, None, None)
(2, '17.06.2024', '6-40', '111112', 'ME', 'NOONE', 'MESSAGE 2', 1, None, None)
(6, '17.06.2024', '6-40', '111112', 'ME', 'NOONE', 'MESSAGE 2', 1, None, None)
(7, '17.06.2024', '6-41', '111113', 'ME', 'NOONE', 'MESSAGE 3', 1, 'SOMENOTE', None)
>>> 