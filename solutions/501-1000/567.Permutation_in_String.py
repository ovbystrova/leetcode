from collections import Counter 


class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """

        if len(s1) > len(s2):
            return False

        s1_counter = Counter(s1)
        s2_counter = Counter(s2[:len(s1)-1])

        start_pointer = 0

        while start_pointer + len(s1) <= len(s2):

            s2_counter[s2[start_pointer + len(s1) - 1]] += 1
            if s1_counter == s2_counter:
                return True

            s2_counter[s2[start_pointer]] -= 1
            if s2_counter[s2[start_pointer]] == 0:
                del s2_counter[s2[start_pointer]] 
            start_pointer += 1
        
        return False


            