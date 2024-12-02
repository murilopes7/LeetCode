#This is a code of LeetCode
#This is the version that i thought but i lasted too long in this 

class Solution(object):
    def mergeAlternately(self, word1, word2):
        result = []
        i = 0

        #Make it a loop checking if i is less than the length of the strings
        while i < len(word1) or i < len(word2):
            #If it is the word1 is the greatest, so you append it on the index i
            if i < len(word1):
                result.append(word1[i])
                
            #same thing but with word2
            if i < len(word2):
                result.append(word2[i])
            i += 1 

        #Concatenate its values
        return ''.join(result)


#Another good solution that works really faster 
""" 

class Solution(object):
    def mergeAlternately(self, word1, word2):
        res = ""
        left = 0
        right = 0
        turn = 0
        while(left<len(word1) or right<len(word2)):
            if not turn:
                res += word1[left]
                left+=1
                if (right<len(word2)):
                    turn=1
            else:
                res += word2[right]
                right+=1
                if (left<len(word1)):
                    turn=0
        return res 
        
"""