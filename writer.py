import time
from datetime import datetime

SECONDS_TO_SLEEP = 2
STARTING_LINES_NUM = 1000 * 1000
LOG_FILE_NAME = "log.txt"


if __name__ == '__main__':
    with open(LOG_FILE_NAME, "w") as file:
        file.write(f"start\n")
        for l in range(STARTING_LINES_NUM):
            file.write(f"{l}\n")

    print("file initialized")

    while True:
        with open(LOG_FILE_NAME, "a") as file:
            file.write(f"{datetime.now()}\n")

        time.sleep(SECONDS_TO_SLEEP)
