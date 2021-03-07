import os
import p1
import p2
import p3
import re
import sys
import iptc
import nmap
import socket
import requests
import subprocess
from pyfiglet import *
from scapy.all import *

def main():
    choice ='0'
    while choice =='0':
        custom_fig = Figlet(font='big')
        print(custom_fig.renderText("Network\'s Guy"))
        print("Coded with \u2764\ufe0f By @mSult4n \n")
        print(" 1) Scan IPs \n 2) listen 2 unknown ports & Block \n 3) Sniff traffic & check src IP \n")

        choice = input ("Please select an option:")
        if choice == "1":
            p1.port_scan()
        elif choice == "2":
            p2.point2()
        elif choice == "3":
            p3.print_summary(pkt)
        else:
            print("I don't understand your choice.")

main()
