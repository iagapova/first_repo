from collections import deque

MAX_LEN = 5

lifo = deque(maxlen=MAX_LEN)


def push(element):
    return lifo.appendleft(element)


def pop():
    return lifo.popleft()
