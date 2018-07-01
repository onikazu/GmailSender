import smtplib
from email.mime.text import MIMEText
from email.utils import formatdate

import configparser

inifile = configparser.ConfigParser()
inifile.read('./info.ini', 'UTF-8')

FROM_ADDRESS = inifile.get('address', 'mail1')
MY_PASSWORD = inifile.get('password', 'pass1')
TO_ADDRESS = inifile.get('address', 'mail2')
SUBJECT = 'GmailのSMTPサーバ経由'
BODY = 'pythonでメール送信'


def create_message(from_addr, to_addr, subject, body):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = from_addr
    msg['To'] = to_addr
    msg['Date'] = formatdate()
    return msg


def send(from_addr, to_addrs, msg):
    smtpobj = smtplib.SMTP('smtp.gmail.com', 587)
    smtpobj.ehlo()
    smtpobj.starttls()
    smtpobj.ehlo()
    smtpobj.login(FROM_ADDRESS, MY_PASSWORD)
    smtpobj.sendmail(from_addr, to_addrs, msg.as_string())
    smtpobj.close()


if __name__ == '__main__':

    to_addr = TO_ADDRESS
    subject = SUBJECT
    body = BODY

    msg = create_message(FROM_ADDRESS, to_addr, subject, body)
    send(FROM_ADDRESS, to_addr, msg)