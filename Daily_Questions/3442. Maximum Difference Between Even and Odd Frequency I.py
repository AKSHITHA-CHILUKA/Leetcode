from collections import Counter

class Solution:
    def maxDifference(self, s: str) -> int:
        # Count the frequency of each character in the string
        freq = Counter(s)
        
        # Separate the frequencies into odd and even categories
        odd_frequencies = []
        even_frequencies = []
        
        for count in freq.values():
            if count % 2 == 0:
                even_frequencies.append(count)
            else:
                odd_frequencies.append(count)
        
        # If there are no odd or even frequencies, return 0 (though problem guarantees both exist)
        if not odd_frequencies or not even_frequencies:
            return 0
        
        # Find the max odd frequency and min even frequency
        max_odd = max(odd_frequencies)
        min_even = min(even_frequencies)
        
        # The result is max odd frequency minus min even frequency
        return max_odd - min_even
