import re
import os
import sys
import iptc
import nmap
import socket
import requests
import subprocess
from scapy.all import *


def UnkPorts():
    global myIP
    host = socket.gethostbyname(myIP)
    openPorts = []
    for port in range(1, 1000):
        if port not in wellknown and port < 1000:
            scannerTCP = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(0.1)
            status = scannerTCP.connect_ex((host, port))
            if not status:
                openPorts.append(port) 

    for p in openPorts:
        os.system("nc -nvlp " + str(p) + " &")
        os.system("clear")   
    return openPorts

def blockIP(ip):
    chain = iptc.Chain(iptc.Table(iptc.Table.FILTER), "INPUT")
    rule = iptc.Rule()
    rule.in_interface = "eth0"
    rule.src = ip  
    target = iptc.Target(rule, "DROP")
    rule.target = target
    chain.insert_rule(rule)

def ScapySniff():
    sniff(filter="ip",prn=Analyz2Block)
    sniff(filter="ip and host " + myIP, prn=Analyz2Block)

def Analyz2Block(pkt):
    global myIP
    global unKnown
    TcpSport = ""

    if 'TCP' in pkt:
        TcpSport=pkt['TCP'].sport

    if (pkt['IP'].src == myIP)  and TcpSport in unKnown:
        blockIP(pkt['IP'].dst)
        print(f"{pkt['IP'].dst} Blocked\n")
        send_mail()
        print("email sent")
        exit()

def send_mail():
    return requests.post(
        "https://api.mailgun.net/v3/YOUR_DOMAIN_NAME/messages",
        auth=("api", "YOUR_API_KEY"),
        data={"from": "admin <mailgun@YOUR_DOMAIN_NAME>",
            "to": ["YOU@YOUR_DOMAIN_NAME"],
            "subject": "Alert",
            "text": "someone is trying to connect to unKnown ports"})

wellknown = [1, 5, 7, 18, 20, 21, 22, 23, 25, 29, 37, 42, 43, 49, 53, 69, 70, 79, 80, 103, 108, 109, 110, 115, 118, 119, 137, 139, 143, 150, 156, 161, 179, 190, 194, 197, 389, 396, 443, 444, 445, 458, 546, 547, 563, 569, 1080]

myIP = ""
unKnown = UnkPorts()

def point2():
    global myIP
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    myIP = s.getsockname()[0]
    s.close()
    
    if(len(unKnown)):
        print(f"Listening to unknown ports on {myIP}....")
        ScapySniff()


