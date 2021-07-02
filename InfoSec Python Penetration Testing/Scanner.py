#!/usr/bin/python3

import nmap

scanner = nmap.PortScanner()

print("Welcome! This is a simple nmap automation tool")
print("<------------------------------------------------->")

ip_address = input('Please enter the IP address you want to scan: ')
print("The IP you entered is ", ip_address)

resp = inpur("""\nPlease enter the type of scan you want to run
                1) SYN ACK Scan
                2) UDP Scan
                3) Comprehensive scan\n""")
print("You have selected the option: ", resp)

if resp == '1':
    print("NMap version: ",scanner.nmap_version())
    print("SYN ACK Scan")
    
    scanner.scan(ip_address, '1-2000', '-v', '-sS')
    print(scanner.scaninfo())

    print("IP Status ", scanner[ip_address].state())
    print(scanner[ip_address].all_protocols())
    print("Open ports: ", scanner[ip_address]['tcp'].keys())

elif resp == '2':
    print("NMap version: ",scanner.nmap_version())
    print("UDP Scan")

elif resp == '1':
    print("NMap version: ",scanner.nmap_version())
    print("Comprehensive Scan")