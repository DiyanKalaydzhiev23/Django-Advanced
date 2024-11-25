import time

def get_milk():
    print("Servant is going to get milk...")
    time.sleep(1)  # Simulates 1 second to get milk
    print("Servant got the milk.")

def get_coffee():
    print("Servant is going to get coffee...")
    time.sleep(1.5)  # Simulates 1.5 seconds to get coffee
    print("Servant got the coffee.")

def prepare_drink():
    print("Servant is preparing the drink...")
    time.sleep(0.5)  # Simulates 0.5 seconds to prepare the drink
    print("Servant prepared the drink.")

def serve(i):
    start_time = time.time()

    get_milk()
    get_coffee()
    prepare_drink()

    total_time = time.time() - start_time
    print(f"Total time taken: {total_time:.2f} seconds, TASK {i}")

if __name__ == "__main__":
    [serve(i) for i in range(10)]