#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  8 14:15:04 2024

@author: widhi
"""

import socket

def server_program():
    server_socket = socket.socket()
    # Bind to all interfaces so client container can reach it
    server_socket.bind(('0.0.0.0', 4141))  
    
    server_socket.listen(1)
    print("Upcall server listening on 0.0.0.0:4141 (DNS: upcall-server:4141)")
    conn, address = server_socket.accept()  
    print("Connection from:", address)
    
    while True:
        data = conn.recv(1024).decode()
        if not data:
            break
        print("Received from client:", data)
        
        # Simulate upcall (sending an event message to client)
        upcall_message = "Upcall event: Processing " + data
        conn.send(upcall_message.encode())
    
    conn.close()

if __name__ == '__main__':
    server_program()
