class Element:

    def __init__(self, value):
        self.value = value
        self.prev = None


class Stack:

    def __init__(self):
        self.length = 0
        self.tail = None

    """
    Runtime is O(1) since the element is inserted at the end only
    """
    def push(self, value):
        new_element = Element(value)
        if self.tail:
            last_element = self.tail
            new_element.prev = last_element
            self.tail = new_element
        else:
            self.tail = new_element
        self.length += 1

    """
    Runtime is O(1) since the last element is returned and removed from the stack
    """
    def pop(self):
        if self.tail:
            last_element = self.tail
            if self.tail.prev:
                self.tail = self.tail.prev
            else:
                self.tail = None
            self.length -= 1
            return last_element.value
        else:
            return None

    """
    Runtime is constant since length is maintained by the methods
    """
    def len(self):
        return self.length

    def __str__(self):
        str_rpr = ""
        if self.tail:
            last_element = self.tail
            str_rpr += "-------Stack-------"
            while last_element:
                str_rpr += f"\n{last_element.value}"
                last_element = last_element.prev
            str_rpr += "\n-------------------"
            return str_rpr
        else:
            return str_rpr


def main():
    stack = Stack()
    assert stack.pop() is None
    stack.push(5)
    assert stack.len() == 1
    stack.push(8)
    stack.push(6)
    assert stack.pop() == 6
    print(stack)


if __name__ == '__main__':
    main()