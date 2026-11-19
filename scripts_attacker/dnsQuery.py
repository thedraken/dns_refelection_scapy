from scapy.layers.dns import DNS, DNSQR
from scapy.layers.inet import IP, UDP
from scapy.sendrecv import send

send(IP(src="172.20.0.4",
        dst="172.20.0.2")/
        UDP(dport=53)/DNS(rd=1, qd=DNSQR(qname="example.com")), verbose=0, count=10)
