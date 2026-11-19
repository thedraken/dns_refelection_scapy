from scapy.all import *
from scapy.layers.inet import IP, ICMP

send(IP(dst="172.20.0.4")/ICMP())
