import time
import cProfile
import asyncio


# Example 1 by Python time module
def demo():
    start = time.time()
    print("Time consumed")
    end = time.time()
    print("Demo() function takes", end-start, "seconds")


demo()

# Example 2 by Python cProfile
async def f():
    await asyncio.sleep(2)
    print("hello")


cProfile.run('asyncio.run(f())')
