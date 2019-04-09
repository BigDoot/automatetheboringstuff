#!python3
#random chore assignment, edit your email and password

import smtplib, random

emails = ['fadaddad@hotmail.com', 'shit@gmail.com', 'hippyman@gmail.com', 'random@gmail.com', 'hahawasup@gmail.com']
chores = ['dishes', 'bathroom', 'vacuum', 'walk dog', 'dinner']

smtpobj = smtplib.SMTP('smtp.gmail.com', 587)
smtpobj.ehlo()
smtpobj.starttls()
smtpobj.login('youremail', '#yourpassword')

for person in emails:
    randomchore = random.choice(chores)
    chores.remove(randomchore)
    sendmailstatus = smtpobj.sendmail('youremail@gmail.com', person, "Subject: Chores undone.\nDear bro,\nRecords show that you have not done your assigned chore: %s.PLease do it as soon as possible. Thank you!" %randomchore)
    if sendmailstatus != {}:
        print('There was a problem sending email to %s' %person)
smtpobj.quit()
print('Done')
