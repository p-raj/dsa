class PhoneDirectory:
    def __init__(self, maxNumbers: int):
        self.max_num = maxNumbers
        self.used = set()

    def get(self) -> int:
        nums = iter(range(self.max_num + 1))
        n = 0
        while n is not None:
            if self.check(n):
                break
            n = next(nums, None)
        self.used.add(n)
        return n

    def check(self, number: int) -> bool:
        return number not in self.used

    def release(self, number: int) -> None:
        if number in self.used:
            self.used.remove(number)


# Your PhoneDirectory object will be instantiated and called as such:
# obj = PhoneDirectory(maxNumbers)
# param_1 = obj.get()
# param_2 = obj.check(number)
# obj.release(number)
