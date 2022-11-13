import smtplib
from email.message import EmailMessage

print('Welcome to sending mails using python')
print('go to this link https://myaccount.google.com/lesssecureapps?pli=1 login to your account and turn it on')
fromid = input('Please enter your gmail id')
passcode = input('Please enter your password')
toid = input('Please enter gmail id whom you want to send')
# msg = input('Please Enter your message')

mail = EmailMessage()
mail['Subject'] = input('Please enter the subject line')
mail['From'] = fromid
mail['To'] = toid
mail.set_content(input('Please enter your message'))

def sendmail(fromid,passcode,toid,mail):
	server = smtplib.SMTP('smtp.gmail.com',587)
	server.ehlo()
	server.starttls()         # starting tls -> transport layer security(i.e, Put the SMTP connection in TLS (Transport Layer Security) mode)
	server.login(fromid,passcode)
	content = mail.as_string()
	if server.sendmail(fromid,toid,content) == {}:
		print('Mail sent',u'\u2713')
	else:
	    print('Failed')	

	server.quit()

if __name__ == "__main__":
	sendmail(fromid,passcode,toid,mail)
