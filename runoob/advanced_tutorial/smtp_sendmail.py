#!/usr/bin/env python3
# -*- coding: utf-8 -*-
############################
# File Name: smtp_sendmail.py
# Author: One Zero
# Mail: zeroonegit@gmail.com
# Created Time: 2015-12-29 14:59:40
############################

import smtplib

sender = 'from@fromdomain.com'
receivers = ['to@todomain.com']

message = """From: From Person <from@fromdomain.com>
To: To Person <to@todomain.com>
Subject: SMTP e-mail test

This is a test e-mail message.
"""

try:
    smtpObj = smtplib.SMTP('localhost')
    smtpObj.sendmail(sender, receivers, message)
    print("Successfully sent email")
except:
    print("Error: unable to send email")
