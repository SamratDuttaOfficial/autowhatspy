# AutoWhatsPy

## _WhatsApp and Email Automation with Python_

_It does not open any browser window while sending messages through WhatsApp. It works completely in the background._

[![Version](https://img.shields.io/badge/version-1.0.7-blue.svg)]() [![Python Versions](https://img.shields.io/badge/python-3.9-blue.svg)](https://github.com/SamratDuttaOfficial/autowhatspy)
[![MIT License](https://img.shields.io/apm/l/atomic-design-ui.svg?)](https://github.com/SamratDuttaOfficial/autowhatspy) [![PR's Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat)](https://github.com/SamratDuttaOfficial/autowhatspy)  

This package is to be used for educational and testing purposes only. Don't use this package to spam people.

If anyone uses this to spam people, I will not be responsible.

I created this just for educational purposes to help the learners get a better understanding of selenium.

## Author
Created by Samrat Dutta

Github: https://github.com/SamratDuttaOfficial

Linkedin: https://www.linkedin.com/in/SamratDuttaOfficial/

## Github

Please visit the Github repository for a quick tutorial.

https://github.com/SamratDuttaOfficial/autowhatspy

Pull requests are always welcome.

## Features
- Send text and image messages through WhatApp to unlimited numbers/contacts/groups.
- Send emails to multiple email addresses through your email client.
- It does not open any browser window while sending messages through WhatsApp. It works completely in the background.

## Tech

This package is completely built with python. 

##### Packages
Here are some packages you'll need to run this package.

- Selenium - For the webdriver
- Pyperclip - To copy and paste text. (not used in this version)

##### Others
 - [Gechodriver](https://github.com/mozilla/geckodriver) - Firefox driver for Selenium

## Installation

It works best with python 3.9 or above and the latest version of pip to install this package.

```sh
pip install autowhatspy
```

To update the package (if a new version is there)

```sh
pip install autowhatspy --upgrade
```

## Usage

#### For WhatsApp 
##### Functions
---

**Bulk WhatsApp messages to numbers**

To send a single text or image (or both) message to multiple numbers through WhatsApp. This will work even if the numbers are not saved in your contacts. This will work even if you have never messaged the numbers from your WhatsApp. This will not work for a number which is not registered or active on WhatsApp.

```sh
message_to_numbers(msg, numbers_list, gechodriver, gechodriver_log, user_profile, country_code, image)
```

**Bulk WhatsApp messages to contacts**

To send a single text or image (or both) message to multiple contacts through WhatsApp

```sh
message_to_contacts(msg, contacts, gechodriver, gechodriver_log, user_profile, image)
```

**Bulk WhatsApp messages to groups**

To send a single text or image (or both) message to multiple groups through WhatsApp. You have to be a member of the groups with permission to send messages.

```sh
message_to_groups(msg, groups, gechodriver, gechodriver_log, user_profile, image)
```

##### Arguments
---

**msg** - Path to the text file containing the message text. 

_Do not use unnecessary new lines in the text as they will be sent as separate messages to the receipients._

**numbers_list** - Path to the text file containing the list of numbers. 

_The contents of the text file should be like this:_

```sh
919836xxxx10
9624xxxx78
919745xxxx69
7898xxxx56
8985xxxx65
```

_The numbers may or may not have a country code attached to it. It will work either way._

**contacts** - Path to the text file containing the list of contacts. 

_The contents of the text file should be like this:_

```sh
Samrat Dutta
Abraham Lincoln
Sachin
Sourav
Mr. Das
```

_The names in the text file should be exactly same as they are saved in your phone. You must be already talking to them on WhatsApp._

**groups** - Path to the text file containing the list of groups. 

_The contents of the text file should be like this:_

```sh
Group One
Group Two
Personal Group
Family Group
Work Group
```

_The group names in the text file should be exactly same as they are in your WhatsApp (case-sensitive). You have to be a member of the groups with permission to send messages._

**country_code** - The country code of the numbers, without any symbols. Example: 91

**gechodriver** - Path to the gechodriver.exe file.
_Download the gechodriver.exe (link above) and send the path as an argument. You may use the absolute path or the relative path based on how your interpreter works._
_Make sure gechodriver.exe is in the same project folder you are working on. Or add the folder where gechodriver.exe is located in the PATH. Otherwise, an error might occur._
_If you still get an error, downgrade selenium to version 2.53.6._

**gechodriver_log** - Path to the text file where the logs of gechodriver will be saved.
_Make sure gechodriver.log is in the same project folder you are working on. Otherwise, an error might occur._

**user_profile** - Path to the saved firefox user profile.
 - Open firefox. Go to about:profiles and make a new profile.
 - Save it in your project directory with whatever name firefox assigns it.
 - Open that profile, open web.whatsapp.com and scan the QR.
 - Send the path of the profile as the argument to the function.
 - **image** - (Optional) Path to the image/video you want to send. Make sure that it is supported by WhatsApp and is of the permissible length.

#### For Email

##### Functions

---
**Bulk WhatsApp messages to groups**
To send test based email to multiple email addresses. 

```sh
send_emails(_smtp, msg, address_list, subject, your_email_address, passwrd)
```

##### Arguments
---

**_smtp** - SMTP server address of you email client. I used smtp.gmail.com:587 for Gmail in my experiments
 - Gmail SMTP server address: smtp.gmail.com
 - Gmail SMTP name: Your full name
 - Gmail SMTP username: Your full Gmail address (e.g. you@gmail.com)
 - Gmail SMTP password: The password that you use to log in to Gmail
 - Gmail SMTP port (TLS): 587
 - Gmail SMTP port (SSL): 465
 - **Note**: You can use the SMTP server even if you’ve enabled two-factor authentication on your Google account. However, you will need to generate an app password so that the app can still connect.

**msg** - Path to the text file containing the message text. 

**address_list** - Path to the text file containing the list of email addresses. 

_The contents of the text file should be like this:_
```sh
samxxxxxx@gxxx.com
somxxxxxx@yaxxx.com
johnxxxxx@mailxxxxx.com
```
**subject** - Subject of the email you are sending.

**your_email_address** - Your email address associated with the email client you are using.

**passwrd** - Password of the email address you are using.

##### Note

---
Make sure the number of emails in the list does not exceed your daily/monthly limit.

**For Gmail**: With just a free Gmail account, you’ll be able to send up to 500 emails per day. If you have a paid Google Workspace account, your limit is 2,000 emails per day. The limits apply to a “rolling 24 hour period”.

If the program fails to send emails to all the given email addresses, check your own email address and password. Also check if your daily limit is exceeded or not.

## License

MIT 
