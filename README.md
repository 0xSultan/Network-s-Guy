# Network-s-Guy 

1) Scan open IPs using sockets, pass them to Nmap and save the output. 
2) Listen to unknown ports and check if someone is trying to connect, send a mail and block the IP.  
3) Sniff the incoming traffic, check the source IP, if it doesn't match the interface subnet that is sniffing the traffic, an alert is generated. 

# Usage
> git clone https://github.com/Sultan0x1/Network-s-Guy.git  
> chmod -R +x Network-s-Guy   
> cd Network-s-Guy/   
> pip3 install -r requirements.txt   
> python3 main.py  
