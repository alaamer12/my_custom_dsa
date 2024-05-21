from dataclasses import dataclass
from typing import Optional, Callable
import threading


@dataclass
class __Node:
    data: int
    left: Optional['__Node'] = None
    right: Optional['__Node'] = None
    down: Optional['__Node'] = None

# TODO: Provide user functions
class NetDS:
    __instance = None
    __lock = threading.Lock()

    def __init__(self, sorted: bool = False, strict: bool = True, nsew: bool = False, standard: bool = False):
        """
        :param sorted: to make every line sorted nodes
        :param strict: to be able to delete the main line at certain conditions
        :param nsew: to make it all directions
        :param standard: to create the main line on initialization
        """

        self.__root: Optional['__Node'] = None
        self.__sorted = sorted
        self.__strict = strict
        self.__nsew = nsew
        self.__standard = standard
        self.__node_counter: int = 0
        self.__depth: int = 0
        self.__height: int = 0  # High is different from depth, if its nsew

    def __new__(cls, *args, **kwargs) -> 'NetDS':
        with cls.__lock:
            if cls.__instance is None:
                cls.__init_main_line(cls)
                cls.__instance = object.__new__(cls)
        return cls.__instance

    def __init_main_line(self) -> None:
        pass

    def __create_node(self, data) -> '__Node':
        pass

    def create_zero_node(self, data) -> '__Node':
        pass

    def insert(self, data) -> None:
        pass

    def __search(self, data, search_func: Callable) -> Optional[int]:
        pass

    def __delete(self, data, delete_func: Callable) -> None:
        pass

    # TODO: improve the traversing strategy
    def __traverse_from_right(self, traverse_to_func: Callable) -> None:
        pass

    def __traverse_from_left(self, traverse_to_func: Callable) -> None:
        pass


if __name__ == '__main__':
    net = NetDS()
    net.insert(0)
    net.insert(1)
    net.insert(2)
    net.insert(3)
    net.insert(4)
    # net.search(1, lambda x, y: x == y)
