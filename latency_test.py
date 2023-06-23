# -*- coding: utf-8 -*-
"""
Created on Thu Jun 22 04:23:26 2023

@author: neeltron
"""

import ntplib
from tkinter import *
import time
from datetime import datetime, timezone
root=Tk()

variable=StringVar()

def update_label(time):
    i=0
    while 1:
        time = get_ntp_time()
        i=i+1
        variable.set(time)
        root.update()

def get_ntp_time():

    ntp_pool = ['time.google.com']

    def call_ntp(serverAddress):
        call = ntplib.NTPClient()
        return call.request(server, version=3)

    for server in ntp_pool:
        response = call_ntp(server)
        time = datetime.fromtimestamp(response.tx_time + response.delay/2, timezone.utc)
        print('-')
        a = print("hi")
        print(a)
    
    return time

your_label=Label(root,textvariable=variable)
your_label.pack()
start_button=Button(root,text="start",command=update_label(time))
start_button.pack()
root.mainloop()
    
