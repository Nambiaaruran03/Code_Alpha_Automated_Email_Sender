import smtplib
import ssl
smtp_port = 587                 
smtp_server = "smtp.gmail.com"  

email_from = "nambiaaruran1@gmail.com"
email_to = "nambiaaruran.2105102@srec.ac.in"
pswd = "knbpoxkxxnakldxi"
message = "Dear god, please help!!!"
simple_email_context = ssl.create_default_context()
try:
    # Connect to the server
    print("Connecting to server...")
    TIE_server = smtplib.SMTP(smtp_server, smtp_port)
    TIE_server.starttls(context=simple_email_context)
    TIE_server.login(email_from, pswd)
    print("Connected to server :-)")
    
    # Send the actual email
    print()
    print(f"Sending email to - {email_to}")
    TIE_server.sendmail(email_from, email_to, message)
    print(f"Email successfully sent to - {email_to}")
except Exception as e:
    print(e)
finally:
    TIE_server.quit()





