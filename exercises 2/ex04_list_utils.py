""""""

__author__ = "730705811"


def all(check_list: list[int], x: int) -> bool:
    # Checks if all the values in the list match the int
    idx: int = 0
    if len(check_list) == 0:
        return False
    while idx < len(check_list):
        if x != check_list[idx]:
            return False
        idx += 1
    return True


def max(check_list: list[int]) -> int:
    # Raises an error if the list is empty
    if len(check_list) == 0:
        raise ValueError("max() arg is an empty List")
    idx: int = 0
    max_value: int = 0
    # Returns max value in the list
    while idx < len(check_list):
        if check_list[idx] > max_value:
            max_value = check_list[idx]
        idx += 1
    return max_value


def is_equal(check_list: list[int], new_list: list[int]) -> bool:
    # Returns True if the lists are the same
    idx: int = 0
    while idx < len(new_list):
        if new_list[idx] != check_list[idx] or len(new_list) != len(check_list):
            return False
        idx += 1
    return True


def extend(a: list[int], b: list[int]) -> None:
    idx: int = 0
    while idx < len(b):
        a.append(b[idx])
        idx += 1
    print(a)
