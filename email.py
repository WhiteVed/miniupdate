import smtplib
server = smtplib.SMTP("smtp.cock.li",587)
server.starttls()
server.login("faceysupport@cock.li","facey@123")
print("done")
