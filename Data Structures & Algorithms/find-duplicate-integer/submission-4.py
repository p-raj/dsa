class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = 0, 0
        while True:
            fast = nums[nums[fast]] # fast = node.next.next
            slow = nums[slow] # slow = node.next
            if fast == slow:
                break
        slow2 = 0
        while True:
            slow2 = nums[slow2]
            slow = nums[slow]
            if slow2 == slow:
                return slow
