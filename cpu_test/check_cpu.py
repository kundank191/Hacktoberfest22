import time

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

def main():
    start_time = time.time()
    prime_count = 0
    max_number = 1000000  # Adjust this value to control the intensity of the test

    for number in range(2, max_number):
        if is_prime(number):
            prime_count += 1

    end_time = time.time()
    elapsed_time = end_time - start_time

    print(f"Prime numbers found: {prime_count}")
    print(f"Elapsed time: {elapsed_time:.2f} seconds")

if __name__ == "__main__":
    main()
