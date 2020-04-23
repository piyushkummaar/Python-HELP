import smtplib
from email.message import EmailMessage
from string import  Template
from pathlib import Path

# html = Path('index.html').read_text()
# s = Template(html)
# s.substitute(name='piyush')
html = Template(Path('index.html').read_text())

email = EmailMessage()

email['from'] = 'Piyush Kumar'
email['to'] = 'rajatsainisim@gmail.com'
email['subject'] = 'Verify your account'

email.set_content(html.substitute(name='piyush'),'html')

with smtplib.SMTP(host='smtp.gmail.com',port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('beeaarr2@gmail.com', 'james_bon007')
    smtp.send_message(email)
    print("all good!!!")
