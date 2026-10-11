class Solution:
    def mostVisitedPattern(
        self, username: List[str], timestamp: List[int], website: List[str]
    ) -> List[str]:
        # username = ["ua","ua","ua","ub","ub","ub"]
        # timestamp = [1,2,3,4,5,6]
        # website = ["a","b","a","a","b","c"]
        arr = zip(timestamp, username, website)
        arr = sorted(arr)

        map_ = defaultdict(list)
        for _, u, w in arr:
            map_[u].append(w)
        
        patterns = defaultdict(int)
        for u, lw in map_.items():
            if len(lw) < 3:
                continue
            else:
                lft = 0
                rgt = lft + 2
                while rgt < len(lw):
                    tup = (lw[lft], lw[lft+1], lw[lft+2])
                    lft += 1
                    rgt += 1
                    patterns[tup] += 1
        patterns = dict(sorted(patterns.items(), key=lambda item: item[1], reverse=True))
        print(patterns)
        return list(next(iter(patterns), []))