# -*- coding: UTF-8 -*-

# code a func to send mail from smtp.163.com
''' 
程序设计：
目的：  用一个发件人账户从一个xlsx 表格中逐条发送邮件。 
步骤： 
	1. 读取excel文件：收件人，和邮件正文。
	2. 定义一个函数，按  【收件人】 和 【邮件正文】 发送邮件
	3. 历遍循环，把读出的【收件人】 和 【邮件正文】 放到邮件函数中发送。

'''

import smtplib
from email.mime.text import MIMEText
from email.header import Header
import openpyxl

# define user account
user_pw = 'lx88979888'
sender_addr = 'liuxun931@163.com'

smtp_server = 'smtp.163.com'
sm = smtplib.SMTP()

# open xlsx
wkbk = openpyxl.load_workbook('mails_to_send.xlsx')
ws = wkbk['lx_sheet']


#  END make mail content
	

# send mail func
def send_my_email(receiver_mailaddr, message):
	try:
		sm.connect(smtp_server, 25)
		sm.ehlo()
		sm.login(sender_addr, user_pw)
		sm.sendmail(sender_addr, receiver_mailaddr, message)
		sm.quit()
	except:
		print('Failed to send mail')

# define a func to eliminate blank space of input.
def prompt(prompt):
    return input(prompt).strip()
# end function

## fetch data from xlsx & send mail
for row in ws.rows:
	# put receiver and msg to run:
	receiver_mailaddr = row[0].value
	#sender_addr = prompt(sender_addr)
	#receiver_mailaddr  = prompt(receiver_mailaddr).split()
	sa = row[2].value
	msg = ("From: %s\r\nTo: %s\r\n\r\n"
       % (sender_addr, receiver_mailaddr))
	msg = msg + sa
	print(msg)
	send_my_email(receiver_mailaddr, msg)

			


