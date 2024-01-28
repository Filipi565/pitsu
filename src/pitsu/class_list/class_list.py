from ..errors import ClassError

class Class_List:
    def __init__(self):
        self.__v: list[str] = list()

    def __iter__(self):
        return iter(self.__v)

    def append(self, obj: str):
        if not isinstance(obj, str):
            raise ClassError(f"expected str, not {type(obj).__name__}")

        self.__v.append(obj)
    
    def remove(self, obj: str):
        if not isinstance(obj, str):
            raise ClassError(f"expected str, not {type(obj).__name__}")

        self.__v.remove(obj)
    
    def clear(self):
        self.__v.clear()