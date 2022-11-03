import linecache
import os
import pickle
import time
import atexit

DATA_FILE_NAME = f"{__file__.split('.')[0]}.dat"
LOG_FILE_NAME = "log.txt"
SECONDS_TO_SLEEP = 1

line_number = 1


def on_exit():
    with open(DATA_FILE_NAME, "wb") as data_file:
        pickle.dump(line_number, data_file)


if __name__ == '__main__':
    atexit.register(on_exit)

    if os.path.isfile(DATA_FILE_NAME):
        with open(DATA_FILE_NAME, "rb") as data_file:
            data = pickle.load(data_file)
            line_number = data

    while True:
        line = linecache.getline(LOG_FILE_NAME, line_number)

        if line:
            print(line, end='')
            line_number += 1

        else:
            time.sleep(SECONDS_TO_SLEEP)
            linecache.checkcache(LOG_FILE_NAME)
