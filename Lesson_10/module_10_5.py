import datetime
import multiprocessing


def read_info(name):
    all_data = []
    with open(name) as file:
        while True:
            line = file.readline()
            all_data.append(line)
            if not line:
                break


filenames = [f'./file {number}.txt' for number in range(1, 5)]
# линейный вызов (0:00:12.539914)
start1 = datetime.datetime.now()
for filename in filenames:
    read_info(filename)
end1 = datetime.datetime.now()
print(end1 - start1)

# многопроцессный вызов (0:00:08.721998)
if __name__ == '__main__':
    with multiprocessing.Pool(processes=4) as pool:
        start2 = datetime.datetime.now()
        pool.map(read_info, filenames)
    end2 = datetime.datetime.now()
    print(end2 - start2)
