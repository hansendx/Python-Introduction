from sys import argv
from typing import Generator


def fibonacci(numbers_to_produce: int) -> Generator[int, None, None]:
    last = 0
    current = 1
    for _ in range(0, numbers_to_produce):
        yield current
        current, last = (last + current, current)

if __name__ == "__main__":
    if len(argv) > 1 and argv[1].isnumeric():
        for number in fibonacci(int(argv[1])):
            print(number)
