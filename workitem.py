import random


class WorkItem():
    '''
    Рабочий элемент - "Решение системы"
    A1x + B1y = C1
    A2x + B2y = C2
    '''

    # Конструктор
    def __init__(self):
        self.A1 = random.randint(1, 100)
        self.B1 = random.randint(1, 100)
        self.C1 = random.randint(1, 100)
        self.A2 = random.randint(1, 100)
        self.B2 = random.randint(1, 100)
        self.C2 = random.randint(1, 100)

    x = 0
    y = 0
