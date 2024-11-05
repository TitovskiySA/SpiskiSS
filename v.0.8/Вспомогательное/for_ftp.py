Python 3.9.10 (tags/v3.9.10:f2f3f53, Jan 17 2022, 15:14:21) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import ftplib
>>> ip = "10.240.65.130"
>>> ftp = ftplib.FTP(ip)
>>> login = ""
>>> passw = ""
>>> ftp.login(login, passw)
'230 Guest login ok, access restrictions apply.'
>>> ftp.cwd("/Incoming")
'250 CWD command successful.'
>>> filename = "11.04.23.doc"
>>> newfile = "newfile.doc"
>>> MyPath = "C:\\Python\\Списки присутствующих\\" + newfile
>>> ftp.retrbinary("RETR " + filename, open(MyPath, "wb").write)
'226 Transfer complete.'
>>> filenames = ftp.nlst()
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    filenames = ftp.nlst()
  File "C:\Users\Titovskiysa\AppData\Local\Programs\Python\Python39\lib\ftplib.py", line 553, in nlst
    self.retrlines(cmd, files.append)
  File "C:\Users\Titovskiysa\AppData\Local\Programs\Python\Python39\lib\ftplib.py", line 465, in retrlines
    line = fp.readline(self.maxline + 1)
  File "C:\Users\Titovskiysa\AppData\Local\Programs\Python\Python39\lib\codecs.py", line 322, in decode
    (result, consumed) = self._buffer_decode(data, self.errors, final)
UnicodeDecodeError: 'utf-8' codec can't decode byte 0xd1 in position 9: invalid continuation byte
>>> with open(MyPath, "wb") as file:
	ftp.retrbinary("RETR " + filename, file.write)
	file.close()

	
Traceback (most recent call last):
  File "<pyshell#15>", line 2, in <module>
    ftp.retrbinary("RETR " + filename, file.write)
  File "C:\Users\Titovskiysa\AppData\Local\Programs\Python\Python39\lib\ftplib.py", line 436, in retrbinary
    with self.transfercmd(cmd, rest) as conn:
  File "C:\Users\Titovskiysa\AppData\Local\Programs\Python\Python39\lib\ftplib.py", line 393, in transfercmd
    return self.ntransfercmd(cmd, rest)[0]
  File "C:\Users\Titovskiysa\AppData\Local\Programs\Python\Python39\lib\ftplib.py", line 353, in ntransfercmd
    host, port = self.makepasv()
  File "C:\Users\Titovskiysa\AppData\Local\Programs\Python\Python39\lib\ftplib.py", line 327, in makepasv
    untrusted_host, port = parse227(self.sendcmd('PASV'))
  File "C:\Users\Titovskiysa\AppData\Local\Programs\Python\Python39\lib\ftplib.py", line 839, in parse227
    raise error_reply(resp)
ftplib.error_reply: 200 Type set to I.
>>> ftp.retrbinary("RETR " + filename, open(MyPath, "wb").write)
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    ftp.retrbinary("RETR " + filename, open(MyPath, "wb").write)
  File "C:\Users\Titovskiysa\AppData\Local\Programs\Python\Python39\lib\ftplib.py", line 436, in retrbinary
    with self.transfercmd(cmd, rest) as conn:
  File "C:\Users\Titovskiysa\AppData\Local\Programs\Python\Python39\lib\ftplib.py", line 393, in transfercmd
    return self.ntransfercmd(cmd, rest)[0]
  File "C:\Users\Titovskiysa\AppData\Local\Programs\Python\Python39\lib\ftplib.py", line 353, in ntransfercmd
    host, port = self.makepasv()
  File "C:\Users\Titovskiysa\AppData\Local\Programs\Python\Python39\lib\ftplib.py", line 327, in makepasv
    untrusted_host, port = parse227(self.sendcmd('PASV'))
  File "C:\Users\Titovskiysa\AppData\Local\Programs\Python\Python39\lib\ftplib.py", line 839, in parse227
    raise error_reply(resp)
