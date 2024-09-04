class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        if len(s) == 1: return 1
        if k == 1:
            count = 1
            while count < len(s):
                if s[count] != s[count - 1]: break
                count += 1
            if count == len(s): return len(s)
            else:
                maxLen = 0
                maxInd = count
                while count < len(s):
                    newSA = s[:count] + "A" + s[count + 1:]
                    newSB = s[:count] + "A" + s[count + 1:]
                    newCount = count - 1
                    backwardStreakA = 0
                    while newCount >= 0 and s[newCount] == newSA[count]: 
                        newCount -= 1
                        backwardStreakA += 1
                    newCount = count - 1
                    backwardStreakB = 0
                    while newCount >= 0 and s[newCount] == newSB[count]: 
                        newCount -= 1
                        backwardStreakB += 1

                    
        
