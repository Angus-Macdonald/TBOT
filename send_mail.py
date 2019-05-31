#Importing email modules
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

from email_cred import * #importing my credentials
email_send = 'n10448888@qut.edu.au'#sending to my email

subject = 'Useful Humans' #subject line

#Selecting who to, from, subject
msg = MIMEMultipart()
msg['From'] = email_user
msg['To'] = email_send
msg['Subject'] = subject

#the text body
body = 'List of potential allies!'
msg.attach(MIMEText(body,'plain'))

#attaching the file
filename='UsefulHumans.txt'
attachment  =open(filename,'rb')

#structuring and encoding of email
part = MIMEBase('application','octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition',"attachment; filename= "+filename)

msg.attach(part)
text = msg.as_string()
#sending to outlook sever with QUT email uses
server = smtplib.SMTP('smtp.outlook.com',587)
server.starttls()
server.login(email_user,email_passwrd)

#Send and quit
server.sendmail(email_user,email_send,text)
server.quit()
