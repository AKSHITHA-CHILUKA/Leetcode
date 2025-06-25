import bisect
import math

class Solution:
    def kthSmallestProduct(self, nums1: list[int], nums2: list[int], k: int) -> int:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        candidates = [
            nums1[0] * nums2[0],
            nums1[0] * nums2[-1],
            nums1[-1] * nums2[0],
            nums1[-1] * nums2[-1]
        ]
        low, high = min(candidates), max(candidates)
        def cnting(mid):
            cnt = 0
            for a in nums1:
                if a == 0:
                    if mid >= 0:
                        cnt += len(nums2)
                elif a > 0:
                    # b <= mid / a
                    t = mid / a
                    idx = bisect.bisect_right(nums2, math.floor(t))
                    cnt += idx
                else:  # a < 0
                    # b >= ceil(mid / a)
                    t = mid / a
                    thr = math.ceil(t)
                    idx = bisect.bisect_left(nums2, thr)
                    cnt += len(nums2) - idx
            return cnt
        ans = high
        while low <= high:
            mid = (low + high) // 2
            if cnting(mid) >= k:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return ans
