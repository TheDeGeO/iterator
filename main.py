from src.collections.array_collection import ArrayCollection
from src.collections.binary_tree_collection import BinaryTree
from src.collections.matrix_collection import Matrix
from src.iterators.binary_tree_iterator import Node
from src.interfaces.iterator_interface import Collection

def print_collection(collection: Collection):
    iterator = collection.create_iterator()
    while iterator.has_next():
        print(iterator.next(), end=" ")
    print()

def main():
    # Prueba con array
    array = ArrayCollection([1, 2, 3, 4, 5])
    print("Array:", end=" ")
    print_collection(array)

    # Prueba con árbol binario
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    tree = BinaryTree(root)
    print("Árbol binario:", end=" ")
    print_collection(tree)

    # Prueba con matriz
    matrix = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    print("Matriz:", end=" ")
    print_collection(matrix)

if __name__ == "__main__":
    main() 