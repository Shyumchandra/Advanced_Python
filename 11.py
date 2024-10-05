import concurrent.futures

def do_something(num):
    print(f"doing something with {num}")
with concurrent.futures.ThreadPoolExecutor() as executor:
    for num in range(10):
        executor.submit(do_something,num)