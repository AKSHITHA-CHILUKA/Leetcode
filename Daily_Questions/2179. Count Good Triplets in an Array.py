class Solution:
    def goodTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)

        # Map each number to its index in nums2 – so we know their "real" position
        pos = [0] * n
        for i, val in enumerate(nums2):
            pos[val] = i

        # Convert nums1 into the 'mapped' world of nums2
        mapped = [pos[val] for val in nums1]

        # Basic Binary Indexed Tree setup
        def update(bit, idx, val):
            while idx < len(bit):
                bit[idx] += val
                idx += idx & -idx

        def query(bit, idx):
            res = 0
            while idx > 0:
                res += bit[idx]
                idx -= idx & -idx
            return res

        left = [0] * n
        bit = [0] * (n + 2)  # +2 to avoid boundary screams

        for i in range(n):
            # How many elements < mapped[i] have I seen so far?
            left[i] = query(bit, mapped[i])
            update(bit, mapped[i] + 1, 1)  # BIT is 1-indexed... of course 🙄

        right = [0] * n
        bit = [0] * (n + 2)

        for i in reversed(range(n)):
            # How many elements > mapped[i] are still left?
            right[i] = query(bit, n) - query(bit, mapped[i] + 1)
            update(bit, mapped[i] + 1, 1)

        # Total good triplets = left[i] * right[i] for each i being the middle of triplet
        return sum(left[i] * right[i] for i in range(n))
