import time

from tempmailio import *

mail = TempMailI0(
    user_name='test',
    domain=Domain.random()
)

success = mail.create_email()

print(mail.email_address)

while True:
    inbox = mail.get_inbox()

    if len(inbox) > 0:
        inbox[0].jsonprint()
        exit(0)

    time.sleep(2.5)