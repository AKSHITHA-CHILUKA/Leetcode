class Solution:
    def areaOfMaxDiagonal(self, dimensions: list[list[int]]) -> int:
        max_area, max_diag = 0, 0

        for l, w in dimensions:
            curr_diag = l * l + w * w
            if curr_diag > max_diag or (curr_diag == max_diag and l * w > max_area):
                max_diag = curr_diag
                max_area = l * w

        return max_area
