import asyncio
import random
import time


# asyncio queue is not thread safe

async def worker(name, queue):
    while True:
        # get an work item out of the queue
        # the normal get method is coroutine, will wait if the queue is empty
        sleep_for = await queue.get()

        # simulate work time
        await asyncio.sleep(sleep_for)

        # notify the queue that the work item has been processed
        # task_done() indicate that a formerly enqueued task is complete. Used by queue consumers
        queue.task_done()

        print(f'{name} has slept for {sleep_for:.2f} seconds')


async def main():
    # create a queue to store work
    queue = asyncio.Queue()

    # generate random time to simulate the work
    total_sleep_time = 0
    for _ in range(20):
        sleep_for = random.uniform(0.05, 1.0)
        total_sleep_time += sleep_for
        # put an item into the queue without blocking
        queue.put_nowait(sleep_for)

    # create three worker tasks to process the queue concurrently
    tasks = []
    for i in range(3):
        task = asyncio.create_task(worker(f'worker-{i}', queue))
        tasks.append(task)

    started_at = time.monotonic()
    # wait until the queue is fully processed
    # join() is coroutine, block until all items in the queue have been received and processed
    await queue.join()
    total_slept_for = time.monotonic() - started_at

    # cancel worker tasks
    for task in tasks:
        task.cancel()

    # wait until all worker tasks are cancelled
    await asyncio.gather(*tasks, return_exceptions=True)

    print('===')
    print(f'3 workers slept in parallel for {total_slept_for:.2f} seconds')
    print(f'total expected sleep time:  {total_sleep_time:.2f} seconds')


if __name__ == '__main__':
    asyncio.run(main())
