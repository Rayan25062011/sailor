from socket import AF_INET, SOCK_STREAM, socket
import time
from sailorproxy import moduleproxy


red = "\033[31m"
blue = "\033[34m"
bold = "\033[1m"
reset = "\033[0m"
green = "\033[32m"
yellow = "\033[33m"





def banner(target_address, target_port):
   with socket(AF_INET, SOCK_STREAM) as socket_sock:
      socket_sock.connect_ex((target_address, target_port))
      socket_sock.settimeout(2)
      banner = socket_sock.recv(1024).decode().replace("\n", "")
   print(banner)

print(f"{blue}Session ID{reset}: ULGFBeItYZsaSlIc3VtfZdaXcRXRNIjbEOHPLGbb")


while True:
   sailor = input(f"{red}sailor@root{reset}:{blue}~{reset}$ ")

   if sailor == "new sailor/payloads/sailorproxy":
      port = int(input(f"{red}sailor@root{reset}(port):{blue}~{reset}$ "))
      print(f"[{green}+{reset}] SailorProxy ready for deployment")

   elif sailor == "run sailorproxy":
      moduleproxy(port)


   elif sailor == "new sailor/payloads/sailorsurf":
      print(f"[{green}+{reset}] SailorSurf ready for deployment")
   def sailorsurf(ip):
      s = socket.socket()
      s.listen(80)
      s.accept()
      data = s.recv(1028)
      if ip in data:
         print(f"[{red}!{reset}] IP detected socket connection deleted")
         s.close()




   if "run sailorsurf ip" in sailor:
      hstr = sailor
      hspl = "ip"
      ip = hstr.split(hspl)[1]
      print(f"ip {red}banned{reset} => {ip}")

      sailorsurf(ip)

   if "run sailorbanner" in sailor:
      host = input(f"{red}sailor@root{reset}(host):{blue}~{reset}$ ")
      port = int(input(f"{red}sailor@root{reset}(port):{blue}~{reset}$ "))
      banner(host, port)
