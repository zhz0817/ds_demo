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
        temp = self.head
        if index < 0 or index >= self.length:
            raise IndexError("Index out of")
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

    def remove_by_value(self, x: int):
        if self.length == 0:
            return
        if self.head.data == x:
            self.head = self.head.next
            return
        pre = self.head
        cur = self.head.next
        while cur is not None:
            if cur.data == x:
                pre.next = cur.next
                break
            pre = cur
            cur = cur.next

    def remove_by_index(self, x: int):
        if x >= self.length:
            raise IndexError("Index out of range")
        if 0 == x:
            self.head = self.head.next
            return
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

    def insert_by_index(self, index: int, val: int):
        if index < 0 or index > self.length + 1:
            raise IndexError("Index out of range")
        node = ListNode(data=val)
        if index == 0:
            node.next = self.head
            self.head = node
            return
        temp = self.head
        pos = 0
        while pos+1 < index:
            temp = temp.next
        node.next = temp.next
        temp.next = node


if __name__ == '__main__':
    link_list = LinkList()
    for i in range(5):
        link_list.append_first(i)
    link_list.display()
