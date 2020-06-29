# import pyperclip
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import getpass


def login():
    global FROM
    FROM = input('Enter Cengage email-id: ')
    global PASSWORD
    PASSWORD = getpass.getpass('Enter Cengage Password: ')
    SERVER = "smtp.office365.com"
    global s
    s = smtplib.SMTP(host=SERVER, port=587, timeout=(15*60))
    s.starttls()

    try:
        s.login(FROM, PASSWORD)
        print("\nLogged in successfully!\n")
    except Exception:
        print("\nSorry! Login unsuccessful. Please re-enter credentials.\n")
        login()


login()

message = MIMEMultipart()

# recipient = 'shalder@smartshifttech.com,suraj.talwar@cengage.com' # can be a list
recipient = input("Enter TO email-id: ")
message["From"] = FROM
# message["To"] = recipient
message['To'] = ','.join(recipient.split(','))


def get_details():
    global var1, var2, var3, var4, var5, subject
    var1 = input('Application affected: ')
    var2 = input('Issue: ')
    var3 = input('Incident Reported Date and Time: ')
    var4 = input('Slack Subchannel: ')
    var5 = input(
        'Issue Description - Initial report(enter info in single line): ')
    message["Subject"] = input('Subject: ')
    subject = message["Subject"]
        



def input_data_into_html(var1, var2, var3, var4, var5):
    global html
    html = f"""\
    <!DOCTYPE html>
    <html>
    <body>
    <table border="2" cellpadding="5" style="width: 850px; table-layout: fixed; border-collapse: collapse; word-wrap: break-word;">
        <!-- <tbody style="border-color: rgb(31, 73, 125); border-style: solid; border-width: 2px;"> -->
        <tbody>
            <tr>
                <td align="center" colspan="4" style="background-color: rgb(255, 192, 0); border: 2px solid rgb(31, 73, 125);"><strong>CRITSIT NOTIFICATION</strong></td>
            </tr>
            <tr>
                <td align="center" colspan="4" style="background-color: rgb(255, 0, 0); border: 2px solid rgb(31, 73, 125);"><strong>Status: In Progress</strong></td>
            </tr>
            <tr>
                <td colspan="4" style="background-color:rgb(149, 179, 215); border: 2px solid rgb(31, 73, 125);"><strong>Incident Description</strong></td>
            </tr>
            <tr>
                <td colspan="4"><strong>Application/Service/Major Component*: {var1} </strong></td>
            </tr>
            <tr>
                <td colspan="4"><strong>Issue*: </strong>{var2}</td>
            </tr>
            <tr>
                <td colspan="1"><strong>Impact:</strong> Internal/External</td>
                <td colspan="3">External</td>
            </tr>
            <tr>
                <td colspan="4">
                    <small>
                        Note: KITT notifications (for Sales/Marketing communication) will be automatically sent for every external incident. Created by Tech Support mgmt. 
                    </small>
                </td>
            </tr>
            <tr>
                <td colspan="4" style="background-color:rgb(149, 179, 215); border: 2px solid rgb(31, 73, 125);"><strong>Incident Details</strong></td>
            </tr>
            <tr>
                <td colspan="1"><strong>Incident Severity (Sev 1/2/3):</strong></td>
                <td colspan="3"></td>
            </tr>
            <tr>
                <td colspan="1"><strong>Incident Reported Date/Time:*</strong></td>
                <td colspan="1">{var3}</td>
                <td colspan="1"><strong>Resolution Date/Time:</strong></td>
                <td colspan="1"></td>
            </tr>
            <tr>
                <td colspan="1"><strong>Incident ID # (if available)</strong></td>
                <td colspan="3"></td>
            </tr>
            <tr>
                <td colspan="1"><strong>Reported By: </strong></td>
                <td colspan="3"></td>
            </tr>
            <tr>
                <td colspan="2" style="background-color:rgb(149, 179, 215); border: 2px solid rgb(31, 73, 125);"><strong>Bridge/Incident Manager (IM) Details</strong></td>
                <td colspan="2" style="background-color:rgb(149, 179, 215); border: 2px solid rgb(31, 73, 125);"><strong>Resources/Technology Details</strong></td>
            </tr>
            <tr>
                <td colspan="2"></td>
                <td colspan="1">Service</td>
                <td colspan="1"></td>
            </tr>
            <tr>
                <td colspan="1">Email ID</td>
                <td colspan="1">n/a</td>
                <td colspan="1">Team/Engineer</td>
                <td colspan="1"></td>
            </tr>
            <tr>
                <td colspan="2">Slack Subchannel:* {var4}</td>
                <td colspan="1">Business/System Owner </td>
                <td colspan="1"></td>
            </tr>
            <tr colspan="4" style="height: 84px; background-color:rgb(149, 179, 215); border: 2px solid rgb(31, 73, 125);">
                <td colspan="4">
                    <strong>Issue Description (and updates): </strong>
                        <br>
                        <br>
                    <small><em>Initial Report:</em></small>
                        <br>
                        <br>
                    * {var5}
                </td>
            </tr>
            <tr>
                <td colspan="4"><strong>Next Update:* </strong>In 30 minutes</td>
            </tr>
        </tbody>
    </table>
    </body>
    </html>
    """

# Output details for verification


def verify_details(var1m, var2m, var3m, var4m, var5m, subjectm):
    input_data_into_html(var1m, var2m, var3m, var4m, var5m)
    message["Subject"] = subjectm
    print('\n-----------Verify entered details---------------\n')
    print('[1] Subject: ', subjectm)
    print('[2] Application affected: ', var1m)
    print('[3] Issue: ', var2m)
    print('[4] Incident Reported Date and Time: ', var3m)
    print('[5] Slack Subchannel: ', var4m)
    print('[6] Issue Description - Initial report: ', var5m)
    print('Your email-id: ', FROM)
    print('Sending To: ', recipient, end='\n\n')
    send = input(
        "Enter y to send. To modify any field, enter the corresponding field's number: ")

    if send.lower() == 'y':
        return send_mail()
    elif send.lower() == 'n':
        return print('\nExiting App...')
    elif send == '1':
        subjectm = input('Subject: ')
        return verify_details(var1m, var2m, var3m, var4m, var5m, subjectm)
    elif send == '2':
        var1m = input('Application affected: ')
        return verify_details(var1m, var2m, var3m, var4m, var5m, subjectm)
    elif send == '3':
        var2m = input('Issue: ')
        return verify_details(var1m, var2m, var3m, var4m, var5m, subjectm)
    elif send == '4':
        var3m = input('Incident Reported Date and Time: ')
        return verify_details(var1m, var2m, var3m, var4m, var5m, subjectm)
    elif send == '5':
        var4m = input('Slack Subchannel: ')
        return verify_details(var1m, var2m, var3m, var4m, var5m, subjectm)
    elif send == '6':
        var5m = input(
            'Issue Description - Initial report(enter info in single line): ')
        return verify_details(var1m, var2m, var3m, var4m, var5m, subjectm)
    else:
        print('Invalid input\n')
        return verify_details(var1m, var2m, var3m, var4m, var5m, subjectm)


def send_mail():
    # Turn these into plain/html MIMEText objects
    part1 = MIMEText(html, "html")
    # Add HTML/plain-text parts to MIMEMultipart message
    message.attach(part1)
    print("Sending Initial Critsit...")
    s.sendmail(FROM, recipient.split(','), message.as_string())
    s.quit()
    print("Sent!")


get_details()
verify_details(var1, var2, var3, var4, var5, subject)

input("Press ENTER key to close...\n")  # required for stand-alone exe file
