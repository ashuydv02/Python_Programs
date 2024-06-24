import asyncio
import time

# Program 1

async def coroutineEg1():
    print("hello")
    await asyncio.sleep(1)
    print("world")

# asyncio.run(coroutine1())


# Program 2

async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)


async def coroutineEg2():
    print(f"started at {time.strftime('%X')}")

    await say_after(1, "hello")
    await say_after(1, "world")

    print(f"finished at {time.strftime('%X')}")


# asyncio.run(coroutineEg2())
# print(dir(asyncio))

# Program 3 Example of coroutines in which we can run tasks simultaneously


async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)


async def coroutineEg3():
    task1 = asyncio.create_task(say_after(2, "hello"))
    task2 = asyncio.create_task(say_after(2, "world"))

    print(f"started at {time.strftime('%X')}")

    await task1
    await task2

    print(f"finished at {time.strftime('%X')}")


# asyncio.run(coroutineEg3())


# Running Tasks concurrently

async def factorial(name, number, n):
    f = 1
    for i in range(2, number + 1):
        print(f"Task {name}: Compute factorial({number}), currently i={i}...")
        await asyncio.sleep(n)
        f *= i
    print(f"Task {name}: factorial({number}) = {f}")
    return f


async def main():

    L = await asyncio.gather(
        factorial("A", 2, 3),
        factorial("B", 3, 2),
        factorial("C", 4, 1),
    )
    print(L)


asyncio.run(main())
