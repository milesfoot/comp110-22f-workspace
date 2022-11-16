from __future__ import annotations

from typing import Optional


class Node:
    data: int
    # next: Union[Node, None]
    next: Optional[Node]

    def __init__(self, data: int, next: Optional[Node]):
        self.data = data
        self.next = next


    def __str__(self) -> str:
        if self.next is None:
            return f"{self.data} -> None"
        else: 
            return f"{self.data} -> {self.next.__str__()}"

    def sum(node: Optional[Node]) -> int:
        # could use loop
        if node is None:
            return 0
        else: 
            return node.data + sum(node.next)


    def count(node: Optional[Node], current_count: int = 0) -> int:
        if node is None:
            return current_count + 1
        else:
            return count(node.next, current_count + 1)


head: Node = Node(3, None)
head = Node(2, None)
head = Node(1, head)
print(sum(head))
