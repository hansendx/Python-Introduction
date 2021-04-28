from .fibonacci import fibonacci

from unittest import TestCase

TEST_CASE = TestCase()


def test_fibonacci() -> None:
    result = list(fibonacci(numbers_to_produce=10))
    assert result[0] == 0
    TEST_CASE.assertListEqual([0, 1, 1, 2, 3, 5, 8, 13, 21, 34], result)
    expected = 64202014863723094126901777428873111802307548623680
    TEST_CASE.assertEqual(expected, list(fibonacci(300))[240])
