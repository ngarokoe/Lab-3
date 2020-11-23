import socket
import workitem
import pickle


def solution_workitem(workitem):
    '''
    Решение выражения
    :param workitem: workitem
    :return: x + y
    '''
    Summ= A + B
    return Summ


def test_workitem(workitem_server, list_otv):
    '''
    Проверка решения выражения
    :param list_otv: список коэффициентов A,B
    :param workitem_server:
    :return: true - если решено правильно, false - если решено неверно
    '''
    Summ = solution_workitem(workitem_server)
    if Summ == list_otv[0] 
        return True
    return False


# Создаем очередь заданий
workitem_1 = workitem.WorkItem()
workitem_2 = workitem.WorkItem()
workitem_3 = workitem.WorkItem()
# Флаги, отвечающие за решенность задания
flag_1 = False
flag_2 = False
flag_3 = False
# Сервер
sock = socket.socket()
sock.bind(('', 9090))
sock.listen(1)
while True:
    while True:
        # Клиент подключается
        conn, addr = sock.accept()
        print("Клиент : успешно подключился к серверу заданий. Выдаем клиенту задание...", addr)
        if flag_1 == False:
            # Для сериализации через pickle необходимо коэффициенты засунуть в список
            list_K = [workitem_1.A, workitem_1.B]
            # сериализируем данные в байты
            data = pickle.dumps(list_K)
            # Отправляем задание в байтах клиенту
            conn.sendall(data)
            # Получаем от клиента решенное задание в байтах
            data = conn.recv(4096)
            # Десеализируем
            list_otv = pickle.loads(data)
            # Проверяем решение
            if test_workitem(workitem_1, list_otv):
                print("Первая задача успешно выполнена. Закрываем соединение...")
                flag_1 = True
                conn.close()
                break
            else:
                print("Первая задача не выполнена. Закрываем соединение... ")
                conn.close()
                break
        if flag_2 == False:
            # Для сериализации через pickle необходимо коэффициенты засунуть в список
            list_K = [workitem_2.A, workitem_2.B]
            # сериализируем данные в байты
            data = pickle.dumps(list_K)
            # Отправляем задание в байтах клиенту
            conn.sendall(data)
            # Получаем от клиента решенное задание в байтах
            data = conn.recv(4096)
            # Десеализируем
            list_otv = pickle.loads(data)
            # Проверяем решение
            if test_workitem(workitem_2, list_otv):
                print("Вторая задача успешно выполнена. Закрываем соединение...")
                flag_2 = True
                conn.close()
                break
            else:
                print("Вторая задача не выполнена. Закрываем соединение... ")
                conn.close()
                break
        if flag_3 == False:
            # Для сериализации через pickle необходимо коэффициенты засунуть в список
            list_K = [workitem_3.A, workitem_3.B]
            # сериализируем данные в байты
            data = pickle.dumps(list_K)
            # Отправляем задание в байтах клиенту
            conn.sendall(data)
            # Получаем от клиента решенное задание в байтах
            data = conn.recv(4096)
            # Десеализируем
            list_otv = pickle.loads(data)
            # Проверяем решение
            if test_workitem(workitem_3, list_otv):
                print("Третья задача успешно выполнена. Закрываем соединение...")
                flag_3 = True
                conn.close()
                break
            else:
                print("Третья задача не выполнена. Закрываем соединение... ")
                conn.close()
                break
       
        print("Все задачи успешно выполнены. Очередь заданий пустая. Необходимо перезапустить сервер...")
        conn.close()
