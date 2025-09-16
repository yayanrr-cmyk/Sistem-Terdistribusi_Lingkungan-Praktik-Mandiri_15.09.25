#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  8 14:04:45 2024

@author: widhi
"""

import socket

def server_program():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Bind to all interfaces so other containers can reach the server
    server_socket.bind(('0.0.0.0', 2222))  
    
    server_socket.listen(1)
    print("Server listening on 0.0.0.0:2222")
    conn, address = server_socket.accept()  
    print("Connection from:", address)
    
    while True:
        data = conn.recv(1024).decode()
        if not data:
            break
        print("Received from client:", data)
        
        # Respond back to the client
        response = "Echo: " + data
        conn.send(response.encode())  
    
    conn.close()

if __name__ == '__main__':
    server_program()
