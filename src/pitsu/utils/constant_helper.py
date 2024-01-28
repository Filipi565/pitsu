from random import randint
from ..errors import ConstantError
from ..typing import Constant

class _constant_helper:
    def __init__(self, start = -50, end = 50):
        self.__values = list(range(start, end+1))
        self.__start = start
        self.__end = end
        self.__max_attempts = len(self.__values)
    
    def create(self) -> Constant:
        attempts = 0
        while True:
            number = randint(self.start, self.end)
            if attempts == self.__max_attempts:
                raise ConstantError(f"attempts passed of {self.__max_attempts}")
            try:
                value = self.__values[number]
                self.__values.remove(value)
                return value
            except:
                attempts += 1

    @property
    def start(self):
        return self.__start
    
    @property
    def end(self):
        return self.__end

Constant_Helper = type("Constant_Helper", (_constant_helper,), {})()