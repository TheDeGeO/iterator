from abc import ABC, abstractmethod
from typing import Any

class Iterator(ABC):
    @abstractmethod
    def has_next(self) -> bool:
        pass
    
    @abstractmethod
    def next(self) -> Any:
        pass

class Collection(ABC):
    @abstractmethod
    def create_iterator(self) -> Iterator:
        pass 