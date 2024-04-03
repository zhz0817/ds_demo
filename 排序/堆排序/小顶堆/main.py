class SmailTopHeap:

    def __init__(self):
        self.nums = []

    def push(self, val: int):
        self.nums.append(val)
        self.forward_head_sort()

    def pop(self) -> int:
        ans = self.nums[0]
        self.nums[0] = self.nums[-1]
        self.nums.pop(-1)
        self.forward_tail_sort()
        return ans

    def forward_head_sort(self):
        cur = len(self.nums) - 1
        while True:
            if cur % 2 == 0:
                parent = cur // 2 - 1
            else:
                parent = cur // 2
            if parent < 0:
                break
            if self.nums[parent] > self.nums[cur]:
                temp = self.nums[parent]
                self.nums[parent] = self.nums[cur]
                self.nums[cur] = temp
                cur = parent
            else:
                break

    def forward_tail_sort(self):
        cur = 0
        while True:
            left = 2 * cur + 1
            right = 2 * cur + 2
            if right < len(self.nums):
                if self.nums[cur] < self.nums[left] and self.nums[cur] < self.nums[right]:
                    break
                elif self.nums[right] > self.nums[left]:
                    self.nums[cur], self.nums[left] = self.nums[left], self.nums[cur]
                    cur = left
                else:
                    self.nums[cur], self.nums[right] = self.nums[right], self.nums[cur]
                    cur = right
            elif left < len(self.nums):
                if self.nums[cur] < self.nums[left]:
                    break
                else:
                    self.nums[cur], self.nums[left] = self.nums[left], self.nums[cur]
                    cur = left
            else:
                break


if __name__ == '__main__':
    smail_top = SmailTopHeap()
    for i in range(0, 100)[::-1]:
        smail_top.push(i)
    while len(smail_top.nums) > 0:
        ans = smail_top.pop()
        print(ans)
