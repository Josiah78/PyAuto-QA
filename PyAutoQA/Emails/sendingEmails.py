import smtplib

smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
smtpObj.ehlo()
smtpObj.starttls()
smtpObj.login('josiahjamison08@gmail.com', 'paperplanes')
smtpObj.sendmail('josiahjamison08@gmail.com', 'josiahjamison7@gmail.com', 'Subject: This is a subject \nThis is the body')