ftplib.error_reply: 200 Type set to I.
>>> file.close()
>>> ftp.retrbinary("RETR " + filename, open(MyPath, "wb").write)
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    ftp.retrbinary("RETR " + filename, open(MyPath, "wb").write)
  File "C:\Users\Titovskiysa\AppData\Local\Programs\Python\Python39\lib\ftplib.py", line 436, in retrbinary
    with self.transfercmd(cmd, rest) as conn:
  File "C:\Users\Titovskiysa\AppData\Local\Programs\Python\Python39\lib\ftplib.py", line 393, in transfercmd
    return self.ntransfercmd(cmd, rest)[0]
  File "C:\Users\Titovskiysa\AppData\Local\Programs\Python\Python39\lib\ftplib.py", line 353, in ntransfercmd
    host, port = self.makepasv()
  File "C:\Users\Titovskiysa\AppData\Local\Programs\Python\Python39\lib\ftplib.py", line 327, in makepasv
    untrusted_host, port = parse227(self.sendcmd('PASV'))
  File "C:\Users\Titovskiysa\AppData\Local\Programs\Python\Python39\lib\ftplib.py", line 839, in parse227
    raise error_reply(resp)
ftplib.error_reply: 200 Type set to I.
>>> newfile = "newfile1.doc"
>>> MyPath = "C:\\Python\\Списки присутствующих\\" + newfile
>>> ftp.retrbinary("RETR " + filename, open(MyPath, "wb").write)
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    ftp.retrbinary("RETR " + filename, open(MyPath, "wb").write)
  File "C:\Users\Titovskiysa\AppData\Local\Programs\Python\Python39\lib\ftplib.py", line 436, in retrbinary
    with self.transfercmd(cmd, rest) as conn:
  File "C:\Users\Titovskiysa\AppData\Local\Programs\Python\Python39\lib\ftplib.py", line 393, in transfercmd
    return self.ntransfercmd(cmd, rest)[0]
  File "C:\Users\Titovskiysa\AppData\Local\Programs\Python\Python39\lib\ftplib.py", line 353, in ntransfercmd
    host, port = self.makepasv()
  File "C:\Users\Titovskiysa\AppData\Local\Programs\Python\Python39\lib\ftplib.py", line 327, in makepasv
    untrusted_host, port = parse227(self.sendcmd('PASV'))
  File "C:\Users\Titovskiysa\AppData\Local\Programs\Python\Python39\lib\ftplib.py", line 839, in parse227
    raise error_reply(resp)
ftplib.error_reply: 200 Type set to I.
>>> import ftplib
>>> ip = "10.240.65.130"
>>> ftp = ftplib.FTP(ip)
>>> login = ""
>>> passw = ""
>>> ftp.login(login, passw)
SyntaxError: multiple statements found while compiling a single statement
>>> ftp.cwd("/Incoming")
'250 CWD command successful.'
>>> filename = "11.04.23.doc"
>>> newfile = "newfile.doc"
>>> MyPath = "C:\\Python\\Списки присутствующих\\" + newfile
>>> ftp.retrbinary("RETR " + filename, open(MyPath, "wb").write)
'227 Entering Passive Mode (10,240,65,130,238,101)'
>>> 
================================ RESTART: Shell ================================
>>> import ftplib
>>> ip = "10.135.11.177"
>>> ftp = ftplib.FTP(ip)
>>> login = "DB"
>>> passw = "TSA&44186"
>>> ftp.login(login, passw)
'230 User logged in.'
>>> filename = "Base_13.12.2021.xlsx"
>>> filenames = ftp.nlst()
>>> print(str(filenames))
['Base_13.12.2021.xlsx']
>>> for fileftp in filenames:
	print("1")

	
1
>>> newfile = "temp.xlsx"
>>> MyPath = "C:\\Python\\Списки присутствующих\\" + newfile
>>> for fileftp in filenames:
	ftp.retrbinary("RETR " + fileftp, open(MyPath, "wb").write)

	
'226 Transfer complete.'
>>> 