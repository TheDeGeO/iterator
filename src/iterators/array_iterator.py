from typing import List, Any
from ..interfaces.iterator_interface import Iterator

class ArrayIterator(Iterator):
    def __init__(self, array: List[Any]):
        self._array = array
        self._position = 0

    def has_next(self) -> bool:
        return self._position < len(self._array)

    def next(self) -> Any:
        if self.has_next():
            item = self._array[self._position]
            self._position += 1
            return item
        return None 