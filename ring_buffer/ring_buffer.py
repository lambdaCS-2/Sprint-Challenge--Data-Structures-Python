from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        if self.storage.length < self.capacity:
            # see if there is a head
            if self.storage.head == None:
                # if not add
                self.storage.add_to_head(item)
                # track current node
                self.current = self.storage.head
            else:
                
                self.storage.add_to_tail(item)
                self.current = self.storage.head
        else:
            # if buffer becomes full need to add items at the oldest (head)
            if self.current.next == None:
                self.current.value = item
                self.current = self.storage.head
            else:
                self.current.value = item
                self.current = self.current.next


    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        # TODO: Your code here
        current = self.storage.head
        while (current):
            list_buffer_contents.append(current.value)
            current = current.next

        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
