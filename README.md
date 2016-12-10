# sms-export.py for PyS60 and date humanizer from original Lokala.org Kristoffer Nyber work

## sms-export.py

Exporting short messages on S60 phones by Kristoffer Nyberg.                                     

For more information : http://www.lokala.org/?page_id=1479

French how-to : http://linuxfr.org/users/siltaar/journaux/sauvegarder-les-sms-d-un-nokia-symbian

### Original instructions of sms-export.py 0.2 (updated)

First you need to install Python S60 on your phone.

Current (2016) location of the last working Python for S60 Series is here : https://garage.maemo.org/projects/pys60/

You will probably need to change the date of your phone to get it back to the year of release of the Python package (e.g. 2010) to be allowed to actually install Python, and its shell.

After you have installed Python on your phone, unpack the sms-export package somewhere. In this example, I’m using the desktop. Using Bluetooth, transfer the files sms-export.py and sms-export-to.py to your phone. The phone will get a new message. When you open the message, the Python installer starts automatically.

The installer will ask you how to install the python code. Select “install as Python script”.

Now start Python and select “run script”. You should find sms-export.py in the menu. Run it. When the script is done, it should print how many messages were exported.

Using some kind of file browser on your phone, navigate to the E: drive and send sms-export.txt to your computer. You are done.

If you want to export messages you have sent, not just received, do like this. Move or delete all current messages away from the inbox. Move all sent messages to the inbox. Run sms-export-to.txt. Move or delete the sent messages. Don’t leave them in the inbox. Transfer the file sms-export.txt to your computer.

If you want to split up the big file as one file per message, copy sms-export.txt to the sms-export script directory right beside sms-split.py.

If you want to get human readable date and time for the exported SMS, use the humanize-datetimes-in-sms-export.py script as described below.

## humanize-datetimes-in-sms-export.py 

Reads an sms-export.txt file in input and writes on standard output the same file with human readable date and time fields.

