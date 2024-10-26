import time
import multiprocessing

def read_info(name):
    all_data = []
    with open(name, 'r') as f:
        line = f.readline()
        while line:
            all_data.append(line.strip())
            line = f.readline()

if __name__ == '__main__':
    filenames = [f'./file {number}.txt' for number in range(1, 5)]

    # Линейный вызов
    start_time = time.time()
    for filename in filenames:
        read_info(filename)
    end_time = time.time()
    linear_time = end_time - start_time

    print(f'Линейный вызов: {linear_time}')


    # Многопроцессный вызов
    # start_time = time.time()
    # with multiprocessing.Pool(processes=multiprocessing.cpu_count()) as pool:
    #     pool.map(read_info, filenames)
    # end_time = time.time()
    # multiprocessing_time = end_time - start_time
    # print(f'Многопроцессный вызов: {multiprocessing_time}')


