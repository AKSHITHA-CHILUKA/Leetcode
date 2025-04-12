from collections import Counter
from math import factorial
from itertools import product

class Solution:
    def countGoodIntegers(self, num_digits: int, divisor: int) -> int:
        valid_digit_frequencies = set()

        def frequency_to_tuple(freq_dict):
            return tuple(freq_dict.get(str(digit), 0) for digit in range(10))

        def construct_palindrome(left_half, middle_digit=""):
            return "".join(left_half) + middle_digit + "".join(reversed(left_half))

        if num_digits == 1:
            for single_digit in range(1, 10):
                if single_digit % divisor == 0:
                    valid_digit_frequencies.add(frequency_to_tuple(Counter(str(single_digit))))
        else:
            half_length = num_digits // 2
            all_digits = '0123456789'

            left_half_combinations = product(all_digits, repeat=half_length)

            if num_digits % 2 == 0:
                for left_half in left_half_combinations:
                    if left_half[0] == '0':
                        continue  
                    palindrome_str = construct_palindrome(left_half)
                    palindrome_value = int(palindrome_str)
                    if palindrome_value % divisor == 0:
                        valid_digit_frequencies.add(frequency_to_tuple(Counter(palindrome_str)))
            else:

                for left_half in left_half_combinations:
                    if left_half[0] == '0':
                        continue 
                    for middle_digit in all_digits:
                        palindrome_str = construct_palindrome(left_half, middle_digit)
                        palindrome_value = int(palindrome_str)
                        if palindrome_value % divisor == 0:
                            valid_digit_frequencies.add(frequency_to_tuple(Counter(palindrome_str)))


        total_valid_permutations = 0
        for freq_tuple in valid_digit_frequencies:
            digit_counts = list(freq_tuple)


            total_permutations = factorial(num_digits)
            for count in digit_counts:
                total_permutations //= factorial(count)

            invalid_permutations = 0
            if digit_counts[0] > 0:
                remaining_counts = digit_counts.copy()
                remaining_counts[0] -= 1
                invalid_permutations = factorial(num_digits - 1)
                for count in remaining_counts:
                    invalid_permutations //= factorial(count)

            valid_permutations = total_permutations - invalid_permutations
            total_valid_permutations += valid_permutations

        return total_valid_permutations
