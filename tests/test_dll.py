import pytest
from linked_list.double_linked_list \
    import Element, LinkedList, reverse_linked_list


def test_double_linked_list():
    linked_list = LinkedList()
    assert linked_list.length == 0
    linked_list.add_at_tail(1)
    assert linked_list.length == 1
    assert linked_list.tail.val == 1
    assert linked_list.tail.next is None
    linked_list.add_at_head(2)
    assert linked_list.length == 2
    assert linked_list.head.val == 2
    assert linked_list.head.prev is None
    linked_list.add_at_head(3)
    assert linked_list.length == 3
    assert linked_list.tail.val == 1
    assert linked_list.head.val == 3
    assert linked_list.head.next.val == 2
    linked_list.add_at_tail(4)
    assert linked_list.length == 4
    assert linked_list.tail.val == 4
    assert linked_list.tail.prev.val == 1
    assert linked_list.head.val == 3
    assert linked_list.get(0) == 3
    assert linked_list.get(1) == 2
    assert linked_list.get(2) == 1
    assert linked_list.get(3) == 4
    linked_list.add_at_index(4, 5)
    assert linked_list.tail.val == 5
    assert linked_list.length == 5
    assert linked_list.tail.prev.val == 4
    assert linked_list.head.val == 3
    linked_list.add_at_index(0, -1)
    assert linked_list.length == 6
    assert linked_list.head.val == -1
    assert linked_list.head.next.val == 3
    linked_list.add_at_index(1, -2)
    assert linked_list.length == 7
    assert linked_list.head.val == -1
    assert linked_list.tail.val == 5
    assert linked_list.get(1) == -2
    assert linked_list.get(2) == 3
    linked_list.delete_at_index(0)
    assert linked_list.length == 6
    assert linked_list.head.val == -2
    assert linked_list.get(0) == -2
    linked_list.delete_at_index(5)
    assert linked_list.length == 5
    assert linked_list.tail.val == 4
    assert linked_list.get(4) == 4
    linked_list.delete_at_index(1)
    assert linked_list.length == 4
    assert linked_list.head.val == -2
    assert linked_list.tail.val == 4
    assert linked_list.get(1) == 2


def test_reversed_linked_list():
    linked_list = LinkedList()
    linked_list.add_at_tail(1)
    linked_list.add_at_tail(2)
    linked_list.add_at_tail(3)
    assert linked_list.get(0) == 1
    assert linked_list.get(1) == 2
    assert linked_list.get(2) == 3
    reversed_linked_list = reverse_linked_list(linked_list)
    assert reversed_linked_list.get(0) == 3
    assert reversed_linked_list.get(1) == 2
    assert reversed_linked_list.get(2) == 1


def test_empty_linked_list():
    linked_list = LinkedList()
    assert linked_list.length == 0
    assert linked_list.get(1) == 'Index out of range'
    with pytest.raises(AttributeError):
        assert linked_list.head.value is None
    with pytest.raises(AttributeError):
        assert linked_list.tail.value is None
    linked_list.delete_at_index(1)
    assert linked_list.length == 0


def test_iteration():
    linked_list = LinkedList()
    linked_list.add_at_tail(2)
    linked_list.add_at_head(1)
    linked_list.add_at_tail(3)
    linked_list.add_at_tail(4)
    result = []
    for i in linked_list:
        result.append(i)
    assert result == [1, 2, 3, 4]
    linked_list = LinkedList()
    result = []
    for i in linked_list:
        result.append(i)
    assert result == []
