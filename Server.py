import socket
import workitem
import pickle


def solution_workitem(workitem):
    '''
    Решение системы
    :param workitem: workitem
    :return: x, y
    '''
    d = workitem.A1 * workitem.B2 - workitem.A2 * workitem.B1
    dx = workitem.C1 * workitem.B2 - workitem.C2 * workitem.B1
    dy = workitem.A2 * workitem.C1 - workitem.A1 * workitem.C2
    x = dx / d
    y = dy / d
    return x, y


def test_workitem(workitem_server, list_otv):
    '''
    Проверка решения системы
    :param list_otv: список коэффициентов уравнения A1,B1...B2,C2
    :param workitem_server:
    :return: true - если решено правильно, false - если решено неверно
    '''
    # Сервер решает систему уравнений
    x, y = solution_workitem(workitem_server)
    if x == list_otv[0] and y == list_otv[1]:
        return True
    return False


# Создаем очередь заданий
workitem_1 = workitem.WorkItem()
workitem_2 = workitem.WorkItem()
workitem_3 = workitem.WorkItem()
workitem_4 = workitem.WorkItem()
# Флаги, отвечающие за решенность задания
flag_1 = False
flag_2 = False
flag_3 = False
flag_4 = False
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
            list_K = [workitem_1.A1, workitem_1.B1, workitem_1.C1, workitem_1.A2, workitem_1.B2, workitem_1.C2]
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
            list_K = [workitem_2.A1, workitem_2.B1, workitem_2.C1, workitem_2.A2, workitem_2.B2, workitem_2.C2]
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
            list_K = [workitem_3.A1, workitem_3.B1, workitem_3.C1, workitem_3.A2, workitem_3.B2, workitem_3.C2]
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
        if flag_4 == False:
            # Для сериализации через pickle необходимо коэффициенты засунуть в список
            list_K = [workitem_4.A1, workitem_4.B1, workitem_4.C1, workitem_4.A2, workitem_4.B2, workitem_4.C2]
            # сериализируем данные в байты
            data = pickle.dumps(list_K)
            # Отправляем задание в байтах клиенту
            conn.sendall(data)
            # Получаем от клиента решенное задание в байтах
            data = conn.recv(4096)
            # Десеализируем
            list_otv = pickle.loads(data)
            # Проверяем решение
            if test_workitem(workitem_4, list_otv):
                print("Четвертая задача успешно выполнена. Закрываем соединение...")
                flag_4 = True
                conn.close()
                break
            else:
                print("Четвертая задача не выполнена. Закрываем соединение... ")
                conn.close()
                break
        print("Все задачи успешно выполнены. Очередь заданий пустая. Необходимо перезапустить сервер...")
        conn.close()
