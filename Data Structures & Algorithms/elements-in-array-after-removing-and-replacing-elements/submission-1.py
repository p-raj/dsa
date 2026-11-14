DBG = True


class Solution:
    def elementInNums(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        res = []
        size = len(nums)
        # phases -> draining, filling
        # in draining phase we get to []
        # in filling phase we get back [...]
        # size: 1
        # 0:[1], 1:[], 2:[1], 3:[]
        # size: 2
        # 0:[1,2], 1:[2], 2:[], 3:[1], 4:[1,2], 5:[2], 6:[], 7:[1], 8:[1,2], 9:[2], 10:[]
        # 2->3->3->3
        # size: 3
        # 0:[1,2,3], 1:[2,3], 2:[3], 3:[], 4:[1], 5:[1,2], 6:[1,2,3], 7:[2,3], 8:[3], 9: []
        # 3->5->5->5....
        # size: 4
        # 0:[1,2,3,4], 1:[2,3,4], 2:[3,4], 3:[4], 4:[], 5:[1], 6:[1,2], 7:[1,2,3], 8:[1,2,3,4],...
        # 4->7
        # initially size = empty => steps: size
        # then size = fill & size -1 = empty => steps: size * 2 - 1
        # queries = [[5, 1], [6, 2], [7, 1], [8, 1], [9, 1], [10, 1]]
        for time, index in queries:
            if time == size:
                res.append(-1)
            elif time < size:
                cursor = (time + index)%size
                if cursor > size:
                    res.append(-1)
                else:
                    res.append(nums[cursor])
            else:
                # time is gt size
                # now every (size*2-1) the array is empty
                # fills in size steps
                # empties in size - 1 steps
                s = size * 2 - 1
                t = time % s + 1

                if t < size:
                    if index <= t:
                        res.append(nums[index])
                    else:
                        res.append(-1)
                else:
                    cursor = (time + index) % size
                    if cursor > size:
                        res.append(-1)
                    else:
                        res.append(nums[cursor])

        return res
