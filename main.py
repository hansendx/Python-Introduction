# Python course example snippets
# %% Yous should always declare your imports at the top of a module
import math
from typing import Generator, Iterable, List
from datetime import datetime, timedelta


# %% Python syntax: blocks


for number in range(1, 11):
    print(number)


# %% A statement to declare a variable

test = 1


# %% An expression made up of two expressions.

test_two = "a" + "{letter}c".format(letter="b")


# %% A statement with an expression.
formatted_number = "{0:05d}".format(1)
print(formatted_number)

# %% Decision making: if, elif, else
a_variable = []

if a_variable:
    print("That is a one.")
elif a_variable == 2:
    print("That is a two.")
else:
    print("That's too much, man!")

# %% Loops

for number in range(1, 11):
    print(number)

number = 1

while number <= 10:
    print(number)
    number = number + 1

# %% What is True?

some_truthy_values = [
    1,
    2,
    "A String",
    [1],
    [None],
    (1),
    {"a": 1},
    "",
    None,
    0,
    [],
    (),
    {},
]

for value in some_truthy_values:
    print("{} is {}".format(value, bool(value)))

# %% Build-in types

some_type_examples = [1, 0.0, True, ""]

for example in some_type_examples:
    print('"{}" is of type {}'.format(example, type(example)))

# %% Python is strongly typed

# "12" + 0.0


# %% Problem with numbers
print(0.1 + 0.2 == 0.3)
print(0.1 + 0.2)
print(math.isclose(0.1 + 0.2, 0.3))


# %% Lists

# You can create empty lists with [] and list()

# Or you can create a list with initial elements
numbers = [1, 2, 3, 4]
print(numbers)

# Lists are mutable
more_numbers = numbers
more_numbers.append(1)
print(numbers)

# %% Slicing

numbers_to_ten = list(range(1, 11))
numbers_to_fife = numbers_to_ten[:5]
numbers_from_fife = numbers_to_ten[5:]
print(numbers_to_fife)
print(numbers_from_fife)
print(numbers_to_ten[1:10:2])

# %% List comprehension

print([number for number in range(1, 10) if number % 2 == 0])
some_words = [words for words in "Here are some Words".split()]
# %% Dictionaries

class_age = {"Anne": 27, "John": 25, "Marie": 24, "Dan": 30}

input_string = input()

if input_string in class_age:
    print(f"{input_string} is {class_age[input_string]} years old.")
else:
    print(f"{input_string} is not in this class.")

# %% Dictionary comprehension

names = [name for name in class_age.keys()]
ages = list(class_age.values())
print(names)
print(ages)
class_ages_again = {name: age for name, age in zip(names, ages)}
print(class_ages_again)

# %% Sets

names_set = {"Jeff", "Cara", "Jeff", "Ben"}
names_set

if "Jeff" in names_set:
    print('"Jeff" is in names_set')

number_set = {1, 2, 3, 4}

if 4 in number_set:
    print("4 is in number_set")

# %% Tuples

names_tuple = ("Jeff", "Cara", "Ben")

tuple_dict = {names_tuple: "Some People"}


# %% Functions


def remove_even(numbers: Iterable[int]) -> List[int]:
    """Remove even numbers from an iterable of numbers."""
    cleaned_numbers = list()
    for number in numbers:
        if number % 2 != 0:
            cleaned_numbers.append(number)
    return cleaned_numbers


print(remove_even([1, 2, 3, 4]))
print(remove_even(range(1, 20)))

# %% Generators


def range_generator(start: int, stop: int, step: int = 1) -> Generator[int, None, None]:
    while start < stop:
        yield start
        start = start + step


gen = range_generator(1, 10)
print(next(gen))
print(next(gen))

# %% Classes


class SimpleClass(object):
    ATTRIBUTE = "World"

    @classmethod
    def class_method(cls) -> None:
        print(f"Hellow {cls.ATTRIBUTE}")

    @staticmethod
    def static_method() -> None:
        print("Hello someone.")


instance = SimpleClass()
instance.class_method()
instance.static_method()


# %% Objects

# class_age = {"Anne": 27, "John": 25, "Marie": 24, "Dan": 30}


class OnlineClass:
    name: str
    dates: List[datetime]

    def __init__(self, name: str, date: str, day_frequency: int, occurences: int) -> None:
        self.name = name

        self.dates = [datetime.strptime(date, "%d/%m/%y")]

        for time in range(1, occurences + 1):
            self.dates.append(self.dates[-1] + timedelta(days=day_frequency))


class Pupil:
    name: str
    age: int
    classes: List[OnlineClass]

    def __init__(self, name, age, _class) -> None:
        self.name = name
        self.age = age
        self.classes = [_class]

    def add_class(self, _class):
        self.classes.append(_class)

    def schedule(self):
        for _class in self.classes:
            print(_class.dates)


a_class = OnlineClass("english", "21/3/21", 7, 3)
b_class = OnlineClass("math", "22/3/21", 7, 4)
a_pupil = Pupil("Jeff", 15, a_class)

a_pupil.add_class(b_class)

a_pupil.schedule()


# %% Objects 2


class Range:
    start: int
    stop: int
    step: int

    def __init__(self, start: int, stop: int, step: int):
        self.start, self.stop, self.step = (start, stop, step)

    def generator(self) -> Generator[int, None, None]:
        while self.start < self.stop:
            yield self.start
            start = self.start + self.step

    def range_list(self) -> List[int]:
        return list(range(self.start, self.stop, self.step))


range_instance = Range(1, 20, 2)
print(range_instance.generator())
range_instance.range_list()

# %% CSV

from csv import DictWriter, DictReader

test_rows = [{"a": 1, "b": 2}, {"a": 40, "b": 34}]

with open("test.csv", "w") as test_file:
    test_writer = DictWriter(test_file, fieldnames=["a", "b"])
    test_writer.writeheader()
    for row in test_rows:
        test_writer.writerow(row)

# %%


def a(x: int, y: int):
    x + y


def b():
    a(1, "a")


from unittest import TestCase


class TestTest(TestCase):
    def test_a(self):
        self.assertEqual(2, a(1, 1))


b()


# %%
