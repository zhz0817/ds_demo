class ListNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prior = None


class LinkList:
    def __init__(self):
        self.head = ListNode(-1)
        self.tail = self.head
        self.length = 0

    def clear(self):
        self.head = ListNode(-1)
        self.tail = self.head
        self.length = 0

    def is_empty(self):
        return self.length == 0

    def append_last(self, data):
        node = ListNode(data=data)
        self.tail.next = node
        node.prior = self.tail
        self.tail = self.tail.next
        self.length += 1

    def get_length(self) -> int:
        return self.length

    def get_value_by_index(self, index) -> int:
        if index < 0 or index >= self.length:
            raise IndexError("Index out of")
        temp = self.head.next
        while index > 0 and temp is not None:  # temp is not None 可以不写
            temp = temp.next
            index -= 1
        return temp.data

    def display(self):
        temp = self.head.next
        while temp is not None:
            print(temp.data)
            temp = temp.next

    def index_of(self, x: int) -> int:
        temp = self.head.next
        ans = 0
        while temp is not None:
            if temp.data == x:
                return ans
            ans += 1
            temp = temp.next
        return -1

    def remove_by_value(self, x: int) -> int:
        if self.length == 0:
            return 0
        pre = self.head
        cur = self.head.next
        while cur is not None:
            if cur.data == x:
                pre.next = cur.next
                cur.next.prior = pre
                self.length -= 1
                return 1
            pre = cur
            cur = cur.next
        return 0

    def remove_by_index(self, x: int):
        if x >= self.length or x < 0:
            raise IndexError("Index out of range")
        self.length -= 1
        pre = self.head
        cur = self.head.next
        index = 0
        while cur is not None:
            if index == x:
                pre.next = cur.next
                cur.next.prior = pre
                break
            pre = cur
            cur = cur.next
            index += 1

    def insert_by_index(self, index: int, val: int):
        if index < 0 or index > self.length:
            raise IndexError("Index out of range")
        node = ListNode(data=val)
        temp = self.head
        pos = 0
        while pos < index:
            temp = temp.next
            pos += 1
        node.next = temp.next
        node.prior = temp
        temp.next = node
        self.length += 1


if __name__ == '__main__':
    link_list = LinkList()
    for i in range(5):
        link_list.append_last(i)
    link_list.insert_by_index(5, 5)
    link_list.display()
