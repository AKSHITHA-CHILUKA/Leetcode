from typing import List

class Solution:
    def maxPartitionsAfterOperations(self, s: str, k: int) -> int:
        n = len(s)
        bit_masks = [1 << (ord(c) - 97) for c in s]

        def build_prefix_info(arr: List[int]):
            prefix_count = [0]
            prefix_mask = [0]
            mask = 0
            groups = 0
            for bit in arr:
                mask |= bit
                if mask.bit_count() > k:
                    groups += 1
                    mask = bit
                prefix_count.append(groups)
                prefix_mask.append(mask)
            return prefix_count, prefix_mask

        prefix_count, prefix_mask = build_prefix_info(bit_masks)
        suffix_count, suffix_mask = build_prefix_info(bit_masks[::-1])

        res = 0
        for i in range(n):
            left_groups = prefix_count[i]
            right_groups = suffix_count[-(i + 2)]
            left_mask = prefix_mask[i]
            right_mask = suffix_mask[-(i + 2)]
            combined_mask = left_mask | right_mask
            left_bits = left_mask.bit_count()
            right_bits = right_mask.bit_count()
            combined_bits = combined_mask.bit_count()

            if min(combined_bits + 1, 26) <= k:
                total = left_groups + right_groups + 1
            elif left_bits == right_bits == k and combined_bits < 26:
                total = left_groups + right_groups + 3
            else:
                total = left_groups + right_groups + 2

            if total > res:
                res = total

        return res
