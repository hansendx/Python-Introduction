from unittest import TestCase

from scripts.car import Car


class TestCars(TestCase):
    """All tests for the Car class."""

    test_car: Car

    def setUp(self) -> None:
        """Set up a reference car."""
        self.test_car = Car()
        return super().setUp()

    def test_acceleration(self) -> None:
        """Can we accelerate the car?"""
        self.test_car.accelerate(10)
        expected = "10.0 km/h"
        self.assertEqual(expected, self.test_car.speed)

    def test_braking(self) -> None:
        """Does braking work as expected?"""
        self.test_car.accelerate(100)
        self.test_car.brake(20)
        expected = "20.0 km/h"
        self.assertEqual(expected, self.test_car.speed)
        # Should not get faster, when braking
        self.test_car.brake(30)
        self.assertEqual(expected, self.test_car.speed)

    def test_horn(self) -> None:
        """Can we use horn and set its tone?"""
        expected = "Honk"
        self.assertEqual(expected, self.test_car.horn_sound)
        different_car = Car(horn_sound="Honk!")

        reference_horn = self.test_car.horn_sound
        new_horn = different_car.horn_sound
        self.assertNotEqual(reference_horn, new_horn)

        self.assertEqual(f"{expected}!", different_car.horn_sound)
