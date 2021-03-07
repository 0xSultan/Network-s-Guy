from scapy.all import *
import socket


def print_summary(pkt):
    global myIP
    if IP in pkt:
        ip_dst=pkt[IP].dst

    lo_subn = re.findall(r"\d{1,3}\.\d{1,3}\.\d{1,3}",myIP)
    dst = pkt[IP].dst
    dst_sub = re.findall(r"\d{1,3}\.\d{1,3}\.\d{1,3}",dst)

    if ( ( dst_sub[0] != lo_subn[0]) ):
        print("Alert " + str(ip_dst) + "  doesn't match the interface subnet")
sniff(filter="ip",prn=print_summary)