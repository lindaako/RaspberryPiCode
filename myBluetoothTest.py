#!/usr/bin/python
#-*- coding: utf-8 -*-
from bluetooth import *
import BtAutoPair
import korean


def sendMessageTo(targetBluetoothMacAddress):
  port = 1
  sock=bluetooth.BluetoothSocket( bluetooth.RFCOMM )
  sock.connect((targetBluetoothMacAddress, port))
  sock.send("Messsage received")
  sock.close()
  
def receiveMessages(no_error, data):

  
  server_sock = BluetoothSocket(RFCOMM)
  server_sock.bind(("",PORT_ANY))
  server_sock.listen(1)

  uuid = "00001101-0000-1000-8000-00805F9B34FB"

  advertise_service( server_sock, "SampleServer",
			service_id = uuid,
			service_classes = [uuid, SERIAL_PORT_CLASS],
			profiles = [SERIAL_PORT_PROFILE],#,
		   )

  client_sock,address = server_sock.accept()
  print "Accepted connection from " + str(address)
  

  try: 
    data = client_sock.recv(1024)
      
  except IOError:
    pass
      
      
  
  if data :
    
    print "received [%s]" % data
    
    with open('book.txt', 'w+') as f:
        f.write(data)
          
    no_error = 1
    client_sock.send("Message received")
    client_sock.close()
    server_sock.close()
    
  
def lookUpNearbyBluetoothDevices():
  nearby_devices = bluetooth.discover_devices()
  for bdaddr in nearby_devices:
    print str(bluetooth.lookup_name( bdaddr )) + " [" + str(bdaddr) + "]"
    
autopair = BtAutoPair.BtAutoPair()
autopair.enable_pairing()    
#lookUpNearbyBluetoothDevices()
receiveMessages(0, 0)
