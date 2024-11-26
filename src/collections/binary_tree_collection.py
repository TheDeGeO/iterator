from ..interfaces.iterator_interface import Collection
from ..iterators.binary_tree_iterator import BinaryTreeIterator, Node

class BinaryTree(Collection):
    def __init__(self, root: Node):
        self._root = root

    def create_iterator(self) -> BinaryTreeIterator:
        return BinaryTreeIterator(self._root) 