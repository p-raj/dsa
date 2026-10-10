class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        strt = 0
        waiting = 0
        for indx, (arrv, prep) in enumerate(customers):
            if strt < arrv:
                strt = arrv
            wait = prep + strt
            print(f"{indx=} | {arrv=} {strt=} {prep=}")
            print(f"{indx=} | {wait=} {strt=} {wait-arrv=}")
            waiting += (wait - arrv)
            strt = wait
            print("..")
        print(waiting, waiting / len(customers))
        return waiting / len(customers)
