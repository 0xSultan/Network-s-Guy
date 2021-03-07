import re
import os
import sys
import iptc
import nmap
import socket
import logging
import requests
import subprocess
from pyfiglet import *
from scapy.all import *


#get_open_ports
def port_scan():
    try:
        ip_scan=subprocess.Popen("arp-scan -l",shell=True, stdout=subprocess.PIPE,stderr=subprocess.PIPE, stdin=subprocess.PIPE)
        out=str(ip_scan.stdout.read(),"utf-8")
        up_ips=re.findall(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}",out)
        print("Active Hosts Are: " + str(up_ips) + "\n")

        resul_port =''
        for ip in up_ips:
            for port in range(1, 500):
                s1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
                socket.setdefaulttimeout(0.1)
                result = s1.connect_ex((ip,port)) 
                if not result:
                    resul_port += str(port) + ','
                s1.close()
            print(str(ip) +" has open ports: " + str(resul_port) + "\n")
            ports = "-p "+ str(resul_port)
            print(resul_port, file=open('open_ports.txt', 'a'))
            nm = nmap.PortScanner()
            nm.scan(hosts=ip, arguments=ports)
            print(nm.csv())
            print (nm.csv(),file=open('nmap_scan.csv','a'))

        print("___________________________________________________")
        print("The ports saved in open_ports.txt")
        print("The Scan Result saved in nmap_scan.csv")

    except:
        print("scan error")
        exit()
