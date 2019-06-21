import asyncio


# an object is an awaitable object if it can be used in an await expression
# 3 main types of awaitable objects: coroutines, Tasks, and Futures

# the term 'coroutine' can be used for two closely related concepts
# a coroutine function: an async def function
# a coroutine object: an object returned by calling a coroutine function

async def nested():
    return 42


async def main():
    # if call like this, nested() function won't run, a coroutine object is created but not awaited
    # nested()

    # run like this, coroutines can be awaited from other coroutines
    print(await nested())

    # Tasks are used to schedule coroutines concurrently
    # wrap the coroutine into a Task and schedule its execution, return the Task object
    task = asyncio.create_task(nested())
    print(await task)

    # A Future is a special low level awaitable object that represents an eventual result of an asynchronous operation
    # When a Future object is awaited it means that the coroutine will wait
    # until the Future is resolved in some other place
    # normally no need to create Future objects at the application level code


if __name__ == '__main__':
    # asyncio.run() function creates a new event loop and closes it at the end
    # used as a main entry point for asyncio programs
    # cannot be called when another asyncio event loop is running in the same thread
    asyncio.run(main())
