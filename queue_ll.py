class Element:

    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class CustomQueue:

    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def enqueue(self, value):
        """
        This operation adds a new element at the end of queue.
        Runtime is O(1) since the self.tail points to the end of queue.
        :parameter value: Data to be added to the queue.
        """
        new_element = Element(value)
        if self.head is None:
            self.head = new_element
        elif self.tail:
            prev_element = self.tail
            prev_element.next = new_element
            new_element.prev = prev_element
        self.tail = new_element
        self.length += 1

    def dequeue(self):
        """
        Runtime O(1) since the first element is available at head.
        :return: The very first element of the queue and removes it.
        """
        if self.head:
            first_element = self.head
            self.head = first_element.next
            self.head.prev = None
            first_element.next = None
            first_element.prev = None
            self.length -= 1
            return first_element.value
        else:
            return None

    def peek(self):
        """
        :return: The element at the beginning of queue without removing it.
        Runtime O(1) since the first element is available at head.
        """
        return self.head.value

    def len(self):
        """
        :return: The length of the queue.
        Runtime is O(1) as the length is maintained by operations.
        """
        return self.length

    def __str__(self):
        if self.head:
            queue_list = []
            current_element = self.head
            while current_element:
                queue_list.append(str(current_element.value))
                current_element = current_element.next
            return ", ".join(queue_list)


def main():
    queue = CustomQueue()
    assert queue.dequeue() is None
    queue.enqueue(5)
    queue.enqueue(9)
    queue.enqueue(2)
    assert queue.dequeue() == 5
    assert queue.peek() == 9
    assert queue.len() == 2
    queue.enqueue(3)
    queue.enqueue(1)
    queue.enqueue(7)
    print(queue)
    queue.dequeue()
    print(queue)


if __name__ == '__main__':
    main()
