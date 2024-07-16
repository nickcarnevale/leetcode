# https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
	
        # Approach: 
        # keep track of left and right pointers
        # use a hashmap 
            
        # Approach: 
        # keep track of left and right pointers
        # use a hashmap 
            
        n = len(s)	
        m = {}
        
        # edge case
        if n == 0:
            return 0
        if n == 1:
            return 1

        left = 0
        # insert the first element into the hashmap
        m[s[left]] = left
        # return value is at least one
        k = 1


        for i in range(1,n):
            if s[i] in m:
                # if the number is in the hashmap
                # case1: s[i] is inside the current window, we need to change the window by moving left pointer to m[s[i]] + 1.
                # case2: s[i] is not inside the current window, we can keep increase the window
                if m[s[i]] < left:
                     k = max(k, i-left+1)
                else:
                    left = m[s[i]] + 1
            else:
                k = max(k, i-left+1)
            
            m[s[i]] = i

        return k

