import time

n_values = [10, 100, 1000, 10000, 100000]

def for_loop(n):
    sum = 0
    for i in range(1, n+1):
        sum += i
    return sum

def while_loop(n):
    sum = 0
    i = 1
    while i <= n:
        sum += i
        i += 1
    return sum

for n in n_values:
    start_time = time.time()
    result = for_loop(n)
    end_time = time.time()
    time_total = end_time - start_time
    print(f"For loop sum of {n} numbers: {result},  time: {time_total:.6f} seconds")

    start_time = time.time()
    result = while_loop(n)
    end_time = time.time()
    time_total = end_time - start_time
    print(f"While loop sum of {n} numbers: {result},  time: {time_total:.6f} seconds")