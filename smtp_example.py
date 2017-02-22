import smtplib

# define a func to eliminate blank space of input.
def prompt(prompt):
    return input(prompt).strip()
# end function
	
# def alters
fromaddr = prompt("From: ")
toaddrs  = prompt("To: ").split()
print("Enter message, end with ^D (Unix) or ^Z (Windows):")

# Add the From: and To: headers at the start!
msg = ("From: %s\r\nTo: %s\r\n\r\n"
       % (fromaddr, ", ".join(toaddrs)))
while True:
    try:
        line = input()
    except EOFError:
        break
    if not line:
        break
    msg = msg + line

print("Message length is", len(msg))


try:
	sm = smtplib.SMTP()
	sm.connect('smtp.163.com', 25)
	sm.helo()
	sm.ehlo()
	sm.login('liuxun931@163.com', 'lx88979888')
	sm.sendmail(fromaddr, toaddrs, msg)
	sm.quit()
except:
	print('Failed to send mail-msg.')

