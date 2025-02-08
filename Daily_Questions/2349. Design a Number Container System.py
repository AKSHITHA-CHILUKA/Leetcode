import heapq

class NumberContainers:
    def __init__(self):
        self.index_val = {}
        self.res = {}

    def change(self, index: int, number: int) -> None:
        if index in self.index_val:
            prevNum = self.index_val[index]
            if prevNum == number:
                return
            self.res[prevNum].discard(index)

        if number not in self.res:
            self.res[number] = set()
        self.res[number].add(index)
        self.index_val[index] = number

    def find(self, number: int) -> int:
        if number not in self.res or not self.res[number]:
            return -1
        return min(self.res[number])
