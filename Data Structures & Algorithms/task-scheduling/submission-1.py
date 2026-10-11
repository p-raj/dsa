from collections import Counter
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        cpu = []
        freq = Counter(tasks)
        freq = dict(sorted(freq.items(), key=lambda item: item[1],reverse=True))
        for task, tcount in freq.items():
            while tcount > 0:
                slotted = False
                for idx, cpu_task in enumerate(cpu):
                    if not tcount:
                        break
                    if task not in cpu_task and None in cpu_task:
                        cpu_task[cpu_task.index(None)] = task
                        cpu[idx] = cpu_task
                        slotted = True
                        tcount -= 1
                if tcount and not slotted:
                    cts = [None] * (n + 1)
                    cts[0] = task
                    cpu.append(cts)
                    tcount -= 1
        cycles = 0
        cpu[-1] = list(filter(lambda x: x is not None,cpu[-1]))
        for t in cpu:
            for i in t:
                cycles += 1
        return cycles