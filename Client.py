import pickle
import socket

sock = socket.socket()
sock.connect(('localhost', 9090))
# Получаем задание от сервера
data = sock.recv(4096)
list_K = pickle.loads(data)
# Решаем систему
list_otv = [list_K[0] + list_K[1], list_K[0] - list_K[1]]
data = pickle.dumps(list_otv)
sock.sendall(data)
sock.close()
