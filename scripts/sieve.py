import math
from sys import argv
from typing import Set


def sieve_of_eratosthenes(max_number: int) -> Set[int]:
    non_primes = set()
    primes = set()
    smallest_prime_factor = int(math.sqrt(max_number))
    for number in range(2, smallest_prime_factor + 1):
        if number in non_primes:
            continue

        primes.add(number)
        non_primes.update(gather_multiples(number, max_number))

    for number in range(smallest_prime_factor, max_number + 1):
        if number not in non_primes:
            primes.add(number)

    return primes


def gather_multiples(number: int, max_number: int) -> Set[int]:
    multiples = set()
    factor = 2
    for factor in range(number, max_number // number + 1):
        multiples.add(number * factor)
    return multiples


if len(argv) > 1 and argv[1].isnumeric():
    print(sorted(sieve_of_eratosthenes(int(argv[1]))))
