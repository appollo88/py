"""import smtplib
 
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login("liuxun931@gmail.com", "lx061511")
 
msg = "YOUR MESSAGE!"
server.sendmail("liuxun931@gmail.com", "liuxun931@163.com", msg)
server.quit()
"""


# smtplib module send mail

import smtplib

TO = 'liuxun931@163.com'
SUBJECT = 'TEST MAIL'
TEXT = 'Here is a message from python.'

# Gmail Sign In
gmail_sender = 'liuxun931@gmail.com'
gmail_passwd = 'lx061511'

server = smtplib.SMTP('smtp.gmail.com', 587)
server.ehlo()
server.starttls()
server.login(gmail_sender, gmail_passwd)

BODY = '\r\n'.join(['To: %s' % TO,
                    'From: %s' % gmail_sender,
                    'Subject: %s' % SUBJECT,
                    '', TEXT])

try:
    server.sendmail(gmail_sender, [TO], BODY)
    print ('email sent')
except:
    print ('error sending mail')

server.quit()