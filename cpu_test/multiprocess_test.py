import time
import multiprocessing

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def find_primes(start, end, result_queue):
    prime_count = 0
    for number in range(start, end):
        if is_prime(number):
            prime_count += 1
    result_queue.put(prime_count)

def main():
    num_threads = 4  # Adjust the number of threads as needed
    max_number = 10000000  # Adjust this value to control the intensity of the test

    chunk_size = max_number // num_threads
    result_queue = multiprocessing.Queue()
    processes = []

    start_time = time.time()

    for i in range(num_threads):
        start = i * chunk_size + 2
        end = start + chunk_size if i < num_threads - 1 else max_number
        process = multiprocessing.Process(target=find_primes, args=(start, end, result_queue))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()

    prime_count = sum(result_queue.get() for _ in range(num_threads))

    end_time = time.time()
    elapsed_time = end_time - start_time

    print(f"Prime numbers found: {prime_count}")
    print(f"Elapsed time: {elapsed_time:.2f} seconds")

if __name__ == "__main__":
    main()
