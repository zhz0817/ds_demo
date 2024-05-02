class ListNode:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkList:
    def __init__(self):
        self.head = None
        self.length = 0

    def clear(self):
        self.head = None
        self.length = 0
        # self.__init__() #因为构造函数会返回对象

    def is_empty(self):
        return self.length == 0

    def append_first(self, data):
        node = ListNode(data=data)
        if self.head is None:
            self.head = node
        else:
            node.next = self.head
            self.head = node
        self.length += 1

    def get_length(self):
        return self.length

    def get_value_by_index(self, index) -> int:
        if index < 0 or index >= self.length:
            raise IndexError("Index out of")
        temp = self.head
        while index > 0 and temp is not None:  # temp is not None 可以不写
            temp = temp.next
            index -= 1
        return temp.data

    def display(self):
        temp = self.head
        while temp is not None:
            print(temp.data)
            temp = temp.next

    def index_of(self, x: int) -> int:
        temp = self.head
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
        if self.head.data == x:
            self.head = self.head.next
            return 1
        pre = self.head
        cur = self.head.next
        while cur is not None:
            if cur.data == x:
                pre.next = cur.next
                self.length -= 1
                return 1
            pre = cur
            cur = cur.next
        return 0

    def remove_by_index(self, x: int) -> int:
        if x >= self.length or x < 0:
            # raise IndexError("Index out of range")
            return 0
        self.length -= 1
        if x == 0:
            self.head = self.head.next
            return 1
        pre = self.head
        cur = self.head.next
        index = 1
        while cur is not None:
            if index == x:
                pre.next = cur.next
                break
            pre = cur
            cur = cur.next
            index += 1
        return 1

    def insert_by_index(self, index: int, val: int) -> int:
        if index < 0 or index > self.length:
            # raise IndexError("Index out of range")
            return 0
        self.length += 1
        node = ListNode(data=val)
        if index == 0:
            node.next = self.head
            self.head = node
            return 1
        temp = self.head
        pos = 0
        while pos + 1 < index:
            temp = temp.next
            pos += 1
        node.next = temp.next
        temp.next = node
        return 1


if __name__ == '__main__':
    link_list = LinkList()
    for i in range(5):
        link_list.append_first(i)
    for i in range(5):
        link_list.remove_by_index(0)
    link_list.insert_by_index(0, 1)
    print(link_list.get_length())
