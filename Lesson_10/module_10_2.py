from time import sleep
from threading import Thread


class Knight(Thread):
    def __init__(self, name, power):
        super().__init__()
        self.name = str(name)
        self.power = power
        self.num_of_warriors = 100

    def run(self):
        print(f"{self.name}, на нас напали!")
        num_of_days = 0
        while self.num_of_warriors > 0:
            sleep(1)
            num_of_days += 1
            self.num_of_warriors -= self.power
            print(f"{self.name} сражается {num_of_days} дней(дня), осталось {self.num_of_warriors} воинов")
        print(f"{self.name} одержал победу спустя {num_of_days} дней(дня)")


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight('Sir Galahad', 20)

first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()

print("Все битвы закончились")
