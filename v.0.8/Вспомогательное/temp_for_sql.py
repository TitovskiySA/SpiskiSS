import sqlite3
import socket

with sqlite3.connect('DataBase_18.03.2024.db') as sql:
    cursor = sql.execute("SELECT name FROM sqlite_master WHERE type = 'table';")
    tables = [table[0] for table in cursor.fetchall()]
    print("NAME = " + str(tables))

    cursor = sql.execute("SELECT * from Paths")
    paths = []
    for row in cursor:
        print(str(row))
        paths.append(row)

    for path in paths:
        print(str(path))

    add = []
    cursor = sql.execute("SELECT RCS from SpiskiSS_Users WHERE HostName = " + "'" + str(socket.gethostname()) + "'")
    for row in cursor:
        print(str(row[0]))
        add.append(row[0])

    print(len(add))

    cursor = sql.execute("SELECT HostName, RCS from SpiskiSS_Users")
    for row in cursor:
        print(str(row[0]))
        add.append(row[0])

    print(len(add))
