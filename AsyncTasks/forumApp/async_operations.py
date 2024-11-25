import asyncio
import time

async def get_milk():
    print("Servant is going to get milk...")
    await asyncio.sleep(1)  # Simulates 1 second to get milk
    print("Servant got the milk.")

async def get_coffee():
    print("Servant is going to get coffee...")
    await asyncio.sleep(1.5)  # Simulates 1.5 seconds to get coffee
    print("Servant got the coffee.")

async def prepare_drink():
    print("Servant is preparing the drink...")
    await asyncio.sleep(0.5)  # Simulates 0.5 seconds to prepare the drink
    print("Servant prepared the drink.")

async def serve(i):
    start_time = time.time()

    # Run get_milk and get_coffee concurrently
    await asyncio.gather(get_milk(), get_coffee())

    # Prepare the drink after both tasks are complete
    await prepare_drink()

    total_time = time.time() - start_time
    print(f"Total time taken: {total_time:.2f} seconds, TASK {i}")

async def main():
    start_time = time.time()
    await asyncio.gather(*[serve(i) for i in range(10)])
    end_time = time.time()

    print(f"Total time needed {end_time - start_time}")

if __name__ == "__main__":
    asyncio.run(main())