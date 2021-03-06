#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 04:08:50 2019

@author: lucky
"""

import smtplib, ssl

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

re_email="lucky19125@iiitd.ac.in"
username="api"
date="December 13"
time="10:00 am"
msg = MIMEMultipart()
msg["Subject"] = "Interview Invitation"
msg["From"] = "luckyagarwal459@gmail.com"
msg["To"] = re_email
body = MIMEText("Dear " + username +",\n\
As a result of your application for the position of Software Developer, I would like to invite you to attend an interview on " + date + ", at " + time +" at our office in Quincy, Massachusetts.\
You will have an interview with the department manager, Edie Wilson. The interview will last about 45 minutes. Please bring three references as well as a copy of your drivers license to the interview.\
\nIf the date or time of the interview is inconvenient, please contact me by phone (518-555-5555) or email (tgunn@randall.com) to arrange another appointment. We look forward to seeing you.\
\nBest regards,\
\nLucky agarwal\
\n_______\
\nlucky agarwal\
\nAdministrative Director\
\nRandall & Associates\
")
msg.attach(body)
smtp = smtplib.SMTP('smtp.gmail.com', 587)
smtp.starttls() 
smtp.login("luckyagarwal459@gmail.com", "ykcul@123") 
smtp.sendmail(msg["From"], msg["To"].split(","), msg.as_string())
smtp.quit()
print("success")