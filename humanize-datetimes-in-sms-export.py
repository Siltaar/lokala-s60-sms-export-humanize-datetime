#!/usr/bin/python
#
# Author: Siltaar <siltaar@d12s.fr>
# Date:    2016-12-10
# License: CC by-sa
# Usage : ./humanize-dates-for-sms-export.py sms-export.txt > humanized-sms-export.txt
# Description: Reads a sms-export.txt file in input and writes on standard
# output the same file with human readable date and time fields.
# For more information about sms-export.py : http://www.lokala.org/?page_id=1479
# French how-to : http://linuxfr.org/users/siltaar/journaux/sauvegarder-les-sms-d-un-nokia-symbian

import fileinput
import re
import sys
import time

for line in fileinput.input():
    s = re.search('Time: ([0-9]+\.[0-9]+)', line)

    if s:
        sms_dt = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(float(s.group(1))))
        sys.stdout.write('Time: %s\n' % sms_dt)
    else:
        sys.stdout.write(line)

