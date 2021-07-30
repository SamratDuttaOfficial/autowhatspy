'''
Made by: Samrat Dutta
LinkedIn: https://www.linkedin.com/in/samratduttaofficial
Github: https://github.com/SamratDuttaOfficial

Make sure the number of emails in the list does not exceed your daily/monthly limit.
SMTP for gmail I used during testing was smtp.gmail.com:587
'''

import smtplib
from email.mime.text import MIMEText


def send_emails(_smtp, msg, address_list, subject, your_email_address, passwrd):
    try:
        with open(address_list, 'r', encoding='utf8') as f:
            emails = [email.strip() for email in f.readlines()]
            print('Found the email address list file. '
                  'If the list exceeds your daily/monthly emails limit, '
                  'sending will fail for addresses beyond that limit.')
    except FileNotFoundError:
        print('ERROR: Please provide a proper path of the email address list file. '
              'Make sure the file contains all the email addresses in different lines.')
        exit(0)
    except:
        print('The file content should will be like this:\n'
              'samxxxxxx@gxxx.com\n'
              'somxxxxxx@yaxxx.com\n'
              'johnxxxxx@mailxxxxx.com\n')
        exit(0)

    try:
        with open(msg, 'r', encoding='utf8') as f:
            msg_text = MIMEText(f.read())
    except FileNotFoundError:
        print('ERROR: Please provide a proper path of the email text file.')
        exit(0)

    msg_text['Subject'] = subject
    msg_text['From'] = your_email_address

    try:
        server = smtplib.SMTP(_smtp)
        server.starttls()
    except:
        print('An error occurred while starting the SMTP TLS. Please check the SMTP address used.')
        exit(0)

    try:
        server.login(your_email_address, passwrd)
    except:
        print('An error occurred while logging in to the SMTP server. '
              'Please read the README.md file for more information about this.')
        exit(0)

    print("Sending emails with subject: " + str(msg_text['Subject']))

    for email in emails:
        del msg_text['To']
        msg_text['To'] = email
        try:
            server.sendmail(your_email_address, email, msg_text.as_string())
            print("Sent mail to: " + email)
        except smtplib.SMTPException:
            print("An error occurred for this email: " + email)
            continue

    server.quit()
    print("Task Completed!")
