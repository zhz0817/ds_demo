class ListNode:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkList:
    def __init__(self):  # self.head.next = self.tail 是一定要的，否则插入那里要写if
        self.head = ListNode(-1)
        self.tail = self.head
        self.head.next = self.tail
        self.length = 0

    def clear(self):
        self.head = ListNode(-1)
        self.tail = self.head
        self.head.next = self.tail
        self.length = 0

    def is_empty(self):
        return self.length == 0

    def append_last(self, data):
        node = ListNode(data=data)
        self.tail.next = node
        self.tail = self.tail.next
        self.tail.next = self.head
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
                pre.next = cur.next  # 假如cur是最后一个，那它的next已经是head了，不用分情况区分
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
                pre.next = cur.next  # 假如cur是最后一个，那它的next已经是head了，不用分情况区分，只需要保证满足最后一个的next是head即可
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
        node.next = temp.next  # 如果是空链表并且插入第一个位置(也是最后一个位置)，temp的next是自身，正好循环了
        temp.next = node 
        self.length += 1


if __name__ == '__main__':
    link_list = LinkList()
    for i in range(5):
        link_list.insert_by_index(i, i)
    link_list.display()
