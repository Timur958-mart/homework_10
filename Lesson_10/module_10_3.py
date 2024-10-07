from threading import Thread, Lock
from random import randint
from time import sleep


class Bank():

    def __init__(self):
        self.balance = 0
        self.lock = Lock()

    def deposit(self):
        for i in range(100):
            x = randint(50, 500)
            self.balance += x
            print(f"Пополнение: {x}. Баланс: {self.balance}")
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            sleep(0.001)

    def take(self):
        for j in range(100):
            y = randint(50, 500)
            print(f"Запрос на {y}")
            if y <= self.balance:
                self.balance -= y
                print(f"Снятие: {y}. Баланс: {self.balance}")
            else:
                print(f"Запрос отклонён, недостаточно средств")
                self.lock.acquire()


bk = Bank()

th1 = Thread(target=Bank.deposit, args=(bk,))
th2 = Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()

th1.join()
th2.join()

print(f"Итоговый баланс: {bk.balance}")

