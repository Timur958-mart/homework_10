import time
from datetime import datetime
from threading import Thread


def write_words(word_count, file_name):
    for i in range(1, word_count + 1):
        with open(file_name, 'a', encoding='utf-8') as file:
            file.write(f"Какое-то слово № {i}\n")
        time.sleep(0.1)
    print(f"Завершилась запись в файл {file_name}")


start_time_1 = datetime.now()
write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')
end_time_1 = datetime.now()
res_time_1 = end_time_1 - start_time_1
print(f"Время работы функций {res_time_1}")

start_time_2 = datetime.now()
thr_first = Thread(target=write_words, args=(10, 'example5.txt'))
thr_second = Thread(target=write_words, args=(30, 'example6.txt'))
thr_third = Thread(target=write_words, args=(200, 'example7.txt'))
thr_fourth = Thread(target=write_words, args=(100, 'example8.txt'))

thr_first.start()
thr_second.start()
thr_third.start()
thr_fourth.start()

thr_first.join()
thr_second.join()
thr_third.join()
thr_fourth.join()

end_time_2 = datetime.now()
res_time_2 = end_time_2 - start_time_2
print(f"Время работы потоков {res_time_2}")
