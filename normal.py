import time
import threading
import asyncio

# 🔹 Decorator to measure execution time
def timing(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        print(f"{func.__name__} took {time.time() - start:.4f}s")
        return result
    return wrapper


# 🔹 Generator (data stream simulation)
def data_generator(n):
    for i in range(n):
        yield i


# 🔹 Class with advanced features
class DataProcessor:
    def __init__(self):
        self.data = []

    def add_data(self, value):
        self.data.append(value)

    def __str__(self):
        return f"DataProcessor with {len(self.data)} items"

    def process(self):
        return [x * x for x in self.data]


# 🔹 Multithreading function
def threaded_task(name):
    for i in range(3):
        print(f"Thread {name}: {i}")
        time.sleep(1)


# 🔹 Async function
async def async_task(name, delay):
    print(f"Async task {name} started")
    await asyncio.sleep(delay)
    print(f"Async task {name} finished")


# 🔹 Main advanced function
@timing
def main():
    print("Starting Advanced Program...\n")

    # 1. Generator usage
    gen = data_generator(5)

    # 2. Class usage
    processor = DataProcessor()

    for value in gen:
        processor.add_data(value)

    print(processor)

    # 3. Processing data
    result = processor.process()
    print("Processed Data:", result)

    # 4. File handling
    with open("output.txt", "w") as f:
        f.write(str(result))

    # 5. Multithreading
    t1 = threading.Thread(target=threaded_task, args=("A",))
    t2 = threading.Thread(target=threaded_task, args=("B",))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    # 6. Async tasks
    asyncio.run(run_async_tasks())

    print("\nProgram Finished!")


# 🔹 Async runner
async def run_async_tasks():
    await asyncio.gather(
        async_task("X", 2),
        async_task("Y", 1)
    )


# 🔹 Run program
if __name__ == "__main__":
    main()