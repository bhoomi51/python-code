import smtplib
sender_mail = 'bhoomigandhi51@gmail.com'
receivers_mail = ['bhoomigandhi03@gmail.com']
message = """From: From Person %s  
To: To Person %s  
Subject: Sending SMTP e-mail   
This is a test e-mail message.  
"""%(sender_mail,receivers_mail)
try:
   password = input('Enter the password');
   smtpObj = smtplib.SMTP('gmail.com',465)
   smtpobj.login(sender_mail,password)
   smtpObj.sendmail(sender_mail, receivers_mail, message)
   print("Successfully sent email")
except Exception:
   print("Error: unable to send email")