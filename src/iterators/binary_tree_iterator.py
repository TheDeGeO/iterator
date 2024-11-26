from typing import Any
from ..interfaces.iterator_interface import Iterator

class Node:
    def __init__(self, value: Any):
        self.value = value
        self.left = None
        self.right = None

class BinaryTreeIterator(Iterator):
    def __init__(self, root: Node):
        self._stack = []
        self._current = root
        self._fill_stack()

    def _fill_stack(self):
        while self._current:
            self._stack.append(self._current)
            self._current = self._current.left

    def has_next(self) -> bool:
        return len(self._stack) > 0

    def next(self) -> Any:
        if not self.has_next():
            return None
        
        node = self._stack.pop()
        current = node.right
        self._current = current
        self._fill_stack()
        return node.value 