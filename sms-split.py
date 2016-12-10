#!/usr/bin/python
# -*- coding: mac-roman -*-
#
# Splitting the SMS inbox file produced by sms-export.py into one file per 
# message. Some renaming is done too. Note that this script expects the 
# input to be MacRoman! Also, you *will* need to edit the re.sub in the 
# beginning of the for loop sooner or later.
#
# Make a subdirectory called SMS before running if it doesn't exist already.
#
# The input file must be called sms-export.txt.

import re
from datetime import *
import os 
import os.path
import time

input = open("sms-export.txt", "r")

content = ""
who = ""
ts = float(0)
date = ""
outfile_name = ""
fromline = ""

who_re = re.compile("^From: ")
to_re = re.compile("^To: ")
time_re = re.compile("^Time: ")
div_re = re.compile("^-\+-\+-\+-\+-\+-\+-\+-\+-\+-\+$")

for line in input:
    # If line starts w. From: set who
    if (who_re.match(line)):
	who_arr = re.split("^From: ", line.rstrip(), 1)
	who = who_arr[1]
	who_file = "from " + who
	fromline = "From: " + who

    # If line starts w. To: set who
    if (to_re.match(line)):
	who_arr = re.split("^To: ", line.rstrip(), 1)
	who = who_arr[1]
	who_file = "to " + who
	fromline = "To: " + who

    # If line starts with Time: set time via float cast and set
    # timestamp to format 2006-12-31 17:12:06. Set the outfile to
    # SMS <from> 2006-12-31 17.12.06.txt
    elif (time_re.match(line)):
	time_arr = re.split("^Time: ", line.rstrip(), 1)
	ts = float(time_arr[1])
	timestamp = datetime.fromtimestamp(ts)
	date = timestamp.strftime("%Y-%m-%d %H:%M:%S")
	file_date = timestamp.strftime("%Y-%m-%d %H.%M.%S")
	who_file = re.sub("ö", "o", who_file)
	who_file = re.sub("Ö", "O", who_file)
	who_file = re.sub("å", "a", who_file)
	who_file = re.sub("Å", "A", who_file)
	who_file = re.sub("ä", "a", who_file)
	who_file = re.sub("Ä", "a", who_file)
	who_file = re.sub("é", "e", who_file)
	who_file = re.sub("É", "E", who_file)
	# who_file = re.sub("", "", who_file)
	outfile_name = "./SMS/SMS " + who_file + " " + file_date + ".txt"

    # if the line is -+-+-+-+-+-+-+-+-+-+, open, write the file and
    # close. 
    # Set the file access time and last modified time to the timestamp
    # Finally, empty content variables
    elif (div_re.match(line)):
	print "Writing", outfile_name
	out = open(outfile_name, "w")
	out.write(fromline + "\n")
	out.write("Date: " + date + "\n")
	out.write(content.rstrip() + "\n")
	out.close()
	os.utime(outfile_name, (ts, ts))
	outfile_name = ""
	who = ""
	date = ""
	content = ""
	fromline = ""

    # If not, add line to content.
    else:
	content = content + line
