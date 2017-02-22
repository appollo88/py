# code a func to send mail from smtp.163.com

import smtplib
from email.mime.text import MIMEText

sm = smtplib.SMTP()
'''
#---------------------------send an email via smtp.163.com --------------------
# init smtp
sm = smtplib.SMTP()
# end init smtp

# define 
server_name = '163'
smtp_server = 'smtp.' + server_name + '.com'
user_accoutname = 'liuxun931'
user_account = user_accoutname + '@' + server_name + '.com'
user_pw = 'lx88979888'
receiver_mailaddr = 'liuxun931@163.com'

print(smtp_server)
print(user_account)
print(user_pw) 

# try to connect
sm.connect(smtp_server, 25)
sm.helo()
sm.ehlo()
sm.login(user_account, user_pw)
sm.sendmail(user_account, receiver_mailaddr, 'msg')

# quit
sm.quit()
# end quit 

#-------------------------------end send an email via smtp.163.com --------------------
'''

#add a mail message
with open('mail_message.txt') as fp:
    # Create a text/plain message
    msg = MIMEText(fp.read())

me = 'liuxun931@163.com'
you = 'liuxun931@163.com'
msg['Subject'] = 'The contents of mail_message.txt.' 
msg['From'] = me
msg['To'] = you
# sm.send_message(msg)

try:
	sm = smtplib.SMTP()
	sm.connect('smtp.163.com', 25)
	sm.helo()
	sm.ehlo()
	sm.login('liuxun931@163.com', 'lx88979888')
	sm.sendmail('liuxun931@163', 'liuxun931@163.com', msg)
	sm.quit()
except:
	print('Failed to send mail-msg.')


def send_my_email(user_accountname, user_pw, server_name, receiver_mailaddr):
	# user_accountname, user_pw, server_name, receiver_mailaddr 
	# ('liuxun931', 'lx88979888', '163', 'liuxun931@163.com')
	# server_name = '163'
	smtp_server = 'smtp.' + server_name + '.com'
	# user_accoutname = 'liuxun931'
	user_account = user_accountname + '@' + server_name + '.com'
	# user_pw = 'lx88979888'
	# receiver_mailaddr = 'liuxun931@163.com'
	
	sm = smtplib.SMTP()
	sm.connect(smtp_server, 25)
	sm.helo()
	sm.ehlo()
	sm.login(user_account, user_pw)
	sm.sendmail(user_account, receiver_mailaddr, 'msg')

	# quit
	sm.quit()