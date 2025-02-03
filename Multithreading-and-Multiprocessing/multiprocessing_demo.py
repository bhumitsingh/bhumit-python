## Processes that run in parallel
### CPU-Bound tasks: Tasks that are heavy on CPU usage (eg., Mahematical computations, Data Processing).
## parallel Execution: Multiple cores of the CPU

import multiprocessing
import time

def square_numbers():
    for i in range(5):
        time.sleep(1.5)
        print(f"Square : {i*i}")

def cube_numbers():
    for i in range(5):
        time.sleep(1.5)
        print(f"Cube : {i*i*i}")


if __name__ == "__main__":
    # Create Two Processes
    p1 = multiprocessing.Process(target = square_numbers)
    p2 = multiprocessing.Process(target = cube_numbers)

    t = time.time()
    ## Start the processes
    p1.start()
    p2.start()

    ## Wait for the processes to complete
    p1.join()
    p2.join()

    finished_time = time.time()-t
    print(finished_time)