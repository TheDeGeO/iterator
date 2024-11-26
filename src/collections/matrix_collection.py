from typing import List, Any
from ..interfaces.iterator_interface import Collection
from ..iterators.matrix_iterator import MatrixIterator

class Matrix(Collection):
    def __init__(self, matrix: List[List[Any]]):
        self._matrix = matrix

    def create_iterator(self) -> MatrixIterator:
        return MatrixIterator(self._matrix) 