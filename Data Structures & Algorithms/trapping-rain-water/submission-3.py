DBG = True


class Solution:
    def trap(self, height: List[int]) -> int:
        H = height
        res = 0
        if len(H) == 0:
            return 0
        
        lft_max = [0] * len(H)
        rgt_max = [0] * len(H)

        lft_max[0] = H[0]

        for i in range(1, len(H)):
            lft_max[i] = max(
                lft_max[i-1],
                H[i]
            )
        
        rgt_max[-1] = H[-1]
        for i in range(len(H)-2,-1,-1):
            rgt_max[i] = max(
                rgt_max[i+1],
                H[i]
            )
        
        for i in range(len(H)):
            level = min(lft_max[i], rgt_max[i])
            res += level - height[i]

        return res

#         l2r_max = [-1] * len(height)
#         r2l_max = [-1] * len(height)

# # MONOTONIC STACK
#         # rgt = len(height) - 1
#         # mx_stack = []
#         # while rgt >= 0:
#         #     while mx_stack and H[mx_stack[-1]] < H[rgt]:
#         #         mx_stack.pop()
#         #     mx_stack.append(rgt)
#         #     rgt -= 1
#         # print(mx_stack)
#         # mx_stack.reverse()
#         # i = 0
#         # imx = 0
#         # while i < len(l2r_max) and imx < len(mx_stack):
#         #     j = i
#         #     mx = mx_stack[imx]
#         #     while j < mx:
#         #         l2r_max[j] = mx
#         #         j += 1
#         #     i = j
#         #     imx += 1
#         # print(l2r_max)

#         # lft = 0
#         # mx_stack = []
#         # while lft < len(H):
#         #     while mx_stack and H[mx_stack[-1]] < H[lft]:
#         #         mx_stack.pop()
#         #     mx_stack.append(lft)
#         #     lft += 1
#         # print(mx_stack)
#         # i = 0
#         # imx = 0
#         # while i < len(r2l_max) and imx < len(mx_stack):
#         #     j = i
#         #     mx = mx_stack[imx]
#         #     while j < mx:
#         #         r2l_max[j] = mx
#         #         j += 1
#         #     i = j
#         #     imx += 1
#         # print(r2l_max)

#         # DBG and print(f"{l2r_max=}")
#         # DBG and print(f"{r2l_max=}")
#         for i in range(len(height)):
#             rt_mx = l2r_max[i]
#             lt_mx = r2l_max[i]
#             if rt_mx == -1 or lt_mx == -1:
#                 continue
#             else:
#                 delta = min(height[rt_mx], height[lt_mx]) - height[i]
#                 print(f"{i=} | {delta=} | {height[rt_mx]=} <> {height[lt_mx]=}")
#                 res += delta
#                 print(f"{i=} | {res=} | {rt_mx=} {lt_mx=}")
#         return res
