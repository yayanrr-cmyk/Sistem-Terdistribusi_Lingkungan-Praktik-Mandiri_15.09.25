#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  4 13:46:07 2024

@author: widhi
"""

import zmq

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")
q=0
while True:
    q+=1
    message = socket.recv()
    print(f"Received request: {message+b' '+str(q).encode()}")
    socket.send(b"World")
