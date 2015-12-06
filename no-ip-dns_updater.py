#!/usr/bin/env python

'''
    Script to update the ip-adress from www.noip.com
    This file should be in /etc/cron.daily or /etc/cron.hourly
    Or you can customize the update with Crontab

    To be able to access the logfile, this script should be run as root

    written by 5lot5 - 5lot5 at telenet dot be
'''

import os, sys
from time import strftime

username = "Your_username"
userpass = "Your_Password"
hostname = "Your_DNS_host"
logfile = '/var/log/noipdns.log'

ip = os.popen('curl ipecho.net/plain').read()
url = str('curl http://'+username+':'+userpass+'@dynupdate.no-ip.com/nic/update?hostname='+hostname+'&myip='+str(ip))
response = os.popen(url).read()
log = open(logfile, 'a')

if 'good' in response:
    log.write(strftime('%d-%m-%Y | %H:%M | ')+"Update was successfull \n")
elif 'nochg' in response:
    log.write(strftime('%d-%m-%Y | %H:%M | ')+"No update needed..IP is up-to-date \n")
else:
    log.write(strftime('%d-%m-%Y | %H:%M | ')+"Error Connecting to the server.. \n")
log.close()
