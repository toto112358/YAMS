from ftplib import FTP
ftp = FTP('ftp.us.debian.org')
ftp.login()
ftp.cwd('debian')
