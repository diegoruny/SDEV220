from datetime import datetime
import multiprocessing
import time
import random

# Write the current date to today.txt
with open('today.txt', 'w') as file:
    file.write(datetime.now().strftime('%Y-%m-%d'))

# Read the content of today.txt into today_string
with open('today.txt', 'r') as file:
    today_string = file.read()

# Parse the date from today_string
parsed_date = datetime.strptime(today_string, '%Y-%m-%d')


def print_time():
    time.sleep(random.uniform(0, 1))  # Wait for a random number of seconds
    print(f"Current time: {datetime.now()}")

if __name__ == '__main__':
    processes = []
    for _ in range(3):
        process = multiprocessing.Process(target=print_time)
        processes.append(process)
        process.start()

    for process in processes:
        process.join()  # Wait for all processes to finish