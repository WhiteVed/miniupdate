import smtplib
server =smtplib.SMTP("smtp.gmail.com",587)
server.starttls()
server.login('sfacechecker@gmail.com',"wdrbvzdidynsmrgi")
server.sendmail("sfacechecker@gmail.com","whiteved@protonmail.com","email is from facesupport")
print("mailsend")