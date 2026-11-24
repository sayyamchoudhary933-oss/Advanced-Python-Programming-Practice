
import threading
import time

def count_numbers():
    for i in range(1, 6):
        print("Counting:", i)
        time.sleep(0.5)

def calculate_squares():
    for i in range(1, 6):
        print("Square of", i, "=", i * i)
        time.sleep(0.5)

def calculate_cubes():
    for i in range(1, 6):
        print("Cube of", i, "=", i * i * i)
        time.sleep(0.5)

if __name__ == "__main__":
    t1 = threading.Thread(target=count_numbers)
    t2 = threading.Thread(target=calculate_squares)
    t3 = threading.Thread(target=calculate_cubes)

    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()

    print("All tasks completed.")
