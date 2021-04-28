from sys import argv
from typing import Generator


def fibonacci(numbers_to_produce: int) -> Generator[int, None, None]:
    current = 0
    next = 1
    for _ in range(0, numbers_to_produce):
        yield current
        next, current = (current + next, next)


def cli():
    if len(argv) > 1 and argv[1].isnumeric():
        for number in fibonacci(int(argv[1])):
            print(number)


if __name__ == "__main__":
    if len(argv) > 1 and argv[1].isnumeric():
        for number in fibonacci(int(argv[1])):
            print(number)
