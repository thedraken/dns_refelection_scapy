from scapy.layers.inet import IP, TCP
from scapy.sendrecv import sr

res, unans = sr(IP(dst="172.20.0.4")/TCP(dport=(1,100), flags="S"), timeout=1)
# filter the results by executing the lambda function which extracts all the records showing
# open ports.
res.nsummary(lfilter=lambda s,r: (r.haslayer(TCP) and (r.getlayer(TCP).flags & 2)))
res.nsummary(lfilter = lambda s,r: r.sprintf("%TCP.flags%") == "SA")
res.nsummary()
