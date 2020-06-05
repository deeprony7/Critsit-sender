# import pyperclip
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib, ssl
import critsit
import getpass

message = MIMEMultipart()
message["Subject"] = input('Subject: ')
SERVER = "smtp.office365.com"
FROM = input('Enter Cengage email-id: ')
TO = "shalder@smartshifttech.com" # must be a list
PASSWORD = getpass.getpass('Enter Cengage Password: ')

message["From"] = FROM
message["To"] = TO


# Turn these into plain/html MIMEText objects
part1 = MIMEText(critsit.html, "html")

# Add HTML/plain-text parts to MIMEMultipart message
message.attach(part1)

# Output details for verification

print('\n\n-----------Verify entered details---------------\n')
print('Subject: ', message["Subject"])
print('Application affected: ', critsit.var1)
print('Issue: ', critsit.var2)
print('Incident Reported Date and Time: ', critsit.var3)
print('Slack Subchannel: ', critsit.var4)
print('Issue Description - Initial report: ', critsit.var5)
print('Your email-id: ', FROM)
print('Sending To: ', TO)

send = input("Ready to send? (y/n): ")

s = smtplib.SMTP(host=SERVER, port=587)
s.starttls()
s.login(FROM, PASSWORD)

# Send the mail
if send.lower() == 'y':
    print("Sending Initial Critsit...")
    s.sendmail(FROM, TO, message.as_string())
    s.quit()
    print("Sent!")
else:
    print('Mail not sent')
    
input("Press ENTER key to close...\n") #required for stand-alone exe file
