import pickle
import socket

sock = socket.socket()
sock.connect(('localhost', 9090))
# Получаем задание от сервера
data = sock.recv(4096)
list_K = pickle.loads(data)
# Решаем систему
d = list_K[0] * list_K[4] - list_K[3] * list_K[1]
dx = list_K[2] * list_K[4] - list_K[5] * list_K[1]
dy = list_K[3] * list_K[2] - list_K[0] * list_K[5]
list_otv = [dx/d, dy/d]
data = pickle.dumps(list_otv)
sock.sendall(data)
sock.close()
