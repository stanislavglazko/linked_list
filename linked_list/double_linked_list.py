class Element:
    def __init__(self, val, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next

    def __repr__(self):
        return str(self.__dict__)

    def __str__(self):
        return str(self.__dict__)


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __str__(self):
        return str(self.head.__dict__)

    def __iter__(self):
        head = self.head
        while head:
            yield head.val
            head = head.next

    def add_at_tail(self, val):
        new_element = Element(val)
        if not self.tail:
            self.tail = new_element
            self.head = new_element
            self.length += 1
            return
        new_element.prev = self.tail
        new_element.next = None
        self.tail.next = new_element
        self.tail = new_element
        self.length += 1

    def add_at_head(self, val):
        new_element = Element(val)
        if not self.head:
            self.head = new_element
            self.tail = new_element
            self.length += 1
            return
        new_element.next = self.head
        new_element.prev = None
        self.head.prev = new_element
        self.head = new_element
        self.length += 1

    def add_at_index(self, index, val):
        if index == self.length:
            self.add_at_tail(val)
            return
        elif index == 0:
            self.add_at_head(val)
            return
        elif index > self.length:
            return
        new_element = Element(val)
        counter = 0
        if index <= self.length // 2:
            current_element = self.head
            while counter != index:
                current_element = current_element.next
                counter += 1
        else:
            current_element = self.tail
            while counter != (self.length - index - 1):
                current_element = current_element.prev
                counter += 1
        new_element.next = current_element
        new_element.prev = current_element.prev
        current_element.prev.next = new_element
        current_element.prev = new_element
        self.length += 1

    def get(self, index):
        if index >= self.length:
            return 'Index out of range'
        counter = 0
        if index <= self.length // 2:
            current_element = self.head
            while counter != index:
                current_element = current_element.next
                counter += 1
        else:
            current_element = self.tail
            while counter != (self.length - 1 - index):
                current_element = current_element.prev
                counter += 1
        return current_element.val

    def delete_at_index(self, index):
        if index >= self.length:
            return
        if self.length == 1:
            self.head = None
            self.tail = None
            self.length = 0
            return
        if index == 0:
            new_head = self.head.next
            new_head.prev = None
            self.head = new_head
            self.length -= 1
            return
        if index == self.length - 1:
            new_tail = self.tail.prev
            new_tail_next = None # noqa
            self.tail = new_tail
            self.length -= 1
            return
        counter = 0
        if index <= self.length // 2:
            current_element = self.head
            while counter != index:
                current_element = current_element.next
                counter += 1
        else:
            current_element = self.tail
            while counter != (self.length - index - 1):
                current_element = current_element.prev
                counter += 1
        current_element.prev.next, current_element.next.prev = \
            current_element.next, current_element.prev
        self.length -= 1


def reverse_linked_list(linked_list):
    reversed_linked_list = LinkedList()
    length = linked_list.length
    counter = 0
    current_element = linked_list.tail
    while counter != length:
        reversed_linked_list.add_at_tail(current_element.val)
        current_element = current_element.prev
        counter += 1
    return reversed_linked_list


linked_list = LinkedList()
linked_list.add_at_tail(2)
linked_list.add_at_head(1)
linked_list.add_at_tail(3)
linked_list.add_at_tail(4)

iterator = iter(linked_list)
a = iterator.__next__()
b = iterator.__next__()
c = iterator.__next__()
print([a, b, c])
new_iterator = iter(linked_list)
answer = []
for i in new_iterator:
    answer.append(i)
print(answer)
