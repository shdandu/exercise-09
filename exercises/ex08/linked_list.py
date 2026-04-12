from __future__ import annotations

__author__ = "730705811"

"""Create Node class and functions."""


class Node:
    """Node in a singly-linked list recursive structure."""

    value: int
    next: Node | None

    def __init__(self, value: int, next: Node | None):
        """Initalize Node."""
        self.value = value
        self.next = next

    def __str__(self) -> str:
        """Return everything in Node."""
        if self.next is None:
            return f"{self.value} -> None"
        else:
            return f"{self.value} -> {self.next}"


courses: Node = Node(110, Node(210, Node(211, None)))
print(courses)


def value_at(head: Node | None, index: int) -> int:
    """Value at an index."""
    if head is None:
        raise IndexError("Index is out of bounds on the list.")
    if index == 0:
        return head.value
    else:
        return value_at(head.next, index - 1)


def max(head: Node | None) -> int:
    """Max value."""
    if head is None:
        raise ValueError("Cannot call max with None")
    if head.next is None:
        return head.value
    check_max = max(head.next)
    if head.value > check_max:
        return head.value
    else:
        return check_max


def linkify(items: list[int]) -> Node | None:
    """Link item."""
    if len(items) == 0:
        return None
    return Node(items[0], linkify(items[1:]))


def scale(head: Node | None, factor: int) -> Node | None:
    """Multiply every item by a factor."""
    if head is None:
        return None
    return Node(head.value * factor, scale(head.next, factor))
