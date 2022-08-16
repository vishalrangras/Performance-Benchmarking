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
            Runtime of O(n) as the worst case.
        """
        if self.head:
            # Case when the linked list is having one or more elements
            current_element = self.head
            index = 0
            while current_element.next:
                if current_element.value == value:
                    return index  # Return the index if the value is found
                current_element = current_element.next  # Point to next element as the current element for traversal
                index += 1
            if current_element.value == value:  # Check if the value is in last element
                return index
            else:
                return None  # Return None if the value is not found
        else:
            # Case when the linked list does not have any element
            return -999 # Return -999 if the linked list is empty

    def get(self, index):
        """
            This method returns the element at a given index
            Runtime O(n) as the worst case.
        """
        current_index = 0
        if self.head:
            current_element = self.head
            while current_element.next:
                if current_index == index:
                    return current_element
                current_element = current_element.next
                current_index += 1
            if current_index == index:
                return current_element
            return None  # This is the case when index is out of bound
        else:
            return -999 # Return -999 if the linked list is empty

    def insert_at(self, value, index):
        """
            This method inserts a new element at a given index. This method has runtime of O(N) as it would
            require the list traversal by calling get() method.
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
            :returns -999 if the linked list is empty
            :returns None if the value could not be found
            :returns 0 if the value is deleted successfully
        """
        if self.head:
            current_element = self.head
            if current_element.value == value:
                self.head = current_element.next
                self.length -= 1
                return 0
            prev_element = self.head
            while current_element.next:
                if current_element.value == value:
                    prev_element.next = current_element.next
                    self.length -= 1
                    return 0
                else:
                    prev_element = current_element
                    current_element = current_element.next
            if current_element.value == value:
                prev_element.next = current_element.next
                self.length -= 1
                return 0
        else:
            return -999

    def delete_at(self, index):
        """
            This methods deletes the element at a given index.
            Runtime is O(n) since it uses get method to reach the element at given index.
            Raises exception for invalid index
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
            prev_element = self.get(index-1)
            element_at_index = self.get(index)
            prev_element.next = element_at_index.next
        self.length -= 1

    def len(self):
        """
            This method returns the length of the linked list.
            Runtime is O(1) since this value is maintained in LinkedList class.
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
    print(f"Length of the linked list: {ll.len()}")


if __name__ == '__main__':
    main()
