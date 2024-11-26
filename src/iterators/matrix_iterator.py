from typing import List, Any
from ..interfaces.iterator_interface import Iterator

class MatrixIterator(Iterator):
    def __init__(self, matrix: List[List[Any]]):
        self._matrix = matrix
        self._row = 0
        self._col = 0

    def has_next(self) -> bool:
        return self._row < len(self._matrix)

    def next(self) -> Any:
        if not self.has_next():
            return None

        item = self._matrix[self._row][self._col]
        self._col += 1
        
        if self._col >= len(self._matrix[self._row]):
            self._col = 0
            self._row += 1
            
        return item 