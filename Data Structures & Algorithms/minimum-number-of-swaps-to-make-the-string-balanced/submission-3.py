class Solution:
    def minSwaps(self, s: str):
        chars = list(s)
        n = len(chars)

        balance = 0
        right = n - 1
        swaps = []

        for i in range(n):
            if chars[i] == "[":
                balance += 1
            else:
                balance -= 1

            # Prefix became invalid.
            if balance < 0:
                # Find the rightmost '[' that we can bring here.
                while chars[right] != "[":
                    right -= 1

                # chars[i] is necessarily ']'
                # chars[right] is '['
                chars[i], chars[right] = chars[right], chars[i]

                swaps.append((i, right))

                # Before swapping, position i contributed -1.
                # After swapping, it contributes +1.
                #
                # So the prefix balance increases by 2:
                #
                #     -1 -> +1
                #
                balance += 2

                # This '[' has now been used.
                right -= 1

        print(swaps, "".join(chars))
        return len(swaps)