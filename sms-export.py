# A very simple script for exporting the SMS inbox on S60 phones.
#
# Author: Kristoffer Nyberg

import inbox
from codecs import open

inb = inbox.Inbox()
msgs = inb.sms_messages()
no = 0

# open a file for export
f = open("E:\sms-export.txt", "a", "utf-8")

for msg in msgs:
    no = no + 1
    frm = inb.address(msg)
    time = inb.time(msg)
    content = inb.content(msg)
    f.write("From: " + frm + "\n")
    f.write("Time: " + repr(time) + "\n")
    f.write(content + "\n")
    f.write("-+-+-+-+-+-+-+-+-+-+\n")

f.close()
print "Converted ", no, " messages."
