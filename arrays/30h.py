# https://leetcode.com/problems/substring-with-concatenation-of-all-words/

class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """

        # Sliding window approach

        step = len(words[0])
        window = step * len(words)
        left = 0
        r = []
        store = {}

        # Create our hashmap with the frequency of each word
        for word in words:
            if word in store:
                store[word] += 1
            else:
                store[word] = 1

        # Traverse the string with a sliding window
        while left <= len(s) - window:
            # Create a deep copy of the store dictionary
            copy = store.copy()
            counter = 0
            current = s[left:left + window]
            # Check the current window
            for i in range(0, window, step):
                word = current[i:i + step]
                if word in copy and copy[word] > 0:
                    copy[word] -= 1
                    counter += 1
                else:
                    break

            # If all words are matched
            if counter == len(words):
                r.append(left)

            left += 1

        return r