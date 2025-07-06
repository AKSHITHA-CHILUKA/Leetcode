class FindSumPairs:
    def __init__(self, nums1, nums2):
        self.n1 = nums1
        self.n2 = nums2

    def add(self, index, val):
        self.n2[index] += val

    def count(self, tot):
        res = 0
        for x in self.n1:
            for y in self.n2:
                if x + y == tot:
                    res += 1
        return res
