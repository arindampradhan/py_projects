# send your friend a mial
# if u want to spam also iterate it ;)
# just change the second my_mail to do false mail like 
# mail.sendmail("iamsupermail@gmail.com",to_mail,content) ;D


import smtplib
mail = smtplib.SMTP('smtp.gmail.com:587')
mail.starttls()
content = raw_input("give the message?\n")
print
my_mail = raw_input("ur email address -> ")
my_passwd = raw_input("ur email passwd -> ")
print 

to_mail = raw_input("Send mail to ? ")
mail.login(my_mail,my_passwd)
mail.sendmail(my_mail,to_mail,content)
mail.close()


print "ur message was delivered"
