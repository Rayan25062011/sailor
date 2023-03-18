import socket
import sys
from _thread import *


red = "\033[31m"
blue = "\033[34m"
bold = "\033[1m"
reset = "\033[0m"
green = "\033[32m"
yellow = "\033[33m"



def moduleproxy(port):


   red = "\033[31m"
   blue = "\033[34m"
   bold = "\033[1m"
   reset = "\033[0m"
   green = "\033[32m"
   yellow = "\033[33m"

   try:
      listening_port = port
   except KeyboardInterrupt:
      print(f"[{red}-{reset}] User decided to quit")
      sys.exit()


   def start():    #Main Program
      try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind(('', listening_port))
        sock.listen()
        print(f"[{green}+{reset}] Sailor proxy server activated [ {listening_port} ]")
      except Exception as e:
        print(f"[{red}-{reset}] Could not Initialize Socket")
        print(e)
        sys.exit(2)
      while True:
         try:
            conn, addr = sock.accept() #Accept connection from client browser
            data = conn.recv() #Recieve client data
            start_new_thread(conn_string, (conn,data, addr)) #Starting a thread
         except KeyboardInterrupt:
            sock.close()
            print(f"\n[{blue}*{reset}] Sailor proxy Shutdown")
            sys.exit(1)

   def conn_string(conn, data, addr):
      try:
         print(data)
         first_line = data.split(b'\n')[0]

         url = first_line.split()[1]

         http_pos = url.find(b'://') #Finding the position of ://
         if(http_pos==-1):
            temp=url
         else:

            temp = url[(http_pos+3):]
        
         port_pos = temp.find(b':')

         webserver_pos = temp.find(b'/')
         if webserver_pos == -1:
            webserver_pos = len(temp)
         webserver = ""
         port = -1
         if(port_pos == -1 or webserver_pos < port_pos):
            port = 80
            webserver = temp[:webserver_pos]
         else:
            port = int((temp[(port_pos+1):])[:webserver_pos-port_pos-1])
            webserver = temp[:port_pos]
         print(data)
         proxy_server(webserver, port, conn, addr, data)
      except Exception:
         pass

   def proxy_server(webserver, port, conn, addr, data):
      try:
         print(data)
         sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
         sock.connect((webserver, port))
         sock.send(data)

         while 1:
            reply = sock.recv()
            if(len(reply)>0):
               conn.send(reply)
                
               dar = float(len(reply))
               dar = float(dar/1024)
               dar = "%.3s" % (str(dar))
               dar = "%s KB" % (dar)
               print(f"[{yellow}?{reset}] Request Completed: %s => %s <=" % (str(addr[0]), str(dar)))

            else:
               break

         sock.close()

         conn.close()
      except socket.error:
         sock.close()
         conn.close()
         print(sock.error)
         sys.exit(1)

   start()
