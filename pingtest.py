import re
import sys

pingRegex = re.compile(r'(\d+\s\w+)\s\w+\s(\d+.\d+.\d+.\d+):\s\w+=(\d+)\s\w+=(\d+)\s\w+=(\d+.\d+)\s\w+')
mo = pingRegex.search('64 bytes from 159.203.77.159: icmp_seq=136 ttl=50 time=118.519 ms')

print mo.groups()
bytes, ipp_addr, icmp_seq, ttl, ping_time = mo.groups()

print("Bytes %s, IP Address: %s, icmp_seq: %s, TTL: %s, Ping Time: %s") % (bytes, ipp_addr, icmp_seq, ttl, ping_time)
