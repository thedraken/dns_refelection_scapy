from scapy.all import sniff, conf

# Use libpcap so Scapy can detect eth0's link-layer type and dissect
# packets into Ether/IP/UDP/DNS instead of leaving them as Raw.
conf.use_pcap = True

packets = sniff()#filter="arp or icmp or udp port 53")
for packet in packets:
    print(f"Packet Size: {len(packet)} bytes")
    print("Packet Summary:", packet.summary())