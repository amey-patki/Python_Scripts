import smtplib

from email.mime.text import MIMEText

def send_email():
    sender = "paturohu95@gmail.com"
    recipient = "ameypatki28495@gmail.com"
    subject = "Test Email"
    body = "Hi Amey ! This is a test email"
    
    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = sender
    msg["To"] = recipient
    
    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(sender, "password")
        server.sendmail(sender, recipient, msg.as_string())
        
        print("Email sent successfully")
        
send_email()
                     