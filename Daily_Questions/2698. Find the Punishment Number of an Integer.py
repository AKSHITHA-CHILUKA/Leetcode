class Solution:
    def punishmentNumber(self, n: int) -> int:
        def canPartition(num_str, target, start):
            if target == 0 and start == len(num_str):
                return True
            if start >= len(num_str):
                return False
            
            current_number = 0
            for i in range(start, len(num_str)):
                current_number = current_number * 10 + int(num_str[i])
                if current_number > target:
                    break
                if canPartition(num_str, target - current_number, i + 1):
                    return True
            return False
        
        total_punishment = 0
        
        for i in range(1, n + 1):
            square = i * i
            if canPartition(str(square), i, 0):
                total_punishment += square
        
        return total_punishment
