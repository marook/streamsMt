from .messages import isEndMessage, END_MESSAGE

def queueAsIterator(queue):
    while True:
        msg = queue.get()

        if(isEndMessage(msg)):
            break

        yield msg

def iterableToQueue(iterable, queue):
    try:
        for v in iterable:
            queue.put(v)
    finally:
        queue.put(END_MESSAGE)
