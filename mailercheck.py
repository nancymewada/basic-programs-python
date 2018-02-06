import smtplib
import base64
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
source = 'test'
sendto = 'test@gmail.com'
user= 'testt@office365domain.com'
password = 'passwordd'



msg = MIMEMultipart()
msgbody =  'Please find attached copy of results from the source-{}.'.format(source)
msg['Subject'] = 'testmail check Results - {}'.format(source)
msg['From'] = user
msg['To'] = sendto

# Attach HTML to the email
body = MIMEText(msgbody, 'html')
msg.attach(body)
# Attachmenta add to the email
attach_file = MIMEApplication(open("testexcel.xlsx", "rb").read())
attach_file.add_header('Content-Disposition', 'attachment', filename="testexcel.xlsx")
msg.attach(attach_file)

try:
    smtpsrv = "smtp.office365.com"
    smtpserver = smtplib.SMTP(smtpsrv,'587')
    smtpserver.ehlo()
    smtpserver.starttls()
    smtpserver.login(user, password)
    smtpserver.sendmail(user, sendto, msg.as_string())
    print("Email successfully sent to", sendto)
except Exception as e:
    print ('SMTPAuthenticationError')
    print ("Email not sent to", e)
print('done!')
smtpserver.quit()



