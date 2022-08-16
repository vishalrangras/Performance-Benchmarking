class Element(object):

    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList(object):

    def __init__(self, head=None):
        self.head = head
        self.length = 0

    def append(self, value):
        """
            This method appends the element at the end of the linked list
            Runtime of O(n) since entire list traversal is needed.
            :param value: Value to be appended at the end of linked list.
        """
        new_element = Element(value)
        if self.head:
            # Case when the linked list already has one or more elements
            # Traverse till the end of list and then append the new element there
            current_element = self.head  # Starting from the head element
            while current_element.next:  # Iterating till the current_element has a next pointer to reach till end
                current_element = current_element.next  # Assigning the next element as the current element
            # At this point, our current_element points to the last element of our linked list
            # The next attribute of our last element i.e. current_element is None at the moment.
            current_element.next = new_element  # Now the current_element points to the new element
            # making it the last element of our linked list.
        else:
            # Case when the linked list is completely empty
            # The head of the linked list points to the very first element appended to it
            self.head = new_element
        self.length += 1

    def find(self, value):
        """
            This method returns the index of the element for which the value matches the argument
            The improved method iterates on current_element instead of current_element.next
            Runtime of O(n) as the worst case.
            :param value: The value we want to find index of.
            :returns: Index of the passed value. -999 if the list is empty. -1 if the element is not found.
        """
        if self.head:
            index = 0
            current_element = self.head
            while current_element:
                if current_element.value == value:
                    return index
                else:
                    index += 1
                    current_element = current_element.next
            return -1
        else:
            return -999

    def get(self, index):
        """
            This method returns the element at a given index
            The improved method iterates on current_element instead of current_element.next.
            Runtime O(n) as the worst case.
            :param index: The index of the element we want to retrieve.
            :returns: The element at a given index, -999 if the list is empty.
        """
        if index > self.len():
            raise IndexError("Index out of bound")
        elif index < 0:
            raise IndexError("Index cannot be a negative value")
        else:
            current_index = 0
            if self.head:
                current_element = self.head
                while current_element:
                    if current_index == index:
                        return current_element
                    else:
                        current_index += 1
                        current_element = current_element.next
            else:
                return -999

    def insert_at(self, value, index):
        """
            This method inserts a new element at a given index. This method has runtime of O(N) as it would
            require the list traversal by calling get() method.
            :param value: The value to be inserted in the linked list.
            :param index: The index at which the value is to be inserted.
            :raises IndexError: when an invalid index is passed.
        """
        if index > self.length:
            raise IndexError("Index out of bound")
        elif index == self.length:
            self.append(value)
        elif self.head:
            if index > 0:
                prev_element = self.get(index - 1)
                new_element = Element(value)
                new_element.next = prev_element.next
                prev_element.next = new_element
            elif index == 0:
                new_element = Element(value)
                new_element.next = self.head
                self.head = new_element
            else:
                raise IndexError("Index cannot be a negative value")
        else:
            self.append(value)
        self.length += 1

    def push(self, value):
        """
            This method is used to push an element at the beginning of linked list.
            Runtime O(1)
            :param value: The value to be pushed at the beginning of linked list.
        """
        new_element = Element(value)
        if self.head:
            new_element.next = self.head
            self.head = new_element
        else:
            self.head = new_element
        self.length += 1

    def delete(self, value):
        """
            This method deletes the first occurrence of the passed value.
            The improved method leverages the prev_element.next.next to use only single variable.
            It also leverages prev_element as the iterator instead of prev_element.next to cover end of list index.
            :param value: The value to be searched for and deleted from the linked list if found.
            :returns: 0 if the value is deleted successfully, None if the value could not be found,
            -999 if the linked list is empty.
        """
        if self.head:
            if self.head.value == value:
                self.head = self.head.next
                self.length -= 1
                return 0
            prev_element = self.head
            while prev_element:
                if prev_element.next.value == value:
                    prev_element.next = prev_element.next.next
                    self.length -= 1
                    return 0
                else:
                    prev_element = prev_element.next
        else:
            return -999

    def delete_at(self, index):
        """
            This methods deletes the element at a given index.
            The improved method leverages prev_element.next.next
            Runtime is O(n) since it uses get method to reach the element at given index.
            Raises exception for invalid index.
            :param index: The index of the element to be deleted
        """
        if index >= self.length:
            raise IndexError("Index out of bound")
        elif index < 0:
            raise IndexError("Index cannot be a negative value")
        elif index == 0:
            if self.head.next:
                self.head = self.head.next
            else:
                self.head = None
        else:
            prev_element = self.get(index - 1)
            prev_element.next = prev_element.next.next
        self.length -= 1

    def len(self):
        """
            Runtime is O(1) since this value is maintained in LinkedList class.
            :returns: The length of the linked list.
        """
        return self.length

    def __str__(self):
        str_rep = []
        if self.head:
            current_element = self.head
            while current_element.next:
                str_rep.append(str(current_element.value))
                current_element = current_element.next
            str_rep.append(str(current_element.value))
            return "->".join(str_rep)
        else:
            return ""


def main():
    ll = LinkedList()
    assert ll.find(10) == -999
    assert ll.get(0) == -999
    ll.append(5)
    ll.append(2)
    ll.append(-7)
    assert ll.find(2) == 1
    assert ll.find(-7) == 2
    assert ll.find(5) == 0
    assert ll.find(8) is None
    assert ll.get(0).value == 5
    assert ll.get(1).value == 2
    assert ll.get(2).value == -7
    assert ll.get(3) is None
    print(ll)
    ll.insert_at(3, 0)
    print(ll)
    ll.insert_at(4, 2)
    print(ll)
    ll.insert_at(8, 4)
    print(ll)
    ll.push(1)
    ll.push(2)
    print(ll)
    print("Deleting the values")
    ll.delete(2)
    print(ll)
    ll.delete(5)
    print(ll)
    ll.delete(-7)
    print(ll)
    ll.delete_at(4)
    print(f"Deleting element at index 4: {ll}")
    print(f"Length of the linked list: {ll.len()}")


if __name__ == '__main__':
    main()
