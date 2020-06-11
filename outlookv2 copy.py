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
    s = smtplib.SMTP(host=SERVER, port=587)
    s.starttls()
    
    try:
        s.login(FROM, PASSWORD)
        print("\nLogged in successfully!\n")
    except Exception:
        print("\nSorry! Login unsuccessful. Please re-enter credentials.\n")
        login()
login()

message = MIMEMultipart()

TO = "shalder@smartshifttech.com" # can be a list
message["From"] = FROM
message["To"] = TO

def get_details():
    global var1, var2, var3, var4, var5, subject
    var1 = input('Application affected: ')
    var2 = input('Issue: ')
    var3 = input('Incident Reported Date and Time: ')
    var4 = input('Slack Subchannel: ')
    var5 = input('Issue Description - Initial report(enter info in single line): ')
    message["Subject"] = input('Subject: ')
    subject = message["Subject"]


def input_data_into_html(var1, var2, var3, var4, var5):
    global html
    html = f"""\
    <div class="OutlineElement Ltr  BCX2 SCXW140673802" style="direction: ltr;">
        <div class="TableContainer SCXW140673802 BCX2">
            <div class="WACAltTextDescribedBy SCXW140673802 BCX2"><br></div>
            <table border="1" class="Table TableWordWrap SCXW140673802 BCX2" data-tablelook="1184" data-tablestyle="MsoNormalTable" style="border-collapse: collapse; background: transparent none repeat scroll 0% 0%; border-spacing: 0px;">
                <tbody class="SCXW140673802 BCX2">
                    <tr class="TableRow SCXW140673802 BCX2" style="height: 20px;">
                        <td class="SCXW140673802 BCX2" colspan="5" data-celllook="69905" style="background-color: rgb(255, 192, 0); border-color: rgb(31, 73, 125) rgb(31, 73, 125) rgb(31, 78, 121); border-style: solid; border-width: 2px; border-image: none 100% / 1 / 0 stretch; vertical-align: bottom; width: 805px;">
                            <div class="TableCellContent SCXW140673802 BCX2" style="padding: 0px 7px;">
                                <div class="OutlineElement Ltr  BCX2 SCXW140673802" style="direction: ltr;">
                                    <p class="Paragraph SCXW140673802 BCX2" style="font-weight: normal; font-style: normal; vertical-align: baseline; background-color: transparent; color: windowtext; text-align: center; margin-left: 0px; margin-right: 0px; padding-left: 0px; padding-right: 0px; text-indent: 0px;"><span class="TextRun SCXW140673802 BCX2" data-contrast="none" lang="EN-US" style="color: rgb(0, 0, 0); font-weight: bold; font-size: 11pt; font-family: Book Antiqua, Book Antiqua_EmbeddedFont, Book Antiqua_MSFontService, serif; line-height: 18.9px;"><span class="NormalTextRun SCXW140673802 BCX2" style="background-color: inherit;">CRITSIT NOTIFICATION</span></span><span class="EOP SCXW140673802 BCX2" data-ccp-props='{{"201341983":0,"335551550":2,"335551620":2,"335559739":0,"335559740":252}}' style="font-size: 11pt; line-height: 18.9px; font-family: Book Antiqua, Book Antiqua_EmbeddedFont, Book Antiqua_MSFontService, serif;">&nbsp;</span></p>
                                </div>
                            </div>
                        </td>
                    </tr>
                    <tr class="TableRow SCXW140673802 BCX2" style="height: 19px;">
                        <td class="SCXW140673802 BCX2" colspan="5" data-celllook="69905" style="background-color: rgb(255, 0, 0); border-color: currentcolor rgb(31, 73, 125) rgb(31, 78, 121); border-style: none solid solid; border-width: 0px 2px 2px; border-image: none 100% / 1 / 0 stretch; vertical-align: bottom; width: 805px;">
                            <div class="TableCellContent SCXW140673802 BCX2" style="padding: 0px 7px;">
                                <div class="OutlineElement Ltr  BCX2 SCXW140673802" style="direction: ltr;">
                                    <p class="Paragraph SCXW140673802 BCX2" style="font-weight: normal; font-style: normal; vertical-align: baseline; background-color: transparent; color: windowtext; text-align: center; margin-left: 0px; margin-right: 0px; padding-left: 0px; padding-right: 0px; text-indent: 0px;"><span class="TextRun SCXW140673802 BCX2" data-contrast="none" lang="EN-US" style="color: rgb(0, 0, 0); font-weight: bold; font-size: 11pt; font-family: Book Antiqua, Book Antiqua_EmbeddedFont, Book Antiqua_MSFontService, serif; line-height: 18.9px;"><span class="NormalTextRun SCXW140673802 BCX2" style="background-color: inherit;">Status:</span></span><span class="TextRun SCXW140673802 BCX2" data-contrast="none" lang="EN-US" style="color: rgb(0, 0, 0); font-size: 12pt; font-family: Times New Roman, Times New Roman_EmbeddedFont, Times New Roman_MSFontService, serif; line-height: 19.95px;"><span class="NormalTextRun SCXW140673802 BCX2" style="background-color: inherit;">&nbsp;</span></span><span class="TextRun SCXW140673802 BCX2" data-contrast="none" lang="EN-US" style="color: rgb(0, 0, 0); font-weight: bold; font-size: 12pt; font-family: Times New Roman, Times New Roman_EmbeddedFont, Times New Roman_MSFontService, serif; line-height: 19.95px;"><span class="NormalTextRun SCXW140673802 BCX2" style="background-color: inherit;">In Progress</span></span><span class="EOP SCXW140673802 BCX2" data-ccp-props='{{"201341983":0,"335551550":2,"335551620":2,"335559739":0,"335559740":252}}' style="font-size: 12pt; line-height: 19.95px; font-family: Times New Roman, Times New Roman_EmbeddedFont, Times New Roman_MSFontService, serif;">&nbsp;</span></p>
                                </div>
                            </div>
                        </td>
                    </tr>
                    <tr class="TableRow SCXW140673802 BCX2" style="height: 19px;">
                        <td class="SCXW140673802 BCX2" colspan="5" data-celllook="69905" style="background-color: rgb(149, 179, 215); border-color: currentcolor rgb(31, 73, 125) rgb(31, 78, 121); border-style: none solid solid; border-width: 0px 2px 2px; border-image: none 100% / 1 / 0 stretch; vertical-align: bottom; width: 805px;">
                            <div class="TableCellContent SCXW140673802 BCX2" style="padding: 0px 7px;">
                                <div class="OutlineElement Ltr  BCX2 SCXW140673802" style="direction: ltr;">
                                    <p class="Paragraph SCXW140673802 BCX2" style="font-weight: normal; font-style: normal; vertical-align: baseline; background-color: transparent; color: windowtext; text-align: left; margin-left: 0px; margin-right: 0px; padding-left: 0px; padding-right: 0px; text-indent: 0px;"><span class="TextRun SCXW140673802 BCX2" data-contrast="none" lang="EN-US" style="color: rgb(0, 0, 0); font-weight: bold; font-size: 11pt; font-family: Book Antiqua, Book Antiqua_EmbeddedFont, Book Antiqua_MSFontService, serif; line-height: 18.9px;"><span class="NormalTextRun SCXW140673802 BCX2" style="background-color: inherit;">Incident Description&nbsp;</span></span><span class="EOP SCXW140673802 BCX2" data-ccp-props='{{"201341983":0,"335559739":0,"335559740":252}}' style="font-size: 11pt; line-height: 18.9px; font-family: Book Antiqua, Book Antiqua_EmbeddedFont, Book Antiqua_MSFontService, serif;">&nbsp;</span></p>
                                </div>
                            </div>
                        </td>
                    </tr>
                    <tr class="TableRow SCXW140673802 BCX2" style="height: 15px;">
                        <td class="SCXW140673802 BCX2" colspan="5" data-celllook="4369" style="background-color: transparent; border-color: currentcolor rgb(31, 73, 125) rgb(0, 0, 0); border-style: none solid solid; border-width: 0px 2px 1px; border-image: none 100% / 1 / 0 stretch; vertical-align: top; width: 805px;">
                            <div class="TableCellContent SCXW140673802 BCX2" style="padding: 0px 7px;">
                                <div class="OutlineElement Ltr  BCX2 SCXW140673802" style="direction: ltr;">
                                    <p class="Paragraph SCXW140673802 BCX2" style="font-weight: normal; font-style: normal; vertical-align: baseline; background-color: transparent; color: windowtext; text-align: left; margin-left: 0px; margin-right: 0px; padding-left: 0px; padding-right: 0px; text-indent: 0px;"><span class="TextRun SCXW140673802 BCX2" data-contrast="none" lang="EN-US" style="color: rgb(0, 0, 0); font-weight: bold; font-size: 11pt; font-family: Book Antiqua, Book Antiqua_EmbeddedFont, Book Antiqua_MSFontService, serif; line-height: 18px;"><span class="NormalTextRun SCXW140673802 BCX2" style="background-color: inherit;">Application/Service/Major Component</span></span><span class="TextRun SCXW140673802 BCX2" data-contrast="none" lang="EN-US" style="color: rgb(255, 0, 0); font-weight: bold; font-size: 11pt; font-family: Book Antiqua, Book Antiqua_EmbeddedFont, Book Antiqua_MSFontService, serif; line-height: 18px;"><span class="NormalTextRun SCXW140673802 BCX2" style="background-color: inherit;">*</span></span><span class="TextRun SCXW140673802 BCX2" data-contrast="none" lang="EN-US" style="color: rgb(0, 0, 0); font-weight: bold; font-size: 11pt; font-family: Book Antiqua, Book Antiqua_EmbeddedFont, Book Antiqua_MSFontService, serif; line-height: 18px;"><span class="NormalTextRun SCXW140673802 BCX2" style="background-color: inherit;">:</span><span class="NormalTextRun SCXW140673802 BCX2" style="background-color: inherit;">&nbsp;{var1}</span></span><span class="EOP SCXW140673802 BCX2" data-ccp-props='{{"201341983":0,"335559739":0,"335559740":240}}' style="font-size: 11pt; line-height: 18px; font-family: Book Antiqua, Book Antiqua_EmbeddedFont, Book Antiqua_MSFontService, serif;">&nbsp;</span></p>
                                </div>
                            </div>
                        </td>
                    </tr>
                    <tr class="TableRow SCXW140673802 BCX2" style="height: 15px;">
                        <td class="SCXW140673802 BCX2" colspan="5" data-celllook="4369" style="background-color: transparent; border-color: currentcolor rgb(31, 73, 125) rgb(0, 0, 0); border-style: none solid solid; border-width: 0px 2px 1px; border-image: none 100% / 1 / 0 stretch; vertical-align: top; width: 805px;">
                            <div class="TableCellContent SCXW140673802 BCX2" style="padding: 0px 7px;">
                                <div class="OutlineElement Ltr  BCX2 SCXW140673802" style="direction: ltr;">
                                    <p class="Paragraph SCXW140673802 BCX2" style="font-weight: normal; font-style: normal; vertical-align: baseline; background-color: transparent; color: windowtext; text-align: left; margin-left: 0px; margin-right: 0px; padding-left: 0px; padding-right: 0px; text-indent: 0px;"><span class="TextRun SCXW140673802 BCX2" data-contrast="none" lang="EN-US" style="color: rgb(0, 0, 0); font-weight: bold; font-size: 11pt; font-family: Book Antiqua, Book Antiqua_EmbeddedFont, Book Antiqua_MSFontService, serif; line-height: 18px;"><span class="NormalTextRun SCXW140673802 BCX2" style="background-color: inherit;">Issue</span></span><span class="TextRun SCXW140673802 BCX2" data-contrast="none" lang="EN-US" style="color: rgb(255, 0, 0); font-weight: bold; font-size: 11pt; font-family: Book Antiqua, Book Antiqua_EmbeddedFont, Book Antiqua_MSFontService, serif; line-height: 18px;"><span class="NormalTextRun SCXW140673802 BCX2" style="background-color: inherit;">*</span></span><span class="TextRun SCXW140673802 BCX2" data-contrast="none" lang="EN-US" style="color: rgb(0, 0, 0); font-weight: bold; font-size: 11pt; font-family: Book Antiqua, Book Antiqua_EmbeddedFont, Book Antiqua_MSFontService, serif; line-height: 18px;"><span class="NormalTextRun SCXW140673802 BCX2" style="background-color: inherit;">:</span></span><span class="TextRun SCXW140673802 BCX2" data-contrast="none" lang="EN-US" style="color: rgb(0, 0, 0); font-size: 11pt; font-family: Book Antiqua, Book Antiqua_EmbeddedFont, Book Antiqua_MSFontService, serif; line-height: 18px;"><span class="NormalTextRun SCXW140673802 BCX2" style="background-color: inherit;">&nbsp;</span><span class="NormalTextRun SCXW140673802 BCX2" style="background-color: inherit;">{var2}</span></span><span class="EOP SCXW140673802 BCX2" data-ccp-props='{{"201341983":0,"335559739":0,"335559740":240}}' style="font-size: 11pt; line-height: 18px; font-family: Book Antiqua, Book Antiqua_EmbeddedFont, Book Antiqua_MSFontService, serif;">&nbsp;</span></p>
                                </div>
                            </div>
                        </td>
                    </tr>
                    <tr class="TableRow SCXW140673802 BCX2" style="height: 15px;">
                        <td class="SCXW140673802 BCX2" data-celllook="4369" style="background-color: transparent; border-color: currentcolor currentcolor rgb(31, 78, 121) rgb(31, 73, 125); border-style: none solid solid; border-width: 0px 1px 2px 2px; border-image: none 100% / 1 / 0 stretch; vertical-align: top; width: 227px;">
                            <div class="TableCellContent SCXW140673802 BCX2" style="padding: 0px 7px;">
                                <div class="OutlineElement Ltr  BCX2 SCXW140673802" style="direction: ltr;">
                                    <p class="Paragraph SCXW140673802 BCX2" style="font-weight: normal; font-style: normal; vertical-align: baseline; background-color: transparent; color: windowtext; text-align: left; margin-left: 0px; margin-right: 0px; padding-left: 0px; padding-right: 0px; text-indent: 0px;"><span class="TextRun SCXW140673802 BCX2" data-contrast="none" lang="EN-US" style="color: rgb(0, 0, 0); font-weight: bold; font-size: 11pt; font-family: Book Antiqua, Book Antiqua_EmbeddedFont, Book Antiqua_MSFontService, serif; line-height: 18px;"><span class="NormalTextRun SCXW140673802 BCX2" style="background-color: inherit;">Impact:  </span></span><span class="TextRun SCXW140673802 BCX2" data-contrast="none" lang="EN-US" style="color: rgb(0, 0, 0); font-size: 11pt; font-family: Book Antiqua, Book Antiqua_EmbeddedFont, Book Antiqua_MSFontService, serif; line-height: 18px;"><span class="NormalTextRun SCXW140673802 BCX2" style="background-color: inherit;">Internal/External</span></span><span class="EOP SCXW140673802 BCX2" data-ccp-props='{{"201341983":0,"335559739":0,"335559740":240}}' style="font-size: 11pt; line-height: 18px; font-family: Book Antiqua, Book Antiqua_EmbeddedFont, Book Antiqua_MSFontService, serif;">&nbsp;</span></p>
                                </div>
                            </div>
                        </td>
                        <td class="SCXW140673802 BCX2" colspan="4" data-celllook="4369" style="background-color: transparent; border-color: currentcolor rgb(31, 78, 121) rgb(31, 78, 121) currentcolor; border-style: none solid solid none; border-width: 0px 2px 2px 0px; border-image: none 100% / 1 / 0 stretch; vertical-align: middle; width: 577px;">
                            <div class="TableCellContent SCXW140673802 BCX2" style="padding: 0px;">
                                <div class="OutlineElement Ltr  BCX2 SCXW140673802" style="direction: ltr;">
                                    <p class="Paragraph SCXW140673802 BCX2" style="font-weight: normal; font-style: normal; vertical-align: baseline; background-color: transparent; color: windowtext; text-align: left; margin-left: 0px; margin-right: 0px; padding-left: 0px; padding-right: 0px; text-indent: 0px;"><span class="TextRun SCXW140673802 BCX2" data-contrast="none" lang="EN-US" style="color: rgb(0, 0, 0); font-size: 11pt; font-family: Calibri, Calibri_EmbeddedFont, Calibri_MSFontService, sans-serif; line-height: 18px;"><span class="NormalTextRun SCXW140673802 BCX2" style="background-color: inherit;">&nbsp;</span><span class="NormalTextRun SCXW140673802 BCX2" style="background-color: inherit;">External</span></span><span class="EOP SCXW140673802 BCX2" data-ccp-props='{{"201341983":0,"335559739":0,"335559740":240}}' style="font-size: 11pt; line-height: 18px; font-family: Calibri, Calibri_EmbeddedFont, Calibri_MSFontService, sans-serif;">&nbsp;</span></p>
                                </div>
                            </div>
                        </td>
                    </tr>
                    <tr class="TableRow SCXW140673802 BCX2" style="height: 15px;">
                        <td class="SCXW140673802 BCX2" colspan="5" data-celllook="4369" style="background-color: transparent; border-color: currentcolor rgb(31, 78, 121) rgb(31, 78, 121) rgb(31, 73, 125); border-style: none solid solid; border-width: 0px 2px 2px; border-image: none 100% / 1 / 0 stretch; vertical-align: top; width: 805px;">
                            <div class="TableCellContent SCXW140673802 BCX2" style="padding: 0px 7px;">
                                <div class="OutlineElement Ltr  BCX2 SCXW140673802" style="direction: ltr;">
                                    <p class="Paragraph SCXW140673802 BCX2" style="font-weight: normal; font-style: normal; vertical-align: baseline; background-color: transparent; color: windowtext; text-align: left; margin-left: 0px; margin-right: 0px; padding-left: 0px; padding-right: 0px; text-indent: 0px;"><span class="TextRun SCXW140673802 BCX2" data-contrast="none" lang="EN-US" style="color: rgb(0, 0, 0); font-size: 9pt; font-family: Book Antiqua, Book Antiqua_EmbeddedFont, Book Antiqua_MSFontService, serif; line-height: 14px;"><span class="NormalTextRun SCXW140673802 BCX2" style="background-color: inherit;">Note: KITT notifications (for Sales/Marketing communication) will be automatically sent for every&nbsp;</span><span class="NormalTextRun SCXW140673802 BCX2" style="background-color: inherit;">external&nbsp;</span><span class="NormalTextRun SCXW140673802 BCX2" style="background-color: inherit;">incident. Created by Tech Support mgmt.&nbsp;</span></span><span class="EOP SCXW140673802 BCX2" data-ccp-props='{{"201341983":0,"335559739":0,"335559740":240}}' style="font-size: 9pt; line-height: 14px; font-family: Book Antiqua, Book Antiqua_EmbeddedFont, Book Antiqua_MSFontService, serif;">&nbsp;</span></p>
                                </div>
                            </div>
                        </td>
                    </tr>
                    <tr class="TableRow SCXW140673802 BCX2" style="height: 5px;">
                        <td class="SCXW140673802 BCX2" colspan="5" data-celllook="69905" style="background-color: rgb(141, 179, 226); border-color: currentcolor rgb(31, 78, 121) rgb(0, 0, 0) rgb(31, 73, 125); border-style: none solid solid; border-width: 0px 2px 1px; border-image: none 100% / 1 / 0 stretch; vertical-align: middle; width: 805px;">
                            <div class="TableCellContent SCXW140673802 BCX2" style="padding: 0px 7px;">
                                <div class="OutlineElement Ltr  BCX2 SCXW140673802" style="direction: ltr;">
                                    <p class="Paragraph SCXW140673802 BCX2" style="font-weight: normal; font-style: normal; vertical-align: baseline; background-color: transparent; color: windowtext; text-align: left; margin-left: 0px; margin-right: 0px; padding-left: 0px; padding-right: 0px; text-indent: 0px;"><span class="TextRun SCXW140673802 BCX2" data-contrast="none" lang="EN-US" style="color: rgb(0, 0, 0); font-weight: bold; font-size: 11pt; font-family: Book Antiqua, Book Antiqua_EmbeddedFont, Book Antiqua_MSFontService, serif; line-height: 18.9px;"><span class="NormalTextRun SCXW140673802 BCX2" style="background-color: inherit;">Incident Details</span></span><span class="EOP SCXW140673802 BCX2" data-ccp-props='{{"201341983":0,"335559739":0,"335559740":252}}' style="font-size: 11pt; line-height: 18.9px; font-family: Book Antiqua, Book Antiqua_EmbeddedFont, Book Antiqua_MSFontService, serif;">&nbsp;</span></p>
                                </div>
                            </div>
                        </td>
                    </tr>
                    <tr class="TableRow SCXW140673802 BCX2" style="height: 5px;">
                        <td class="SCXW140673802 BCX2" data-celllook="4369" style="background-color: transparent; border-color: currentcolor currentcolor rgb(0, 0, 0) rgb(31, 73, 125); border-style: none solid solid; border-width: 0px 1px 1px 2px; border-image: none 100% / 1 / 0 stretch; vertical-align: middle; width: 227px;">
                            <div class="TableCellContent SCXW140673802 BCX2" style="padding: 0px 7px;">
                                <div class="OutlineElement Ltr  BCX2 SCXW140673802" style="direction: ltr;">
                                    <p class="Paragraph SCXW140673802 BCX2" style="font-weight: normal; font-style: normal; vertical-align: baseline; background-color: transparent; color: windowtext; text-align: left; margin-left: 0px; margin-right: 0px; padding-left: 0px; padding-right: 0px; text-indent: 0px;"><span class="TextRun SCXW140673802 BCX2" data-contrast="auto" lang="EN-US" style="font-weight: bold; font-size: 11pt; font-family: Book Antiqua, Book Antiqua_EmbeddedFont, Book Antiqua_MSFontService, serif; line-height: 18.9px;"><span class="NormalTextRun SCXW140673802 BCX2" style="background-color: inherit;">Incident Severity (</span><span class="NormalTextRun SCXW140673802 BCX2" style="background-color: inherit;">Sev</span><span class="NormalTextRun SCXW140673802 BCX2" style="background-color: inherit;">&nbsp;1/2/3)</span><span class="NormalTextRun SCXW140673802 BCX2" style="background-color: inherit;">:</span></span><span class="EOP SCXW140673802 BCX2" data-ccp-props='{{"201341983":0,"335559739":0,"335559740":252}}' style="font-size: 11pt; line-height: 18.9px; font-family: Book Antiqua, Book Antiqua_EmbeddedFont, Book Antiqua_MSFontService, serif;">&nbsp;</span></p>
                                </div>
                            </div>
                        </td>
                        <td class="SCXW140673802 BCX2" colspan="4" data-celllook="4369" style="background-color: transparent; border-color: currentcolor rgb(31, 73, 125) rgb(0, 0, 0) currentcolor; border-style: none solid solid none; border-width: 0px 2px 1px 0px; border-image: none 100% / 1 / 0 stretch; vertical-align: top; width: 577px;">
                            <div class="TableCellContent SCXW140673802 BCX2" style="padding: 0px;">
                                <div class="OutlineElement Ltr  BCX2 SCXW140673802" style="direction: ltr;">
                                    <p class="Paragraph SCXW140673802 BCX2" style="font-weight: normal; font-style: normal; vertical-align: baseline; background-color: transparent; color: windowtext; text-align: left; margin-left: 0px; margin-right: 0px; padding-left: 0px; padding-right: 0px; text-indent: 0px;"><span class="EOP SCXW140673802 BCX2" data-ccp-props='{{"201341983":0,"335559739":0,"335559740":240}}' style="font-size: 9pt; line-height: 14px; font-family: Book Antiqua, Book Antiqua_EmbeddedFont, Book Antiqua_MSFontService, serif;">&nbsp;</span></p>
                                </div>
                            </div>
                        </td>
                    </tr>
                    <tr class="TableRow SCXW140673802 BCX2" style="height: 5px;">
                        <td class="SCXW140673802 BCX2" data-celllook="4369" style="background-color: transparent; border-color: currentcolor currentcolor rgb(0, 0, 0) rgb(31, 73, 125); border-style: none solid solid; border-width: 0px 1px 1px 2px; border-image: none 100% / 1 / 0 stretch; vertical-align: middle; width: 227px;">
                            <div class="TableCellContent SCXW140673802 BCX2" style="padding: 0px 7px;">
                                <div class="OutlineElement Ltr  BCX2 SCXW140673802" style="direction: ltr;">
                                    <p class="Paragraph SCXW140673802 BCX2" style="font-weight: normal; font-style: normal; vertical-align: baseline; background-color: transparent; color: windowtext; text-align: left; margin-left: 0px; margin-right: 0px; padding-left: 0px; padding-right: 0px; text-indent: 0px;"><span class="TextRun SCXW140673802 BCX2" data-contrast="none" lang="EN-US" style="color: rgb(0, 0, 0); font-weight: bold; font-size: 11pt; font-family: Book Antiqua, Book Antiqua_EmbeddedFont, Book Antiqua_MSFontService, serif; line-height: 18.9px;"><span class="NormalTextRun SCXW140673802 BCX2" style="background-color: inherit;">Incident&nbsp;</span></span><span class="TextRun SCXW140673802 BCX2" data-contrast="auto" lang="EN-US" style="font-weight: bold; font-size: 11pt; font-family: Book Antiqua, Book Antiqua_EmbeddedFont, Book Antiqua_MSFontService, serif; line-height: 18.9px;"><span class="NormalTextRun SCXW140673802 BCX2" style="background-color: inherit;">Reported</span><span class="NormalTextRun SCXW140673802 BCX2" style="background-color: inherit;">&nbsp;</span></span><span class="TextRun SCXW140673802 BCX2" data-contrast="none" lang="EN-US" style="color: rgb(0, 0, 0); font-weight: bold; font-size: 11pt; font-family: Book Antiqua, Book Antiqua_EmbeddedFont, Book Antiqua_MSFontService, serif; line-height: 18.9px;"><span class="NormalTextRun SCXW140673802 BCX2" style="background-color: inherit;">Date/</span><span class="NormalTextRun ContextualSpellingAndGrammarErrorV2 SCXW140673802 BCX2" style="background-color: inherit;">Time:</span></span><span class="TextRun SCXW140673802 BCX2" data-contrast="none" lang="EN-US" style="color: rgb(255, 0, 0); font-weight: bold; font-size: 11pt; font-family: Book Antiqua, Book Antiqua_EmbeddedFont, Book Antiqua_MSFontService, serif; line-height: 18.9px;"><span class="NormalTextRun ContextualSpellingAndGrammarErrorV2 SCXW140673802 BCX2" style="background-color: inherit;">*</span></span><span class="EOP SCXW140673802 BCX2" data-ccp-props='{{"201341983":0,"335559739":0,"335559740":252}}' style="font-size: 11pt; line-height: 18.9px; font-family: Book Antiqua, Book Antiqua_EmbeddedFont, Book Antiqua_MSFontService, serif;">&nbsp;</span></p>
                                </div>
                            </div>
                        </td>
                        <td class="SCXW140673802 BCX2" data-celllook="4369" style="background-color: transparent; border-color: currentcolor rgb(31, 73, 125) rgb(0, 0, 0) currentcolor; border-style: none solid solid none; border-width: 0px 2px 1px 0px; border-image: none 100% / 1 / 0 stretch; vertical-align: middle; width: 189px;">
                            <div class="TableCellContent SCXW140673802 BCX2" style="padding: 0px;">
                                <div class="OutlineElement Ltr  BCX2 SCXW140673802" style="direction: ltr;">
                                    <p class="Paragraph SCXW140673802 BCX2" style="font-weight: normal; font-style: normal; vertical-align: baseline; background-color: transparent; color: windowtext; text-align: left; margin-left: 0px; margin-right: 0px; padding-left: 0px; padding-right: 0px; text-indent: 0px;"><span class="TextRun SCXW140673802 BCX2" data-contrast="none" lang="EN-US" style="color: rgb(0, 0, 0); font-size: 11pt; font-family: Calibri, Calibri_EmbeddedFont, Calibri_MSFontService, sans-serif; line-height: 18px;"><span class="NormalTextRun SCXW140673802 BCX2" style="background-color: inherit;">&nbsp;{var3}</span></span><span class="EOP SCXW140673802 BCX2" data-ccp-props='{{"201341983":0,"335559739":0,"335559740":240}}' style="font-size: 11pt; line-height: 18px; font-family: Calibri, Calibri_EmbeddedFont, Calibri_MSFontService, sans-serif;">&nbsp;</span></p>
                                </div>
                            </div>
                        </td>
                        <td class="SCXW140673802 BCX2" data-celllook="4369" style="background-color: transparent; border-color: currentcolor rgb(31, 73, 125) rgb(0, 0, 0) currentcolor; border-style: none solid solid none; border-width: 0px 2px 1px 0px; border-image: none 100% / 1 / 0 stretch; vertical-align: top; width: 217px;">
                            <div class="TableCellContent SCXW140673802 BCX2" style="padding: 0px;">
                                <div class="OutlineElement Ltr  BCX2 SCXW140673802" style="direction: ltr;">
                                    <p class="Paragraph SCXW140673802 BCX2" style="font-weight: normal; font-style: normal; vertical-align: baseline; background-color: transparent; color: windowtext; text-align: left; margin-left: 0px; margin-right: 0px; padding-left: 0px; padding-right: 0px; text-indent: 0px;"><span class="TextRun SCXW140673802 BCX2" data-contrast="none" lang="EN-US" style="color: rgb(0, 0, 0); font-size: 11pt; font-family: Book Antiqua, Book Antiqua_EmbeddedFont, Book Antiqua_MSFontService, serif; line-height: 18px;"><span class="NormalTextRun SCXW140673802 BCX2" style="background-color: inherit;">Resolution Date</span></span><span class="TextRun SCXW140673802 BCX2" data-contrast="none" lang="EN-US" style="color: rgb(31, 73, 125); font-size: 11pt; font-family: Book Antiqua, Book Antiqua_EmbeddedFont, Book Antiqua_MSFontService, serif; line-height: 18px;"><span class="NormalTextRun SCXW140673802 BCX2" style="background-color: inherit;">/</span></span><span class="TextRun SCXW140673802 BCX2" data-contrast="none" lang="EN-US" style="color: rgb(0, 0, 0); font-size: 11pt; font-family: Book Antiqua, Book Antiqua_EmbeddedFont, Book Antiqua_MSFontService, serif; line-height: 18px;"><span class="NormalTextRun SCXW140673802 BCX2" style="background-color: inherit;">Time</span></span><span class="EOP SCXW140673802 BCX2" data-ccp-props='{{"201341983":0,"335559739":0,"335559740":240}}' style="font-size: 11pt; line-height: 18px; font-family: Book Antiqua, Book Antiqua_EmbeddedFont, Book Antiqua_MSFontService, serif;">&nbsp;</span></p>
                                </div>
                            </div>
                        </td>
                        <td class="SCXW140673802 BCX2" colspan="2" data-celllook="4369" style="background-color: transparent; border-color: currentcolor rgb(31, 73, 125) rgb(0, 0, 0) currentcolor; border-style: none solid solid none; border-width: 0px 2px 1px 0px; border-image: none 100% / 1 / 0 stretch; vertical-align: middle; width: 170px;">
                            <div class="TableCellContent SCXW140673802 BCX2" style="padding: 0px;">
                                <div class="OutlineElement Ltr  BCX2 SCXW140673802" style="direction: ltr;">
                                    <p class="Paragraph SCXW140673802 BCX2" style="font-weight: normal; font-style: normal; vertical-align: baseline; background-color: transparent; color: windowtext; text-align: center; margin-left: 0px; margin-right: 0px; padding-left: 0px; padding-right: 0px; text-indent: 0px;"><span class="EOP SCXW140673802 BCX2" data-ccp-props='{{"201341983":0,"335551550":2,"335551620":2,"335559739":0,"335559740":240}}' style="font-size: 11pt; line-height: 18px; font-family: Calibri, Calibri_EmbeddedFont, Calibri_MSFontService, sans-serif;">&nbsp;</span></p>
                                </div>
                            </div>
                        </td>
                    </tr>
                    <tr class="TableRow SCXW140673802 BCX2" style="height: 5px;">
                        <td class="SCXW140673802 BCX2" data-celllook="4369" style="background-color: transparent; border-color: currentcolor currentcolor rgb(0, 0, 0) rgb(31, 73, 125); border-style: none solid solid; border-width: 0px 1px 1px 2px; border-image: none 100% / 1 / 0 stretch; vertical-align: middle; width: 227px;">
                            <div class="TableCellContent SCXW140673802 BCX2" style="padding: 0px 7px;">
                                <div class="OutlineElement Ltr  BCX2 SCXW140673802" style="direction: ltr;">
                                    <p class="Paragraph SCXW140673802 BCX2" style="font-weight: normal; font-style: normal; vertical-align: baseline; background-color: transparent; color: windowtext; text-align: left; margin-left: 0px; margin-right: 0px; padding-left: 0px; padding-right: 0px; text-indent: 0px;"><span class="TextRun SCXW140673802 BCX2" data-contrast="none" lang="EN-US" style="color: rgb(0, 0, 0); font-weight: bold; font-size: 11pt; font-family: Book Antiqua, Book Antiqua_EmbeddedFont, Book Antiqua_MSFontService, serif; line-height: 18.9px;"><span class="NormalTextRun SCXW140673802 BCX2" style="background-color: inherit;">Customer Impact Start Date/Time: (if known)</span></span><span class="EOP SCXW140673802 BCX2" data-ccp-props='{{"201341983":0,"335559739":0,"335559740":252}}' style="font-size: 11pt; line-height: 18.9px; font-family: Book Antiqua, Book Antiqua_EmbeddedFont, Book Antiqua_MSFontService, serif;">&nbsp;</span></p>
                                </div>
                            </div>
                        </td>
                        <td class="SCXW140673802 BCX2" data-celllook="4369" style="background-color: transparent; border-color: currentcolor rgb(31, 73, 125) rgb(0, 0, 0) currentcolor; border-style: none solid solid none; border-width: 0px 2px 1px 0px; border-image: none 100% / 1 / 0 stretch; vertical-align: middle; width: 189px;">
                            <div class="TableCellContent SCXW140673802 BCX2" style="padding: 0px;">
                                <div class="OutlineElement Ltr  BCX2 SCXW140673802" style="direction: ltr;">
                                    <p class="Paragraph SCXW140673802 BCX2" style="font-weight: normal; font-style: normal; vertical-align: baseline; background-color: transparent; color: windowtext; text-align: left; margin-left: 0px; margin-right: 0px; padding-left: 0px; padding-right: 0px; text-indent: 0px;"><span class="EOP SCXW140673802 BCX2" data-ccp-props='{{"201341983":0,"335559739":0,"335559740":240}}' style="font-size: 11pt; line-height: 18px; font-family: Calibri, Calibri_EmbeddedFont, Calibri_MSFontService, sans-serif;">&nbsp;</span></p>
                                </div>
                            </div>
                        </td>
                        <td class="SCXW140673802 BCX2" data-celllook="4369" style="background-color: transparent; border-color: currentcolor rgb(31, 73, 125) rgb(0, 0, 0) currentcolor; border-style: none solid solid none; border-width: 0px 2px 1px 0px; border-image: none 100% / 1 / 0 stretch; vertical-align: top; width: 217px;">
                            <div class="TableCellContent SCXW140673802 BCX2" style="padding: 0px;">
                                <div class="OutlineElement Ltr  BCX2 SCXW140673802" style="direction: ltr;">
                                    <p class="Paragraph SCXW140673802 BCX2" style="font-weight: normal; font-style: normal; vertical-align: baseline; background-color: transparent; color: windowtext; text-align: left; margin-left: 0px; margin-right: 0px; padding-left: 0px; padding-right: 0px; text-indent: 0px;"><span class="TextRun SCXW140673802 BCX2" data-contrast="none" lang="EN-US" style="color: rgb(0, 0, 0); font-size: 11pt; font-family: Book Antiqua, Book Antiqua_EmbeddedFont, Book Antiqua_MSFontService, serif; line-height: 18px;"><span class="NormalTextRun SCXW140673802 BCX2" style="background-color: inherit;">Customer Impact Resolution&nbsp;</span></span><span class="TextRun SCXW140673802 BCX2" data-contrast="none" lang="EN-US" style="color: rgb(0, 0, 0); font-size: 8pt; font-family: Book Antiqua, Book Antiqua_EmbeddedFont, Book Antiqua_MSFontService, serif; line-height: 13px;"><span class="NormalTextRun SCXW140673802 BCX2" style="background-color: inherit;">(if different)</span></span><span class="EOP SCXW140673802 BCX2" data-ccp-props='{{"201341983":0,"335559739":0,"335559740":240}}' style="font-size: 8pt; line-height: 13px; font-family: Book Antiqua, Book Antiqua_EmbeddedFont, Book Antiqua_MSFontService, serif;">&nbsp;</span></p>
                                </div>
                            </div>
                        </td>
                        <td class="SCXW140673802 BCX2" colspan="2" data-celllook="4369" style="background-color: transparent; border-color: currentcolor rgb(31, 73, 125) rgb(0, 0, 0) currentcolor; border-style: none solid solid none; border-width: 0px 2px 1px 0px; border-image: none 100% / 1 / 0 stretch; vertical-align: middle; width: 170px;">
                            <div class="TableCellContent SCXW140673802 BCX2" style="padding: 0px;">
                                <div class="OutlineElement Ltr  BCX2 SCXW140673802" style="direction: ltr;">
                                    <p class="Paragraph SCXW140673802 BCX2" style="font-weight: normal; font-style: normal; vertical-align: baseline; background-color: transparent; color: windowtext; text-align: center; margin-left: 0px; margin-right: 0px; padding-left: 0px; padding-right: 0px; text-indent: 0px;"><span class="EOP SCXW140673802 BCX2" data-ccp-props='{{"201341983":0,"335551550":2,"335551620":2,"335559739":0,"335559740":240}}' style="font-size: 11pt; line-height: 18px; font-family: Calibri, Calibri_EmbeddedFont, Calibri_MSFontService, sans-serif;">&nbsp;</span></p>
                                </div>
                            </div>
                        </td>
                    </tr>
                    <tr class="TableRow SCXW140673802 BCX2" style="height: 5px;">
                        <td class="SCXW140673802 BCX2" data-celllook="4369" style="background-color: transparent; border-color: currentcolor currentcolor rgb(0, 0, 0) rgb(31, 73, 125); border-style: none solid solid; border-width: 0px 1px 1px 2px; border-image: none 100% / 1 / 0 stretch; vertical-align: middle; width: 227px;">
                            <div class="TableCellContent SCXW140673802 BCX2" style="padding: 0px 7px;">
                                <div class="OutlineElement Ltr  BCX2 SCXW140673802" style="direction: ltr;">
                                    <p class="Paragraph SCXW140673802 BCX2" style="font-weight: normal; font-style: normal; vertical-align: baseline; background-color: transparent; color: windowtext; text-align: left; margin-left: 0px; margin-right: 0px; padding-left: 0px; padding-right: 0px; text-indent: 0px;"><span class="TextRun SCXW140673802 BCX2" data-contrast="none" lang="EN-US" style="color: rgb(0, 0, 0); font-weight: bold; font-size: 11pt; font-family: Book Antiqua, Book Antiqua_EmbeddedFont, Book Antiqua_MSFontService, serif; line-height: 18.9px;"><span class="NormalTextRun SCXW140673802 BCX2" style="background-color: inherit;">Incident ID #</span><span class="NormalTextRun SCXW140673802 BCX2" style="background-color: inherit;">&nbsp;</span></span><span class="TextRun SCXW140673802 BCX2" data-contrast="auto" lang="EN-US" style="font-weight: bold; font-size: 11pt; font-family: Book Antiqua, Book Antiqua_EmbeddedFont, Book Antiqua_MSFontService, serif; line-height: 18.9px;"><span class="NormalTextRun SCXW140673802 BCX2" style="background-color: inherit;">(if available)</span></span><span class="EOP SCXW140673802 BCX2" data-ccp-props='{{"201341983":0,"335559739":0,"335559740":252}}' style="font-size: 11pt; line-height: 18.9px; font-family: Book Antiqua, Book Antiqua_EmbeddedFont, Book Antiqua_MSFontService, serif;">&nbsp;</span></p>
                                </div>
                            </div>
                        </td>
                        <td class="SCXW140673802 BCX2" colspan="4" data-celllook="4369" style="background-color: transparent; border-color: currentcolor rgb(31, 73, 125) rgb(0, 0, 0) currentcolor; border-style: none solid solid none; border-width: 0px 2px 1px 0px; border-image: none 100% / 1 / 0 stretch; vertical-align: top; width: 577px;">
                            <div class="TableCellContent SCXW140673802 BCX2" style="padding: 0px;">
                                <div class="OutlineElement Ltr  BCX2 SCXW140673802" style="direction: ltr;">
                                    <p class="Paragraph SCXW140673802 BCX2" style="font-weight: normal; font-style: normal; vertical-align: baseline; background-color: transparent; color: windowtext; text-align: left; margin-left: 0px; margin-right: 0px; padding-left: 0px; padding-right: 0px; text-indent: 0px;"><span class="EOP SCXW140673802 BCX2" data-ccp-props='{{"201341983":0,"335559739":0,"335559740":240}}' style="font-size: 11pt; line-height: 18px; font-family: Book Antiqua, Book Antiqua_EmbeddedFont, Book Antiqua_MSFontService, serif;">&nbsp;</span></p>
                                </div>
                            </div>
                        </td>
                    </tr>
                    <tr class="TableRow SCXW140673802 BCX2" style="height: 11px;">
                        <td class="SCXW140673802 BCX2" data-celllook="4369" style="background-color: transparent; border-color: currentcolor currentcolor rgb(0, 0, 0) rgb(31, 73, 125); border-style: none solid solid; border-width: 0px 1px 1px 2px; border-image: none 100% / 1 / 0 stretch; vertical-align: middle; width: 227px;">
                            <div class="TableCellContent SCXW140673802 BCX2" style="padding: 0px 7px;">
                                <div class="OutlineElement Ltr  BCX2 SCXW140673802" style="direction: ltr;">
                                    <p class="Paragraph SCXW140673802 BCX2" style="font-weight: normal; font-style: normal; vertical-align: baseline; background-color: transparent; color: windowtext; text-align: left; margin-left: 0px; margin-right: 0px; padding-left: 0px; padding-right: 0px; text-indent: 0px;"><span class="TextRun SCXW140673802 BCX2" data-contrast="none" lang="EN-US" style="color: rgb(0, 0, 0); font-weight: bold; font-size: 11pt; font-family: Book Antiqua, Book Antiqua_EmbeddedFont, Book Antiqua_MSFontService, serif; line-height: 18.9px;"><span class="NormalTextRun SCXW140673802 BCX2" style="background-color: inherit;">Reported By:</span></span><span class="EOP SCXW140673802 BCX2" data-ccp-props='{{"201341983":0,"335559739":0,"335559740":252}}' style="font-size: 11pt; line-height: 18.9px; font-family: Book Antiqua, Book Antiqua_EmbeddedFont, Book Antiqua_MSFontService, serif;">&nbsp;</span></p>
                                </div>
                            </div>
                        </td>
                        <td class="SCXW140673802 BCX2" colspan="4" data-celllook="4369" style="background-color: transparent; border-color: currentcolor rgb(31, 73, 125) rgb(0, 0, 0) currentcolor; border-style: none solid solid none; border-width: 0px 2px 1px 0px; border-image: none 100% / 1 / 0 stretch; vertical-align: top; width: 577px;">
                            <div class="TableCellContent SCXW140673802 BCX2" style="padding: 0px;">
                                <div class="OutlineElement Ltr  BCX2 SCXW140673802" style="direction: ltr;">
                                    <p class="Paragraph SCXW140673802 BCX2" style="font-weight: normal; font-style: normal; vertical-align: baseline; background-color: transparent; color: windowtext; text-align: left; margin-left: 0px; margin-right: 0px; padding-left: 0px; padding-right: 0px; text-indent: 0px;"><span class="EOP SCXW140673802 BCX2" data-ccp-props='{{"201341983":0,"335559739":0,"335559740":240}}' style="font-size: 11pt; line-height: 18px; font-family: Calibri, Calibri_EmbeddedFont, Calibri_MSFontService, sans-serif;">&nbsp;</span></p>
                                </div>
                            </div>
                        </td>
                    </tr>
                    <tr class="TableRow SCXW140673802 BCX2" style="height: 31px;">
                        <td class="SCXW140673802 BCX2" colspan="2" data-celllook="69905" style="background-color: rgb(141, 180, 226); border-color: currentcolor rgb(31, 78, 121) rgb(31, 78, 121) rgb(31, 73, 125); border-style: none solid solid; border-width: 0px 2px 2px; border-image: none 100% / 1 / 0 stretch; vertical-align: middle; width: 417px;">
                            <div class="TableCellContent SCXW140673802 BCX2" style="padding: 0px 7px;">
                                <div class="OutlineElement Ltr  BCX2 SCXW140673802" style="direction: ltr;">
                                    <p class="Paragraph SCXW140673802 BCX2" style="font-weight: normal; font-style: normal; vertical-align: baseline; background-color: transparent; color: windowtext; text-align: left; margin-left: 0px; margin-right: 0px; padding-left: 0px; padding-right: 0px; text-indent: 0px;"><span class="TextRun SCXW140673802 BCX2" data-contrast="auto" lang="EN-US" style="font-weight: bold; font-size: 11pt; font-family: Book Antiqua, Book Antiqua_EmbeddedFont, Book Antiqua_MSFontService, serif; line-height: 18.9px;"><span class="NormalTextRun SCXW140673802 BCX2" style="background-color: inherit;">Bridge/</span></span><span class="TextRun SCXW140673802 BCX2" data-contrast="none" lang="EN-US" style="color: rgb(0, 0, 0); font-weight: bold; font-size: 11pt; font-family: Book Antiqua, Book Antiqua_EmbeddedFont, Book Antiqua_MSFontService, serif; line-height: 18.9px;"><span class="NormalTextRun SCXW140673802 BCX2" style="background-color: inherit;">Incident Manager</span><span class="NormalTextRun SCXW140673802 BCX2" style="background-color: inherit;">&nbsp;</span><span class="NormalTextRun SCXW140673802 BCX2" style="background-color: inherit;">(IM) Details</span></span><span class="EOP SCXW140673802 BCX2" data-ccp-props='{{"201341983":0,"335559739":0,"335559740":252}}' style="font-size: 11pt; line-height: 18.9px; font-family: Book Antiqua, Book Antiqua_EmbeddedFont, Book Antiqua_MSFontService, serif;">&nbsp;</span></p>
                                </div>
                            </div>
                        </td>
                        <td class="SCXW140673802 BCX2" colspan="3" data-celllook="69905" style="background-color: rgb(141, 180, 226); border-color: currentcolor rgb(31, 73, 125) currentcolor currentcolor; border-style: none solid solid none; border-width: 0px 2px 1px 0px; border-image: none 100% / 1 / 0 stretch; vertical-align: middle; width: 387px;">
                            <div class="TableCellContent SCXW140673802 BCX2" style="padding: 0px 7px;">
                                <div class="OutlineElement Ltr  BCX2 SCXW140673802" style="direction: ltr;">
                                    <p class="Paragraph SCXW140673802 BCX2" style="font-weight: normal; font-style: normal; vertical-align: baseline; background-color: transparent; color: windowtext; text-align: left; margin-left: 0px; margin-right: 0px; padding-left: 0px; padding-right: 0px; text-indent: 0px;"><span class="TextRun SCXW140673802 BCX2" data-contrast="none" lang="EN-US" style="color: rgb(0, 0, 0); font-weight: bold; font-size: 11pt; font-family: Book Antiqua, Book Antiqua_EmbeddedFont, Book Antiqua_MSFontService, serif; line-height: 18.9px;"><span class="NormalTextRun SCXW140673802 BCX2" style="background-color: inherit;">Resources/Technology Details</span></span><span class="EOP SCXW140673802 BCX2" data-ccp-props='{{"201341983":0,"335559739":0,"335559740":252}}' style="font-size: 11pt; line-height: 18.9px; font-family: Book Antiqua, Book Antiqua_EmbeddedFont, Book Antiqua_MSFontService, serif;">&nbsp;</span></p>
                                </div>
                            </div>
                        </td>
                    </tr>
                    <tr class="TableRow SCXW140673802 BCX2" style="height: 19px;">
                        <td class="SCXW140673802 BCX2" colspan="2" data-celllook="4369" style="background-color: transparent; border-color: currentcolor currentcolor currentcolor rgb(31, 73, 125); border-style: none solid solid; border-width: 0px 1px 1px 2px; border-image: none 100% / 1 / 0 stretch; vertical-align: top; width: 417px;">
                            <div class="TableCellContent SCXW140673802 BCX2" style="padding: 0px 7px;">
                                <div class="OutlineElement Ltr  BCX2 SCXW140673802" style="direction: ltr;">
                                    <p class="Paragraph SCXW140673802 BCX2" style="font-weight: normal; font-style: normal; vertical-align: baseline; background-color: transparent; color: windowtext; text-align: left; margin-left: 0px; margin-right: 0px; padding-left: 0px; padding-right: 0px; text-indent: 0px;"><span class="EOP SCXW140673802 BCX2" data-ccp-props='{{"201341983":0,"335559739":0,"335559740":240}}' style="font-size: 11pt; line-height: 18px; font-family: Calibri, Calibri_EmbeddedFont, Calibri_MSFontService, sans-serif;">&nbsp;</span></p>
                                </div>
                            </div>
                        </td>
                        <td class="SCXW140673802 BCX2" colspan="2" data-celllook="0" style="background-color: transparent; border: 0px none; vertical-align: bottom; width: 226px;">
                            <div class="TableCellContent SCXW140673802 BCX2" style="padding: 0px 7px;">
                                <div class="OutlineElement Ltr  BCX2 SCXW140673802" style="direction: ltr;">
                                    <p class="Paragraph SCXW140673802 BCX2" style="font-weight: normal; font-style: normal; vertical-align: baseline; background-color: transparent; color: windowtext; text-align: left; margin-left: 0px; margin-right: 0px; padding-left: 0px; padding-right: 0px; text-indent: 0px;"><span class="TextRun SCXW140673802 BCX2" data-contrast="none" lang="EN-US" style="color: rgb(0, 0, 0); font-size: 12pt; font-family: Times New Roman, Times New Roman_EmbeddedFont, Times New Roman_MSFontService, serif; line-height: 19px;"><span class="NormalTextRun SCXW140673802 BCX2" style="background-color: inherit;">Service</span></span><span class="EOP SCXW140673802 BCX2" data-ccp-props='{{"201341983":0,"335559739":0,"335559740":240}}' style="font-size: 12pt; line-height: 19px; font-family: Times New Roman, Times New Roman_EmbeddedFont, Times New Roman_MSFontService, serif;">&nbsp;</span></p>
                                </div>
                            </div>
                        </td>
                        <td class="SCXW140673802 BCX2" data-celllook="4369" style="background-color: transparent; border-color: currentcolor rgb(31, 73, 125) currentcolor currentcolor; border-style: none solid solid; border-width: 0px 2px 1px 1px; border-image: none 100% / 1 / 0 stretch; vertical-align: middle; width: 161px;">
                            <div class="TableCellContent SCXW140673802 BCX2" style="padding: 0px 7px;">
                                <div class="OutlineElement Ltr  BCX2 SCXW140673802" style="direction: ltr;">
                                    <p class="Paragraph SCXW140673802 BCX2" style="font-weight: normal; font-style: normal; vertical-align: baseline; background-color: transparent; color: windowtext; text-align: center; margin-left: 0px; margin-right: 0px; padding-left: 0px; padding-right: 0px; text-indent: 0px;"><span class="TextRun SCXW140673802 BCX2" data-contrast="none" lang="EN-US" style="color: rgb(0, 0, 0); font-size: 11pt; font-family: Calibri, Calibri_EmbeddedFont, Calibri_MSFontService, sans-serif; line-height: 18px;"><span class="NormalTextRun SCXW140673802 BCX2" style="background-color: inherit;">&nbsp;</span></span><span class="EOP SCXW140673802 BCX2" data-ccp-props='{{"201341983":0,"335551550":2,"335551620":2,"335559739":0,"335559740":240}}' style="font-size: 11pt; line-height: 18px; font-family: Calibri, Calibri_EmbeddedFont, Calibri_MSFontService, sans-serif;">&nbsp;</span></p>
                                </div>
                            </div>
                        </td>
                    </tr>
                    <tr class="TableRow SCXW140673802 BCX2" style="height: 41px;">
                        <td class="SCXW140673802 BCX2" data-celllook="4369" style="background-color: transparent; border-color: currentcolor currentcolor currentcolor rgb(31, 73, 125); border-style: none solid solid; border-width: 0px 1px 1px 2px; border-image: none 100% / 1 / 0 stretch; vertical-align: bottom; width: 227px;">
                            <div class="TableCellContent SCXW140673802 BCX2" style="padding: 0px 7px;">
                                <div class="OutlineElement Ltr  BCX2 SCXW140673802" style="direction: ltr;">
                                    <p class="Paragraph SCXW140673802 BCX2" style="font-weight: normal; font-style: normal; vertical-align: baseline; background-color: transparent; color: windowtext; text-align: left; margin-left: 0px; margin-right: 0px; padding-left: 0px; padding-right: 0px; text-indent: 0px;"><span class="TextRun SCXW140673802 BCX2" data-contrast="none" lang="EN-US" style="color: rgb(0, 0, 0); font-size: 11pt; font-family: Book Antiqua, Book Antiqua_EmbeddedFont, Book Antiqua_MSFontService, serif; line-height: 18.9px;"><span class="NormalTextRun SCXW140673802 BCX2" style="background-color: inherit;">Email ID</span></span><span class="EOP SCXW140673802 BCX2" data-ccp-props='{{"201341983":0,"335559739":0,"335559740":252}}' style="font-size: 11pt; line-height: 18.9px; font-family: Book Antiqua, Book Antiqua_EmbeddedFont, Book Antiqua_MSFontService, serif;">&nbsp;</span></p>
                                </div>
                            </div>
                        </td>
                        <td class="SCXW140673802 BCX2" data-celllook="4369" style="background-color: transparent; border-color: currentcolor; border-style: none solid solid none; border-width: 0px 1px 1px 0px; border-image: none 100% / 1 / 0 stretch; vertical-align: bottom; width: 189px;">
                            <div class="TableCellContent SCXW140673802 BCX2" style="padding: 0px 7px;">
                                <div class="OutlineElement Ltr  BCX2 SCXW140673802" style="direction: ltr;">
                                    <p class="Paragraph SCXW140673802 BCX2" style="font-weight: normal; font-style: normal; vertical-align: baseline; background-color: transparent; color: windowtext; text-align: justify; margin-left: 0px; margin-right: 0px; padding-left: 0px; padding-right: 0px; text-indent: 0px;"><span class="TextRun SCXW140673802 BCX2" data-contrast="none" lang="EN-US" style="color: rgb(0, 0, 0); font-size: 11pt; font-family: Calibri, Calibri_EmbeddedFont, Calibri_MSFontService, sans-serif; line-height: 18.9px;"><span class="NormalTextRun SCXW140673802 BCX2" style="background-color: inherit;">n/a</span></span><span class="EOP SCXW140673802 BCX2" data-ccp-props='{{"201341983":0,"335551550":6,"335551620":6,"335559739":0,"335559740":252}}' style="font-size: 11pt; line-height: 18.9px; font-family: Calibri, Calibri_EmbeddedFont, Calibri_MSFontService, sans-serif;">&nbsp;</span></p>
                                </div>
                            </div>
                        </td>
                        <td class="SCXW140673802 BCX2" colspan="2" data-celllook="4369" style="background-color: transparent; border-color: currentcolor currentcolor rgb(31, 78, 121); border-style: solid solid solid none; border-width: 1px 1px 2px 0px; border-image: none 100% / 1 / 0 stretch; vertical-align: bottom; width: 226px;">
                            <div class="TableCellContent SCXW140673802 BCX2" style="padding: 0px 7px;">
                                <div class="OutlineElement Ltr  BCX2 SCXW140673802" style="direction: ltr;">
                                    <p class="Paragraph SCXW140673802 BCX2" style="font-weight: normal; font-style: normal; vertical-align: baseline; background-color: transparent; color: windowtext; text-align: left; margin-left: 0px; margin-right: 0px; padding-left: 0px; padding-right: 0px; text-indent: 0px;"><span class="TextRun SCXW140673802 BCX2" data-contrast="none" lang="EN-US" style="color: rgb(0, 0, 0); font-size: 11pt; font-family: Book Antiqua, Book Antiqua_EmbeddedFont, Book Antiqua_MSFontService, serif; line-height: 18.9px;"><span class="NormalTextRun SCXW140673802 BCX2" style="background-color: inherit;">Team/Engineer</span></span><span class="EOP SCXW140673802 BCX2" data-ccp-props='{{"201341983":0,"335559739":0,"335559740":252}}' style="font-size: 11pt; line-height: 18.9px; font-family: Book Antiqua, Book Antiqua_EmbeddedFont, Book Antiqua_MSFontService, serif;">&nbsp;</span></p>
                                </div>
                            </div>
                        </td>
                        <td class="SCXW140673802 BCX2" data-celllook="4369" style="background-color: transparent; border-color: currentcolor rgb(31, 73, 125) rgb(31, 78, 121) currentcolor; border-style: none solid solid none; border-width: 0px 2px 2px 0px; border-image: none 100% / 1 / 0 stretch; vertical-align: middle; width: 161px;">
                            <div class="TableCellContent SCXW140673802 BCX2" style="padding: 0px 7px;">
                                <div class="OutlineElement Ltr  BCX2 SCXW140673802" style="direction: ltr;">
                                    <p class="Paragraph SCXW140673802 BCX2" style="font-weight: normal; font-style: normal; vertical-align: baseline; background-color: transparent; color: windowtext; text-align: center; margin-left: 0px; margin-right: 0px; padding-left: 0px; padding-right: 0px; text-indent: 0px;"><span class="EOP SCXW140673802 BCX2" data-ccp-props='{{"201341983":0,"335551550":2,"335551620":2,"335559739":0,"335559740":240}}' style="font-size: 11pt; line-height: 18px; font-family: Calibri, Calibri_EmbeddedFont, Calibri_MSFontService, sans-serif;">&nbsp;</span></p>
                                </div>
                            </div>
                        </td>
                    </tr>
                    <tr class="TableRow SCXW140673802 BCX2" style="height: 45px;">
                        <td class="SCXW140673802 BCX2" colspan="2" data-celllook="4369" style="background-color: transparent; border-color: currentcolor currentcolor rgb(31, 78, 121) rgb(31, 73, 125); border-style: none solid solid; border-width: 0px 1px 2px 2px; border-image: none 100% / 1 / 0 stretch; vertical-align: bottom; width: 417px;">
                            <div class="TableCellContent SCXW140673802 BCX2" style="padding: 0px 7px;">
                                <div class="OutlineElement Ltr  BCX2 SCXW140673802" style="direction: ltr;">
                                    <p class="Paragraph SCXW140673802 BCX2" style="font-weight: normal; font-style: normal; vertical-align: baseline; background-color: transparent; color: windowtext; text-align: left; margin-left: 0px; margin-right: 0px; padding-left: 0px; padding-right: 0px; text-indent: 0px;"><span class="TextRun SCXW140673802 BCX2" data-contrast="none" lang="EN-US" style="color: rgb(0, 0, 0); font-size: 11pt; font-family: Book Antiqua, Book Antiqua_EmbeddedFont, Book Antiqua_MSFontService, serif; line-height: 18px;"><span class="NormalTextRun SCXW140673802 BCX2" style="background-color: inherit;">Slack&nbsp;</span><span class="NormalTextRun ContextualSpellingAndGrammarErrorV2 SCXW140673802 BCX2" style="background-color: inherit;">Subchannel</span><span class="NormalTextRun ContextualSpellingAndGrammarErrorV2 SCXW140673802 BCX2" style="background-color: inherit;">:</span></span><span class="TextRun SCXW140673802 BCX2" data-contrast="none" lang="EN-US" style="color: rgb(255, 0, 0); font-weight: bold; font-size: 11pt; font-family: Book Antiqua, Book Antiqua_EmbeddedFont, Book Antiqua_MSFontService, serif; line-height: 18px;"><span class="NormalTextRun ContextualSpellingAndGrammarErrorV2 SCXW140673802 BCX2" style="background-color: inherit;">*</span></span><span class="TextRun SCXW140673802 BCX2" data-contrast="none" lang="EN-US" style="color: rgb(0, 0, 0); font-size: 11pt; font-family: Book Antiqua, Book Antiqua_EmbeddedFont, Book Antiqua_MSFontService, serif; line-height: 18px;"><span class="NormalTextRun SCXW140673802 BCX2" style="background-color: inherit;">&nbsp;</span><span class="NormalTextRun SCXW140673802 BCX2" style="background-color: inherit;">{var4}</span></span><span class="EOP SCXW140673802 BCX2" data-ccp-props='{{"201341983":0,"335559739":0,"335559740":240}}' style="font-size: 11pt; line-height: 18px; font-family: Book Antiqua, Book Antiqua_EmbeddedFont, Book Antiqua_MSFontService, serif;">&nbsp;</span></p>
                                </div>
                            </div>
                        </td>
                        <td class="SCXW140673802 BCX2" colspan="2" data-celllook="4369" style="background-color: transparent; border-color: currentcolor currentcolor rgb(31, 78, 121); border-style: none solid solid none; border-width: 0px 1px 2px 0px; border-image: none 100% / 1 / 0 stretch; vertical-align: bottom; width: 226px;">
                            <div class="TableCellContent SCXW140673802 BCX2" style="padding: 0px;">
                                <div class="OutlineElement Ltr  BCX2 SCXW140673802" style="direction: ltr;">
                                    <p class="Paragraph SCXW140673802 BCX2" style="font-weight: normal; font-style: normal; vertical-align: baseline; background-color: transparent; color: windowtext; text-align: left; margin-left: 0px; margin-right: 0px; padding-left: 0px; padding-right: 0px; text-indent: 0px;"><span class="TextRun SCXW140673802 BCX2" data-contrast="none" lang="EN-US" style="color: rgb(0, 0, 0); font-size: 11pt; font-family: Book Antiqua, Book Antiqua_EmbeddedFont, Book Antiqua_MSFontService, serif; line-height: 18px;"><span class="NormalTextRun SCXW140673802 BCX2" style="background-color: inherit;">&nbsp;&nbsp;</span><span class="NormalTextRun SCXW140673802 BCX2" style="background-color: inherit;">Business/System Owner</span></span><span class="EOP SCXW140673802 BCX2" data-ccp-props='{{"201341983":0,"335559739":0,"335559740":240}}' style="font-size: 11pt; line-height: 18px; font-family: Book Antiqua, Book Antiqua_EmbeddedFont, Book Antiqua_MSFontService, serif;">&nbsp;</span></p>
                                </div>
                            </div>
                        </td>
                        <td class="SCXW140673802 BCX2" data-celllook="4369" style="background-color: transparent; border-color: currentcolor rgb(31, 73, 125) rgb(31, 78, 121) currentcolor; border-style: none solid solid none; border-width: 0px 2px 2px 0px; border-image: none 100% / 1 / 0 stretch; vertical-align: bottom; width: 161px;">
                            <div class="TableCellContent SCXW140673802 BCX2" style="padding: 0px;">
                                <div class="OutlineElement Ltr  BCX2 SCXW140673802" style="direction: ltr;">
                                    <p class="Paragraph SCXW140673802 BCX2" style="font-weight: normal; font-style: normal; vertical-align: baseline; background-color: transparent; color: windowtext; text-align: center; margin-left: 0px; margin-right: 0px; padding-left: 0px; padding-right: 0px; text-indent: 0px;"><span class="EOP SCXW140673802 BCX2" data-ccp-props='{{"201341983":0,"335551550":2,"335551620":2,"335559739":0,"335559740":240}}' style="font-size: 11pt; line-height: 18px; font-family: Calibri, Calibri_EmbeddedFont, Calibri_MSFontService, sans-serif;">&nbsp;</span></p>
                                </div>
                            </div>
                        </td>
                    </tr>
                    <tr class="TableRow SCXW140673802 BCX2" style="height: 84px;">
                        <td class="SCXW140673802 BCX2" colspan="5" data-celllook="69905" style="background-color: rgb(142, 170, 219); border-color: currentcolor rgb(31, 78, 121) rgb(31, 78, 121); border-style: none solid solid; border-width: 0px 2px 2px; border-image: none 100% / 1 / 0 stretch; vertical-align: top; width: 805px;">
                            <div class="TableCellContent SCXW140673802 BCX2" style="padding: 0px 7px;">
                                <div class="OutlineElement Ltr  BCX2 SCXW140673802" style="direction: ltr;">
                                    <p class="Paragraph SCXW140673802 BCX2" style="font-weight: normal; font-style: normal; vertical-align: baseline; background-color: transparent; color: windowtext; text-align: left; margin-left: 0px; margin-right: 0px; padding-left: 0px; padding-right: 0px; text-indent: 0px;"><span class="TextRun Underlined SCXW140673802 BCX2" data-contrast="none" lang="EN-US" style="color: rgb(0, 0, 0); font-weight: bold; text-decoration: underline; font-size: 11pt; font-family: Book Antiqua, Book Antiqua_EmbeddedFont, Book Antiqua_MSFontService, serif; line-height: 18.9px;"><span class="NormalTextRun SCXW140673802 BCX2" style="background-color: inherit;">Issue Description (and u</span><span class="NormalTextRun SCXW140673802 BCX2" style="background-color: inherit;">pdates</span><span class="NormalTextRun SCXW140673802 BCX2" style="background-color: inherit;">)</span><span class="NormalTextRun SCXW140673802 BCX2" style="background-color: inherit;">:</span></span><span class="EOP SCXW140673802 BCX2" data-ccp-props='{{"201341983":0,"335559739":0,"335559740":252}}' style="font-size: 11pt; line-height: 18.9px; font-family: Book Antiqua, Book Antiqua_EmbeddedFont, Book Antiqua_MSFontService, serif;">&nbsp;</span></p>
                                </div>
                                <div class="OutlineElement Ltr  BCX2 SCXW140673802" style="direction: ltr;">
                                    <p class="Paragraph SCXW140673802 BCX2" style="font-weight: normal; font-style: normal; vertical-align: baseline; background-color: transparent; color: windowtext; text-align: left; margin-left: 24px; margin-right: 0px; padding-left: 0px; padding-right: 0px; text-indent: 0px;"><span class="EOP SCXW140673802 BCX2" data-ccp-props='{{"201341983":0,"335559685":360,"335559739":0,"335559740":252}}' style="font-size: 9pt; line-height: 14.7px; font-family: Calibri, Calibri_EmbeddedFont, Calibri_MSFontService, sans-serif;">&nbsp;</span></p>
                                </div>
                                <div class="OutlineElement Ltr  BCX2 SCXW140673802" style="direction: ltr;">
                                    <p class="Paragraph SCXW140673802 BCX2" style="font-weight: normal; font-style: normal; vertical-align: baseline; background-color: transparent; color: windowtext; text-align: left; margin-left: 0px; margin-right: 0px; padding-left: 0px; padding-right: 0px; text-indent: 0px;"><span class="TextRun SCXW140673802 BCX2" data-contrast="auto" lang="EN-US" style="font-style: italic; font-size: 9pt; font-family: Calibri, Calibri_EmbeddedFont, Calibri_MSFontService, sans-serif; line-height: 14.7px;"><span class="NormalTextRun SCXW140673802 BCX2" style="background-color: inherit; color: rgb(0, 0, 0);">Initial report:</span></span><span class="EOP SCXW140673802 BCX2" data-ccp-props='{{"201341983":0,"335559739":0,"335559740":252}}' style="font-size: 9pt; line-height: 14.7px; font-family: Calibri, Calibri_EmbeddedFont, Calibri_MSFontService, sans-serif; color: rgb(0, 0, 0);">&nbsp;</span></p>
                                </div>
                                <div class="ListContainerWrapper SCXW140673802 BCX2">
                                    <ul>
                                        <li class="Paragraph SCXW140673802 BCX2" style="font-weight: normal; font-style: normal; vertical-align: baseline; background-color: transparent; color: windowtext; text-align: left; padding-left: 0px; padding-right: 0px; text-indent: 0px;"><span class="TextRun SCXW140673802 BCX2" data-contrast="none" lang="EN-US" style="color: rgb(0, 0, 0); font-size: 11pt; font-family: Calibri, Calibri_EmbeddedFont, Calibri_MSFontService, sans-serif; line-height: 18.9px;"><span class="NormalTextRun SCXW140673802 BCX2" style="background-color: inherit;">&nbsp;</span><span class="NormalTextRun SCXW140673802 BCX2" style="background-color: inherit;">{var5}</span></span></li>
                                    </ul>
                                </div>
                                <div class="OutlineElement Ltr  BCX2 SCXW140673802" style="direction: ltr;">
                                    <p class="Paragraph SCXW140673802 BCX2" lang="EN-US" style="font-weight: normal; font-style: normal; vertical-align: baseline; background-color: transparent; color: windowtext; text-align: left; margin-left: 24px; margin-right: 0px; padding-left: 0px; padding-right: 0px; text-indent: 0px;"><span class="EOP SCXW140673802 BCX2" data-ccp-props='{{"201341983":0,"335559685":360,"335559739":0,"335559740":252}}' style="font-size: 11pt; line-height: 18.9px; font-family: Calibri, Calibri_EmbeddedFont, Calibri_MSFontService, sans-serif;">&nbsp;</span></p>
                                </div>
                            </div>
                        </td>
                    </tr>
                    <tr class="TableRow SCXW140673802 BCX2" style="height: 35px;">
                        <td class="SCXW140673802 BCX2" colspan="5" data-celllook="4369" style="background-color: transparent; border-color: currentcolor rgb(31, 73, 125); border-style: none solid solid; border-width: 0px 2px 1px; border-image: none 100% / 1 / 0 stretch; vertical-align: middle; width: 805px;">
                            <div class="TableCellContent SCXW140673802 BCX2" style="padding: 0px 7px;">
                                <div class="OutlineElement Ltr  BCX2 SCXW140673802" style="direction: ltr;">
                                    <p class="Paragraph SCXW140673802 BCX2" style="font-weight: normal; font-style: normal; vertical-align: baseline; background-color: transparent; color: windowtext; text-align: left; margin-left: 0px; margin-right: 0px; padding-left: 0px; padding-right: 0px; text-indent: 0px;"><span class="TextRun SCXW140673802 BCX2" data-contrast="none" lang="EN-US" style="color: rgb(0, 0, 0); font-weight: bold; font-size: 11pt; font-family: Book Antiqua, Book Antiqua_EmbeddedFont, Book Antiqua_MSFontService, serif; line-height: 18.9px;"><span class="NormalTextRun SCXW140673802 BCX2" style="background-color: inherit;">Next&nbsp;</span><span class="NormalTextRun ContextualSpellingAndGrammarErrorV2 SCXW140673802 BCX2" style="background-color: inherit;">Update:</span></span><span class="TextRun SCXW140673802 BCX2" data-contrast="none" lang="EN-US" style="color: rgb(255, 0, 0); font-weight: bold; font-size: 11pt; font-family: Book Antiqua, Book Antiqua_EmbeddedFont, Book Antiqua_MSFontService, serif; line-height: 18.9px;"><span class="NormalTextRun ContextualSpellingAndGrammarErrorV2 SCXW140673802 BCX2" style="background-color: inherit;">*</span></span><span class="TextRun SCXW140673802 BCX2" data-contrast="none" lang="EN-US" style="color: rgb(0, 0, 0); font-size: 11pt; font-family: Book Antiqua, Book Antiqua_EmbeddedFont, Book Antiqua_MSFontService, serif; line-height: 18.9px;"><span class="NormalTextRun SCXW140673802 BCX2" style="background-color: inherit;">&nbsp; </span></span><span class="TextRun SCXW140673802 BCX2" data-contrast="none" lang="EN-US" style="color: rgb(0, 0, 0); font-size: 11pt; font-family: Calibri, Calibri_EmbeddedFont, Calibri_MSFontService, sans-serif; line-height: 18.9px;"><span class="NormalTextRun SCXW140673802 BCX2" style="background-color: inherit;">&nbsp;</span><span class="NormalTextRun SCXW140673802 BCX2" style="background-color: inherit;">In 30 minutes</span></span><span class="TextRun SCXW140673802 BCX2" data-contrast="none" lang="EN-US" style="color: rgb(0, 0, 0); font-size: 11pt; font-family: Book Antiqua, Book Antiqua_EmbeddedFont, Book Antiqua_MSFontService, serif; line-height: 18.9px;"><span class="NormalTextRun SCXW140673802 BCX2" style="background-color: inherit;"> </span></span><span class="EOP SCXW140673802 BCX2" data-ccp-props='{{"201341983":0,"335559739":0,"335559740":252}}' style="font-size: 11pt; line-height: 18.9px; font-family: Book Antiqua, Book Antiqua_EmbeddedFont, Book Antiqua_MSFontService, serif;">&nbsp;</span></p>
                                </div>
                            </div>
                        </td>
                    </tr>
                </tbody>
            </table>
        </div>
    </div>
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
    print('Sending To: ', TO, end='\n\n')
    send = input("Enter y to send. To modify any field, enter the corresponding field's number: ")

    if send.lower() == 'y':
        return send_mail()
    elif send.lower() == 'n':
        return print('\nExiting App...')
    elif send == '1': 
        subjectm = input('Subject: ')
        return verify_details(var1m, var2m, var3m, var4m, var5m,subjectm)
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
        var5m = input('Issue Description - Initial report(enter info in single line): ')
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
    s.sendmail(FROM, TO, message.as_string())
    s.quit()
    print("Sent!")

get_details()  
verify_details(var1, var2, var3, var4, var5, subject)

input("Press ENTER key to close...\n") #required for stand-alone exe file