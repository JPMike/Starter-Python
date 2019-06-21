import asyncio


def make_done(future, result):
    print(f'setting future result to {result}')
    # result save to future object for later retrieval
    future.set_result(result)


if __name__ == '__main__':
    event_loop = asyncio.get_event_loop()
    try:
        # A Future represents the result of work that has not been completed yet
        all_done = asyncio.Future()

        print('scheduling mark_done')
        event_loop.call_soon(make_done, all_done, 'the result')

        print('entering event loop')
        result = event_loop.run_until_complete(all_done)
        print(f'returned result: {result}')
    finally:
        print('closing event loop')
        event_loop.close()

    print(f'future result: {all_done.result()}')
