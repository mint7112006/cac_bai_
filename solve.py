import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("144.79.188.39", 40997))

while True:
  data = s.recv(4096)
  if not data:
    break
  print(data.decode(), end="")