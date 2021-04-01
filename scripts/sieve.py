
from sys import argv
from typing import Set


def sieve_of_eratosthenes(max_number: int):
    non_primes = set()
    primes = set()
    for number in list(range(2, max_number+1)):
        if number in non_primes:
            continue

        primes.add(number)
        non_primes.update(sieve_multiples(number, max_number))

    return primes


def sieve_multiples(number: int, max_number: int) -> Set[int]:
    multiples = set()
    factor = 2
    for factor in range(number, max_number//number + 1):
        multiples.add(number*factor)
    return multiples

if len(argv) > 1 and argv[1].isnumeric():
    print(sorted(sieve_of_eratosthenes(int(argv[1]))))
