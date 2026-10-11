from collections import Counter
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        cpu = []
        freq = Counter(tasks)
        freq = dict(sorted(freq.items(), key=lambda item: item[1],reverse=True))
        print(freq)
        for task, count in freq.items():
            while count > 0:
                slotted = False
                for idx, cpu_task in enumerate(cpu):
                    if task not in cpu_task and None in cpu_task:
                        cpu_task[cpu_task.index(None)] = task
                        cpu[idx] = cpu_task
                        slotted = True
                if not slotted:
                    cts = [None] * (n + 1)
                    cts[0] = task
                    cpu.append(cts)
                count -= 1
        cycles = 0
        for t in cpu:
            for i in t:
                if i != None:
                    cycles += 1
        return cycles