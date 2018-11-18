import smtplib

user = 'jedrzej.antkowiak'

password = 'NIEPOKAŻĘPRZEMKOWIMOJEGOHASŁAICHUJ'

sent_from = "asdasd@gmail.com"
to = ["roasd@wp.pl"]
subject = "try this"
body = "treźć"

email_txt = f'''
From: {sent_from}
To: {', '.join(to)}
Subject: {subject}


{body}

'''



try:
    server = smtplib.SMTP_SSL("smtp.wp.pl", 465)
    server.ehlo()
    server.login(user, password)
    server.sendmail(sent_from, to, email_txt)
    server.close()
except:
    print("Coś poszło nie tak")