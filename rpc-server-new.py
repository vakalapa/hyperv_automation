#!/usr/bin/env python
# coding: utf-8
from xmlrpc.server import SimpleXMLRPCServer

def is_even(n):
    return n % 2 == 0

import subprocess
import json

def get_vm():
	process=subprocess.Popen(["powershell","Get-VM | ConvertTo-Json"],stdout=subprocess.PIPE)
	result=process.communicate()[0]
	print (result)
	result = result.decode('utf-8')

	#js_obj = json.loads(str(result))
	return str(result)

server = SimpleXMLRPCServer(("172.18.40.59", 8000))
print("Listening on port 8000...")
server.register_function(is_even, "is_even")
server.register_function(get_vm, "get_vm")
server.serve_forever()