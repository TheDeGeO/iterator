from typing import List, Any
from ..interfaces.iterator_interface import Collection
from ..iterators.array_iterator import ArrayIterator

class ArrayCollection(Collection):
    def __init__(self, items: List[Any]):
        self._items = items

    def create_iterator(self) -> ArrayIterator:
        return ArrayIterator(self._items) 