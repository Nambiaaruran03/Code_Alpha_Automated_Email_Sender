import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

smtp_port = 587                 
smtp_server = "smtp.gmail.com"  

# Set up the email lists
email_from = "nambiaaruran1@gmail.com"
email_list = ["nambiaaruran1@gmail.com", "nambiaaruran.2105102@srec.ac.in"]

pswd = "knbpoxkxxnakldxi"

subject = "New email from TIE with attachments!!"

def send_emails(email_list):

    for person in email_list:
        body = f"""
        line 1
        line 2
        line 3
        etc
        """
        msg = MIMEMultipart()
        msg['From'] = email_from
        msg['To'] = person
        msg['Subject'] = subject

        msg.attach(MIMEText(body, 'plain'))

        filename = "random_data.csv"

        attachment= open(filename, 'rb')  # r for read and b for binary

        attachment_package = MIMEBase('application', 'octet-stream')
        attachment_package.set_payload((attachment).read())
        encoders.encode_base64(attachment_package)
        attachment_package.add_header('Content-Disposition', "attachment; filename= " + filename)
        msg.attach(attachment_package)

        text = msg.as_string()

        print("Connecting to server...")
        TIE_server = smtplib.SMTP(smtp_server, smtp_port)
        TIE_server.starttls()
        TIE_server.login(email_from, pswd)
        print("Succesfully connected to server")
        print()

        print(f"Sending email to: {person}...")
        TIE_server.sendmail(email_from, person, text)
        print(f"Email sent to: {person}")
        print()

    TIE_server.quit()

send_emails(email_list)




        





