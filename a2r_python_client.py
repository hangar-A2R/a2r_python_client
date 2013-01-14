#!/usr/bin/python
import cherrypy as http
import socket, sys
import json as simplejson

from htmlGUI import htmler

from crc8 import crc8

from OSC import OSCClient

# The IP address and port where this GUI server will be available
gui_server_ip   = "91.121.171.80"
gui_server_port = 8181

# The IP address and port where A2R_index is listening
index_ip   = "91.121.171.80"
index_port = 7000

######
#
# Testing Program
#
######

class rest:
	# Instantiate OSCClient (if you need it!)
	#default_osc_port = 6666
	#osc_target_address = ('', default_osc_port)
	#print "\nInstantiating OSCClient:"
	#c = OSCClient()
	#c.connect(osc_target_address)	# connect back to our OSCServer
    	@http.expose
 	def send_data(self,sensor,val,address,port):
		try:
			value = int(val)
		except ValueError:
    			value = 50
		try:
			proxy_port = int(port)
		except ValueError:
    			proxy_port = 77777
		try:
			i = int(sensor)
		except ValueError:
    			i = 0
		crc = crc8()
		types = (0x81,0x82,0x83,0x84,0x85,0x86)
    		type = 0x81
		if ((i>0)and(i<7)):
			type = types[i-1]
    		c = crc.crc(chr(type) + chr((value & 0xff)) + chr(((value >> 8) & 0xff)))
    		#print hex(c)
		s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		s.connect((address,proxy_port))
		s.send(chr(type) + chr((value & 0xff)) + chr(((value >> 8) & 0xff)) + chr(c))
		return """<html><body>OK!</body></html>"""
    	#@http.expose
 	#def classicsynth_volume(self,volume):
	#	try:
	#		i = int(volume)
	#	except ValueError:
    	#		i = 200
	#	message = OSCMessage()
	#	message.setAddress("/control/volume")
	#	message.append(i)
	#	self.c2.send(message)
	#	return """<html><body>OK!</body></html>"""
    	@http.expose
 	def index(self):
		global index_ip
		global index_port
		
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.connect((index_ip,index_port))
		s.send("GET /\r\nAccept: application/json\r\n\r\n")

		json_string = ''

		while 1:
		     buf = s.recv(1000)
		     if not buf:
		         break
		     #sys.stdout.write(buf)
		     json_string = json_string+buf

		s.close()


		sessions = simplejson.loads(json_string.split("\r\n\r\n")[len(json_string.split("\r\n\r\n"))-1])
			
		html_response = htmler()
		
		return html_response.build_index(sessions)


if __name__ == "__main__":

	http.config.update( {'server.socket_host':gui_server_ip, 'server.socket_port':gui_server_port } )
    	http.quickstart( rest() )
	
