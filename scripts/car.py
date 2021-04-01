class Car:

    horn_sound: str = "Honk"
    _speed: float = 0.0

    def __init__(self, horn_sound: str = None) -> object:
        if horn_sound:
            self.horn_sound = horn_sound

    def accelerate(self, kmh: float = 0.0):
        self._speed = self._speed + kmh

    def brake(self, target_kmh: float = 0.0) -> None:
        if target_kmh < self._speed:
            self._speed = float(target_kmh)

    def honk(self) -> None:
        print(self.horn_sound)

    @property
    def speed(self) -> str:
        return f"{self._speed} km/h"


test_car = Car()
test_car.honk()
