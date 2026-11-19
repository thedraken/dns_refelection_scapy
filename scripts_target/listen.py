from scapy.all import sniff
packets = sniff(filter="icmp", count=2)
packets.show()
#>>> 0000 Ether / IP / ICMP 172.20.0.3 > 172.20.0.4 echo-request 0
