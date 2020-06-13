import smtplib

class Notify():
    
    def Send():
        gmail_user = 'krishern0719@gmail.com'
        gmail_password = 'careyprice31'

        user = "Kris"
        sender = "Angelica"

        to = 'krishern727@yahoo.com'
        subject = "New Message :)"
        body = "Hello {}, {} sent you a new message!!".format(user,sender)

        email_text = """\
        From: %s
        To: %s
        Subject %s

        %s
        """ % (gmail_user,to,subject,body)
        try:
            server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
            server.ehlo()
            server.login(gmail_user, gmail_password)
            #print("Logged in")
            server.sendmail(gmail_user,to,email_text)
            #print("Email Sent")
            return 0
        
        except:
            return 1

